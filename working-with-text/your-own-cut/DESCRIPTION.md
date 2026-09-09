# Your Own cut

This is the one you will actually use.

Somebody sends you a spreadsheet.  You export it as CSV - **comma separated
values**, the plainest possible format, one row per line and commas between the
fields:

```
name,score,team
turing,95,red
lovelace,88,blue
hopper,92,red
```

The first line is the **header row**: it names the columns.  Everything after
it is data.

You are going to write a program that pulls out the columns you ask for, by
name, in whatever order you like.

## The header row is the whole trick

Split the header and you get the column names as a list:

```
>>> "name,score,team".split(",")
['name', 'score', 'team']
```

Which means `.index()` tells you where any column lives:

```
>>> header.index("team")
2
```

And now every data row is just indexing:

```
>>> "turing,95,red".split(",")[2]
'red'
```

Work out the positions **once**, from the header, and then apply them to every
row.  That is what lets the user ask for columns by name instead of counting
commas, and it is why the order they ask for them in does not matter.

## The first line is special

You need to treat line 1 differently from the rest, inside a single loop.  The
readable way is a flag that starts as "not seen yet":

```
header = None
for line in sys.stdin:
    fields = line.strip().split(",")
    if header is None:
        header = fields
        ...work out the positions...
        continue
    ...handle a data row...
```

`continue` jumps to the next line, so the data-row code below never runs for
the header.

`None` is Python's word for "no value at all".  Test for it with `is None`,
not `== None`.

## Putting the row back together

```
",".join(picked)
```

Separator first, remember.

## Real CSV is messier than this

What if a field contains a comma?

```
name,quote
turing,"On the contrary, machines think"
```

Real CSV puts quotes around it, and splitting on commas gets that wrong.
Python has a `csv` module that handles quoting, escaped quotes, and different
separators, and for real work you should use it.

We are doing the simple version because the simple version is what you can
write today, and it handles the overwhelming majority of files you will meet.
Knowing *why* it is the simple version is the point.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 16 - Working with CSV Files and JSON Data](https://automatetheboringstuff.com/3e/chapter16.html)
* `man cut` - the real tool, which can only do positions, not names.  Which is
  exactly why people write this program.

# Instructions

Write a `cut` that works on column names.

Your program is given one or more column names as command line arguments, and
a CSV file on standard input whose first line is the header:

```
./cut.py name score
```

For every **data** row, print the requested columns joined by commas, in the
order they were asked for.  Do not print the header row.

So with the arguments `name score` and this input:

```
name,score,team
turing,95,red
lovelace,88,blue
hopper,92,red
```

your program prints:

```
turing,95
lovelace,88
hopper,92
```

And with the arguments `team name` on the same input, the columns come out in
the order you asked for them:

```
red,turing
blue,lovelace
red,hopper
```

If a requested column is not in the header, print this on standard error and
exit with status 1:

```
no such column: <the name>
```

Then go and use it on something real:

```
cat /etc/passwd | tr ':' ',' | head -1
```

```
/challenge/run ./cut.py
```
