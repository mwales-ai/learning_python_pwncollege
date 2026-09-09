# Read a File

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

## What you get back

`.read()` gives you one string containing the whole file:

```
>>> contents
'22 ssh\n25 smtp\n53 dns\n'
```

Those `\n` characters are the line breaks.  They are really there, they count
towards `len()`, and they are why a file of 3 short lines has more characters
than you expected.

```
>>> len(contents)
25
>>> contents.count("\n")
3
```

## Printing a whole file

```
print(contents)
```

gives you a blank line at the end, because the file's last line already ends
with a newline and `print` adds another.  If that bothers you:

```
print(contents, end="")
```

`end=""` tells `print` not to add anything after.

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

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)
* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)

# Instructions

Read a path on standard input, then print that file followed by two summary
lines.

Your program reads one line - the path to a file.  Then it prints:

* the entire contents of the file
* `characters: <how many characters are in it>`
* `lines: <how many newline characters are in it>`

There are files to practise on in `/challenge/data/`.  Go and look at them
first:

```
ls /challenge/data/
cat /challenge/data/ports.txt
```

For `/challenge/data/ports.txt` your program prints:

```
22 ssh
25 smtp
53 dns
80 http
443 https
characters: 40
lines: 5
```

Print the file with `end=""` or the count lines will end up separated from it
by a blank one.  (The judge ignores blank lines, so it will not fail you for
that - but your output will look wrong to you, and that is worth understanding
rather than ignoring.)

```
/challenge/run ./reader.py
```
