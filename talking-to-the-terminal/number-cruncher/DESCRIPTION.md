# Number Cruncher

Here is a program that looks obviously correct and is obviously wrong:

```
first = input()
second = input()
print(first + second)
```

Feed it `12` and `30` and it prints `1230`.

## input() gives you text, not numbers

`input()` always returns a **string**.  `"12"` is not `12`.  They look the
same when printed, and they behave completely differently:

```
>>> "12" + "30"
'1230'
>>> 12 + 30
42
```

`+` on two strings glues them together.  On two numbers it adds them.  Python
is doing exactly what you asked; you just asked for the wrong thing.

And some things simply do not work at all:

```
>>> "12" * "30"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```

A `TypeError` almost always means you have a string where you wanted a number.

## int()

`int()` converts text into a whole number:

```
>>> int("12") + int("30")
42
```

Convert **once, up front**, and give the result a name:

```
first = int(input())
second = int(input())
```

Now `first` and `second` are numbers everywhere else in your program.  If you
sprinkle `int()` around later instead, you will end up with half your program
working on text and the other half on numbers, which is a miserable bug to
find.

`int()` is fussy on purpose.  `int("12.5")` and `int("banana")` both raise a
`ValueError` rather than guessing.  (`float()` is the one that handles `12.5`.)

## A reminder about the operators

| Operator | `17` and `5` | Note |
|----------|--------------|------|
| `+` | `22` | |
| `-` | `12` | |
| `*` | `85` | |
| `/` | `3.4` | always a float |
| `//` | `3` | drops the fraction |
| `%` | `2` | the remainder |
| `**` | `1419857` | 17 to the power of 5 |

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 1 - Python Basics](https://automatetheboringstuff.com/3e/chapter1.html)
* A Byte of Python
  * [Operators and Expressions](https://python.swaroopch.com/op_exp.html)

# Instructions

Read two whole numbers, one per line, and print seven lines of arithmetic.

For input `17` and `5`, print exactly:

```
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 // 5 = 3
17 % 5 = 2
17 ** 5 = 1419857
```

Note that the numbers and the operator are echoed back on each line, in the
order shown, with single spaces around everything.  An f-string makes this
much less painful than gluing strings together by hand.

Watch the `/` line - it is a float, so `8 / 2` prints as `4.0`, not `4`.  That
is correct, do not try to hide it.

```
/challenge/run ./crunch.py
```
