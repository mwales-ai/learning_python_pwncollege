# FizzBuzz, The Filter

Remember FizzBuzz?  Same rules.  Completely different program.

Back in module 4 your FizzBuzz **made up its own data** - it counted from 1 to
100 because you told it to.  This one **processes somebody else's**.  The
numbers arrive on standard input, and you have no idea what they will be.

That is the difference between an exercise and a tool, and it is the single
most important shift in this dojo.

## What is coming at you

Not 1 to 100 in order.  Expect:

* numbers **out of order**
* **negative** numbers
* **huge** numbers
* lines that are **not numbers at all**

The rules are unchanged: multiples of 3 are `Fizz`, multiples of 5 are `Buzz`,
multiples of both are `FizzBuzz`, everything else is the number itself.  And
the branch order still matters - test for both first.

## Negative numbers and %

You might expect `%` to do something strange with negatives.  In Python it
does not:

```
>>> -3 % 3
0
>>> -7 % 3
2
```

Python's `%` always gives a result with the same sign as the divisor, so
`-3 % 3 == 0` and `-3` is a `Fizz`, exactly as you would want.

This is genuinely a Python nicety.  In C, `-7 % 3` is `-1`, and code that
assumes otherwise has caused real bugs.  Do not carry the assumption between
languages.

While you are here: `0 % 3` and `0 % 5` are both `0`, so zero is a `FizzBuzz`.
That is correct.

## Junk input is the real lesson

```
>>> int("banana")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'banana'
```

If you call `int()` on every line, one bad line **kills your program**.

Think about what that means for a filter.  You are handed a million lines,
line 900,000 is corrupt, and your program dies - having printed nothing useful
and destroyed the run.  Real tools do not behave that way.  They complain
about the line they could not use and **carry on**.

So check before you convert:

```
if not line.lstrip("-").isdigit():
    print(f"skipping: {line}", file=sys.stderr)
    continue
```

* `.isdigit()` says whether a string is all digits.  Careful - it says
  **False** for `"-9"`, which is why we strip a leading minus off first.
* `continue` skips to the next trip round the loop.
* The complaint goes to **standard error**, so the good output flows down the
  pipe uncontaminated while a human still sees what went wrong.

That last point is the whole of module 2 finally paying off.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 8 - Input Validation](https://automatetheboringstuff.com/3e/chapter8.html)
    is the grown-up version of this

# Instructions

Rewrite FizzBuzz as a filter.

Read numbers from standard input, one per line.  For each one print, on
**standard output**:

* `FizzBuzz` if it divides evenly by both 3 and 5
* `Fizz` if it divides evenly by 3
* `Buzz` if it divides evenly by 5
* otherwise the number itself, exactly as a number

For any line that is **not** a whole number, print this on **standard error**
and carry on:

```
skipping: <the line>
```

A leading minus sign is part of a number, so `-15` is a `FizzBuzz`, not junk.

**This challenge checks both streams.**

So for this input:

```
banana
12
not a number
15
7up
20
```

standard output is:

```
Fizz
FizzBuzz
Buzz
```

and standard error is:

```
skipping: banana
skipping: not a number
skipping: 7up
```

Your program must not crash on any input.  Check yourself:

```
seq 1 100 | ./fizzbuzz.py
seq 1 100 | shuf | ./fizzbuzz.py
cat /etc/passwd | ./fizzbuzz.py
```

That last one is all junk, so you should get a hundred complaints on stderr,
no output, and no traceback.

Then try this, which is the whole point of the module:

```
seq 1 100 | shuf | ./fizzbuzz.py 2>/dev/null | sort | uniq -c
```

You should get the same counts as when the numbers were in order, because
your program handles each line on its own merits.

```
/challenge/run ./fizzbuzz.py
```
