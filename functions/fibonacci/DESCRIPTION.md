# Fibonacci Numbers

Every function you have written so far does its job and hands back an
answer.  There is nothing stopping a function from asking **itself** for
part of that answer - as long as it knows when to stop.  That is
**recursion**, and it is the idea behind this challenge.

## A function that calls itself: factorial

The classic first example is the factorial - `5! = 5 * 4 * 3 * 2 * 1`, the
product of every whole number from `n` down to `1`.  Written recursively:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Trace `factorial(4)` by hand and watch it unfold:

```
factorial(4) = 4 * factorial(3)
             = 4 * (3 * factorial(2))
             = 4 * (3 * (2 * factorial(1)))
             = 4 * (3 * (2 * (1 * factorial(0))))
             = 4 * (3 * (2 * (1 * 1)))
             = 24
```

Every call waits on the call below it, all the way down to `factorial(0)`,
which answers directly without calling anyone else.  Then the answers
multiply their way back up.

Every recursive function needs exactly these two pieces:

* **A base case** - the simplest possible input, answered directly, with no
  further recursive call.  `factorial(0)` returning `1` is what stops the
  chain.
* **A recursive case** - the function calls itself on a *smaller* version of
  the problem, then uses that result to build its own answer.

Leave out the base case and there is nothing to ever stop the calls -
Python eventually gives up with a `RecursionError`, which is recursion's
version of an infinite loop.

## Fibonacci: two base cases, two calls

The Fibonacci sequence starts `0, 1, 1, 2, 3, 5, 8, 13, 21, 34...` - each
number is the sum of the two before it.  Mathematically:

```
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2)      for n >= 2
```

This is still recursion, but it is shaped a little differently than
`factorial`:

* It needs **two** base cases, not one - `F(0)` and `F(1)` both have to be
  answered directly, since the recursive case reaches back two steps, not
  just one.
* The recursive case makes **two** recursive calls instead of one, and adds
  them together - `fib(n - 1) + fib(n - 2)`, both of which have to finish
  before you have anything to add.

That is the whole shape of it.  Everything else - the base cases, the
recursive case, the `return` - works exactly like `factorial` did.

## The catch: this gets slow, fast

Try tracing `fib(5)` the way you traced `factorial(4)`, and something
uncomfortable shows up: `fib(5)` calls `fib(4)` and `fib(3)`.  `fib(4)`
*also* calls `fib(3)` - a second, completely separate time, which
recomputes everything `fib(3)` needs from scratch.  Go one level further
and `fib(2)` gets computed three separate times.  The duplication compounds
every level down, and the total number of calls grows exponentially with
`n` - roughly `1.6^n` of them.

`fib(30)` makes over two and a half million function calls to produce one
seven-digit answer.  Nothing is broken; the function is correct at every
step.  It is simply redoing enormous amounts of work it already did a
moment ago, because nothing is written down anywhere to remember it.

This exact shape - an innocent-looking piece of code whose work explodes
exponentially on certain inputs - is a real category of security bug
called an **algorithmic complexity attack**.  Some regular expression
engines have inputs that trigger this same exponential blowup (look up
"ReDoS" sometime), and it is also how some old hash table implementations
could be knocked over by an attacker who crafted inputs on purpose. You do
not need to fix the duplication for this challenge - write `fib()` exactly
as recursively as `factorial` above, two base cases and two calls - but
file the *shape* of the problem away. You will meet ways to fix it later.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 3 - Functions](https://automatetheboringstuff.com/3e/chapter3.html)
* A Byte of Python
  * [Functions](https://python.swaroopch.com/functions.html)
* [Wikipedia: ReDoS](https://en.wikipedia.org/wiki/ReDoS) - the regular
  expression flavor of exactly the blowup described above.

# Instructions

Write a recursive `fib(n)` function, the same shape as `factorial` above
but with two base cases and two recursive calls, and use it to print the
`n`th Fibonacci number.

Your program takes one command line argument - a whole number `n`, which
will always be `0` or greater.  Print exactly one line:

```
fibonacci(<n>) = <the nth Fibonacci number>
```

So `./fib.py 10` prints:

```
fibonacci(10) = 55
```

and `./fib.py 0` prints:

```
fibonacci(0) = 0
```

`fib()` must actually be recursive - calling itself for the two smaller
cases - not a `while` loop in disguise.  The judge cannot see how you wrote
it, but a non-recursive `fib()` skips the entire point of this challenge.
Do it anyway.

```
/challenge/run ./fib.py
```
