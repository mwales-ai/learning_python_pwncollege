# Learning Python

Welcome.  This dojo teaches you Python - not as a list of language features to
memorize, but as a **tool you will actually reach for** to solve problems.

It was built for the
[Westshore Wildcat Computer Science Club](https://github.com/westshorecsclub/WildcatCSClub/tree/main),
and it is aimed at high school students who have never programmed before.  You
do not need any prior experience.  You do not need to install anything - the
challenges run in a Linux machine in your browser.

## What makes this dojo different

Most Python books spend a hundred pages inside the language before your
program ever talks to anything outside itself. This dojo won't focus on the
terminology, or advanced python topics. It aims to teach some basic concepts,
let your practice writing problems, and give you enough tools that you can
apply python programs to real world problems. Getting your hands on keyboard
and practicing is one of the best ways to really learn.

Many high school curiculums will use online / web-based python systems because
setting up a computer lab and maintaining it with the proper development tools
is difficult and expensive.  The pwn.college platform hosts virtual machines
that more closely show how you would use Python on a real computer, and also
gives you a chance to learn Linux and how to use command line tools.

Using a command line environment may be new to a student that has only used
tablets and mobile phones for a home computer. Learning how interactive
programs work on the command line is important for:

* Many future CS classes will require it
* While difficult to learn at first, it is often more efficient to use
* Many programming contest like [Lockheed Code Quest](https://www.lockheedmartin.com/en-us/who-we-are/communities/codequest.html)
 require basic CLI style input / ouput features
* It's quicker and faster tool for when an engineer needs to apply Python
  to a real world problem / data table.

##  Pre-requisites for this Dojo

If you have not already, go and do these dojos first:

1. **Start Here** - teaches you how the pwn.college platform itself works.
2. **Linux Luminarium** - teaches you the Linux shell. Not required to complete
   but will help you to complete first 6 modules, Perceiving Permissions, and
   Terminal Muxing modules.

## How most challenges work

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
Me** challenge in the first module is entirely about this. The help menu at
the top of the pwn.college page will give you access to an AI chatbot that
understands how the challenges work and should be able to give you guidance
and not spoil the challenges.

Do not use more powerful AI systems like Claude, Chat GPT, and Gemini. While
being extremely helpful, they are way to often and eager to offer you a full
solution, and giving you the answer without getting to do the work yourself
isn't going to make the material stick.

And if you have questions, bring them to our CS club meetings! I can't wait
to help you, or ask somebody in the club.  That is what it is for.
