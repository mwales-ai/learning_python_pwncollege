# If and Else

```
if attempt == SECRET:
    print("access granted")
else:
    print("access denied")
```

Exactly one of those two lines will print.  Never both, never neither.

## The shape

```
if <something that is true or false>:
    <do this>
else:
    <otherwise do this>
```

Two things are easy to get wrong and both produce errors:

* The **colon** at the end of the `if` line and the `else` line.  Forget it
  and you get `SyntaxError: expected ':'`.
* The **indentation** of the lines underneath.  That indentation is what says
  "this belongs to the if".  Get it wrong and you get an `IndentationError`,
  or worse, a program that runs but does the wrong thing.

The `else` part is optional.  An `if` with no `else` simply does nothing when
the condition is false.

## == is not =

This is the single most common beginner mistake in every language:

* `=` **assigns**.  `x = 5` means "make x refer to 5".
* `==` **compares**.  `x == 5` means "is x equal to 5?" and produces True or
  False.

Python protects you here.  Writing `if x = 5:` is a `SyntaxError`, so you find
out immediately.  In C and several other languages it quietly compiles and
does something you did not want, and people have lost entire afternoons to it.

## The comparison operators

| Operator | Means |
|----------|-------|
| `==` | equal to |
| `!=` | not equal to |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

They work on strings too, and on strings `==` is **exact**:

```
>>> "hunter2" == "Hunter2"
False
>>> "hunter2" == "hunter2 "
False
```

Different case is a different string.  A trailing space is a different string.
This matters constantly when you are comparing something a person typed.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)

# Instructions

Write a password checker.

The secret password is:

```
hunter2
```

Read one line - the attempt - and print exactly one line:

* `access granted` if the attempt is exactly the password
* `access denied` if it is not

Both messages are all lower case.  The comparison is exact, so `Hunter2`,
`HUNTER2` and `hunter` are all denied.

```
/challenge/run ./check.py
```

## One thing worth saying out loud

This is a fine way to learn `if`, and a **terrible** way to check a password.
The secret is sitting in your source code in plain text - anybody who can read
the file knows the password, so it is not a secret at all.

Real systems never store the password.  They store a **hash** of it: a
scrambled version that is easy to compute and effectively impossible to
reverse.  When you log in, they hash what you typed and compare the hashes.

The judge for these challenges works exactly that way, which is why you cannot
find the expected answers by reading the files in `/challenge`.
