# Working With Text

Most of the data in the world is text, and most of it is nearly but not quite
in the shape you need.  This module is the toolbox for that.

There is nothing conceptually hard here - it is a set of methods to learn.  But
these are the ones you will use every single day, and the second challenge is
possibly the most immediately useful thing in this whole dojo: pulling columns
out of a spreadsheet export, from the command line, over a file somebody
emailed you.

One idea underpins all of it:

**Strings are immutable.**  Nothing you call on a string changes it.  Every
method hands you back a *new* string and leaves the original alone:

```
>>> name = "hopper"
>>> name.upper()
'HOPPER'
>>> name
'hopper'
```

A line like `text.strip()` sitting on its own does absolutely nothing.  You
have to keep the result:

```
text = text.strip()
```

That mistake will cost everybody in the club at least one afternoon.  Now it
has cost you a paragraph instead.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 6 - Manipulating Strings](https://automatetheboringstuff.com/3e/chapter6.html)
* A Byte of Python
  * [Data Structures](https://python.swaroopch.com/data_structures.html)
