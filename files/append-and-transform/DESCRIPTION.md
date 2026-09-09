# Append and Transform

Two things left in this module: adding to a file without destroying it, and
reading one file while writing another.

## "a" for append

`"w"` empties the file.  `"a"` does not:

```
with open("/tmp/log.txt", "a") as f:
    f.write("something happened\n")
```

Everything already in the file stays, and your line goes on the end.  If the
file does not exist yet, `"a"` creates it.

This is how every log file on your machine works.  `/var/log/` is full of
files that programs have been appending to for weeks.  If they opened them
with `"w"` you would only ever have the most recent line.

One letter.  Enormous difference.  Get it wrong here and the judge will tell
you, because it puts a header into the log file *before* running your
program, and checks that the header is still there afterwards.

## Two files at once

Nothing stops you having a file open for reading and another open for writing
at the same time:

```
with open(input_path, "r") as source:
    with open(output_path, "a") as dest:
        for line in source:
            dest.write(line.strip().upper() + "\n")
```

Read a line, transform it, write it out.  Repeat.  That is the shape of every
file conversion program ever written.

## Never write back into the file you are reading

```
with open(path, "r") as source:
    with open(path, "w") as dest:      # DO NOT
```

Opening the same file for writing empties it *while you are still reading it*.
You end up with an empty file and no data, and there is no undo.

The way this is done properly is: read the input, write a **new** file, and
only when that has finished successfully, replace the original.  For now,
just always read one file and write a different one.

## .upper() and friends make new strings

```
>>> name = "hopper"
>>> name.upper()
'HOPPER'
>>> name
'hopper'
```

`name` did not change.  Strings are **immutable** - nothing you call on a
string modifies it, they all return a *new* string.  If you want to keep it,
assign it:

```
name = name.upper()
```

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)
* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)

# Instructions

Read a file, upper-case every line, and **append** the result to a log that
already has something in it.

Your program reads two lines on standard input:

```
line 1     the path of the input file to read
line 2     the path of the log file to append to
```

For every line in the input file, append an upper-cased copy to the log file.
Then print exactly one line on standard output:

```
appended <N> lines to <the log path>
```

The log file already exists and already contains these two lines:

```
=== EXISTING LOG HEADER ===
this line was here before your program ran
```

**Those two lines must still be there when you are finished.**  That is the
whole test.  If you open the log with `"w"` instead of `"a"`, they will not
be, and the judge will tell you the file's first line is wrong.

So for input file `/challenge/data/names.txt` containing:

```
turing
lovelace
hopper
```

your program prints:

```
appended 3 lines to /tmp/challenge_log.txt
```

and the log file ends up containing:

```
=== EXISTING LOG HEADER ===
this line was here before your program ran
TURING
LOVELACE
HOPPER
```

Strip each line before you upper-case it, and remember to add the `\n`
yourself - `write()` will not.

```
/challenge/run ./appender.py
```
