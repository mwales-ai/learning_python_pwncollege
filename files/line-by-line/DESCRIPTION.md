# Line by Line

`.read()` gives you the whole file at once.  That is fine for a file of five
lines and a catastrophe for a file of five million - your program would try to
hold the entire thing in memory at once.

There is a better way, and it is beautifully simple:

```
with open(path, "r") as f:
    for line in f:
        print(line)
```

**A file object can be looped over, and you get one line at a time.**  Python
reads a chunk, hands you a line, and forgets it before reading the next.  The
memory it uses does not depend on how big the file is.

This is the single most useful pattern in this dojo.  Log files, CSV exports,
word lists, anything - they are all "walk it a line at a time and do something
with each one."

## The newline, again

Every line you get out of that loop **still has its `\n` on the end**.  You saw
this last challenge from the writing side; here it is from the reading side:

```
>>> line
'22 ssh\n'
>>> len(line)
7
```

If you print those lines you get a blank line between every one, because the
line brings its own newline and `print` adds another.

`.strip()` removes whitespace - including the newline - from both ends:

```
>>> line.strip()
'22 ssh'
>>> len(line.strip())
6
```

**Strip every line you read from a file.**  If you take one habit out of this
module, take that one.  It is also the bug the Hangman challenge is built to
catch, so you may as well learn it now.

(`.strip()` removes spaces and tabs too.  `.rstrip()` only touches the end,
and `.rstrip("\n")` only removes newlines, if you need to be careful about
leading spaces.)

## Counting while you walk

You have done this before - it is the accumulator pattern:

```
count = 0
with open(path, "r") as f:
    for line in f:
        count = count + 1
```

The counter is created before the loop and used after it.

## A file can only be walked once

This surprises everybody:

```
with open(path, "r") as f:
    for line in f:
        count = count + 1
    for line in f:            # this loop runs ZERO times
        print(line)
```

Once you have read to the end, you are at the end.  If you need the lines
twice, either open the file again, or keep them in a list as you go:

```
lines = []
with open(path, "r") as f:
    for line in f:
        lines.append(line.strip())
```

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)
* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)

# Instructions

Number the lines of a file - a little `cat -n`.

Read one line on standard input: the path to a file.  Then print every line of
that file with its number in front, starting at 1:

```
1: <first line>
2: <second line>
```

and finish with one more line:

```
<N> lines
```

There are files to practise on in `/challenge/data/`.  For
`/challenge/data/ports.txt`:

```
1: 22 ssh
2: 25 smtp
3: 53 dns
4: 80 http
5: 443 https
5 lines
```

Strip each line before you print it.  If your output has a blank line between
every entry, that is what you have missed.

Compare your work against the real thing when you are done:

```
cat -n /challenge/data/ports.txt
```

```
/challenge/run ./number.py
```
