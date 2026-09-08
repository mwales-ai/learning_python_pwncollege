# Debug Me

Nobody writes working code the first time.  What separates people who can
program from people who cannot is almost entirely how they react to an error
message: whether they read it, or whether they panic and start changing things
at random.

So let us practice reading them.

There is a broken program at `/challenge/broken.py`.  It has four bugs in it.
Copy it to your home directory and fix them:

```
cp /challenge/broken.py ~/fixed.py
chmod +x ~/fixed.py
python3 ~/fixed.py
```

## How to read a traceback

When Python gives up, it prints something like this:

```
  File "/home/hacker/fixed.py", line 8
    print(f"It was written for the {machin}.")
                                    ^^^^^^
NameError: name 'machin' is not defined. Did you mean: 'machine'?
```

Read it from the **bottom up**:

* The last line is what went wrong: `NameError`, something is not defined.
* Above it, the `^^^^^^` points at exactly which part of the line.
* Above that is the line of code itself, and the line number.

Modern Python often guesses the fix for you - `Did you mean: 'machine'?` is
Python telling you the answer.  Read the whole message before you touch
anything.

## Two families of error

This distinction matters more than it looks:

* A **SyntaxError** or **IndentationError** means Python could not even
  understand the file.  It never ran *any* of it.  You will not see output from
  the correct lines above the mistake, because nothing ran at all.
* A **NameError**, or most other errors, happen while the program is running.
  Everything before the bad line already happened, so you *do* see that output.

That is why fixing these four bugs feels like the program slowly comes to
life: first nothing at all, then the first line, then two.

## Errors come one at a time

Python stops at the first problem it hits.  Fix it, run again, and the *next*
one appears.  This is normal.  Do not try to spot all four at once - fix the
one you are being told about, then rerun.

The four bugs in this program, in the order Python will show them to you:

1. Something is indented that should not be.  Indentation is not decoration in
   Python, it means "this is inside that".
2. A string that never closes its quote.
3. A misspelled variable name.
4. A function name with the wrong capitalization.  `Print` and `print` are two
   different names, and Python only has one of them.

## Further Reading

* A Byte of Python
  * [First Steps](https://python.swaroopch.com/first_steps.html)
* Automate the Boring Stuff with Python
  * [Chapter 3 - Functions](https://automatetheboringstuff.com/3e/chapter3.html)
    has a good section on error messages

# Instructions

Copy `/challenge/broken.py`, fix all four bugs, and make it run.  When it is
working it prints exactly these three lines:

```
Ada Lovelace wrote the first program in 1843.
It was written for the Analytical Engine.
She is called the first programmer.
```

Do not just delete the broken lines and type these three `print()` calls
yourself.  You would pass, and you would have learned nothing.  Fix what is
actually wrong.

Remember to make your fixed copy executable, then:

```
/challenge/run ./fixed.py
```
