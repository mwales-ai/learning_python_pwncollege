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
  loops and lists in module 4, functions in module 5, files in module 6,
  and Unix filters in module 7 - well before dictionaries, which is the one
  module still held back to the end.  The goal is Python as a *useful
  tool*, tied back to the Linux Luminarium dojo, not a language-feature
  tour.  Loops and Lists and Functions have swapped places more than once
  (see the history note below) - check module.yml, not your memory of a
  past session, before assuming which one currently comes first.
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
| 1 | `getting-started` | running-interpreter, string-concatenation, hello-hacker, run-it-yourself, variables-and-fstrings, debug-me |
| 2 | `talking-to-the-terminal` | tippy-tipper, why-are-we-yelling, birthday-banner, hex-to-decimal, two-kinds-of-output, exit-codes, command-line-arguments |
| 3 | `making-decisions` | if-and-else, elif-ladder, quadratic-formula, true-and-false |
| 4 | `loops-and-lists` | guessing-game, is-palindrome, counting-loops, fizzbuzz, lists, olympic-scorecard, secret-decoder-ring |
| 5 | `functions` | define-and-call, is-prime, fibonacci, wps-pin-cracker, stock-tracker |
| 6 | `files` | read-a-file, write-a-file, line-by-line, hangman, word-game, append-and-transform, game-genie-patcher |
| 7 | `unix-filters` | read-from-standard-input, write-your-own-grep, in-the-middle-of-a-pipeline, fizzbuzz-the-filter, count-and-total |
| 8 | `working-with-text` | slicing-strings-apart, your-own-cut |
| 9 | `dictionaries` | lookup-tables, capstone-the-report |

**All nine README modules are built** - 45 challenges as of the last
reshuffle (see git log for the running history of additions/moves/removals;
do not trust this count blindly, recompute from each module.yml if it
matters). There is also a dojo-level `DESCRIPTION.md` beside `dojo.yml`,
which is what pwn.college shows on the dojo's front page.

Functions moved from module 8 to module 4 (2026-10-24), between Making
Decisions and Loops and Lists, on the theory that Loops and Lists gets
more interesting challenge options once functions already exist to
combine with loops. This forced two kinds of cleanup:

* `build-a-toolbox`'s entire premise is "go refactor your FizzBuzz filter
  from Unix Filters" - a hard dependency on a module that now comes well
  *after* Functions. No quick fix exists (neither FizzBuzz challenge - the
  plain one in Loops and Lists or the filter one in Unix Filters - exists
  yet at this point in the curriculum), so it was pulled out of
  `functions/module.yml` and the README rather than rewritten. The files
  are still on disk at `functions/build-a-toolbox/`, just not deployed;
  revisit or delete later.
* `define-and-call` and `wps-pin-cracker`'s golden solutions used
  `for i in range(...)` to read/brute-force a count - rewritten as counted
  `while` loops (the only loop taught this early now), output unchanged
  and reverified against the existing hashes.
* `stock-tracker` moved to the **end** of Loops and Lists instead of
  staying in Functions - its own DESCRIPTION.md teaches `for date in
  dates:` and list indexing, i.e. Loop Over a List's exact lesson, so it
  reads better placed right after that challenge than it would stuck in
  Functions ahead of lists existing at all. Its solution.py also used to
  build `dates` with a slice + list comprehension - neither taught by
  Lists (which only teaches building a list with `.append()` in a loop) -
  so that got rewritten too, output reverified against the live
  `st_server` and unchanged.

Everything else that was already in Loops and Lists (the plain FizzBuzz,
Lists, Loop Over a List, Secret Decoder Ring) needed no changes - they
never depended on Functions existing, only the reverse direction mattered.

