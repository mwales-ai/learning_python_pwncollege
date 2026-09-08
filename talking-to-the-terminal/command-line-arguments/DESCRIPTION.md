# Command Line Arguments

Every real tool on your system takes its input from the command line:

```
grep hacker /etc/passwd
chmod +x myprogram.py
head -5 words.txt
```

Nobody runs `grep`, waits for a prompt, and types the pattern.  The whole
point of a command line tool is that you can say everything in one line - and
that means a *script* can use it too, without a human sitting there typing.

Your programs can do this.

## sys.argv

`sys.argv` is a **list** of the words on the command line that started your
program:

```
import sys
```

If somebody runs:

```
./calc.py 6 7
```

then `sys.argv` is:

```
['./calc.py', '6', '7']
```

Notice two things, and the first one catches everybody exactly once:

* **`sys.argv[0]` is your own program's name.**  The first real argument is
  `sys.argv[1]`, not `sys.argv[0]`.
* **Arguments are strings.**  `sys.argv[1]` is `'6'`, not `6`.  Same as
  `input()`, same fix: `int()`.

`len(sys.argv)` tells you how many words there were, counting the program
name.  So "the user gave me two arguments" is `len(sys.argv) == 3`.

## Quoting

The shell splits on spaces before your program ever sees anything, so this is
three arguments:

```
./greet.py Grace Brewster Hopper
```

and this is one:

```
./greet.py "Grace Brewster Hopper"
```

That is the shell's doing, not Python's.  You met this in Linux Luminarium.

## Arguments or input()?

Both are useful and they are for different jobs:

* **Arguments** are settings: *what* to work on, *how* to do it.  They are
  short, and you want them in your shell history so you can press up-arrow and
  run it again.
* **Standard input** is the data itself, which might be enormous and usually
  comes from another program or a file.

`grep hacker /etc/passwd` is the pattern as an argument and the data from a
file.  `cat /etc/passwd | grep hacker` is the pattern as an argument and the
data on standard input.  Same tool, same split.

## Further Reading

* A Byte of Python
  * [Standard Library](https://python.swaroopch.com/stdlib.html)
* Automate the Boring Stuff with Python
  * [Chapter 1 - Python Basics](https://automatetheboringstuff.com/3e/chapter1.html)

# Instructions

Write a calculator that takes its two numbers from the command line instead of
asking for them.

It is run like this:

```
./calc.py 6 7
```

and prints exactly three lines:

```
6 + 7 = 13
6 * 7 = 42
6 - 7 = -1
```

Your program reads nothing from standard input.  Both numbers come from
`sys.argv`, and remember that they arrive as strings.

Do not print `sys.argv[0]`.  It is the path your program was started with,
which is different depending on how it was run, so it is not part of the
answer.

Test it yourself with a few different pairs before handing it in - especially
one where the subtraction goes negative:

```
./calc.py 6 7
./calc.py 100 25
./calc.py 0 9
```

```
/challenge/run ./calc.py
```
