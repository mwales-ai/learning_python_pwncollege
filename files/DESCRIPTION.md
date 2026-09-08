# Files

Everything you have written so far forgets everything the moment it exits.
Files are how a program remembers, and how it gets at information somebody
else produced.

This is where Python stops being a thing you practice and starts being a tool
you use.  A spreadsheet exported as a text file, a log from a web server, a
list of words, the notes you took last week - all of them are just files, and
all of them are now yours to process.

In this module you will learn to:

* Open a file and read the whole thing at once.
* Write a file, and understand why opening it the wrong way silently destroys
  what was already in it.
* Walk a file one line at a time, which is how you handle a file too big to
  hold in your head or in memory.
* Add to the end of a file without clobbering it, and read one file while
  writing another.

There is one bug in this module that catches absolutely everybody at least
once: **a line read from a file still has its newline on the end.**  When
something is one character longer than it should be, that is why.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)
* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)
