# Two Kinds of Output

This is the most useful habit in this entire dojo, and almost no beginner book
teaches it early enough.

## A worked example

Here is a program that adds two numbers, reporting what it is doing as it
goes:

```python
import sys

a = int(input())
print(f"first number: {a}", file=sys.stderr)

b = int(input())
print(f"second number: {b}", file=sys.stderr)

print("adding them now", file=sys.stderr)

print(a + b)
```

Run it and you would never notice anything odd - everything lands on your
screen, in order:

```
$ echo "12
30" | ./add.py
first number: 12
second number: 30
adding them now
42
```

Now redirect just the answer to a file:

```
$ echo "12
30" | ./add.py > answer.txt
first number: 12
second number: 30
adding them now
$ cat answer.txt
42
```

The three progress lines still showed up on your screen immediately.  The
`42` did not - it went straight into `answer.txt` instead, and never touched
your screen at all.  `>` only ever redirects **standard output**.  The
progress lines are on an entirely different stream, called **standard
error**, and `>` leaves it alone.  That is the whole trick, and you just
watched it happen.

## A program has three streams, not two

| Stream | Number | What it is for |
|--------|--------|----------------|
| standard input | 0 | where input comes from |
| standard output | 1 | **the answer** |
| standard error | 2 | **everything a human needs to read** |

Progress messages, warnings, complaints, "reading file 3 of 10", "that file
does not exist" - none of that is the answer.  It goes to standard error.

`print()` writes to standard output by default.  Pass `file=sys.stderr` to
send a line to the other stream instead - that is the entire mechanism
`add.py` used above, and it is the entire mechanism, full stop.

## Why anyone cares

The same reason makes pipelines work:

```
ls | wc -l
```

If `ls` printed "now listing directory..." on standard output, `wc` would
count it as a line.  Keeping chatter off of standard output is what lets you
wire any Unix tool into any other - you have been relying on this since
Linux Luminarium without being told.

You can prove the split yourself.  `2>` redirects standard error instead:

```
echo "12
30" | ./add.py 2>/dev/null     <- you see ONLY the answer
echo "12
30" | ./add.py >/dev/null      <- you see ONLY the chatter
```

## tee: seeing a stream and saving it at the same time

A quick reminder, since you will reach for this constantly: `tee` sits in the
middle of a pipeline, copies whatever flows through it into a file, and lets
it keep going too - so you see it on screen *and* keep a copy, instead of
having to pick one.

```
$ echo "12
30" | ./add.py | tee answer.txt
first number: 12
second number: 30
adding them now
42
$ cat answer.txt
42
```

Notice the progress lines still showed up immediately, exactly like before.
`tee` only ever sees **standard output** - that is the one stream the pipe
`|` carries from `add.py` into `tee`.  Standard error skips the pipe
entirely and goes straight to your screen.  That is why this gives you both
the live chatter and a saved copy of just the answer, with nothing extra
leaking into `answer.txt`.

## Further Reading

* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)
* Linux Luminarium's redirection material is the other half of this idea.

# Instructions

Write a program that adds two numbers, and reports what it is doing as it
goes.

Read two whole numbers, one per line.

On **standard error**, print exactly these three lines, in this order:

```
first number: <the first number>
second number: <the second number>
adding them now
```

Print the first two *as you read them* - read a number, then report it, then
read the next.

On **standard output**, print exactly one line: the sum.  Nothing else.

So given input `12` and `30`, standard output is the single line:

```
42
```

and standard error is:

```
first number: 12
second number: 30
adding them now
```

**This challenge checks both streams.**  Every earlier challenge ignored
standard error; this one does not.  Right text on the wrong stream fails.

Check yourself before you hand it in.  This should show you only `42`:

```
echo "12
30" | ./adder.py 2> /dev/null
```

and this should show you only the three progress lines:

```
echo "12
30" | ./adder.py > /dev/null
```

```
/challenge/run ./adder.py
```
