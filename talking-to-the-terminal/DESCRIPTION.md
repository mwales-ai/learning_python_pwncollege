# Talking to the Terminal

This module guides you on how to make useful programs that can interact with
the user instead of having all of the data part of the source code of your
program. The same functions that make your program interactive with users will
allow your program to work with other programs.

By the end of this module your programs will be able to:

* Read what somebody types, with `input()`.
* Turn that text into numbers, with `int()`.
* Send answers to one place and progress messages to another - **standard
  output** and **standard error**.
* Report success or failure to the shell with an **exit code**.
* Write a unix-style filter program
* Take their input from the **command line** instead of asking for it.

Those last three are the ones that no beginner book covers this early, and
they are the ones that turn your programs into things that can be used *by
other programs*.  That is the whole idea behind Unix: little tools that each
do one thing, wired together.

## One rule for this whole dojo

**Never give `input()` a prompt.**

```
name = input("What is your name? ")     # NO
name = input()                          # yes
```

The prompt text goes to standard output, mixed in with your actual answer.
The judge is reading standard output, so a prompt makes your very first line
wrong before you have done anything else.

This is not the judge being fussy.  It is the same reason `ls | wc -l` works:
if `ls` chattered at you on standard output, `wc` would count the chatter.
Once you have done the Two Kinds of Output challenge you will know where a
prompt is supposed to go.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 1 - Python Basics](https://automatetheboringstuff.com/3e/chapter1.html)
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Basics](https://python.swaroopch.com/basics.html)
  * [Input and Output](https://python.swaroopch.com/io.html)
