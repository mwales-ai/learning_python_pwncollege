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
  * **Skills:** the `>>>` prompt, variable naming rules, `=` as assignment,
                `exit()`
* **String Concatenation** - Join two ciphertext variables with `+`, then pass
  the result to a `secret_decoder()` function to reveal the flag.  Still
  entirely in the interpreter.
  * **Skills:** strings as values, `+` concatenation, `len()`, calling a
                function with an argument
* **Hello Hackers** - Create `hello.py` with a single `print()` call and run it
  with `python hello.py`.
  * **Skills:** a text editor, saving a `.py` file, `python file.py`, a program
                is just text
* **Run It Yourself** - Add a `#!/usr/bin/env python3` shebang, `chmod +x` your
  script, and run it as `./hello.py`.
  * **Skills:** the shebang line, `chmod +x`, running `./script.py`
* **Tippy Tipper** - Turn a tip calculator with hard-coded numbers into one
  that asks for the subtotal and the tax and tip *percentages*, then reports
  each as an amount plus the total.  The judge runs it three times with random
  subtotals, so echoing the percentages back will not pass.
  * **Skills:** `input()`, `float()`, string vs. numeric `*`, `round()`,
                hard-coding
* **Variables and f-strings** - Store values in variables and print a sentence
  built from them with an f-string.
  * **Skills:** variables, strings vs. numbers, f-strings, `+ - * / // %`
* **Why Are We Yelling?** - Read a line of text and shout it back with the
  vowels censored out: `* S*W * D*CK **T*NG * C*K*`.
  * **Skills:** `.upper()`, `.replace()`, string immutability, reading piped
                stdin
* **Birthday Banner** - Centre a birthday message inside an 80 column banner of
  `*` characters.
  * **Skills:** string replication with `*`, `len()`, `//` and `%`, `.title()`
