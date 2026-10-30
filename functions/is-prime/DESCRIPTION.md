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

## is_factor(): one small function, given to you

Here is a function that answers one tiny question - does `divisor` divide
`number` evenly?

```python
def is_factor(number, divisor):
    return number % divisor == 0
```

That is the entire function.  Add it to your script exactly as written.
Everything else in this challenge - including `is_prime()` itself - is
something you are going to build by **calling `is_factor()` over and over**
from inside a `while` loop, not by writing one giant function that does
everything at once.

## Calling it from a loop

Here is that pattern put to work on a different question: how many
divisors does `12` have in total?

```python
def count_divisors(number):
    count = 0
    divisor = 1
    while divisor <= number:
        if is_factor(number, divisor):
            count = count + 1
        divisor = divisor + 1
    return count
```

`count_divisors(12)` returns `6` - `1`, `2`, `3`, `4`, `6`, and `12` all
divide it evenly.  Notice the shape: a loop variable (`divisor`) starts
somewhere sensible, `is_factor()` gets asked about it on every trip through
the loop, and `divisor` increases by one each time until the loop's
condition says stop.

`is_prime()` is going to have that exact same shape.  It just asks a
different question (is there **any** divisor that divides evenly, instead
of counting all of them) and gives up the moment it finds one - which
means `return` instead of `count = count + 1`.

## The speedup almost nobody is shown

An `is_prime()` built the obvious way - checking every divisor from `2` up
to `n - 1` - works, but does far more work than it needs to.  Think about
`n = 100`.  If a number bigger than `10` divides `100` evenly - say, `50` -
then `100 / 50 = 2`, and `2` is smaller than `10` and *also* divides `100`
evenly.  Divisors always come in pairs that multiply back to `n`, and one
member of every pair is never bigger than the number's own square root.

That means you only ever need to check divisors up to `sqrt(n)` - if
nothing up to there divides `n`, nothing bigger will either, because its
"partner" would already have been caught.  You do not even need a square
root function to use this: `divisor` up to `sqrt(n)` is exactly the same
set of numbers as `divisor * divisor <= n`, and that version only uses
multiplication, which you already have.  Use that as your loop's stopping
condition instead of `divisor < n`.

For a small `n` the difference is invisible.  For a six-digit `n` it is the
difference between instant and noticeably slow - and the judge for this
challenge uses numbers large enough that it matters.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 4 - Functions](https://automatetheboringstuff.com/3e/chapter4.html)
* A Byte of Python
  * [Functions](https://python.swaroopch.com/functions.html)
* [Wikipedia: RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) -
  skim the "Key generation" section to see these two ideas, prime numbers
  and `%`, show up again.

# Instructions

Include the `is_factor()` function from above in your script, exactly as
given. Then write `is_prime(n)` yourself - a `while` loop that calls
`is_factor(n, divisor)` once per divisor, stopping at `divisor * divisor <=
n` instead of `divisor < n`, and returning the moment it finds one, the
way `count_divisors()` above called `is_factor()` but did not write its
own copy of the `%` check.

Handle numbers less than `2` before the loop even starts, the way "What
makes a number prime" defined them - they are not prime, full stop, and no
amount of looping will discover a divisor for a number that has none.  If
you skip this, `is_prime(0)`, `is_prime(1)`, and every negative number will
come back `True` by accident: with `divisor` starting at `2`, `divisor *
divisor <= n` is already false before the loop runs even once, so a loop
that only returns `False` *inside* itself never gets the chance to.

Use `is_prime()` to answer a second question: given a number, find the
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
