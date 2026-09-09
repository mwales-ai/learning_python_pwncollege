# Functions

You have written a lot of programs now.  Some of them are getting long, and
some of them repeat themselves.

A **function** is a named piece of code that takes some values in, does one
job, and hands a result back.  Everything you have been calling - `len()`,
`int()`, `print()`, `open()` - is a function that somebody else wrote.  Now you
write your own.

Functions buy you four things:

* **A name for an idea.**  `fizzbuzz(n)` says what it does.  Twelve lines of
  `if` and `%` in the middle of a loop does not.
* **Write it once.**  Copy-pasted code has to be fixed everywhere, and you will
  always miss one.
* **Somewhere to look when it breaks.**  If the FizzBuzz answers are wrong, the
  bug is in `fizzbuzz()`.  Not somewhere in two hundred lines.
* **Reuse.**  A function that *returns* a value can be used anywhere.  One that
  prints can only ever do the one thing.

That last point is the heart of this module.  **`return` is not `print`.**
`print` shows a human something.  `return` hands a value back to the code that
asked for it.  Beginners reach for `print` because they can see it working;
the moment you need that value for anything else, you have to rewrite the
function.

By the end of this module you will take a program you already wrote and
rearrange it into pieces - which is what real programming mostly is.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 3 - Functions](https://automatetheboringstuff.com/3e/chapter3.html)
* A Byte of Python
  * [Functions](https://python.swaroopch.com/functions.html)
