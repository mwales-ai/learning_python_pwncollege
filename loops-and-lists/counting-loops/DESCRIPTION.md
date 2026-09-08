# Counting Loops

A `while` loop keeps going until something changes.  A `for` loop does
something a **known number of times**, and that turns out to be most of what
you want.

```
for i in range(5):
    print(i)
```

prints `0 1 2 3 4`, each on its own line.

## range()

`range()` produces a sequence of numbers, and it comes in three shapes:

```
range(5)           0 1 2 3 4
range(2, 6)        2 3 4 5
range(1, 10, 2)    1 3 5 7 9
range(5, 0, -1)    5 4 3 2 1
```

* One argument: start at 0, count up to *but not including* it.
* Two arguments: start, stop.
* Three arguments: start, stop, **step**.  A negative step counts down.

## The thing that confuses everybody

**`range()` stops BEFORE the stop value.**

`range(1, 10)` is 1 through 9.  Not 10.  If you want the numbers 1 through 10,
you write `range(1, 11)`.

This looks like a design mistake for about a week and then starts making
sense, because `range(len(mylist))` gives you exactly the valid positions of a
list - which is what you almost always want.

Two consequences worth memorising:

* To include N, write `N + 1` as the stop.
* To count **down** to 1, write `range(n, 0, -1)`.  The stop is 0 because it
  stops before it, so the last number you actually get is 1.

`range(5, 0)` with no step gives you *nothing at all*.  It is already past the
stop, so there is nothing to count.  If a loop mysteriously produces no
output, check this first.

## The loop variable is a real variable

`i` is not just a counter ticking away in the background; you can use it:

```
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

And remember string repetition from the birthday banner - `"*" * 3` is
`"***"`.  Put that in a loop and you have drawn a triangle:

```
for i in range(1, 4):
    print("*" * i)
```

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)

# Instructions

Read one number, `N`, and print three sections.

First the word `Countdown:` on its own line, then the numbers from `N` down to
`1`, one per line.

Then `Times table:` on its own line, then ten lines of `N` times 1 through 10,
in this exact format:

```
N x 1 = ...
```

Then `Triangle:` on its own line, then `N` rows of stars: one star on the
first row, two on the second, up to `N` on the last.

For input `3` the whole output is:

```
Countdown:
3
2
1
Times table:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
Triangle:
*
**
***
```

Each section is a separate `for` loop, and each one needs a different shape of
`range()`.  That is the exercise.

```
/challenge/run ./count.py
```
