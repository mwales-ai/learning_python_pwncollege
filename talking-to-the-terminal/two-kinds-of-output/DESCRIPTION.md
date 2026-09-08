# Two Kinds of Output

This is the most useful habit in this entire dojo, and almost no beginner book
teaches it early enough.

## A program has two output pipes

Every program on Linux gets three streams, not two:

| Stream | Number | What it is for |
|--------|--------|----------------|
| standard input | 0 | where input comes from |
| standard output | 1 | **the answer** |
| standard error | 2 | **everything a human needs to read** |

Progress messages, warnings, complaints, "reading file 3 of 10", "that file
does not exist" - none of that is the answer.  It goes to standard error.

## Why anyone cares

Because of this:

```
./myprogram > answer.txt
```

That redirects **standard output only**.  The answer lands in the file.  The
progress messages still come to your screen, where you can see them.  Both
things happen at once, and neither gets in the other's way.

The same reason makes pipelines work:

```
ls | wc -l
```

If `ls` printed "now listing directory..." on standard output, `wc` would
count it as a line.  Every Unix tool keeps them separate, which is exactly why
you can wire any tool into any other.  You have been relying on this since
Linux Luminarium without being told.

You can prove it to yourself.  `2>` redirects standard error:

```
./myprogram > /dev/null      <- you see ONLY the chatter
./myprogram 2> /dev/null     <- you see ONLY the answer
```

## How to do it in Python

`print()` writes to standard output.  To pick the other stream, pass
`file=sys.stderr`, and `import sys` at the top of your program:

```
import sys

print("the answer")                              # standard output
print("still working...", file=sys.stderr)       # standard error
```

That is the whole technique.

## Now you know where prompts belong

Remember the rule about never giving `input()` a prompt?  A prompt is chatter.
If you want one, this is how you do it properly:

```
print("Name: ", file=sys.stderr)
name = input()
```

Now the human sees the prompt, and the answer stays clean.

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
