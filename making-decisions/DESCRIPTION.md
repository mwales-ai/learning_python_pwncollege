# Making Decisions

Every program you have written so far does exactly the same thing every time.
It reads, it calculates, it prints, it stops.  A program that cannot make a
decision cannot react to anything.

This module is about **branching**: looking at a value and choosing what to do
next.

* `if` and `else` - do this, otherwise do that.
* `elif` - a ladder of choices, taken in order.
* `and`, `or`, `not`, and `in` - combining several conditions into one answer.
* `while` - keep doing something *until* a condition changes, which is the
  first time your program controls how many times it repeats.

The mechanical thing to get right is the shape:

```
if something:
    this line is inside
    so is this one
this line is not
```

The **colon** at the end, and the **indentation** underneath, are how Python
knows where a block starts and stops.  Most languages use curly braces for
this; Python uses the layout you were going to write anyway.  Four spaces is
the convention.  Be consistent - mixing tabs and spaces produces errors that
are genuinely hard to see, because the two look identical on screen.

By the end of this module you will write your first program that keeps going
until *something happens* rather than running a fixed number of steps.  That
is a real game.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)
