# In the Middle of a Pipeline

Your grep can sit at the end of a pipeline.  Now write something that sits in
the **middle**, with a program on each side:

```
cat data.txt | ./yours.py | sort | head -3
```

Nothing about your program changes to make this work.  That is the point.  It
reads standard input and writes standard output, so it does not know or care
whether the thing on either side is a file, a terminal, or another program.

## A pipeline is not a queue

This is the part that surprises people: the programs in a pipeline **all run
at the same time**.

```
cat huge.txt | ./yours.py | head -3
```

`cat` does not read the whole file, finish, and then hand it over.  All three
start together, and data flows through as it is produced.  `head` prints three
lines and exits - and then the programs *behind* it get shut down, because
nobody is listening any more.

This is why `head` on an enormous file is instant, and it is why a
well behaved filter processes one line at a time instead of reading everything
into a list first.  Your loop over `sys.stdin` already does the right thing.

You may occasionally see this when a downstream program stops early:

```
BrokenPipeError: [Errno 32] Broken pipe
```

That is not your bug.  It means something downstream stopped listening while
you were still writing.

## Why stdout discipline matters here

If your program prints anything to standard output that is not the answer -
a banner, a prompt, "processing..." - then the next program in the pipe
receives it as data.  `sort` will sort your banner into the middle of the
results.  `wc -l` will count it.

Everything that is not the answer goes to standard error, where it will appear
on your screen and stay out of the pipe.  You learned how in module 2; this is
where it earns its keep.

## Further Reading

* Linux Luminarium's pipes material, revisited from the other side

# Instructions

Write a filter that numbers each line and shouts it.

Read every line from standard input.  For each one, print:

```
<line number>: <THE LINE IN UPPER CASE>
```

Numbering starts at 1.  `.upper()` gives you an upper-cased copy of a string.

So for this input:

```
hello world
this is a test
```

your program prints:

```
1: HELLO WORLD
2: THIS IS A TEST
```

Print nothing else - no total at the end this time.  This program has to be
usable in the middle of a pipe, and a summary line would be data to whatever
comes next.

Now go and play with it, because this is the fun bit:

```
cat /usr/share/dict/words | ./loud.py | head -5
cat /etc/passwd | ./loud.py | sort | head -3
seq 1 10 | ./loud.py | ./loud.py
```

That last one pipes your program into itself.  Work out what it should print
before you run it.

```
/challenge/run ./loud.py
```
