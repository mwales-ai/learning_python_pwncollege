# Capstone: The Report

Last one.  No new ideas - this is everything you already know, assembled into
one program of the kind you would actually be asked to write.

You are given a log of logins, one username per line, and you produce a report
saying who logged in and how often.

## Counting with a dictionary

This is the pattern.  Learn it:

```
counts = {}
for name in entries:
    counts[name] = counts.get(name, 0) + 1
```

`counts.get(name, 0)` means "how many so far, or zero if this is the first time
I have seen this one".  Add one, put it back.

Without `.get()` you would need an `if name in counts:` around every update.
With it, the first occurrence and the hundredth are handled by the same line.

And `len(counts)` is the number of **distinct** names, for free - because a
dictionary only ever holds one entry per key.

## Sorting by two things at once

You want the most frequent first.  For ties, alphabetical.  One descending, one
ascending - and Python sorts ascending.

Here is the trick.  Python compares **tuples** element by element: it looks at
the first, and only if those are equal does it look at the second.  So a list
of `(count, name)` pairs sorts by count, then by name.

To flip just the count, **negate it**:

```
pairs = []
for name in counts:
    pairs.append((-counts[name], name))
pairs.sort()
```

Now the biggest count has the most negative number and sorts first, while names
still sort A to Z among ties.  Negate it again when you print it.

A tuple is written with round brackets and works like a list you are not
allowed to change.  You have already been using them without noticing - that is
what `for key, value in d.items()` is handing you.

## Errors go on stderr, and you exit nonzero

If the file cannot be read, this matters:

```
print(f"cannot read {path}", file=sys.stderr)
sys.exit(1)
```

Both halves.  Printing the error on **standard output** would put it in the
report, where whatever reads the report next would treat it as data.  Exiting
**0** would tell the shell everything was fine, and this would run the second
half regardless:

```
./report.py missing.txt && ./email_it.py
```

You learned both of those in module 2.  This is what they were for.

To catch the error rather than crashing:

```
try:
    entries = read_entries(path)
except FileNotFoundError:
    print(f"cannot read {path}", file=sys.stderr)
    sys.exit(1)
```

`try`/`except` is the last bit of syntax in this dojo: run this, and if *that*
particular thing goes wrong, do this instead.

## Use functions

You know how now.  One job each - read the file, count the entries, rank them -
plus a `main()`.  You will be glad of it when one part is wrong.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 5 - Dictionaries and Structuring Data](https://automatetheboringstuff.com/3e/chapter5.html)
  * [Chapter 11 - Debugging](https://automatetheboringstuff.com/3e/chapter11.html) covers try/except

# Instructions

Write a login report.

Your program takes **one command line argument**: the path to a log file.  Each
line of that file is one username.  Blank lines are ignored.

```
./report.py /challenge/data/logins.txt
```

Print:

```
total logins: <how many entries there were>
distinct users: <how many different names>
```

then one line per user, **most frequent first**, ties broken alphabetically:

```
<count> <username>
```

So for a file containing:

```
root
hopper
root
turing
hopper
root
lovelace
turing
root
hopper
```

your program prints:

```
total logins: 10
distinct users: 4
4 root
3 hopper
2 turing
1 lovelace
```

If the file cannot be opened, print this on **standard error**:

```
cannot read <the path>
```

and exit with status **1**.  Print nothing on standard output in that case.

**This challenge checks standard output, standard error, and your exit
status.**  It is the capstone; everything counts.

There are log files to try in `/challenge/data/`.  One of them has a tie in
it, so check that your alphabetical tie-break works.

```
/challenge/run ./report.py
```

## And that is the dojo

Look at what that program does.  It takes a filename from the command line,
reads a file it has never seen, counts things with a dictionary, ranks them,
formats a report for a human, keeps its errors out of its output, and tells the
shell whether it worked.

That is a real tool.  Six weeks ago you printed `Hello Hackers`.

Go and point it at something that is not a log file.  Every word in a book,
every IP address in a firewall log, every file extension in a directory - it is
the same program with a different input.  That is the whole job.
