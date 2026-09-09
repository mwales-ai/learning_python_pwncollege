# Learning Python

Welcome.  This dojo teaches you Python - not as a list of language features to
memorise, but as a **tool you will actually reach for**.

It was built for the
[Westshore Wildcat Computer Science Club](https://github.com/westshorecsclub/WildcatCSClub/tree/main),
and it is aimed at high school students who have never programmed before.  You
do not need any prior experience.  You do not need to install anything - the
challenges run in a Linux machine in your browser.

## What makes this dojo different

Most Python books spend a hundred pages inside the language before your
program ever talks to anything outside itself.  We do it backwards on purpose:

* By the **second module** you are handling standard input, standard output,
  standard error, exit codes, and command line arguments.  That is the
  vocabulary every Linux program speaks.
* By the **fifth module** you are reading and writing files.
* By the **sixth** you are writing Unix filters - programs that sit in the
  middle of a pipeline, and you will rebuild `grep` and `wc` yourself.

Classes and decorators and comprehensions can wait.  Being able to point a
program at a pile of data and get an answer out cannot.

The idea is that if you stop halfway through this dojo, you still walk away
able to do something real.

## Who this is useful for

* **Future computer science students.**  Most college programs expect you to
  pick up a language on your own, in a lab that meets an hour a week.  Arriving
  already comfortable is an enormous head start.
* **Anybody interested in cyber security.**  Every tool you will use is a
  command line program that reads input and writes output.  Understanding that
  model is most of the battle, and several challenges here are built around
  security ideas - ciphers, password rules, hex dumps, hashing.
* **Everyone else.**  The single most useful thing in this dojo might be
  challenge 26, where you pull columns out of a spreadsheet export from the
  command line.  That skill outlives any particular job.

## What you should do first

If you have not already, go and do these:

1. **Start Here** - teaches you how the pwn.college platform itself works.
2. **Linux Luminarium** - teaches you the Linux shell.

That second one matters more than you would think.  This dojo leans on the
shell constantly - pipes, redirection, `chmod`, `$?`, `&&` - and it is much
more fun when those are already familiar.  You can work through Linux
Luminarium and this dojo side by side.

## How the challenges work

Each challenge gives you something to read and then something to write.  You
write a Python program in your home directory, make it executable, and hand it
to the judge:

```
chmod +x ./myprogram.py
/challenge/run ./myprogram.py
```

The judge runs your program on several sets of hidden input and checks that
the output is exactly right.  Get them all correct and it prints the flag.

Your program's output has to match exactly - spelling, capitalisation,
punctuation and spacing all count.  That is not the judge being picky.  It is
the actual standard: a program in a pipeline has to produce precisely what the
next program expects, and "close enough" is how real systems break.

A few things worth knowing before you start:

* **Anything you print to standard error is ignored by the judge.**  Leave your
  debugging messages in - `print("got here", file=sys.stderr)` costs you
  nothing.  Module 2 explains why this works.
* **Never give `input()` a prompt.**  `input("Name: ")` prints that prompt to
  standard output, which is where your answer is supposed to go.
* Your home directory `/home/hacker` keeps its contents between challenges, so
  your earlier programs are still there when you want to look at them.

## Books

You do not need one, but a reference helps.  Both of these are free to read
online:

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/3e/)
  by Al Sweigart
* [A Byte of Python](https://python.swaroopch.com/) by Swaroop Chitlur

Individual challenges link to the relevant chapter.

## Stuck?

Read the error message.  Read it again, from the bottom up - the last line
says what went wrong, and modern Python often suggests the fix.  The **Debug
Me** challenge in the first module is entirely about this, because it is the
skill that separates people who can program from people who cannot.

And then ask somebody in the club.  That is what it is for.
