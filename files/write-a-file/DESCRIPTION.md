# Write a File

Reading is half of it.  Now make a program that leaves something behind.

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

Read some lines and write them to a file.

Your program reads:

```
line 1     the path of the file to write
line 2     N, how many lines follow
next N     the lines to write
```

Write those N lines to that file, **one per line**.  Then print exactly one
line on standard output:

```
wrote <N> lines to <the path>
```

So for this input:

```
/tmp/challenge_output.txt
3
kernel
packet
cipher
```

your program prints:

```
wrote 3 lines to /tmp/challenge_output.txt
```

and `/tmp/challenge_output.txt` afterwards contains:

```
kernel
packet
cipher
```

The judge checks the **file**, not just what you printed.  It deletes that file
before running your program, so leftovers from an earlier attempt will not
save you - and a program that prints the right line without writing anything
fails with `that file does not exist afterwards`.

```
/challenge/run ./writer.py
```
