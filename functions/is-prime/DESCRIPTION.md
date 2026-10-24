# Is It Prime?

Prime numbers are not just a math-class memory - they are the entire reason
modern encryption works.  RSA, the algorithm protecting half the internet's
traffic, picks two enormous primes and multiplies them together, betting
that nobody can factor the result back apart in a human lifetime.  Before
any of that, you need a way to answer one question: is this number prime?

## What makes a number prime

A number is **prime** if it is greater than 1 and nothing divides it evenly
except 1 and itself.  `7` is prime - only `1` and `7` divide it evenly.  `8`
is not - `2` and `4` divide it evenly too.  `0` and `1` are not prime; they
are their own special case, excluded by definition.

`%` is how you ask "does this divide evenly?" - you have been using it since
Variables and f-strings:

```
>>> 8 % 2
0
>>> 7 % 2
1
```

A remainder of `0` means it divides evenly.  So "does `d` divide `n`
evenly?" is just `n % d == 0`.

## Building is_prime() with a while loop

The straightforward plan: try every number from `2` up to `n - 1` as a
possible divisor.  If any of them divides `n` evenly, `n` is not prime.  If
none of them do, it is.

```python
def is_prime(n):
    if n < 2:
        return False

    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return False
        divisor = divisor + 1

    return True
```

Notice `return` inside a `while` loop works exactly like it does anywhere
else - the moment `is_prime` finds a divisor, it hands back `False` and
stops right there, loop and all.  You do not need a flag variable to
remember what happened; returning **is** how you report it.

## The speedup almost nobody is shown

That function works, but it does far more work than it needs to.  Think
about `n = 100`. If a number bigger than `10` divides `100` evenly - say,
`50` - then `100 / 50 = 2`, and `2` is smaller than `10` and *also* divides
`100` evenly. Divisors always come in pairs that multiply back to `n`, and
one member of every pair is never bigger than the number's own square root.

That means you only ever need to check divisors up to `sqrt(n)` - if
nothing up to there divides `n`, nothing bigger will either, because its
"partner" would already have been caught. You do not even need a square
root function to use this: `divisor` up to `sqrt(n)` is exactly the same
set of numbers as `divisor * divisor <= n`, and that version only uses
multiplication, which you already have.

```python
def is_prime(n):
    if n < 2:
        return False

    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor = divisor + 1

    return True
```

For a small `n` the difference is invisible. For a six-digit `n` it is the
difference between instant and noticeably slow - and the judge for this
challenge uses numbers large enough that it matters.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 3 - Functions](https://automatetheboringstuff.com/3e/chapter3.html)
* A Byte of Python
  * [Functions](https://python.swaroopch.com/functions.html)
* [Wikipedia: RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) -
  skim the "Key generation" section to see these two ideas, prime numbers
  and `%`, show up again.

# Instructions

Write an `is_prime(n)` function, using the while-loop-and-`%` technique
above, and use it to answer a second question: given a number, find the
first prime number that is **greater than or equal to it**.

Your program takes one command line argument - a whole number, `n`, which
may be negative, zero, or positive.

* If `n` itself is prime, print exactly one line:

  ```
  <n> is prime
  ```

* If `n` is not prime, print exactly two lines: that it is not, and the
  next prime number at or after it:

  ```
  <n> is not prime
  the next prime is <answer>
  ```

So `./prime.py 17` prints:

```
17 is prime
```

and `./prime.py 20` prints:

```
20 is not prime
the next prime is 23
```

Do not search downward, and do not assume `n` is positive - `./prime.py -5`
and `./prime.py 0` are both real test cases, and the answer to both is `2`.

```
/challenge/run ./prime.py
```
