# Learning Python ([pwn.college dojo](https://pwn.college))

This repo is a [Pwn.college](https://pwn.college) dojo for learning
[Python](https://python.org) at a high school level for
[cyber security clubs](https://github.com/westshorecsclub/WildcatCSClub).

To use this dojo as a student:

* Goto pwn.college and setup a user account
* Complete the Start Here dojo challenges (this teaches you how the pwn.college
  platform works)
* At this point, students can do whatever dojos they want, but I would suggest
  looking at the following 2 dojo's next (you can even do them one at a time or
  together)
  * Linux Luminarium (teaches you alot about how the Linux shell works)
  * Learning Python (LINK TBD)

# Resources

For learning a new programming language it's often handy to have a book to
read, along with a way to practice what you are learning.  There are 2 FREE 
online Python reference books that I would suggest for new students:

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/3e/)
  by Al Sweigart.  The free version is web-only / read via your web browser.
  It's also available professionally printed for a cost from:
  * [No Starch Press](https://nostarch.com/automate-boring-stuff-python-3rd-edition)
  * [Amazon](https://www.amazon.com/Automate-Boring-Stuff-Python-3rd/dp/1718503407)
  * I've often seen it included in programming book bundles at
    [Humble Bundle](https://humblebundle.com)
* [A Byte of Python](https://python.swaroopch.com/) by Swaroop Chitlur

# Challenges and Concepts

The dojo is 30+ challenges, grouped into 9 modules.  The challenges are
deliberately *not* numbered - we expect to insert new ones between existing
ones as the material gets refined - but the order within and between modules is
meaningful.  That order gets to *useful* things (talking to the terminal,
reading and writing files, and writing Unix filters) much earlier than a
typical Python book does.  The goal is not to march through every language
feature, it is to make Python a tool you actually reach for.

Every challenge follows the same pattern: you write a Python program in your
home directory, run it (or let the challenge run it), and if it behaves
correctly you get the flag.

## Module 1: Getting Started

* **Hello, Hacker** - Create `hello.py` with a single `print()` call and run
  it with `python hello.py`.  Teaches: the editor, saving a file, running the
  interpreter, and that a program is just a text file.
* **Run It Yourself** - Add a `#!/usr/bin/env python3` shebang, `chmod +x`
  your script, and run it as `./hello.py`.  Teaches: a Python script is a
  regular Linux program; ties directly back to the Linux Luminarium dojo.
* **Debug Me** - You are given a program that will not run (missing colon,
  bad indentation, unbalanced quote, typo'd name).  Fix it until it runs.
  Teaches: reading a traceback, `SyntaxError` vs `NameError`, line numbers are
  your friend.
* **Variables and f-strings** - Store values in variables and print a
  sentence built from them with an f-string.  Teaches: variables, strings vs
  numbers, `f"..."` formatting, `+`, `-`, `*`, `/`, `//`, `%`.

## Module 2: Talking to the Terminal

* **Say My Name** - Use `input()` to read a name and greet the user.
  Teaches: interactive programs, `input()` always returns a string.
* **Number Cruncher** - Read two numbers from the user, convert them with
  `int()`, and print the results of some math.  Teaches: type conversion, and
  why `"3" + "4"` is `"34"`.
* **Hex to Decimal** - Read a hexadecimal number like `1f`, `0xDEAD`, or
  `ff00` and print its decimal value, then go the other way with `hex()`.
  Teaches: `int(text, 16)` and the base argument you did not know `int()` had,
  upper vs lower case digits, stripping a `0x` prefix, and `f"{n:x}"` /
  `f"{n:02X}"` formatting.  Discussion: why hex exists at all, why one hex
  digit is exactly 4 bits and one byte is exactly 2 hex digits, and why every
  hex dump, memory address, color code, and MAC address you will ever see in
  security work is written this way.  Also worth showing `int(text, 2)` for
  binary while we are here.
* **Two Kinds of Output** - Print the answer on stdout and your debug
  chatter on stderr with `print(..., file=sys.stderr)`.  Prove it by running
  `./prog > out.txt` and seeing only the chatter on screen.  Teaches: stdout is
  data, stderr is for humans - the single most useful habit in this dojo.
* **Exit Codes** - Use `sys.exit(0)` and `sys.exit(1)` to report success or
  failure, then check with `echo $?`.  Teaches: how the shell knows if your
  program worked, and how `&&` and `||` decide what to run next.
* **Command Line Arguments** - Read `sys.argv` so your program takes its
  input from the command line instead of asking.  Teaches: `argv[0]` is the
  program name, arguments are strings, handling "not enough arguments".

## Module 3: Making Decisions

* **If and Else** - Branch on a comparison and print one of two answers.
  Teaches: `if`/`else`, indentation as a block, `==` vs `=`.
* **The elif Ladder** - Turn a number into a letter grade (or a password
  strength, or a D&D damage tier).  Teaches: `elif` chains, order matters,
  ranges of values.
* **True and False** - Combine conditions with `and`, `or`, and `not` to
  validate input.  Teaches: booleans, comparison operators, `in`, short-circuit
  evaluation.
* **The Guessing Game** - A `while` loop that keeps asking until the player
  guesses the secret number, printing "too high" or "too low" each time.
  Teaches: `while`, loop conditions, `break`; and it is the first challenge
  that feels like a real *game*.

## Module 4: Loops and Lists

* **Counting Loops** - Use `for i in range(...)` to print a countdown, a
  times table, and a triangle of stars.  Teaches: `for`, `range()` with 1, 2,
  and 3 arguments.
* **FizzBuzz** - The classic.  Print the numbers 1 to 100, one per line, but
  print `Fizz` for multiples of 3, `Buzz` for multiples of 5, and `FizzBuzz`
  for multiples of both.  Teaches: the modulus operator `%` and the "is it
  evenly divisible" test `n % 3 == 0`, putting a loop and an `if`/`elif`
  ladder together, and why the order of those branches decides whether you
  get `FizzBuzz` or just `Fizz`.  Discussion: this exact problem is famous as
  a screening question handed to new grads and new software engineers in job
  interviews - not because it is hard, but because it quickly shows whether
  someone can turn a plain-English rule into working code.  You are doing it
  in week one.
* **Lists** - Build a list, index it, slice it, `append()` to it, and take
  its `len()`.  Teaches: lists, zero-based indexing, negative indexes,
  `IndexError`.
* **Loop Over a List** - Walk a list to find the biggest item, the total,
  and the average.  Teaches: the accumulator pattern, `for item in list:`,
  `sum()`/`min()`/`max()`.

## Module 5: Files

* **Read a File** - Open a file, `read()` the whole thing, print it.
  Teaches: `open()`, file paths, `FileNotFoundError`.
* **Write a File** - Write your answer to a file instead of the screen, and
  verify it with `cat`.  Teaches: `"w"` mode, that `"w"` destroys the old
  contents, and `with open(...) as f:`.
* **Line by Line** - Loop over a file one line at a time and process each
  one.  Teaches: `for line in f:`, why every line ends in `\n`, and
  `.strip()`.
* **Append and Transform** - Add to a log file with `"a"` mode, then read
  one file, change it, and write the result to a second file.  Teaches: file
  modes, reading and writing at the same time, not clobbering your input.

## Module 6: Unix Filters

* **Read From Standard Input** - Loop over `sys.stdin` so your program
  works with both `cat data.txt | ./prog` and typed input ending in Ctrl-D.
  Teaches: stdin is just another file, and what a *filter* is.
* **Write Your Own grep** - Print only the lines that contain a given
  string (taken from `sys.argv`).  Teaches: combining argv + stdin + `if` +
  `in`; you have now rebuilt a real Unix tool.
* **In the Middle of a Pipeline** - A filter that transforms every line
  (upper-case it, renumber it, reverse it) and works in the middle of a pipe:
  `cat f | ./yours | sort | head`.  Teaches: composability, why writing to
  stdout matters.
* **FizzBuzz, The Filter** - Same rules as before, but the numbers are no
  longer `1` through `100` in order.  They arrive on stdin - arbitrary, out of
  order, negative, huge, with blank lines mixed in - one per line, and for each
  one you print `Fizz`, `Buzz`, `FizzBuzz`, or the number itself.  Teaches:
  turning a program that *generates* its own data into one that *processes*
  someone else's, more practice with `%` (including what it does to negative
  numbers), `int()` on lines that may be junk, and the payoff of the split you
  learned earlier - a bad line is a complaint on stderr, not a crash.  Try it
  with `seq 1 100 | ./fizzbuzz.py`, then with `shuf` in between, and confirm
  you get the same set of answers.
* **Count and Total** - Rebuild `wc -l`, then sum a column of numbers piped
  in from another program.  Teaches: counters, `int()` on messy input, ignoring
  blank lines.

## Module 7: Working With Text

* **Slicing Strings Apart** - Use `split()`, `join()`, `strip()`,
  `upper()`, `lower()`, `replace()`, `startswith()`, and `find()` on real
  lines of text.  Teaches: the string methods you will use forever.
* **Your Own cut** - Given a CSV (the kind a spreadsheet exports), pull out
  named columns and print a clean report.  Teaches: `split(",")`, indexing
  fields, skipping the header row - and that you can now do spreadsheet work
  from the command line.

## Module 8: Functions

* **Define and Call** - Write a function that takes an argument, does the
  work, and `return`s a value; call it several times.  Teaches: `def`,
  parameters, `return` vs `print`, local variables.
* **Build a Toolbox** - Refactor an earlier filter so each step is its own
  function, plus a `main()` and default parameter values.  Teaches: why
  functions exist, naming things well, reusing code instead of copy-pasting.
  A good one to do to your FizzBuzz filter: a `fizzbuzz(n)` function that
  returns a string, and a loop that does nothing but read, call, and print.

## Module 9: Dictionaries

* **Lookup Tables** - Use a dictionary to translate codes to names (HTTP
  status codes, port numbers, or a substitution cipher).  Teaches: keys and
  values, `d[key]`, `.get()`, `in`, `KeyError`, looping with `.items()`.
* **Capstone: The Report** - Read a data file, count occurrences with a
  dictionary, sort the results, and write a formatted report - using argv for
  the filename, stderr for errors, stdout for the report, and functions to keep
  it tidy.  Teaches: everything above, together, in the shape of a program you
  would actually write at a job.
