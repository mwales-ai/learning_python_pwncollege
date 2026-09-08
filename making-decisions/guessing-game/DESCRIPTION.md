# The Guessing Game

Time to build a game.

Every program you have written runs a fixed number of steps and stops.  This
one keeps going until something happens - and it does not know in advance how
long that will take.  That is what a `while` loop is for.

## while

```
while <something is true>:
    <do this again>
```

A `for` loop over `range(10)` runs ten times, and you knew that before you
started.  A `while` loop runs until its condition stops being true, which
might be the first time round or the four hundredth.

The standard shape for "keep going until something happens" is:

```
while True:
    ...
    if <we are done>:
        break
```

`while True:` is a loop that never ends by itself.  `break` jumps out of it
immediately, skipping the rest of the loop body.  This is not a hack - it is
the normal way to write this.

## Counting how many times round

The counter goes **before** the loop and is increased **inside** it:

```
guesses = 0
while True:
    guesses = guesses + 1
    ...
```

Put `guesses = 0` inside the loop by mistake and it resets every single time,
so your count is always 1.  Watch for that.

(`guesses += 1` is shorthand for the same thing, and you will see it
everywhere.)

## The hazard

A `while` loop that never becomes false runs forever.  The usual cause is
reading the input **outside** the loop:

```
guess = int(input())      # read ONCE
while True:
    if guess < secret:    # tests the same number forever
        print("too low")
```

That never changes `guess`, so it never gets anywhere.  If your terminal locks
up, press `Ctrl-C` to kill it.  The judge gives your program 10 seconds and
then stops it and fails the test case, so an infinite loop shows up as a
timeout rather than a hang.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)

# Instructions

Write the number guessing game.

Read the secret number on the first line, then read guesses one per line until
one of them is right.

For each guess, print exactly one line:

```
<guess> is too low
<guess> is too high
<guess> is correct!
```

When the guess is correct, stop reading and print one final line:

```
It took you <number of guesses> guesses.
```

The count includes the winning guess.

So for this input:

```
50
25
75
60
55
50
```

your program prints:

```
25 is too low
75 is too high
60 is too high
55 is too high
50 is correct!
It took you 5 guesses.
```

Two things to watch:

* Compare **numbers**, not text.  As strings, `"9"` is greater than `"10"`,
  because comparison goes character by character and `9` comes after `1`.
  `int()` both the secret and every guess.
* The input always contains a correct guess eventually, so you do not need to
  handle running out of input.

```
/challenge/run ./guess.py
```

## Now play it properly

The secret comes from the input so the judge can check your game.  For an
actual game, let the computer pick:

```
import random
secret = random.randint(1, 100)
```

Then run it and play - it is a genuinely decent game, and you wrote it. If you
always guess the middle of what is left, you can beat any number from 1 to 100
in seven guesses.  That strategy has a name, **binary search**, and it is one
of the most important ideas in computer science.
