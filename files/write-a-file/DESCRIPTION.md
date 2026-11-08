# File Decoder Ring

Reading is half of it.  Now make a program that leaves something behind -
a decoded file, this time.

## Opening for writing

```
with open("/tmp/output.txt", "w") as f:
    f.write("hello\n")
```

The `"w"` is the only change from reading.  But it is a big one.

## "w" destroys the file

**The moment you open a file with `"w"`, its contents are gone.**  Not when
you write to it - when you *open* it.  Open a file with `"w"` and change your
mind, and you have still emptied it.

That is worth being frightened of exactly once.  A great many people have
destroyed a file they cared about with a one letter typo:

| Mode | Means |
|------|-------|
| `"r"` | read.  The file must already exist. |
| `"w"` | write.  **Empties the file first.**  Creates it if it does not exist. |
| `"a"` | append.  Adds to the end, keeps what is there.  You will use this next challenge. |

## write() is not print()

Two differences, and both catch people:

* **`write()` does not add a newline.**  `print()` does.  If you write three
  lines without newlines you get one long line:

  ```
  f.write("alpha")
  f.write("bravo")        ->  alphabravo
  ```

  You have to add them yourself:

  ```
  f.write("alpha\n")
  f.write(line + "\n")
  ```

* **`write()` only takes strings.**  `f.write(42)` is a `TypeError`.  Use
  `str(42)`, or an f-string, which is usually what you wanted anyway:

  ```
  f.write(f"{count} lines\n")
  ```

Today's task will not have you adding `"\n"` by hand - you will see why in a
moment - but do not let that fool you into thinking `write()` started adding
them for you.  It still never adds anything you did not put there yourself.

## Secret Decoder Ring, with files this time

You already built a substitution cipher decoder - same key format, on
standard input:

```
line 1   the original characters, e.g. abcdefghijklmnopqrstuvwxyz
line 2   what they were turned into, e.g. nopqrstuvwxyzabcdefghijklm
```

and the same rule for using it: the key describes how a message was
**encoded**, so decoding goes backwards - find each character in the
**second** line, and replace it with the character at the same position of
the **first**.  Anything not in the key passes through unchanged.

What is different is where the encoded message comes from and where the
decoded one goes: two **files**, named on the **command line** instead of
typed in.  You have already used `sys.argv` for this, back in Command Line
Arguments and FizzBuzz - `sys.argv[1]` and `sys.argv[2]` are the two paths
here.

## Decode the whole file in one pass

Read the entire encoded file at once, the same `.read()` you already know:

```python
with open(input_path, "r") as f:
    encoded = f.read()
```

Then run it through the exact same character-by-character loop Secret
Decoder Ring taught you - except now it is walking the **whole file's**
text, newlines and all, instead of one line you typed:

```python
decoded = ""
for ch in encoded:
    if ch in substituted:
        decoded = decoded + original[substituted.index(ch)]
    else:
        decoded = decoded + ch
```

A newline character is not in the key any more than a space or a punctuation
mark is, so it passes straight through, completely unchanged - which means
every line break in the encoded file lands in exactly the same place in
`decoded`.  That is the whole reason this challenge does not need `.strip()`,
does not need to split the file into lines, and does not need to add any
`"\n"` back by hand: the decoded string already has them, because the
encoded one did.

## Check your work

The whole point is that the file exists afterwards, so go and look at it:

```
cat /tmp/output.txt
wc -l /tmp/output.txt
```

If `cat` shows nothing, either you never wrote anything, or you wrote to a
different path than you think.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)
* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)

# Instructions

Decode a file and write the result to another file.

Your program is given two paths on the **command line**:

```
/challenge/run ./filedecoder.py <input path> <output path>
```

Standard input gives you the key, same as Secret Decoder Ring:

```
line 1     the original characters
line 2     what they were turned into
```

Read the entire file at the input path, decode it one character at a time
using that key, and write the decoded result to the output path.  Then
print exactly one line on standard output:

```
decoded <N> characters into <the output path>
```

So if `/challenge/data/message.txt` contains:

```
yvxw
x zxy
```

and your program is run as:

```
/challenge/run ./filedecoder.py /challenge/data/message.txt /tmp/decoded.txt
```

given this key on standard input:

```
abcde
xyzwv
```

your program prints:

```
decoded 11 characters into /tmp/decoded.txt
```

and `/tmp/decoded.txt` afterwards contains:

```
bead
a cab
```

The judge checks the **file**, not just what you printed, and it deletes
that file before running your program, so leftovers from an earlier attempt
will not save you.

```
/challenge/run ./filedecoder.py /challenge/data/message.txt /tmp/decoded.txt
```
