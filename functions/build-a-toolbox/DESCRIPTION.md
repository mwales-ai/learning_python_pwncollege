# Build a Toolbox

Go and open your FizzBuzz filter from the Unix Filters module.

It works.  It is also one long strip of code where reading the input, deciding
whether the input is usable, and working out the FizzBuzz answer are all
tangled together in a single loop.  You are going to take it apart.

This is **refactoring**: changing how a program is arranged without changing
what it does.  It is a large fraction of what working programmers actually
spend their time on.

## One job each

```
def is_number(text):
    """True if text is a whole number, minus sign allowed."""
    return text.lstrip("-").isdigit()

def fizzbuzz(n):
    """Return the FizzBuzz word for n, or n itself as a string."""
    ...

def main(argv):
    for line in sys.stdin:
        ...
```

Now each piece can be understood, and fixed, on its own.  If the answers are
wrong, the bug is in `fizzbuzz`.  If junk lines are mishandled, it is in
`is_number`.  You are never reading the whole program at once.

Notice `fizzbuzz` **returns** the word rather than printing it.  That is what
makes it reusable - `main` decides where it goes.  A version that printed could
never be used for anything else.

## Default parameter values

```
def fizzbuzz(n, fizz_at=3, buzz_at=5):
```

`fizz_at` and `buzz_at` now have **defaults**.  Anyone can still call
`fizzbuzz(9)` and get the old behaviour, but `fizzbuzz(9, 4, 6)` changes the
rules.

This is how you add a feature without breaking anything that already exists.
Every call written before the change keeps working.

Parameters with defaults must come **after** the ones without, or it is a
`SyntaxError` - Python would have no way to tell which argument was which.

## Docstrings

The string just under the `def` line is a **docstring**.  It is not a comment;
it is attached to the function and Python can show it to you:

```
>>> help(fizzbuzz)
```

One line saying what the function returns is plenty.

## main() and the magic incantation

```
def main(argv):
    ...

if __name__ == "__main__":
    main(sys.argv)
```

That last bit looks like nonsense, and here is what it actually does.

When you run a file directly, Python sets `__name__` to `"__main__"`.  When
another program **imports** your file, `__name__` is the file's name instead.
So the guard means: *only run the filter if I am the program being run.*

Which means somebody can now write `import fizzbuzz` and use your
`fizzbuzz()` function in their own program, without your input loop firing.
Your file has become a **library** as well as a tool.

Every serious Python file you will ever read has this at the bottom.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 3 - Functions](https://automatetheboringstuff.com/3e/chapter3.html)
* A Byte of Python
  * [Modules](https://python.swaroopch.com/modules.html)

# Instructions

Rewrite your FizzBuzz filter as a set of functions, and make the divisors
configurable.

The behaviour is exactly the same as the FizzBuzz filter, with one addition:

* Run with **no arguments**, it uses 3 and 5, exactly as before.
* Run with **two arguments**, it uses those instead:

  ```
  ./fizzbuzz.py 4 6
  ```

  Now multiples of 4 are `Fizz`, multiples of 6 are `Buzz`, and multiples of
  both are `FizzBuzz`.

Numbers arrive on standard input, one per line.  For each one print the word
or the number on standard output.  For any line that is not a whole number,
print this on standard error and carry on:

```
skipping: <the line>
```

**This challenge checks both streams.**

So `./fizzbuzz.py` given `12` prints `Fizz`, and `./fizzbuzz.py 4 6` given
`12` prints `FizzBuzz`.

Your program must contain:

* a function that returns the FizzBuzz word for a number, **with the two
  divisors as parameters that default to 3 and 5**
* a `main()` function
* the `if __name__ == "__main__":` guard

The judge can only see what your program prints, so it cannot check that you
actually split it into functions.  Do it anyway.  The next challenge is the
capstone, and you will want the practice.

```
/challenge/run ./fizzbuzz.py
```
