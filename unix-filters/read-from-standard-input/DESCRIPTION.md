# Read From Standard Input

Here is the whole trick, and it is smaller than you expect:

```
import sys

for line in sys.stdin:
    print(line.strip())
```

**`sys.stdin` is a file object.**  Everything you learned about files last
module applies to it unchanged - you loop over it a line at a time, and every
line arrives with its `\n` still attached, so you strip it.

There is no `open()` and no `close()`.  The shell connected it before your
program started.

## Why this is better than input()

Every challenge so far has been told how many lines to expect, because
`input()` has no graceful way to notice the end of the input - it raises
`EOFError` and your program dies.

Looping over `sys.stdin` just **stops** when the input runs out.  Which means
your program now works on however much data it is given, without being told in
advance.  That is not a small convenience; it is the difference between a
classroom exercise and a tool.

## Where the input comes from

All three of these run the same program, and it cannot tell them apart:

```
cat data.txt | ./myfilter.py      # another program feeds it
./myfilter.py < data.txt          # a file feeds it
./myfilter.py                     # you feed it, then press Ctrl-D
```

That last one is worth trying.  Run your program with no input redirected, type
a few lines, and press **Ctrl-D** on an empty line.  `Ctrl-D` means "end of
input" - it is not a key your program receives, it is the terminal telling the
system there is no more.  That is what ends the loop.

(If you press `Ctrl-C` instead, you kill the program.  Different thing.)

## One warning

**Do not mix `input()` and `for line in sys.stdin:` in the same program.**  The
loop reads ahead in large chunks for speed, so a later `input()` will find
lines already consumed and skip them.  Pick one and stick with it.  From here
on, filters use the loop.

## Further Reading

* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)

# Instructions

Write a filter that echoes what it is given, with a marker, and counts it.

Read every line from standard input.  For each one print:

```
> <the line>
```

When the input runs out, print one more line:

```
<N> lines
```

Your program is not told how many lines are coming.  That is the point.

So for this input:

```
kernel
packet
cipher
```

it prints:

```
> kernel
> packet
> cipher
3 lines
```

Try all three ways of feeding it:

```
echo "kernel
packet" | ./echo.py
./echo.py < /etc/passwd
./echo.py
```

For the last one, type some lines and press Ctrl-D when you are done.

```
/challenge/run ./echo.py
```
