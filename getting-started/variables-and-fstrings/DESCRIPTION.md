# Variables and f-strings

A **variable** is a name for a value.  You compute something once, give it a
name, and use the name afterwards:

```
>>> width = 17
>>> height = 6
>>> area = width * height
>>> area
102
```

The `=` here is not the `=` from math class.  It does not mean "these are
equal", it means "work out the thing on the right, and make the name on the
left refer to it."

## f-strings

Putting values into text used to be awkward.  Now you put an `f` in front of
the quote and write `{ }` around anything you want dropped in:

```
>>> name = "Ada Lovelace"
>>> print(f"{name} is measuring a {width} by {height} rectangle.")
Ada Lovelace is measuring a 17 by 6 rectangle.
```

Without the `f` you just get the braces printed literally, which is a very
common first mistake:

```
>>> print("{name} is here")
{name} is here
```

You can put a whole expression inside the braces - `f"area is {width*height}"`
works - but computing into a variable first is usually easier to read, and far
easier to fix when it is wrong.

## The arithmetic operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | add | `17 + 6` | `23` |
| `-` | subtract | `17 - 6` | `11` |
| `*` | multiply | `17 * 6` | `102` |
| `/` | divide | `102 / 2` | `51.0` |
| `//` | integer divide | `17 // 6` | `2` |
| `%` | remainder | `17 % 6` | `5` |
| `**` | power | `2 ** 10` | `1024` |

Two of these surprise everybody:

* **`/` always gives you a float.**  `102 / 2` is `51.0`, not `51`.  Watch for
  that `.0` in your output - it is supposed to be there.
* **`//` throws the fraction away, it does not round.**  `17 // 6` is `2`, and
  so is `19 // 6`.  It is not "round to the nearest".

Together, `//` and `%` are how you break a quantity into pieces.  Seconds into
hours, minutes and seconds is the classic:

```
>>> total = 3725
>>> total // 3600          # how many whole hours
1
>>> (total % 3600) // 60   # what is left, in whole minutes
2
>>> total % 60             # what is left after that
5
```

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 1 - Python Basics](https://automatetheboringstuff.com/3e/chapter1.html)
* A Byte of Python
  * [Basics](https://python.swaroopch.com/basics.html)
  * [Operators and Expressions](https://python.swaroopch.com/op_exp.html)

# Instructions

Write a program that reads nothing and prints a small report.

Start with exactly these four variables:

```
name = "Ada Lovelace"
width = 17
height = 6
total_seconds = 3725
```

Then work out and print these six lines:

```
Ada Lovelace is measuring a 17 by 6 rectangle.
The area is 102 square units.
The perimeter is 46 units.
Half the area is 51.0 square units.
17 divided by 6 is 2 with 5 left over.
3725 seconds is 1 hours, 2 minutes and 5 seconds.
```

Where the numbers come from:

* area is width times height
* perimeter is twice the width plus twice the height
* half the area uses `/`, which is why it shows as `51.0` and not `51`
* "divided by ... with ... left over" is `//` and `%`
* the last line breaks 3725 seconds into hours, minutes and seconds

Yes, you can see the answers above, and yes, you could just print those six
lines and pass.  Do not.  Every number after the first line should come out of
a calculation on those four variables - that is the entire point, and the next
challenge is much harder if you skip it.

Make it executable and hand it in:

```
/challenge/run ./report.py
```
