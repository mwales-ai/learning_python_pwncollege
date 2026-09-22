# The Quadratic Formula

Time to make the `elif` ladder do something you would actually want a
computer for.

You probably met this in algebra class: given `a`, `b`, and `c` in

```
a*x^2 + b*x + c = 0
```

the quadratic formula finds the value(s) of `x` that make the equation true:

```
x = (-b + sqrt(b^2 - 4ac)) / (2a)
x = (-b - sqrt(b^2 - 4ac)) / (2a)
```

Two versions of the same formula, one with `+` and one with `-`, because a
square root has two answers: `sqrt(9)` is both `3` and `-3`, since `3*3` and
`(-3)*(-3)` are both `9`.

This is not just a classroom exercise.  Physics engines use it to work out
when a thrown object hits the ground.  Graphics code uses it to find where a
ray hits a sphere.  It shows up anywhere something curves.

## The discriminant decides how many answers there are

The expression under the square root, `b^2 - 4ac`, is called the
**discriminant**.  Everything interesting about this problem comes down to
its sign, which is exactly the kind of three-way decision `elif` is for:

* **Positive** - the square root is a real number, and the `+` and `-`
  versions of the formula give two *different* answers.  Two roots.
* **Zero** - the square root is `0`, so `+ 0` and `- 0` are the same thing.
  Both versions of the formula collapse to one answer.  Graphically, the
  curve just barely touches zero at its vertex instead of crossing it - hence
  calling this one the **vertex root**.
* **Negative** - you would be taking the square root of a negative number.
  Python's `**0.5` cannot do that with ordinary numbers, and neither can you
  on paper.  There is no real answer.  No roots.

```python
discriminant = b * b - 4 * a * c

if discriminant < 0:
    # no real roots
elif discriminant == 0:
    # exactly one root - the vertex
else:
    # two roots
```

Look familiar?  It is the same shape as the elif ladder you just wrote for
letter grades - test in order, first match wins, `else` catches whatever is
left.

## Square roots without `import`

You do not need `math.sqrt()` for this.  Raising a number to the power
`0.5` is the same operation:

```
>>> 9 ** 0.5
3.0
>>> 2 ** 0.5
1.4142135623730951
```

Combined with `round()` from Tippy Tipper, that is everything you need.

## Reading the coefficients from the command line

`a`, `b`, and `c` belong on the command line, not typed at a prompt - they
are settings for what to solve, exactly the kind of thing Command Line
Arguments talked about.  Remember the two things that always trip people up
with `sys.argv`:

* `sys.argv[0]` is your own program's name.  The first real argument is
  `sys.argv[1]`.
* Everything in `sys.argv` is a **string**.  `float()` it before doing math.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)
  * [Operators](https://python.swaroopch.com/op_exp.html) covers `**`

# Instructions

Write a program that solves `a*x^2 + b*x + c = 0` for `x`, given `a`, `b`,
and `c` as three command line arguments, in that order.

```
./quadratic.py 1 -5 6
```

**You may assume `a` is never `0`.**  If it were, this would not be a
quadratic equation any more, and that is a different problem for a different
day.

Compute the discriminant, `b^2 - 4ac`, and print output that depends on its
sign:

**Discriminant is negative** - print exactly one line:

```
NO ROOTS
```

**Discriminant is zero** - print exactly two lines: the words `VERTEX ROOT`,
then the one root, rounded to 2 decimal places with `round()`:

```
VERTEX ROOT
2.0
```

**Discriminant is positive** - print exactly two lines: the root using `+`
first, then the root using `-`, each rounded to 2 decimal places:

```
3.0
2.0
```

So for `1 -5 6` above (`a=1, b=-5, c=6`), the discriminant is
`(-5)^2 - 4*1*6 = 1`, which is positive, and the full output is:

```
3.0
2.0
```

## Check your argument count

Your program is only ever handed exactly three coefficients.  If it is run
with the wrong number of arguments - two, four, or none - print something
useful to standard error and exit with status `1` instead of trying to solve
anything:

```python
import sys

if len(sys.argv) != 4:
    print("need exactly 3 arguments: a b c", file=sys.stderr)
    sys.exit(1)
```

The exact wording of that error message is up to you - it goes to standard
error and is not graded on its contents - but the exit status **is**
checked, and remember that a program that never calls `sys.exit()` reports
success (`0`) automatically.

Do not print `sys.argv[0]`.

```
/challenge/run ./quadratic.py
```
