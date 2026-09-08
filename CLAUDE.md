# CLAUDE.md

Notes for future LLM runs working in this repo.

## What this repo is

A [pwn.college](https://pwn.college) **dojo** that teaches Python to high
school students in a cyber security club.  It is a curriculum repo, not an
application repo: most of the "code" here is challenge configuration,
challenge descriptions (teaching material), and judging scripts.

**Read [README.md](README.md) first.**  It holds the full curriculum plan -
30+ challenges grouped into 9 modules - and it is the source of truth for what
gets built next.  Do not invent a new challenge order or scope from scratch;
work from that list.

Key things the README encodes that are easy to get wrong if you skip it:

* The ordering is deliberate and **not** the ordering a normal Python book
  uses.  Students hit stdout vs stderr, exit codes, and `sys.argv` in module 2,
  files in module 5, and Unix filters in module 6 - long before functions and
  dictionaries.  The goal is Python as a *useful tool*, tied back to the Linux
  Luminarium dojo, not a language-feature tour.
* Challenges in the README are **intentionally unnumbered**, because we expect
  to insert new ones between existing ones.  Keep it that way.  Module headings
  stay; per-challenge numbers do not.
* Audience is high school students, many of whom have never programmed.  Match
  the existing DESCRIPTION.md voice: friendly, second person, worked examples
  in fenced code blocks, plenty of "here is what the error looks like".

## Repo layout

```
dojo.yml                      dojo id, name, award emoji, docker image, module list
README.md                     THE CURRICULUM PLAN - start here
<module-id>/
    module.yml                module name + ordered list of challenge ids
    DESCRIPTION.md            module-level intro shown on the website
    <challenge-id>/
        DESCRIPTION.md        teaching material + instructions (see below)
        .init                 runs as root at challenge start
        run                   the judge; suid, reads /flag
        .eval_data/           test_cases.txt + hashes.txt (multi-case judge only)
chal_crafting/common/         reusable judge machinery, copied per challenge
chal_crafting/learning_python_pwncollege_solutions/
                              PRIVATE submodule: Python solutions / golden scripts
```

Modules currently built:

| Module | Directory | Challenges |
|--------|-----------|------------|
| 1 | `getting-started` | hello-hacker, run-it-yourself, debug-me, variables-and-fstrings, birthday-banner |
| 2 | `talking-to-the-terminal` | say-my-name, number-cruncher, hex-to-decimal, two-kinds-of-output, exit-codes, command-line-arguments |
| 3 | `making-decisions` | if-and-else, elif-ladder, true-and-false, guessing-game |
| 4 | `loops-and-lists` | counting-loops, fizzbuzz, lists, loop-over-a-list, secret-decoder-ring |
| 5 | `files` | hangman |

README modules 1 to 4 are complete.  Module 5 has only its first game; modules
6 to 9 do not exist yet.  Add them to `dojo.yml` in README order.

**The curriculum order is a hard constraint on challenge design.**  A challenge
may only need language features the README has already introduced, and that
rules out things you would reach for without thinking:

* Modules 1 to 3 come before loops, so those challenges must be **loop free**.
  That is why `command-line-arguments` takes exactly two arguments and indexes
  them, and why `exit-codes` is handed the status to exit with rather than
  deciding it - `if` had not been taught yet either.
* Module 2 comes before `if`, module 4 before `.split()` and `.join()`.  The
  `lists` challenge builds its list with a counted loop and `.append()` for
  exactly this reason.
* Reading an unknown number of lines needs `try/except EOFError`, which is
  never taught.  So challenges take a **count** first, or a sentinel that ends
  the input - see `hangman` and `guessing-game`.

## How a pwn.college challenge works here

* `DESCRIPTION.md` is rendered on the challenge's web page.  `.init` runs as
  root when the challenge VM starts and writes `/challenge/README.md`
  containing **only the instructions section**, so the student has the task at
  hand inside the VM without the whole lesson.
* The way it finds that section is a `grep -in instruction` that takes the
  **last** match and tails from there.  **Trap: never use the word
  "instruction" anywhere after the `# Instructions` heading**, or the in-VM
  README gets truncated to a fragment.  Also keep `# Instructions` as the last
  such heading in the file.
* `run` is the judge.  Its shebang is `#!/usr/bin/exec-suid -- ...` so it can
  read `/flag`.  It must print the flag itself; there is no separate flag
  plumbing.
* The student passes their script path to the judge:
  `/challenge/run /home/hacker/my_script.py`.

## The two judge patterns in `chal_crafting/common/`

**1. `judge_script/` - single fixed output, no test data.**
`craft_generic_judge.py` takes the desired output on stdin and emits a
standalone `judge.py` with SHA-256 hashes of each expected line baked in.  Used
when the answer is one fixed block of text.  `hello-hacker` predates this and
just string-compares, which is fine for a first challenge.

**2. `multi-case-judge/` - the one to use for most challenges.**  This is the
pattern `birthday-banner` uses and the one that fits the README's filter and
stdin challenges.

* `.eval_data/test_cases.txt` - input for each case, cases separated by a line
  reading `END_TEST_CASE`.
* `.eval_data/hashes.txt` - SHA-256 of each expected output line, same
  `END_TEST_CASE` separators.  **Generated, never hand-written.**
* `gen_hashes.py <golden_script> <test_cases.txt> <hashes.txt>` - runs the
  golden script once per test case and writes the hashes.  Run this at
  authoring time, on your own machine; commit the resulting `hashes.txt`.
* `run` - re-runs the student's script per case as user `hacker` and compares
  line hashes.
* `init.sh` also does `chmod 0600 /challenge/.eval_data/*` and `chmod 0700
  /challenge/.eval_data` so the student cannot read the test cases or hashes.
  Copy this, do not forget it.

### Optional .eval_data files

`test_cases.txt` and `hashes.txt` are required.  Everything else is optional,
and a challenge that does not need it just leaves the file out.  Every file
present must have the **same number of test cases**, or the judge refuses to
run.

| File | Effect | Generate with |
|------|--------|---------------|
| `args.txt` | command line arguments per case, one argument per line | `--args` |
| `stderr_hashes.txt` | stderr is judged too, not ignored | `--stderr-hashes` |
| `exit_codes.txt` | exit status is judged, one integer per line | `--exit-codes` |

`END_TEST_CASE` is a **terminator, not a separator**: a section with no lines
in it is a real test case meaning "this program reads nothing from stdin".
That is how `fizzbuzz`, `debug-me`, `variables-and-fstrings` and
`run-it-yourself` are expressed - a `test_cases.txt` that is nothing but
`END_TEST_CASE` lines.

Two traps that cost real time:

* **Never make a challenge print `sys.argv[0]`.**  It is the path the script
  was invoked with - the solution's path when generating hashes, the student's
  path when judging - so it can never match.
* **Never make output depend on a path, a clock, or randomness** for the same
  reason.  `hangman` takes the wordlist path as input precisely so the path
  can differ between the two runs without reaching the output.

Judge behavior worth knowing when writing challenge instructions:

* Every line is `.strip()`ed before hashing, so leading/trailing whitespace on
  a line is forgiven, but *interior* spacing must match exactly.
* Blank lines are skipped entirely when hashing output.
* **stderr is captured and ignored.**  This is deliberate and valuable - it is
  what makes the README's stdout-vs-stderr lessons enforceable, and it lets
  students leave debug prints on stderr without failing.
* The judge invokes the student's script **directly** (`[script]`), not
  `python3 script`.  The student therefore needs a `#!/usr/bin/env python3`
  shebang and `chmod +x`, and the judge checks for both up front and prints
  the fix.  That is exactly the "Run It Yourself" challenge, so
  any challenge using this judge must come after it, or the instructions must
  say to do both.

### Judge bugs that were found and fixed

Recorded so nobody reintroduces them.  All four were verified by test before
being fixed, and the first two were confirmed fixed the same way.

1. **Too little output raised `IndexError`** and showed the student a Python
   traceback.  The guard compared the wrong list.  Now the judge compares the
   lines that exist first (so a wrong line is reported before a missing one),
   then reports counts.
2. **Extra output lines were accepted and the flag handed over.**  The check
   compared the *input* length to the expected-output length, which is
   meaningless.  Now it compares actual output length.
3. `read_in_file` did `break` on an empty section, silently discarding every
   test case after a stray blank.  Now `continue`.  Note the consequence: a
   test case whose input is genuinely empty is not expressible.
4. `main` used `zip()` on the two `.eval_data` files, silently truncating - and
   quietly making the challenge easier - if they disagreed.  Now it refuses to
   run and says the challenge is misconfigured.

Also added while in there:

* A **10 second timeout** per test case (`TEST_CASE_TIMEOUT`).  A beginner's
  runaway `while` loop should fail the challenge, not hang the judge.
* Up front checks for "file does not exist", "is a directory", and "is not
  executable", the last of which prints the `chmod +x` and shebang fix.  This
  is the single most likely beginner mistake given that the judge executes the
  script directly.
* `clean_output_lines()`, shared by the judge and `gen_hashes.py`.  **These two
  must strip and drop blank lines identically or generated hashes will not line
  up with judged output.**  If you change one, change both.

The judge lives in `chal_crafting/common/multi-case-judge/run` and is **copied**
into each challenge directory.  There is no include mechanism, so a fix has to
be propagated by hand to every challenge that uses it.

### Interpreter path in suid scripts

`run` is suid via `exec-suid`.  Use an **absolute interpreter path**
(`#!/usr/bin/exec-suid -- /usr/local/bin/python3 -I`), never `/usr/bin/env
python3`: the student controls `PATH`, and `env` resolves through it, so an
`env` shebang on a suid program invites the student to supply their own
`python3`.  `-I` (isolated mode) blocks `PYTHONPATH` and the user site
directory but does nothing about `PATH`.  Both challenges now use the absolute
path.

## Solutions and golden scripts: the private submodule

Solutions live in a **separate private repo**, included here as a git
submodule at `chal_crafting/learning_python_pwncollege_solutions`
(`git@github.com:mwales-ai/learning_python_pwncollege_solutions.git`).  This
repo - the dojo - is intended to become public; the solutions repo must stay
private.  Someone cloning the public dojo without access just gets an empty
directory, which is the point.

Each solution does two jobs:

1. **A quick reference for educators**, so a club advisor can unstick a
   student without re-deriving the challenge.
2. **The golden script** that generates the challenge's expected output.  The
   judge never stores an answer - only SHA-256 hashes of each expected output
   line, produced by running the solution against `test_cases.txt`.

Because of job 2, **a solution must produce byte-exact expected output**, not
merely a correct answer.

### Solutions are written in Python

The structure mirrors the dojo exactly: a challenge at
`<module-id>/<challenge-id>/` here has its solution at
`<module-id>/<challenge-id>/solution.py` in the submodule.  Every solution has
a `#!/usr/bin/env python3` shebang and is `chmod +x`, because the judge
executes the student's script directly rather than passing it to `python3`.

Write solutions the way we want a *student* to write them at that point in the
curriculum - no language feature the dojo has not taught yet.  The solution
doubles as the model answer an educator will put on a projector.

**Never commit a solution into this (public) repo.**  The submodule is the only
place they belong.  If a script must live in the public repo for some reason,
write it in **Perl** and not in Python or C - Perl is on every Ubuntu system
and in the target image, needs no compile step, is good at line-oriented text,
and is alien enough to block copy-paste; Python would be a ready-made answer
key, and C would leak the planned C version of this dojo.  This was the policy
before the private submodule existed and remains the fallback.  (Verified: a
Perl golden script for `birthday-banner` reproduces all 16 committed hashes
byte-for-byte through `gen_hashes.py`.)

### Regenerating hashes

```
chal_crafting/common/multi-case-judge/gen_hashes.py \
    chal_crafting/learning_python_pwncollege_solutions/<module>/<chal>/solution.py \
    <module>/<chal>/.eval_data/test_cases.txt \
    <module>/<chal>/.eval_data/hashes.txt
```

Always regenerate after editing `test_cases.txt`.  `gen_hashes.py` now refuses
to write the file if the golden script exits nonzero or prints nothing, and
the judge refuses to run if the two files disagree on test case count.

## Authoring a new challenge - checklist

1. Pick the next challenge from the README list; keep the README ordering.
2. `mkdir <module>/<challenge-id>`.
3. Write `DESCRIPTION.md`: teaching material, `# Further Reading` links into
   *A Byte of Python* / *Automate the Boring Stuff*, then `# Instructions`
   last.  Remember the "instruction" keyword trap above.
4. Write the solution in the **private submodule** at
   `chal_crafting/learning_python_pwncollege_solutions/<module>/<chal>/solution.py`,
   in Python, with a shebang and `chmod +x`.  It is both the educator reference
   and the golden script.  Never put it in the challenge directory, where it
   would ship to the student's VM.
5. Write `.eval_data/test_cases.txt`.  Make the cases fun - the existing
   birthday-banner cases are famous hackers and CS figures, which is the tone
   to match.  Include edge cases (odd/even lengths, mixed case, quotes).
6. Run `gen_hashes.py <solution.py> test_cases.txt .eval_data/hashes.txt`.
7. Copy `.init` from `chal_crafting/common/multi-case-judge/init.sh` and `run`
   from the same folder.  `chmod +x` both.
8. Add the challenge id + name to the module's `module.yml`.
9. Confirm the judge passes the solution, then confirm a deliberately wrong
   answer fails - test a *wrong line*, a *missing line*, and an *extra line*
   separately.  Those were three different bugs once.
10. Commit the submodule first, then the dojo repo (which records the new
    submodule commit).

## Housekeeping / open items

* `README.md` has "LINK TBD" for this dojo's own URL.
* 21 of 35 planned challenges exist (README modules 1-4 done, plus hangman).
* `secret-decoder-ring`'s test cases are generated by `make_test_cases.py`,
  which lives beside its solution in the private submodule.  It asserts that
  every message survives a clean encode/decode round trip - without that
  check it is easy to write a test case whose "correct" answer is nonsense,
  because a plaintext character also appeared in the cipher alphabet.  Keep
  the leading test case's cipher **asymmetric**: ROT13 and Atbash are their
  own inverse, so a student who runs the key backwards would silently pass
  them and get confusing feedback on a later case.
* The `judge_script/` single fixed output judge still has its expected-output
  hashes baked into a base64 blob inside `craft_generic_judge.py`, which must
  be kept in sync by hand with `judge_template.py`.  Nothing uses it yet.
* `/usr/local/bin/python3` is used as the suid interpreter path based on what
  `hello-hacker` shipped with.  Worth confirming against the actual image
  (`mwales/pwncollege_base`) the first time a challenge is deployed.

### Challenges that need a data file

`hangman` ships its own wordlist at `/challenge/words.txt` and its `.init`
adds a `chmod 0644` for it.  Two things to know before copying the pattern:

* **Do not judge against `/usr/share/dict/words`.**  It is a symlink to
  `/etc/dictionaries-common/words`, whose contents depend on which dictionary
  packages happen to be installed, so two machines can disagree and the hashes
  become unreproducible.  The same argument rules out scraping the web at run
  time.  `words.txt` is 500 computing-flavored words mined once from a scraped
  corpus and then **frozen** inside `make_wordlist.py` in the private
  submodule, which emits it deterministically with no network access.  The
  scrape-and-score pipeline is kept beside it in `wordlist_pipeline/` for
  provenance and so the list can be extended deliberately - it scrapes ~124
  computing Wikipedia articles plus both recommended books, scores every word
  against a non-computing Wikipedia background corpus, and curates the top
  500.  **If the wordlist changes, the test cases and hashes must be
  regenerated**, and any word named in `DESCRIPTION.md` or in
  `make_test_cases.py` has to still be present at the same line number.
* **The wordlist path is an input line, not a constant in the program.**  That
  is what makes hashes generatable off the challenge VM: the shipped
  `test_cases.txt` names `/challenge/words.txt`, which does not exist on an
  authoring machine, so `make_test_cases.py` takes the path to embed as an
  argument and a second copy naming a local path is used to run
  `gen_hashes.py`.  The two differ only in that line, and the path never
  reaches the output - but they are only equivalent while both point at
  wordlists with **identical content**.  Regenerate the hashes if `words.txt`
  ever changes.

## Conventions

* Commit often, with real messages describing what changed and why - the parent
  `checkouts/CLAUDE.md` asks for this across all repos here.
* Challenge and module ids are `kebab-case`; they are directory names.
* Two spaces after a period in prose, ~79 column wrapping, in both README.md
  and DESCRIPTION.md files.  Match it.
* The existing judge scripts are tab-indented in `judge_script/` and
  4-space-indented in `multi-case-judge/`.  Match whichever file you are
  editing; do not reformat wholesale.
