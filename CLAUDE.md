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
```

Modules currently built: `getting-started` (`hello-hacker`, `birthday-banner`).

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

Judge behavior worth knowing when writing challenge instructions:

* Every line is `.strip()`ed before hashing, so leading/trailing whitespace on
  a line is forgiven, but *interior* spacing must match exactly.
* Blank lines are skipped entirely when hashing output.
* **stderr is captured and ignored.**  This is deliberate and valuable - it is
  what makes the README's stdout-vs-stderr lessons enforceable, and it lets
  students leave debug prints on stderr without failing.
* The judge invokes the student's script **directly** (`[script]`), not
  `python3 script`.  The student therefore needs a `#!/usr/bin/env python3`
  shebang and `chmod +x`.  That is exactly the "Run It Yourself" challenge, so
  any challenge using this judge must come after it, or the instructions must
  say to do both.

### Known bugs in `multi-case-judge/run` (verified, not theoretical)

These are copied into every challenge that uses the pattern, so fix them in
`chal_crafting/common/multi-case-judge/run` *and* in each challenge's copy.

1. **Too little output crashes with a traceback instead of a nice message.**
   If the student's correct lines are a prefix of the expected output but they
   print fewer lines, `hashes_out[i]` raises `IndexError` and the student sees
   a Python stack trace.  The guard `if len(hash_hex) < (i - 1)` compares the
   wrong list; it should test `i >= len(hashes_out)`.
2. **Extra output lines are accepted and the flag is given away.**  The check
   `if len(test_data) > len(hash_hex)` compares the *input* length to the
   expected-output length, which is meaningless.  It should compare
   `len(hashes_out) > len(hash_hex)`.  Confirmed: a solution that prints the
   correct three lines plus a garbage fourth line passes.
3. `read_in_file` does `break` on an empty test case, so a stray blank section
   silently truncates the rest of the file.  `continue` would be safer.
4. `main` uses `zip(verify_hashes, test_data)`, which silently truncates if the
   two files disagree on case count.  **Always regenerate `hashes.txt` after
   touching `test_cases.txt`.**

Also inconsistent between challenges: `hello-hacker/run` hardcodes
`/usr/local/bin/python3` while the multi-case judge uses `/usr/bin/env
python3`.  Prefer `/usr/bin/env python3`.

## Golden scripts: DO NOT WRITE THEM IN PYTHON

This repo is intended to become **public**.  The judging machinery came from
dojos that lived in private repos, where it was fine to keep a "golden"
reference implementation next to the challenge - you run it to generate the
exact expected output, then hash that into `hashes.txt`.

In a public repo, a golden script written in Python is a ready-made answer key.
A student looking for the solution to "write a FizzBuzz filter" would find a
working Python FizzBuzz filter sitting in the repo.

**Policy:**

* **Never write a golden/reference solution in Python.**
* **Never write one in C either.**  A C version of this dojo is planned, and
  similar challenges will exist there; a C golden script would leak that
  dojo's answers the same way.
* **Write golden scripts in Perl.**  Rationale: `perl` is present on every
  Ubuntu system and in the target image (`mwales/pwncollege_base`), needs no
  compile step, is excellent at exactly the line-oriented text processing these
  judges need, and is syntactically alien enough that a beginning student
  cannot paste it into a `.py` file and have anything happen.
* Acceptable alternates when they genuinely fit: **awk** for trivial
  line filters, **dc** for a purely numeric challenge if you want the
  stack-based-and-unreadable effect.  **Avoid C++** - it is close enough to C
  to partially leak the future C dojo.

Verified working: a Perl golden script for `birthday-banner` reproduces all 16
committed hashes in `.eval_data/hashes.txt` byte-for-byte through the existing
`gen_hashes.py`, with no changes to the toolchain.  Skeleton:

```perl
#!/usr/bin/perl
# GOLDEN SCRIPT - not Python on purpose, see CLAUDE.md
use strict; use warnings;

while (my $line = <STDIN>) {
    chomp $line;
    $line =~ s/^\s+|\s+$//g;
    next if $line eq "";
    # ... produce the exact expected output ...
    print "...\n";
}
```

Handy Perl equivalents for things these challenges ask for:

| Python | Perl |
|--------|------|
| `"*" * 80` | `"*" x 80` |
| `s.strip()` | `$s =~ s/^\s+\|\s+$//g` |
| `s.title()` | `$s =~ s/([a-zA-Z]+)/\u\L$1/g` |
| `s.upper()` / `s.lower()` | `uc $s` / `lc $s` |
| `int(s, 16)` | `hex($s)` |
| `f"{n:02X}"` | `sprintf("%02X", $n)` |
| `n % 3 == 0` | `$n % 3 == 0` |

Residual risk to accept knowingly: a determined student can still *read* Perl.
The real protection is that only hashes ship to the challenge VM, and
`.eval_data` is mode 0600.  The language choice is there to stop casual
copy-paste, not a motivated reverse engineer.  If a challenge ever needs a
genuinely secret reference implementation, keep it out of this repo entirely
rather than trying to obfuscate it.

## Authoring a new challenge - checklist

1. Pick the next challenge from the README list; keep the README ordering.
2. `mkdir <module>/<challenge-id>`.
3. Write `DESCRIPTION.md`: teaching material, `# Further Reading` links into
   *A Byte of Python* / *Automate the Boring Stuff*, then `# Instructions`
   last.  Remember the "instruction" keyword trap above.
4. Write the golden script **in Perl** (see policy above).  Keep it in
   `chal_crafting/` or outside the repo - do not drop it in the challenge dir
   where it would ship to the VM.
5. Write `.eval_data/test_cases.txt`.  Make the cases fun - the existing
   birthday-banner cases are famous hackers and CS figures, which is the tone
   to match.  Include edge cases (odd/even lengths, mixed case, quotes).
6. Run `gen_hashes.py <golden.pl> test_cases.txt .eval_data/hashes.txt`.
7. Copy `.init` from `chal_crafting/common/multi-case-judge/init.sh` and `run`
   from the same folder.  `chmod +x` both.
8. Add the challenge id + name to the module's `module.yml`.
9. Solve it yourself in Python and confirm the judge passes it, then confirm a
   deliberately wrong answer fails.

## Housekeeping / open items

* `getting-started/module.yml` lists only `hello-hacker`.  **`birthday-banner`
  is built but not registered**, so it will not appear in the dojo.  Add it.
* The judge bugs above are unfixed.
* `README.md` has "LINK TBD" for this dojo's own URL.
* Only 2 of 33 planned challenges exist.

## Conventions

* Commit often, with real messages describing what changed and why - the parent
  `checkouts/CLAUDE.md` asks for this across all repos here.
* Challenge and module ids are `kebab-case`; they are directory names.
* Two spaces after a period in prose, ~79 column wrapping, in both README.md
  and DESCRIPTION.md files.  Match it.
* The existing judge scripts are tab-indented in `judge_script/` and
  4-space-indented in `multi-case-judge/`.  Match whichever file you are
  editing; do not reformat wholesale.