**Reverted (2026-11-02):** Loops and Lists moved back in front of
Functions (module 4 and 5 again, in that order), undoing the swap above.
`stock-tracker` moved with it - back into Functions, appended after
`wps-pin-cracker` this time (it needs `subprocess.run()` from there), now
that Loops and Lists being first means its `for date in dates:` /
`.append()` dependencies are satisfied either way. Its DESCRIPTION.md and
solution.py needed no content changes, just a path-comment fix (`Solution:
loops-and-lists / stock-tracker` -> `functions / stock-tracker`) - the
"Back in Cracking a WPS PIN" and "the accumulator pattern from Loop Over a
List" references in its text both still read correctly regardless of
which module order is active, since neither claims a specific distance.
`define-and-call` and `wps-pin-cracker` kept their `while`-loop solutions
from the previous swap rather than reverting to `for`/`range()` - no need,
they still work correctly either way - but their stale comments claiming
"Functions now comes before Loops and Lists" were fixed since that is
false again. `build-a-toolbox` remains shelved regardless of this swap -
its dependency is on Unix Filters (module 7), which stays after both
Functions and Loops and Lists no matter which of modules 4/5 each one is.
**Moral:** before writing a challenge that assumes "Functions comes before
Loops and Lists" or vice versa as a fact, check `dojo.yml`/the README -
this has now flipped twice.

