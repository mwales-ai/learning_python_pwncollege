# Secret Decoder Ring

A **substitution cipher** is one of the oldest ways to hide a message.  You
pick a replacement for every letter, then swap each letter of your message for
its replacement.  Julius Caesar really did use one, which is why shifting every
letter down the alphabet by a fixed amount is still called a Caesar cipher.

Here is a tiny one.  The top line is the characters we started with, and the
bottom line is what each one gets turned into:

```
abcde
xyzwv
```

So `a` becomes `x`, `b` becomes `y`, `c` becomes `z`, and so on.  The word
`bead` would be encoded as `yvxw`.

Notice what makes this work: **position**.  `b` is at position 1 of the top
line, so we look at position 1 of the bottom line and find `y`.  That is the
whole trick, and you already know how to find something's position in Python.

## Looping over a string

You have been looping over a range of numbers.  You can also loop directly
over a string, and Python hands you one character at a time:

```
>>> for ch in "cat":
...     print(ch)
...
c
a
t
```

## Finding a position with .index()

The `.index()` method tells you where something first appears:

```
>>> "abcde".index("c")
2
>>> "xyzwv"[2]
'z'
```

Read those two lines together, because that is the cipher in a nutshell.

There is a catch.  If you ask for something that is not there, your program
does not politely return -1, it crashes:

```
>>> "abcde".index("q")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

So check first with the `in` operator you met in the last module:

```
>>> "q" in "abcde"
False
```

## Building up a string a piece at a time

This is the **accumulator pattern** again, the same idea as adding up a total,
except we are adding onto a string instead of a number.  Start with an empty
string and glue pieces onto the end:

```
>>> result = ""
>>> for ch in "cat":
...     result = result + ch.upper()
...
>>> result
'CAT'
```

The empty string `""` is to string building what `0` is to adding up numbers:
the thing you start with before you have anything.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 4 - Lists](https://automatetheboringstuff.com/3e/chapter4.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)
  * [Data Structures](https://python.swaroopch.com/data_structures.html)

# Instructions

You have intercepted some encoded messages, and you have gotten hold of the
key.  Write a program that decodes them.

Your program reads everything from `input()`, one line at a time, in this
order:

```
line 1     the original characters
line 2     what each of those characters was turned into
line 3     how many secret messages follow (a number)
after that that many encoded messages, one per line
```

For each encoded message, print the decoded message on its own line.  Print
nothing else on standard output.

**Read the key carefully.**  It describes how the message was **encoded**:
original on top, replacement underneath.  You are going the other way, so for
each character of a secret message, find it in the **second** line and replace
it with the character at the same position of the **first** line.

Any character that does not appear in the key was never changed, so leave it
exactly as it is.  Spaces and punctuation usually fall into this group.

Here is a complete example.  If your program is given this input:

```
abcde
xyzwv
2
yvxw
x zxy
```

it should print:

```
bead
a cab
```

Note the space in the second message.  A space is not in the key, so it stays
a space.  If your program crashes with `ValueError: substring not found`, that
is the mistake you have made.

When your program works, make it executable and hand it to the judge:

```
chmod +x ./decoder.py
/challenge/run ./decoder.py
```

Your program has to get every message in every test case right to earn the
flag.
