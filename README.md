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

The dojo is 40 challenges, grouped into 9 modules.  The challenges are
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

* **Running the Interpreter** - Start the Python interpreter, evaluate an
  expression, make a variable, and print one that has already been set for you.
  Nothing is written to a file yet - this is the "type something and see what
  happens" challenge.
  * **Skills:**
    * The interactive `>>>` prompt as a place to try things out
    * Rules for valid variable names
    * `=` as assignment, not mathematical equality
    * `exit()` to leave the interpreter
* **String Concatenation** - Join two ciphertext variables with `+`, then pass
  the result to a `secret_decoder()` function to reveal the flag.  Still
  entirely in the interpreter.
  * **Skills:**
    * Strings as a kind of value, like numbers
    * `+` as string concatenation
    * `len()` on a string
    * Calling a function and passing it an argument
* **Hello Hackers** - Create `hello.py` with a single `print()` call and run it
  with `python hello.py`.
  * **Skills:**
    * Using a text editor to create a `.py` file
    * Saving a file with a `.py` extension
    * Running a script with `python file.py`
    * A program is just a text file until it is run
* **Run It Yourself** - Add a `#!/usr/bin/env python3` shebang, `chmod +x` your
  script, and run it as `./hello.py`.
  * **Skills:**
    * The shebang line, `#!/usr/bin/env python3`
    * `chmod +x` to make a script executable
    * Running a script directly with `./script.py`
    * A Python script is a regular Linux program - ties directly back to the
      Linux Luminarium dojo
* **Tippy Tipper** - Turn a tip calculator with hard-coded numbers into one
  that asks for the subtotal and the tax and tip *percentages*, then reports
  each as an amount plus the total.  The judge runs it three times with random
  subtotals, so echoing the percentages back will not pass.
  * **Skills:**
    * `input()` to read a line of text from the user
    * `float()` to convert user input into a number
    * Why `"5" * 5` is `"55555"`, not `25` - strings vs numbers
    * `round()` for formatting a computed value
    * Hard-coding, and why a program should ask for its inputs instead
* **Variables and f-strings** - Store values in variables and print a sentence
  built from them with an f-string.
  * **Skills:**
    * Storing values in named variables
    * Strings vs numbers as distinct types
    * `f"..."` string formatting
    * The arithmetic operators `+ - * / // %`
* **Why Are We Yelling?** - Read a line of text and shout it back with the
  vowels censored out: `* S*W * D*CK **T*NG * C*K*`.
  * **Skills:**
    * `.upper()` to change case
    * `.replace()` to substitute characters
    * String immutability - methods return a new string, they never change the
      original
    * Reading standard input piped into a program (`cat file | ./script.py`)
* **Birthday Banner** - Centre a birthday message inside an 80 column banner of
  `*` characters.
  * **Skills:**
    * String replication with `*` (`"*" * 5`)
    * `len()` to measure a string
    * `//` and `%` to split leftover space evenly
    * `.title()` for title case
