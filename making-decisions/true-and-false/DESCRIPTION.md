# Password Complexity

Every signup form you have ever used has one of these: a little meter that
scores your password as you type it.  You are going to build the logic
behind one.

Here is something that is not obvious until somebody says it out loud:

**A comparison is a value.**

```
>>> 5 > 3
True
>>> 5 == 3
False
```

`5 > 3` is not special if-flavoured syntax.  It is an expression that produces
`True`, exactly the way `5 + 3` produces `8`.  Which means you can put it in a
variable:

```
>>> long_enough = 5 > 3
>>> long_enough
True
>>> print(f"long enough: {long_enough}")
long enough: True
```

`True` and `False` are the two **boolean** values, named after George Boole.
Python capitalises them.  `true` is not a thing and will get you a `NameError`.

## Combining conditions

| Operator | True when |
|----------|-----------|
| `A and B` | **both** A and B are true |
| `A or B` | **at least one** of them is true |
| `not A` | A is false |

```
>>> age = 16
>>> age >= 13 and age <= 19
True
>>> not (age == 16)
False
```

A note on `or`: in English "or" often means one or the other but not both.  In
programming it always means **at least one**, including both.

## Booleans are numbers wearing a costume

This is the part that surprises everybody:

```
>>> True + True + False
2
>>> True == 1
True
>>> False == 0
True
```

`bool` is secretly a kind of `int`.  `True` **is** `1` and `False` **is**
`0`, not just something that looks like it.  Which means if you have five
`True`/`False` conditions and want to know how many of them hold, you do
not need a single `if` - you just add them:

```
>>> has_length = True
>>> has_number = True
>>> has_symbol = False
>>> has_length + has_number + has_symbol
2
```

## The `in` operator

`in` asks whether something appears inside a string (or a list):

```
>>> "cat" in "concatenate"
True
>>> "z" in "hello"
False
```

## Checking for any of several characters

There is no single function for "does this string contain a digit" at this
point in the dojo - but you already have everything you need.  Chain `in`
checks together with `or`, one per digit:

```
>>> password = "Hunter2"
>>> has_number = ("0" in password or "1" in password or "2" in password
...               or "3" in password or "4" in password or "5" in password
...               or "6" in password or "7" in password or "8" in password
...               or "9" in password)
>>> has_number
True
```

It is long, but it is only **one idea** - "at least one digit is in here" -
so it still gets exactly one name.  The same pattern works for any small set
of characters you are checking for, no matter how many `in` checks it takes.

## Checking for mixed case without a loop

`.upper()` and `.lower()` return a whole new string - they do not tell you
directly whether a string is "mixed case".  But comparing the original
against each of them does:

```
>>> password = "Hunter2"
>>> password != password.lower()   # True means it HAS an uppercase letter
True
>>> password != password.upper()   # True means it HAS a lowercase letter
True
```

If converting to lowercase *changed* the string, something in there was
uppercase.  If converting to uppercase *changed* it, something was
lowercase.  Mixed case means both are true at once.

## Name your conditions

When a decision has several parts, do not cram them into one giant
expression:

```
score = (len(password) > 8) + (len(password) > 16) + (password != password.lower() and password != password.upper()) + ("0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password) + ("!" in password or "@" in password or "#" in password or "$" in password or "%" in password)
```

That is correct and nobody can read it, least of all you in a week.  Give
each part a name:

```
long_enough = len(password) > 8
very_long = len(password) > 16
mixed_case = password != password.lower() and password != password.upper()
has_number = "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password

score = long_enough + very_long + mixed_case + has_number
```

Now each line reads like a sentence, and when the total comes out wrong you
can print each part and see immediately which one is to blame.  That is the
debugging technique this challenge is really teaching.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Operators and Expressions](https://python.swaroopch.com/op_exp.html)

# Instructions

Write a password complexity checker.

Read one line: a password.  Award one point for each of these that is true,
and print exactly six lines:

```
longer than 8: <True or False>
longer than 16: <True or False>
mixed case: <True or False>
has a number: <True or False>
has a symbol: <True or False>
score: <total points, 0 to 5>
```

The rules:

* **longer than 8** - the password is **more than** 8 characters.  Exactly 8
  does not count.
* **longer than 16** - the password is **more than** 16 characters.  Exactly
  16 does not count.
* **mixed case** - it contains at least one uppercase letter **and** at
  least one lowercase letter.
* **has a number** - it contains at least one digit, `0` through `9`.
* **has a symbol** - it contains at least one of these five characters:
  `! @ # $ %`.  Any other punctuation does not count.
* **score** - how many of the five rules above are true.  `0` to `5`.

So for password `Hunter2!`:

```
longer than 8: False
longer than 16: False
mixed case: True
has a number: True
has a symbol: True
score: 3
```

`Hunter2!` is exactly 8 characters, which is why both length rules say
`False` - this is the same "exactly on the boundary" trap as the elif
ladder, and it is checked on purpose.

And for `SuperSecurePass123!`:

```
longer than 8: True
longer than 16: True
mixed case: True
has a number: True
has a symbol: True
score: 5
```

Do not write `if` statements that print the words `True` and `False`
yourself.  Work out each condition as a value, put it in a variable, and let
the f-string print it - and let addition compute `score` for you.  That is
the whole point of the challenge.

```
/challenge/run ./complexity.py
```
