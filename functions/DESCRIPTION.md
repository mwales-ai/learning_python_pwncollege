# Functions

You have written a lot of programs now.  Some of them are getting long, and
some of them repeat themselves.

A **function** is a named piece of code that takes some values in, does one
job, and hands a result back.  Everything you have been calling - `len()`,
`int()`, `print()`, `open()` - is a function that somebody else wrote.  Now you
write your own.

Functions buy you four things:

* **A name for an idea.**  `encrypt_msg(p)` says what it does. You can usually
  get a good idea of what a chunk of code in a function does by looking at the
  name. 
* **Write it once.**  Copy-pasted code has to be fixed everywhere, and you will
  always miss one. A popular theme in programming is _D.R.Y._ which stands for
  Don't Repeat Yourself. If you see a chunk of code that is duplicated, turn it
  into a function.
* **Fix it Once.**  Nobody is perfect, your code will have bugs from time to
  time.  The only thing worse than fixing a bug is finding it and fixing it
  again later in a different part of your program.
* **Reuse.**  You can call a function as many timea as you want.  Anytime your
  code needs to repeat what the function does, call it instead.  Saves us all
  that typing.  Maybe you even use this function later again in a different
  program too.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 3 - Functions](https://automatetheboringstuff.com/3e/chapter3.html)
* A Byte of Python
  * [Functions](https://python.swaroopch.com/functions.html)
