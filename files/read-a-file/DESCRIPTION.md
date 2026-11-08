# Hex to Binary

Everything you have written so far forgets everything the moment it exits.
Files are how a program remembers, and how it gets at information somebody
else produced.

## open()

```
f = open("/challenge/data/ports.txt", "r")
contents = f.read()
f.close()
```

`open()` gives you a **file object**.  The `"r"` means you are opening it for
reading.  `.read()` hands back the **entire contents as one string** -
newlines and all.  `.close()` lets go of it.

## Always use `with`

You will almost never see the version above in real code.  This is the one
you want:

```
with open("/challenge/data/ports.txt", "r") as f:
    contents = f.read()
```

The `with` block closes the file for you when it ends - even if something goes
wrong inside and your program crashes.  Forgetting `.close()` is a bug that
does not show up until your program is doing something serious, at which point
it shows up spectacularly.  Get in the habit now.

Note the shape: a colon, and the work indented underneath.  Same as `if` and
`for`.

## When the file is not there

This is the error you will meet most often, for the rest of your life:

```
>>> open("/challenge/data/nope.txt", "r")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/challenge/data/nope.txt'
```

Nine times out of ten it is a typo in the path, or the program is running in a
different directory than you thought.  `pwd` tells you where you are and `ls`
tells you what is actually there.

## sys.stdin is already a file

Here is something that was true the whole time: `sys.stdin` **is** a file
object.  Not something that behaves a little like one - it is the actual
same kind of thing `open()` hands you, just already opened for you before
your program's first line even runs.  That means it has the same `.read()`:

```python
import sys

raw = sys.stdin.read()
```

No `open()`, no `with`, nothing to close - the terminal (or whatever is
piping into your program) holds it open for you.  Everything you just
learned about reading a file applies directly: `.read()` gives you one big
string, newlines and all.

## Hex, as a string of bytes instead of one number

Hex to Decimal showed you a single hex number.  Today's input is a whole
*stream* of them - one hex number per byte, however they happen to be
grouped on the page, and your job is to turn the whole thing back into the
raw bytes it represents.

`bytes.fromhex()` does the actual conversion, and it is more forgiving than
you would expect:

```
>>> bytes.fromhex("48656c6c6f")
b'Hello'
>>> bytes.fromhex("48 65 6c 6c 6f")
b'Hello'
>>> bytes.fromhex("48\n65\t6c 6c\n6f")
b'Hello'
```

Any amount of whitespace between byte pairs - spaces, tabs, newlines, any
mix - is simply ignored.  Upper and lower case hex digits both work.  What
it will **not** tolerate is a `0x` prefix, since `x` is not a hex digit:

```
>>> bytes.fromhex("0x48")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: non-hexadecimal number found in fromhex() arg at position 0
```

So if the input might have `0x`/`0X` in front of some bytes, strip it
first.  `.split()` breaks the whole blob into whitespace-separated chunks
regardless of how it was laid out, and slicing - which you already have from
Olympic Scorecard - checks and removes a prefix on each one:

```python
hex_digits = ""
for chunk in raw.split():
    if chunk[:2].lower() == "0x":
        chunk = chunk[2:]
    hex_digits += chunk

data = bytes.fromhex(hex_digits)
```

`chunk[:2].lower() == "0x"` catches `0x` and `0X` both, and `chunk[2:]` is
everything after those first two characters - or the whole chunk unharmed,
if it never had the prefix to begin with.

## Writing bytes instead of text

`data` from `bytes.fromhex()` is a `bytes` object, not a `str` - it is
Python's type for raw binary data.  Writing it needs the binary version of
`"w"`:

```python
with open(path, "wb") as f:
    f.write(data)
```

The `b` in `"wb"` is the whole difference.  In text mode, `f.write()` wants
a `str` and you would have to convert; in binary mode, it wants exactly what
`bytes.fromhex()` already gave you, so there is nothing to convert at all.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)
* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)

# Instructions

Read hex from standard input and write the bytes it represents to a file.

Your program is given the output path as a **command line argument**:

```
/challenge/run ./hex2bin.py /tmp/output.bin
```

Standard input contains hex digits describing the bytes to write.  It may be
one long run of digits, or broken into chunks separated by any mix of
spaces, tabs, and newlines.  Upper and lower case hex digits are both valid,
and any chunk may optionally start with `0x` or `0X`, which should be
ignored rather than treated as part of the number.

Decode it to bytes and write exactly those bytes to the path given on the
command line.  Then print exactly one line on standard output:

```
wrote <N> bytes to <the path>
```

So for this input on standard input:

```
48 65 6c 6c 6f 2c 20 57 6f 72 6c 64 21
```

run as:

```
/challenge/run ./hex2bin.py /tmp/output.bin
```

your program prints:

```
wrote 13 bytes to /tmp/output.bin
```

and `/tmp/output.bin` afterwards contains:

```
Hello, World!
```

The judge checks the **file**, not just what you printed, and it deletes
that file before running your program, so leftovers from an earlier attempt
will not save you.

```
/challenge/run ./hex2bin.py /tmp/output.bin
```