* **Debug Me** - You are given a program that will not run (bad indentation,
  unbalanced quote, typo'd name, wrong capitalization).  Fix it until it runs.
  * **Skills:**
    * Reading a Python traceback
    * `SyntaxError` vs `NameError` - what each one means
    * Fixing one error at a time and rerunning, rather than guessing at all of
      them at once

## Module 2: Talking to the Terminal

* **Say My Name** - Use `input()` to read a name and greet the user.
  * **Skills:**
    * Writing an interactive program with `input()`
    * `input()` always returns a string
* **Number Cruncher** - Read two numbers from the user, convert them with
  `int()`, and print the results of some math.
  * **Skills:**
    * `int()` to convert text into a number
    * Why `"3" + "4"` is `"34"`, not `7`, until you convert
* **Hex to Decimal** - Read a hexadecimal number like `1f`, `0xDEAD`, or `ff00`
  and print its decimal value, then go the other way with `hex()`.
  * **Skills:**
    * `int(text, 16)` - the base argument you did not know `int()` had
    * Hex digits are case-insensitive, and `0x` prefixes are optional
    * `f"{n:x}"` and `f"{n:02X}"` formatting
    * `hex()` to go from a number back to hex text
    * `int(text, 2)` for binary, while we are here
  * **Discussion:** Why hex exists at all - one hex digit is exactly 4 bits,
    one byte is exactly 2 hex digits - and why every hex dump, memory address,
    color code, and MAC address you will ever see in security work is written
    this way.
* **Two Kinds of Output** - Print the answer on stdout and your debug chatter
  on stderr with `print(..., file=sys.stderr)`.  Prove it by running `./prog >
  out.txt` and seeing only the chatter on screen.
  * **Skills:**
    * `print(..., file=sys.stderr)`
    * stdout is for data, stderr is for humans - the single most useful habit
      in this dojo
    * Redirecting stdout with `> out.txt` and watching stderr still reach the
      screen
* **Exit Codes** - Use `sys.exit(0)` and `sys.exit(1)` to report success or
  failure, then check with `echo $?`.
  * **Skills:**
    * `sys.exit(code)` to set a program's exit status
    * `echo $?` to check the last exit status
    * `&&` and `||` in the shell, driven by exit status
* **Command Line Arguments** - Read `sys.argv` so your program takes its input
  from the command line instead of asking.
  * **Skills:**
    * `sys.argv` as a list of command line words
    * `argv[0]` is the program's own name, not the first argument
    * Command line arguments arrive as strings
    * Checking `len(sys.argv)` before assuming an argument exists

## Module 3: Making Decisions

* **If and Else** - Branch on a comparison and print one of two answers.
  * **Skills:**
    * `if` / `else`
    * Indentation as a block, not decoration
    * `==` for comparison vs `=` for assignment
* **The elif Ladder** - Turn a number into a letter grade (or a password
  strength, or a D&D damage tier).
  * **Skills:**
    * `elif` chains
    * First match wins, and why branch order matters
    * Testing ranges of values without needing both bounds
* **True and False** - Combine conditions with `and`, `or`, and `not` to
  validate input.
  * **Skills:**
    * Booleans (`True` / `False`) as values
    * Comparison operators (`==`, `!=`, `<`, `>`, ...)
    * `and`, `or`, `not`
    * `in` to test membership
    * Short-circuit evaluation
* **The Guessing Game** - A `while` loop that keeps asking until the player
  guesses the secret number, printing "too high" or "too low" each time - the
  first challenge that feels like a real *game*.
  * **Skills:**
    * `while` loops
    * Loop conditions that depend on user input
    * `break` to exit a loop early

## Module 4: Loops and Lists

* **Counting Loops** - Use `for i in range(...)` to print a countdown, a times
  table, and a triangle of stars.
  * **Skills:**
    * `for` loops
    * `range()` with one, two, and three arguments
    * Counting down with a negative step
* **FizzBuzz** - The classic.  Print the numbers 1 to 100, one per line, but
  print `Fizz` for multiples of 3, `Buzz` for multiples of 5, and `FizzBuzz`
  for multiples of both.
  * **Skills:**
    * The modulus operator `%`
    * The "evenly divisible" test, `n % 3 == 0`
    * Combining a loop with an `if`/`elif` ladder
    * Branch order deciding `FizzBuzz` vs just `Fizz`
  * **Discussion:** This exact problem is famous as a screening question handed
    to new grads and new software engineers in job interviews - not because it
    is hard, but because it quickly shows whether someone can turn a
    plain-English rule into working code.  You are doing it in week one.
* **Lists** - Build a list, index it, slice it, `append()` to it, and take its
  `len()`.
  * **Skills:**
    * Creating and indexing a list
    * Zero-based indexing
    * Negative indexes
    * `.append()`
    * `IndexError`
* **Loop Over a List** - Walk a list to find the biggest item, the total, and
  the average.
  * **Skills:**
    * The accumulator pattern
    * `for item in list:`
    * `sum()`, `min()`, `max()`
* **Secret Decoder Ring** - You are handed the key to a substitution cipher -
  one line of original characters, and underneath it what each was turned into
  - followed by a pile of intercepted messages to decode.  The real lesson is
  that a position in one line maps to the same position in the other.
  * **Skills:**
    * Looping over the characters of a string
    * `.index()` to find a position
    * Guarding `.index()` with `in` so an unmapped character does not crash you
    * The accumulator pattern, building a string instead of a number
  * **Discussion:** Substitution ciphers are genuinely ancient - Caesar used
    one - and this is the first challenge whose output is something you would
    actually want to read.  We come back to this problem in the dictionaries
    module, where it gets much shorter.

## Module 5: Files

* **Read a File** - Open a file, `read()` the whole thing, print it.
  * **Skills:**
    * `open()`
    * File paths
    * `FileNotFoundError`
* **Write a File** - Write your answer to a file instead of the screen, and
  verify it with `cat`.
  * **Skills:**
    * `"w"` mode
    * `"w"` destroys the file's old contents
    * `with open(...) as f:`
* **Line by Line** - Loop over a file one line at a time and process each one.
  * **Skills:**
    * `for line in f:`
    * Every line ends in `\n`
    * `.strip()`
* **Hangman** - Build the actual game.  The secret word is pulled out of a
  wordlist file by line number, you get six wrong guesses, and correct letters
  fill in the blanks.
  * **Skills:**
    * Reading a file line by line while counting
    * `break` to stop early once you find what you need
    * The newline-on-the-end bug, in the place where it really hurts - one
      stray `\n` and your board has an extra underscore
  * **Discussion:** Every Linux box ships a dictionary at
    `/usr/share/dict/words`, a hundred thousand lines that are useless to open
    by hand and perfect to open from a program.  Spell checkers read it; so do
    people cracking passwords.  The wordlist path is an input, so students can
    point the finished game at the system dictionary and play for real.  The
    500 word list the challenge ships was itself mined out of computing
    articles and the two recommended books by counting words - a preview of the
    capstone, and the description walks through how it was done.
* **Append and Transform** - Add to a log file with `"a"` mode, then read one
  file, change it, and write the result to a second file.
  * **Skills:**
    * `"a"` append mode
    * Reading one file while writing another
    * Never opening your input file for writing

## Module 6: Unix Filters

* **Read From Standard Input** - Loop over `sys.stdin` so your program works
  with both `cat data.txt | ./prog` and typed input ending in Ctrl-D.
  * **Skills:**
    * Looping over `sys.stdin`
    * stdin behaves just like a file
    * What a *filter* is
* **Write Your Own grep** - Print only the lines that contain a given string
  (taken from `sys.argv`).
  * **Skills:**
    * Combining `sys.argv`, stdin, `if`, and `in`
    * Rebuilding a real Unix tool out of parts you already know
    * Exit status 0 when something matched, 1 when nothing did
* **In the Middle of a Pipeline** - A filter that transforms every line
  (upper-case it, renumber it, reverse it) and works in the middle of a pipe:
  `cat f | ./yours | sort | head`.
  * **Skills:**
    * Composability - reading stdin and writing stdout, nothing else
    * Why stray output on stdout breaks the next program in the pipe
* **FizzBuzz, The Filter** - Same rules as before, but the numbers are no
  longer `1` through `100` in order.  They arrive on stdin - arbitrary, out of
  order, negative, huge, with blank lines mixed in - one per line, and for each
  one you print `Fizz`, `Buzz`, `FizzBuzz`, or the number itself.
  * **Skills:**
    * Turning a program that *generates* its own data into one that *processes*
      someone else's
    * More practice with `%`, including what it does to negative numbers
    * Validating a line before calling `int()` on it
    * The payoff of stdout/stderr - a bad line is a complaint on stderr, not a
      crash
  * **Discussion:** Try it with `seq 1 100 | ./fizzbuzz.py`, then with `shuf`
    in between, and confirm you get the same set of answers.
* **Count and Total** - Rebuild `wc -l`, then sum a column of numbers piped in
  from another program.
  * **Skills:**
    * A running counter
    * `int()` on messy real-world input
    * Skipping blank lines

## Module 7: Working With Text

* **Slicing Strings Apart** - Use `split()`, `join()`, `strip()`, `upper()`,
  `lower()`, `replace()`, `startswith()`, and `find()` on real lines of text.
  * **Skills:**
    * `.split()`
    * `.join()`
    * `.strip()`
    * `.upper()` / `.lower()`
    * `.replace()`
    * `.startswith()`
    * `.find()`
* **Your Own cut** - Given a CSV (the kind a spreadsheet exports), pull out
  named columns and print a clean report.
  * **Skills:**
    * `split(",")` to parse a CSV line
    * Indexing fields by position
    * Treating the header row specially
    * Doing spreadsheet-style work from the command line

## Module 8: Functions

* **Define and Call** - Write a function that takes an argument, does the work,
  and `return`s a value; call it several times.
  * **Skills:**
    * `def` to define a function
    * Parameters
    * `return` vs `print`
    * Local variables
* **Build a Toolbox** - Refactor an earlier filter so each step is its own
  function, plus a `main()` and default parameter values.
  * **Skills:**
    * Refactoring into single-purpose functions
    * `main()` as an entry point
    * Default parameter values
    * Reusing code instead of copy-pasting
  * **Discussion:** A good one to do to your FizzBuzz filter: a `fizzbuzz(n)`
    function that returns a string, and a loop that does nothing but read,
    call, and print.

## Module 9: Dictionaries

* **Lookup Tables** - Rewrite the Secret Decoder Ring using a dictionary
  instead of two parallel strings and `.index()`.  The point of the challenge
  is the comparison - the same problem, most of the code gone, and no more
  searching for a position.
  * **Skills:**
    * Dictionaries: keys and values
    * `d[key]` to look something up
    * `.get()` with a default
    * `KeyError`
    * Looping with `.items()`
    * Building a dict from two sequences
  * **Discussion:** Other lookup tables worth mentioning: HTTP status codes,
    port numbers.
* **Capstone: The Report** - Read a data file, count occurrences with a
  dictionary, sort the results, and write a formatted report.
  * **Skills:**
    * Counting occurrences with a dictionary
    * Sorting results
    * Combining argv, stderr, stdout, and functions in one program
    * Every earlier skill, together, in the shape of a program you would
      actually write at a job

