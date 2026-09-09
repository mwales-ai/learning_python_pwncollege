# Count and Total

Two more real tools, in one program: counting lines, and adding up a column of
numbers.

## Rebuilding wc -l

```
wc -l /etc/passwd
```

That is a program you have used a hundred times, and it is four lines of
Python: a counter before the loop, `+ 1` inside it, print it after.

One nice detail if you compare yours to the real one.  `wc -l` counts
**newline characters**, not lines.  So a file whose last line has no newline on
the end comes out one short:

```
hacker@dojo:~$ printf 'a\nb' | wc -l
1
```

Two lines of text, `wc` says one.  That is not a bug, it is the definition.
Your version, looping over lines, will say two.  Neither is wrong - but this is
exactly the sort of difference that makes two tools disagree and sends somebody
hunting for a bug that is not there.

## Adding up a column

This is the one you will actually use.  Any time something produces a column of
numbers, you can total it:

```
./sizes.sh | ./total.py
cut -d, -f3 sales.csv | ./total.py
```

Being able to do that from the command line, over data somebody else produced,
is a genuinely useful skill and you now have it.

## Several accumulators at once

Nothing says a loop may only keep one running total.  Create them all before
the loop and update whichever ones apply:

```
lines = 0
numbers = 0
total = 0

for line in sys.stdin:
    lines = lines + 1
    if <it is a number>:
        numbers = numbers + 1
        total = total + int(line)
```

Notice that `lines` goes up for **every** line, while `numbers` and `total`
only move for the ones that are numbers.  Being deliberate about which counter
each line affects is the entire skill here.

## Messy input, again

Same test as last challenge:

```
line.lstrip("-").isdigit()
```

Real data is never as tidy as your test data.  A column of numbers exported
from a spreadsheet will have a header row, blank lines, and at least one cell
where somebody typed `n/a`.

## Further Reading

* `man wc`
* Automate the Boring Stuff with Python
  * [Chapter 8 - Input Validation](https://automatetheboringstuff.com/3e/chapter8.html)

# Instructions

Read every line from standard input and print exactly three lines:

```
lines: <how many lines there were altogether>
numbers: <how many of them were whole numbers>
total: <those numbers added up>
```

Lines that are not numbers still count towards `lines`.  They just do not
contribute to `numbers` or `total`.

A leading minus sign is part of a number.

So for this input:

```
5
banana
15
not a number
20
```

your program prints:

```
lines: 5
numbers: 3
total: 40
```

If there are no numbers at all, `total` is `0`.

Try it on real data and compare against the tools you are copying:

```
cat /etc/passwd | ./count.py
wc -l /etc/passwd
seq 1 100 | ./count.py
```

The last one should total 5050, which is a number worth recognising - Gauss
worked it out in primary school, reportedly in about a minute, and there is a
lovely trick to it.

```
/challenge/run ./count.py
```