* **Debug Me** - You are given a program that will not run (bad indentation,
  unbalanced quote, typo'd name, wrong capitalization).  Fix it until it runs.
  * **Skills:** reading tracebacks, `SyntaxError` vs `NameError`, fixing one
                error at a time

## Module 2: Talking to the Terminal

* **Say My Name** - Use `input()` to read a name and greet the user.
  * **Skills:** interactive programs, `input()` always returns a string
* **Number Cruncher** - Read two numbers from the user, convert them with
  `int()`, and print the results of some math.
  * **Skills:** `int()`, why `"3" + "4"` is `"34"`
* **Hex to Decimal** - Read a hexadecimal number like `1f`, `0xDEAD`, or `ff00`
  and print its decimal value, then go the other way with `hex()`.
  * **Skills:** `int(text, 16)`, hex digits and `0x` prefixes, `f"{n:02X}"`,
                `hex()`, `int(text, 2)`
  * **Discussion:** Why hex exists at all - one hex digit is exactly 4 bits,
    one byte is exactly 2 hex digits - and why every hex dump, memory address,
    color code, and MAC address you will ever see in security work is written
    this way.
* **Two Kinds of Output** - Print the answer on stdout and your debug chatter
  on stderr with `print(..., file=sys.stderr)`.  Prove it by running `./prog >
  out.txt` and seeing only the chatter on screen.
  * **Skills:** `print(..., file=sys.stderr)`, stdout vs stderr, output
                redirection
* **Exit Codes** - Use `sys.exit(0)` and `sys.exit(1)` to report success or
  failure, then check with `echo $?`.
  * **Skills:** `sys.exit(code)`, `echo $?`, `&&` and `||`
* **Command Line Arguments** - Read `sys.argv` so your program takes its input
  from the command line instead of asking.
  * **Skills:** `sys.argv`, `argv[0]` is the program name, args arrive as
                strings, `len(sys.argv)`

## Module 3: Making Decisions

* **If and Else** - Branch on a comparison and print one of two answers.
  * **Skills:** `if`/`else`, indentation as a block, `==` vs `=`
* **The elif Ladder** - Turn a number into a letter grade (or a password
  strength, or a D&D damage tier).
  * **Skills:** `elif` chains, first match wins, branch order
* **The Quadratic Formula** - Solve `ax^2 + bx + c = 0` for real, branching on
  the sign of the discriminant to print two roots, one vertex root, or
  `NO ROOTS`.
  * **Skills:** `elif` on a computed value, `**0.5`, combining `sys.argv` with
                branching, checking argument count
* **True and False** - Combine conditions with `and`, `or`, and `not` to
  validate input.
  * **Skills:** booleans, comparison operators, `and`/`or`/`not`, `in`,
                short-circuit evaluation
* **The Guessing Game** - A `while` loop that keeps asking until the player
  guesses the secret number, printing "too high" or "too low" each time - the
  first challenge that feels like a real *game*.
  * **Skills:** `while` loops, loop conditions, `break`

## Module 4: Loops and Lists

* **Counting Loops** - Use `for i in range(...)` to print a countdown, a times
  table, and a triangle of stars.
  * **Skills:** `for`, `range()` with 1, 2, and 3 arguments, a negative step
* **FizzBuzz** - The classic.  Print the numbers 1 to 100, one per line, but
  print `Fizz` for multiples of 3, `Buzz` for multiples of 5, and `FizzBuzz`
  for multiples of both.
  * **Skills:** `%`, the divisibility test `n % 3 == 0`, loop + `if`/`elif`,
                branch order
  * **Discussion:** This exact problem is famous as a screening question handed
    to new grads and new software engineers in job interviews - not because it
    is hard, but because it quickly shows whether someone can turn a
    plain-English rule into working code.  You are doing it in week one.
* **Lists** - Build a list, index it, slice it, `append()` to it, and take its
  `len()`.
  * **Skills:** creating and indexing a list, zero-based and negative indexes,
                `.append()`, `IndexError`
* **Loop Over a List** - Walk a list to find the biggest item, the total, and
  the average.
  * **Skills:** the accumulator pattern, `for item in list:`,
                `sum()`/`min()`/`max()`
* **Secret Decoder Ring** - You are handed the key to a substitution cipher -
  one line of original characters, and underneath it what each was turned into
  - followed by a pile of intercepted messages to decode.  The real lesson is
  that a position in one line maps to the same position in the other.
  * **Skills:** looping over string characters, `.index()`, guarding with `in`,
                the accumulator pattern
  * **Discussion:** Substitution ciphers are genuinely ancient - Caesar used
    one - and this is the first challenge whose output is something you would
    actually want to read.  We come back to this problem in the dictionaries
    module, where it gets much shorter.

## Module 5: Files

* **Read a File** - Open a file, `read()` the whole thing, print it.
  * **Skills:** `open()`, file paths, `FileNotFoundError`
* **Write a File** - Write your answer to a file instead of the screen, and
  verify it with `cat`.
  * **Skills:** `"w"` mode, that `"w"` truncates, `with open(...) as f:`
* **Line by Line** - Loop over a file one line at a time and process each one.
  * **Skills:** `for line in f:`, the trailing `\n`, `.strip()`
* **Hangman** - Build the actual game.  The secret word is pulled out of a
  wordlist file by line number, you get six wrong guesses, and correct letters
  fill in the blanks.
  * **Skills:** reading a file while counting, `break`, the newline-on-the-end
                bug
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
  * **Skills:** `"a"` mode, reading one file while writing another, not
                clobbering your input

## Module 6: Unix Filters

* **Read From Standard Input** - Loop over `sys.stdin` so your program works
  with both `cat data.txt | ./prog` and typed input ending in Ctrl-D.
  * **Skills:** looping over `sys.stdin`, stdin as just another file, what a
                filter is
* **Write Your Own grep** - Print only the lines that contain a given string
  (taken from `sys.argv`).
  * **Skills:** `sys.argv` + stdin + `if` + `in`, exit status 0 vs 1
* **In the Middle of a Pipeline** - A filter that transforms every line
  (upper-case it, renumber it, reverse it) and works in the middle of a pipe:
  `cat f | ./yours | sort | head`.
  * **Skills:** composability, stdin in and stdout out, nothing else
* **FizzBuzz, The Filter** - Same rules as before, but the numbers are no
  longer `1` through `100` in order.  They arrive on stdin - arbitrary, out of
  order, negative, huge, with blank lines mixed in - one per line, and for each
  one you print `Fizz`, `Buzz`, `FizzBuzz`, or the number itself.
  * **Skills:** processing data instead of generating it, `%` on negatives,
                validating input, stderr for bad lines
  * **Discussion:** Try it with `seq 1 100 | ./fizzbuzz.py`, then with `shuf`
    in between, and confirm you get the same set of answers.
* **Count and Total** - Rebuild `wc -l`, then sum a column of numbers piped in
  from another program.
  * **Skills:** counters, `int()` on messy input, skipping blank lines

## Module 7: Working With Text

* **Slicing Strings Apart** - Use `split()`, `join()`, `strip()`, `upper()`,
  `lower()`, `replace()`, `startswith()`, and `find()` on real lines of text.
  * **Skills:** `.split()`, `.join()`, `.strip()`, `.upper()`/`.lower()`,
                `.replace()`, `.startswith()`, `.find()`
* **Your Own cut** - Given a CSV (the kind a spreadsheet exports), pull out
  named columns and print a clean report.
  * **Skills:** `split(",")`, indexing fields, handling the header row

## Module 8: Functions

* **Define and Call** - Write a function that takes an argument, does the work,
  and `return`s a value; call it several times.
  * **Skills:** `def`, parameters, `return` vs `print`, local variables
* **Build a Toolbox** - Refactor an earlier filter so each step is its own
  function, plus a `main()` and default parameter values.
  * **Skills:** refactoring into functions, `main()`, default parameter values,
                reuse over copy-paste
  * **Discussion:** A good one to do to your FizzBuzz filter: a `fizzbuzz(n)`
    function that returns a string, and a loop that does nothing but read,
    call, and print.

## Module 9: Dictionaries

* **Lookup Tables** - Rewrite the Secret Decoder Ring using a dictionary
  instead of two parallel strings and `.index()`.  The point of the challenge
  is the comparison - the same problem, most of the code gone, and no more
  searching for a position.
  * **Skills:** dict keys and values, `d[key]`, `.get()`, `KeyError`,
                `.items()`, building a dict from two sequences
  * **Discussion:** Other lookup tables worth mentioning: HTTP status codes,
    port numbers.
* **Capstone: The Report** - Read a data file, count occurrences with a
  dictionary, sort the results, and write a formatted report.
  * **Skills:** counting with a dict, sorting results, combining argv, stderr,
                stdout, and functions


