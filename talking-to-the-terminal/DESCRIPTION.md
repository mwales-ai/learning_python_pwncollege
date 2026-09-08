# Talking to the Terminal

Most Python books spend their first hundred pages inside the language and only
later mention that programs talk to the outside world.  We are going to do it
now, because it is what makes a program *useful* instead of a toy.

By the end of this module your programs will be able to:

* Read what somebody types, with `input()`.
* Turn that text into numbers, with `int()`.
* Send answers to one place and progress messages to another - **standard
  output** and **standard error**.
* Report success or failure to the shell with an **exit code**.
* Take their input from the **command line** instead of asking for it.

Those last three are the ones that no beginner book covers this early, and
they are the ones that turn your programs into things that can be used *by
other programs*.  That is the whole idea behind Unix: little tools that each
do one thing, wired together.  You met the wiring in Linux Luminarium.  Now
you get to build tools that plug into it.

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
