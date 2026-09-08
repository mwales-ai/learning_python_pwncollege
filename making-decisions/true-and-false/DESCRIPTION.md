# True and False

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
>>> big_enough = 5 > 3
>>> big_enough
True
>>> print(f"big enough: {big_enough}")
big enough: True
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

## The `in` operator

`in` asks whether something appears inside a list or a string:

```
>>> "hunter2" in ["password", "123456", "hunter2"]
True
>>> "cat" in "concatenate"
True
>>> "z" in "hello"
False
```

And `not in` is the opposite, written the way you would say it:

```
>>> password not in COMMON
True
```

This is enormously useful and you will use it constantly.

## Name your conditions

When a decision has several parts, do not cram them into one giant `if`:

```
if (username == "root" or username == "admin") and len(password) >= 8 and password not in COMMON:
```

That is correct and nobody can read it.  Give each part a name:

```
name_ok = username == "root" or username == "admin"
long_enough = len(password) >= 8
not_common = password not in COMMON

allowed = name_ok and long_enough and not_common
```

Now the last line reads like a sentence.  Better still, when it comes out
`False` and you do not know why, you can **print each part** and see
immediately which one is the problem.  That is the debugging technique this
challenge is really teaching.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Operators and Expressions](https://python.swaroopch.com/op_exp.html)

# Instructions

Write a login checker that shows its working.

Read two lines:

```
line 1     a username
line 2     a password
```

Then print exactly four lines:

```
username ok: <True or False>
password long enough: <True or False>
not a common password: <True or False>
login allowed: <True or False>
```

The rules:

* **username ok** - the username is `root` or `admin`.  Nothing else.
* **password long enough** - it is at least 8 characters.  `len()` gives you
  the length.
* **not a common password** - it is *not* one of these five:

  ```
  password    123456    hunter2    letmein    qwerty
  ```

* **login allowed** - all three of the above are true.

So for username `admin` and password `hunter2`:

```
username ok: True
password long enough: False
not a common password: False
login allowed: False
```

Do not write `if` statements that print the words `True` and `False`
yourself.  Work out each condition as a value, put it in a variable, and let
the f-string print it.  That is the whole point of the challenge - and it is
far less typing.

```
/challenge/run ./login.py
```
