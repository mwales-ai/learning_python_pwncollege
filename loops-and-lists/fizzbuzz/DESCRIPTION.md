# FizzBuzz

This one is famous.

Print the numbers from 1 to 100, one per line, except:

* if the number divides evenly by **3**, print `Fizz` instead
* if it divides evenly by **5**, print `Buzz` instead
* if it divides evenly by **both**, print `FizzBuzz` instead

That is the whole problem.  It is a children's counting game.

## Why it is famous

FizzBuzz is the classic screening question handed to new graduates and new
software engineers in job interviews.  Not because it is hard - you can see
that it is not - but because a surprising number of people who *say* they can
program cannot turn a plain English rule into working code.

It gets used because it takes two minutes, it needs nothing but a loop and
some branching, and there is nowhere to hide.

You are doing it in your first month.

## The modulus operator

`%` gives the **remainder** after division:

```
>>> 17 % 5
2
>>> 15 % 5
0
>>> 15 % 3
0
```

A remainder of zero means it divided evenly.  So "n is a multiple of 3" is:

```
n % 3 == 0
```

Get comfortable with that shape.  It is how you test for even numbers
(`n % 2 == 0`), how you wrap around a list, and how the decoder ring you are
about to write handles the alphabet.

## The actual trap

Here is where most people go wrong.  Think carefully about the *order* of your
branches:

```
if n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
```

This looks reasonable and it is wrong.  Remember from the elif ladder: **first
match wins**.  When `n` is 15, the very first test is true, so it prints `Fizz`
and never looks at the rest.  The `FizzBuzz` branch can never run at all.

And the failure is sneaky - the first fourteen lines are perfect.  You have to
get to line 15 before anything looks wrong.  This is exactly why interviewers
like the question.

**Test for both first.**

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)

# Instructions

Print the numbers from 1 to 100, one per line, with the FizzBuzz rules
applied.

Your program reads nothing.  The first few lines and the interesting ones:

```
1
2
Fizz
4
Buzz
Fizz
7
...
14
FizzBuzz
16
...
```

Line 15 is `FizzBuzz`.  Line 100 is `Buzz`.  There are exactly 100 lines.

Spelling and capitalisation matter: `Fizz`, `Buzz`, `FizzBuzz`.

```
/challenge/run ./fizzbuzz.py
```

We come back to this problem in the filters module, where instead of counting
to 100 you will apply the same rules to whatever numbers arrive on standard
input - in any order, including negative ones.