The Guessing Game also moved (2026-11-02), from the end of Making
Decisions to the **start** of Loops and Lists - it teaches the `while`
loop, which is a loop, not a decision, and now sits right before `for`
(ASCII Values) the same way it always immediately preceded it before (the
two were already adjacent across the module boundary; this just moves the
boundary instead of the challenge's neighbors). Updated both
`module.yml`s, the README, and both modules' own `DESCRIPTION.md`:
Making Decisions dropped its "`while` - keep doing something until a
condition changes" bullet, and Loops and Lists' intro now mentions `while`
alongside `for` as the two loop shapes this module covers. No challenge
content changed - just the one stale path comment in solution.py (`making-
decisions / guessing-game` -> `loops-and-lists / guessing-game`).

Nice side effect: `CLAUDE.md`'s own "Modules 1 to 3 come before loops, so
those challenges must be loop free" claim (two sections below) used to be
false the moment you checked it - Guessing Game, in module 3, used a
`while` loop. It is now actually true.

Added `is-palindrome` right after it (2026-11-02) - second challenge in
Loops and Lists, "Is It a Palindrome?". It reuses the `while` loop from
Guessing Game and is the actual FIRST introduction of string indexing
(`word[i]`) and the `len(word) - 1` last-position rule, via a two-pointer
walk comparing characters from both ends inward. This pushed ASCII
Values down to third and meant ASCII Values' own "Indexing into a
string" section needed a rewrite - it used to introduce `word[i]` fresh;
now it recaps Is It a Palindrome? and spends its own words on
`range(len(word))` and left-to-right iteration instead, which is the
part that is actually new there.

ASCII Values changed again (2026-11-03): it now walks the string with
`for char in word:` instead of `range(len(word))` + `word[i]` - this
task never needs the position, only the character, so direct iteration
fits better than the index-based walk it used before. That made ASCII
Values the real FIRST introduction of `for item in sequence`, which
pushed the claim down two more challenges: Loop Over a List's opening
used to introduce `for value in numbers:`/`for ch in "cat":` as brand
new, and Secret Decoder Ring's "Looping over a string" section re-
introduced the same thing again - both rewritten to recap ASCII Values
instead. Loop Over a List's own new content is unchanged by this -
generalizing the pattern from a string to a real `list`, plus the
accumulator pattern, which was always the actual point of that
challenge. `range(len(word))` stays taught in ASCII Values regardless,
just reframed as "you'll need this soon" (Is It a Palindrome? already
used it; FizzBuzz needs plain `range()` right after) rather than "this
task needs it."

`lists` was replaced wholesale with Anagram Finder (2026-11-05), keeping
the same challenge id and the same slot (5th in Loops and Lists, right
after FizzBuzz and before Loop Over a List) but none of the old content.
The old Lists challenge taught list literals, `.append()`, zero-based and
negative indexing, and `IndexError` by having the student build a list
with a counted loop and report on it; the new one keeps the list-literal
and `.append()`/indexing basics as a short recap (indexing was already
independently covered on strings by Is It a Palindrome?, so this does not
need to be load-bearing) and spends its real content on `.split()`,
`sorted()` vs `.sort()`, and `", ".join(...)` - none of which were
taught anywhere before this point in the curriculum. This is a genuine
curriculum-order change, not just new content: `.split()`/`sorted()`/
`.join()` used to be first taught in `define-and-call` (module 5,
one-line mention), `slicing-strings-apart` (module 8, the real first
deep-dive), and `capstone-the-report` (module 9, `.sort()` on tuples),
respectively. `slicing-strings-apart`'s split()/join() sections were
rewritten from "this is new" to "here's a reminder" accordingly (see its
own history, not repeated here); `define-and-call`, `lookup-tables`, and
`capstone-the-report` needed no changes - none of them claimed novelty,
so reading them as a recap costs nothing.

The task the student solves (anagram detection: given a line of words,
which of the words after the first share all the same letters as it) is
the thing that forces `sorted()` into this early a slot - comparing
`sorted(word_a) == sorted(word_b)` is the natural beginner-level way to
check "same letters, any order" without a hand-rolled letter-counting
dictionary, which is not available yet (dictionaries are module 9). Two
words of different length can never be anagrams, and comparing their
sorted letter-lists already encodes that for free via list `==`, so no
separate length check is needed.

The user's original request named `/usr/share/dict/words` as the word
source. The **student's program never reads that file** - doing so would
hit the exact reproducibility problem this file already documents under
"Challenges that need a data file" (its contents differ by machine/
installed dictionary packages, same as the reason `hangman` ships its
own frozen `words.txt` instead of using it directly). Instead, the live
system dictionary on the authoring machine was used only to confirm, at
authoring time, that the words chosen for `test_cases.txt` are real
English words and genuinely are or are not anagrams of each other
(`sorted(a) == sorted(b)`) - the same role `/usr/share/dict/words` has
always been safe for (flavor and realism when hand-picking test data),
never as something the judged program touches at runtime.

`loop-over-a-list` was replaced wholesale with Olympic Scorecard
(2026-11-06), same id and same slot (6th in Loops and Lists, right after
Anagram Finder and before Secret Decoder Ring), keeping the accumulator
pattern and the seeding trap (seed a highest/lowest search with the
first item, not 0) since both are referenced **by name** downstream -
`stock-tracker`'s "lowest price so far" tracker and
`secret-decoder-ring`'s string-building section both say "the same
accumulator pattern from X", so X had to still teach it under whatever
its new name is. Both of those references were updated from "Loop Over
a List" to "Olympic Scorecard" as part of this change; nothing else in
the repo named the old title.

The task itself (drop the lowest and highest judge's score from a list,
average the rest - the real scoring rule in events like diving and
gymnastics) is what motivates the new content: `sorted(scores)[1:-1]`
finds and drops both extremes in one line, which is the **first**
teaching of list slicing in the dojo (the old Lists challenge's README
blurb once mentioned "slice it" but its actual DESCRIPTION.md never
covered slicing, and Anagram Finder deliberately avoided it too - see
that challenge's own history note - to avoid overloading one challenge
with both `.split()`/`sorted()`/`.join()` and slicing). The exercise
itself now permits the `sum()`/`max()`/`min()` built-ins on the
remaining list rather than demanding another hand-written loop - the
discipline of writing the search by hand once still happens, in this
same challenge's teaching content for the seeding trap, so nothing is
lost by not repeating it a second time against the remaining list.

`files/read-a-file` was replaced wholesale with Hex to Binary
(2026-11-08), same id and same slot (1st in Files). The old exercise
read a path from stdin and printed the file plus a character/line
count; the new one reads hex digits from stdin (any whitespace, any
case, chunks optionally `0x`/`0X`-prefixed) and writes the decoded
bytes to a path given as a **command line argument**. The `open()`/
`with`/`.read()`/`FileNotFoundError` teaching sections were kept
essentially unchanged, because `write-a-file`'s "the `\"w\"` is the
only change from reading" line depends on them having already been
taught here. Added: `sys.stdin` is itself a file object (no `open()`
needed), `bytes.fromhex()` (ignores whitespace between byte pairs but
not `0x`, which has to be stripped with `.split()` + slicing first),
and `open(path, "wb")` for writing the resulting `bytes` object
directly. The now-unused `data/` directory and its `.init` chmod
lines were removed - the new exercise has no sample files to read.

This is also the dojo's first exposure to the `bytes` type and binary
file mode, which used to belong to `game-genie-patcher` (6th in Files,
the ROM patcher). Its "Binary files are not text files" section was
rewritten from a first introduction to a recap - reading in binary
mode (`"rb"`) and indexing into `bytes` to get an int are still new
there, only "binary mode and the `bytes` type exist" moved earlier.

The judge's output-file check reads the written file in **text**
mode (`open(out_path, "r")`) to hash it line by line, the same as
stdout - it was never built to compare raw binary content. So despite
the "binary" framing, every test case's hex decodes to plain ASCII
text (`"Hello, World!"`, `"pwn.college"`, etc.) - real non-ASCII bytes
in a test case would make the judge itself crash trying to read the
file back. This is a constraint of the shared judge, not something
worth fixing per-challenge; it was checked at authoring time by trying
a case-sensitivity bug (`"0x"` only, missing `"0X"`) against the test
data **before** trusting it, which caught a real gap - the first draft
of the test cases never happened to use an uppercase `0X` prefix - and
led to adding one.

`files/write-a-file` was replaced wholesale with File Decoder Ring
(2026-11-08), same id and same slot (2nd in Files). The old exercise
read a path and N lines from stdin and wrote them to that file; the
new one is Secret Decoder Ring's exact substitution-cipher key and
algorithm (same stdin format: original line, then substituted line),
but the encoded message and the decoded result are both now files
named with `sys.argv[1]`/`sys.argv[2]` instead of typed on stdin and
printed to stdout. Kept the `"w"` truncation warning, the mode table,
and the `write()` is not `print()` section essentially unchanged -
all still exactly as true as before, since the new exercise still
opens its output with `"w"`. Added a note that this task does not
need manual `"\n"` insertion, so students do not conclude `write()`
started adding newlines for them: the whole encoded file is read and
decoded in one pass with `.read()`/one loop, and since a newline is
never a key character, it passes through decoding untouched, landing
in the same place in the output as it was in the input - no line
splitting, no `.strip()`, no re-adding newlines by hand.

Test data lives in a new `files/write-a-file/data/` directory (one
static encoded file per cipher, mirroring the pattern the old
`read-a-file`'s now-deleted `data/` directory used) rather than any
per-test-case input-file mechanism, because the shared judge has no
such thing - `output_seeds.txt`/`output_paths.txt`/
`output_file_hashes.txt` only cover the file the program *writes*.
`args.txt` (shipped, `/challenge/data/...` paths) and the solutions
submodule's own `local_args.txt` (authoring-time, real local paths)
diverge only in that one path - and the golden solution does not
print the input path, only the output path and a character count,
specifically so that divergence never reaches judged output (the
same trap this file already documents under "Never make output
depend on a path").

As with the original Secret Decoder Ring, the first test case's key
(`abcde`/`xyzwv`) is deliberately asymmetric; later cases reuse
rot13, atbash, and a digit-complement cipher, all of which are their
own inverse and would silently round-trip through a direction bug.
Verified this by running a decode-in-the-encode-direction bug against
the suite: it fails only on the first (asymmetric) case, passing the
other three by coincidence, exactly as that risk predicts - which is
why the asymmetric case has to be first, not later.

Added `word-game` (2026-11-10), 5th in Files, right after Hangman and
before Append and Transform - a genuinely new challenge, not a
replacement, which is why the dojo's count moved from 44 to 45. A
Wordle-like game: `sys.argv[1]` is a puzzle number, `puzzle_number %
len(word_bank)` picks the solution deterministically from
`/challenge/word-bank.txt` (~2,300 common words), guesses are read
from stdin and checked against the much larger
`/challenge/valid-words.txt` (~13,000 words, a superset of
word-bank), and feedback is printed with real ANSI color codes -
green for right-position, yellow for "elsewhere in the word", no
color for absent. An invalid guess (not in valid-words) prints to
stderr and exits 1 immediately rather than consuming one of the six
tries, which keeps the judge's stdin fixed-length per test case
without needing `try/except EOFError` (never taught) for a dynamic
reprompt loop.

Deliberately simpler than real Wordle, by the user's own request: the
coloring does not track how many of each letter are still available
to "claim," so a guess with two of the same letter can show yellow
twice even when the solution only has one of that letter and real
Wordle would credit just one. The DESCRIPTION.md explains this
tradeoff explicitly rather than silently shipping a near-miss of the
real game. Per the user's instruction, the teaching content shows
exactly one color+reset example (`print("\033[32mHello\033[0m, world!")`)
and stops - no generic `colorize(text, color)` helper is handed to
the student, so writing one is left as their own exercise.

Both word lists (`word-bank.txt`, `valid-words.txt`) are the real
Wordle lists, user-supplied, 5-letter lowercase words one per line,
shipped at the challenge root (`/challenge/word-bank.txt`, not inside
a `data/` subdirectory) rather than packaged into a `data/` folder -
matching `hangman`'s own `words.txt`-at-root precedent, not
`write-a-file`'s `data/` one, since both precedents already coexist
in this module and the user had already placed the files that way
before asking for the challenge itself.

Authoring hit the same hardcoded-absolute-path problem the "Challenges
that need a data file" section describes, but in a new shape: the
golden solution hardcodes `/challenge/word-bank.txt` and
`/challenge/valid-words.txt` directly in the code (not via an
argument), so there is no `args.txt`-style file to swap for a local
path. Fixed by generating hashes against a throwaway `sed`-rewritten
copy of the solution (paths swapped to the real local files, logic
byte-for-byte otherwise) that is never committed - unlike
`local_args.txt`/`local_cases.txt`, which stay in the solutions repo
because they are data, this is a mechanical one-line path swap of the
code itself, safe to regenerate from the real solution.py any time
rather than worth maintaining as a tracked file.

Test data design caught two real gaps worth remembering: the first
draft of every test guess happened to also be a `word-bank.txt` word,
so a solution that validated guesses against the small solution list
instead of the large valid-words list passed every case anyway - not
caught until a guess that is a valid word but NOT a possible solution
(`wombs`) was deliberately added. And `exit_codes.txt` is **not**
`END_TEST_CASE`-delimited like every other `.eval_data` file - it is
one bare integer per line, read by a separate `read_exit_codes()` in
the judge - which was only discovered after writing it with
delimiters, watching `gen_hashes.py` silently overwrite it back to
the bare format, and reading the judge source to confirm that was
correct rather than fighting it.

Tippy Tipper, Why Are We Yelling, and Birthday Banner were moved from
Getting Started into Talking to the Terminal, and Say My Name and Number
Cruncher were deleted outright (2026-09-30/10-03): their skills all
overlapped (interactive `input()`, string/number conversion, string
formatting), and what was unique to Say My Name and Number Cruncher turned
out to already be retaught elsewhere - the module's own `DESCRIPTION.md`
already states the "never give input() a prompt" rule, and
unix-filters/read-from-standard-input re-teaches "input can come from a
pipe or a file" in more depth - except for two narrower things that had no
other home: Number Cruncher's explicit int()-raises-ValueError-but-
float()-doesn't contrast, and its "convert once, up front, name it"
advice. Both were folded into Tippy Tipper's new "Convert once, right
after you read it" subsection before the two challenges were deleted.

Why Are We Yelling moved second, after noticing it was the only Getting
Started challenge that reads stdin at all, and it never actually names
`input()` - it used to come after Tippy Tipper (which does teach `input()`)
in the original Getting Started order, and lost that when Tippy Tipper
moved out from in front of it. Placed right after Tippy Tipper in Talking
to the Terminal (restoring that same ordering, one module over) and before
Birthday Banner, which depends on the `.center()`/`.title()` string
methods Why Are We Yelling introduces. Fixed Birthday Banner's "the string
methods we showed you in the last module" to name Why Are We Yelling
directly, since it is now in the same module rather than the previous one.

**The curriculum order is a hard constraint on challenge design.**  A challenge
may only need language features the README has already introduced, and that
rules out things you would reach for without thinking:

* Modules 1 to 3 come before loops, so those challenges must be **loop free**.
  That is why `command-line-arguments` takes exactly two arguments and indexes
  them, and why `exit-codes` is handed the status to exit with rather than
  deciding it - `if` had not been taught yet either.
* Module 2 comes before `if`.  `.split()`, `sorted()`/`.sort()`, and `.join()`
  are now taught in module 4, by `lists` (Anagram Finder); list slicing
  (`[1:-1]`) is taught right after it, by `loop-over-a-list` (Olympic
  Scorecard) - see the history notes below.  Nothing earlier than either
  may use them.
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
| `output_paths.txt` | a file the program must WRITE, one path per case | `--output-paths` |
| `output_seeds.txt` | content placed at that path before the run | `--output-seeds` |
| `output_file_hashes.txt` | expected final contents of that file | `--output-file-hashes` |

The output-file trio is how the file-writing challenges are judged.  Without a
seed the judge **deletes** the path before running, so a leftover file cannot
pass a program that writes nothing.  With a seed it writes that content and
chmods it 0666 - the judge runs as root and the student's program as `hacker`,
so a root-owned 0644 file would be unwritable.  A seed is also what proves the
difference between `"a"` and `"w"`: `append-and-transform` seeds a header and
checks it survives.

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

  This bites in a subtle place.  Several challenges name `/challenge/data/...`
  in their shipped `test_cases.txt`, which does not exist on an authoring
  machine, so the solutions repo carries a `local_cases.txt` (or
  `local_args.txt`) naming a local path, and hashes are generated from that.
  **That only works while the differing path never reaches judged output.**
  The capstone originally printed `cannot read {path}` on stderr for its
  missing-file case, which broke it - fixed by using the same non-existent
  `/challenge/data/nope.txt` in both files, since it is absent either way.
  There is a check for this class of bug: run each golden script with local
  paths and grep its stdout and stderr for the authoring path prefix.

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

Solutions live in a **separate private repo**,
`git@github.com:mwales-ai/learning_python_pwncollege_solutions.git`.  This repo
- the dojo - is intended to become public; the solutions repo must stay
private.

It **used to be a git submodule** here and no longer is.  pwn.college clones
the dojo recursively and cannot authenticate to a private submodule, so the
link was removed.  The two repos are now independent, and
`chal_crafting/learning_python_pwncollege_solutions/` is in `.gitignore`.

Clone it into that same path by hand when authoring - all the tooling expects
it there:

```
git clone git@github.com:mwales-ai/learning_python_pwncollege_solutions.git \
    chal_crafting/learning_python_pwncollege_solutions
```

**Commit and push the two repos separately.**  Nothing links them any more, so
nothing will remind you.

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
* All 40 challenges exist.  Anything further is new material, not
  catching up - and any new challenge still has to obey the curriculum order
  constraint above.
* Module 1's `running-interpreter` and `string-concatenation` are a different
  shape from every other challenge: their `run` is an `exec-suid` **interactive
  interpreter** (`python3 -I -i`) that pre-loads variables, rather than a judge
  that executes a student script.  There is no `.eval_data` and no solution
  script - the student types at a `>>>` prompt.  Do not "fix" them to match the
  others, and remember the audit and regression scripts skip anything without a
  solution.
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
