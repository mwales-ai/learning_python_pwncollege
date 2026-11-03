# FizzBuzz

This one is famous.

Print the numbers from `start` to `stop`, one per line, except:

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

## The range comes from the command line now

`start` and `stop` arrive as `sys.argv[1]` and `sys.argv[2]`, the same way
the coefficients did in The Quadratic Formula.  Both are strings, same as
always - `int()` them before doing math.

## Checking text before you convert it

Up to now, a bad command line argument has just been allowed to crash the
program with a traceback.  This time, check first.  `.isdigit()` tells you
whether every character in a string is a digit `0`-`9`:

```
>>> "123".isdigit()
True
>>> "12.5".isdigit()
False
>>> "abc".isdigit()
False
```

`.isdigit()` says `False` for a negative number too, because `-` is not a
digit - `"-5".isdigit()` is `False`, even though `-5` is a perfectly good
whole number.  `.lstrip("-")` removes leading `-` characters (the same
family as `.strip()`, which you already know, but only from the left
side), so strip the sign off first and check what is left:

```
>>> "-5".lstrip("-")
'5'
>>> "-5".lstrip("-").isdigit()
True
```

That one line - `text.lstrip("-").isdigit()` - is "is this text a valid
whole number, negative sign allowed" without ever calling `int()` on
something that might not be one.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)

# Instructions

Print the numbers from `start` to `stop`, **inclusive**, one per line, with
the FizzBuzz rules applied.  `start` and `stop` arrive as two command line
arguments, in that order, and either one may be negative.

Check the arguments before using them, in this order, and stop at the
first problem you find.  Print the message to standard error and exit
with status `1`:

| Problem | Message |
|---------|---------|
| not exactly 2 arguments | `Usage: fizzbuzz.py <start> <stop>` |
| `start` is not a whole number | `start must be a whole number` |
| `stop` is not a whole number | `stop must be a whole number` |
| `start` is greater than `stop` | `start must be less than or equal to stop` |

Only once all four checks pass should you print anything on standard
output.

So `./fizzbuzz.py 1 15` prints:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

and `./fizzbuzz.py 10 5` prints nothing on standard output, and on standard
error:

```
start must be less than or equal to stop
```

`start` can equal `stop` - that is a real one-line range, not an error.
`0` counts as a whole number.  A negative `start` is fine as long as it is
not bigger than `stop`: `./fizzbuzz.py -5 5` is a real 11-line range.

```
/challenge/run ./fizzbuzz.py
```

We come back to this problem in the filters module, where instead of a
range you choose yourself, you will apply the same rules to whatever
numbers arrive on standard input - in any order, including negative ones.
