# Dictionaries

The last new idea in this dojo, and one of the most useful in programming.

A **list** holds things in order, and you get at them by position - `words[0]`.
That works when the position is what you care about.

A **dictionary** holds things by **name**.  You get at them by whatever label
makes sense:

```
ports = {22: "ssh", 80: "http", 443: "https"}
counts = {"root": 42, "hopper": 3}
```

You have already needed this twice without having it:

* The Secret Decoder Ring searched a string with `.index()` for every single
  character.  With a dict, it is a lookup.
* Counting how many times each thing appears is impossible with what you had.
  With a dict, it is one line.

Those are the two challenges in this module: the decoder ring, rewritten - and
then the capstone, which pulls together every habit in this dojo into one
program of the kind you would actually be paid to write.

## Why lookups matter

`.index()` **searches**.  It starts at the beginning and walks until it finds a
match, so a table twice as big takes twice as long.

A dictionary **jumps straight to the answer**, and it takes the same time
whether it holds ten entries or ten million.  The technique behind that is
called *hashing*, and it is the same idea underneath password storage, file
checksums, and git.  You do not need to know how it works to use it - but it
is worth knowing that it is not magic, and that it is why dictionaries are
everywhere.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 5 - Dictionaries and Structuring Data](https://automatetheboringstuff.com/3e/chapter5.html)
* A Byte of Python
  * [Data Structures](https://python.swaroopch.com/data_structures.html)
