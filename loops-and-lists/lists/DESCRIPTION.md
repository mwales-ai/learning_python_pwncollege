# Lists

So far every variable has held exactly one thing.  A **list** holds many
things under a single name, in order.

```
>>> words = ["alpha", "bravo", "charlie"]
>>> words
['alpha', 'bravo', 'charlie']
```

Square brackets make a list.  `[]` is an empty one, which is usually where you
start.

## Indexing starts at zero

```
>>> words[0]
'alpha'
>>> words[1]
'bravo'
```

The first item is at position **0**, not 1.  So a list of 3 items has valid
positions 0, 1 and 2 - and asking for `words[3]` is an error:

```
>>> words[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

That "off by one" is so common it has a name.  An `IndexError` almost always
means you counted from 1 somewhere, or used `len()` as a position.

## Negative indexes

Python counts backwards from the end with negative numbers:

```
>>> words[-1]
'charlie'
>>> words[-2]
'bravo'
```

`words[-1]` is the last item.  Get used to writing that instead of
`words[len(words) - 1]` - it is shorter, it is clearer, and it is one fewer
place to get the arithmetic wrong.

## len() and append()

`len()` works on a list just like it works on a string:

```
>>> len(words)
3
```

`.append()` adds one item to the **end**:

```
>>> words.append("delta")
>>> words
['alpha', 'bravo', 'charlie', 'delta']
>>> len(words)
4
```

One warning.  `.append()` changes the list in place and hands back `None`.  So
this destroys your list:

```
>>> words = words.append("echo")     # NO
>>> words
>>> print(words)
None
```

Just call it.  Do not assign the result.

## Walking a list by position

You already know `range(len(mylist))` gives exactly the valid positions.  That
is how you visit items in a particular order - for example, backwards:

```
for i in range(len(words) - 1, -1, -1):
    print(words[i])
```

Read that `range` carefully.  Start at the last valid position, step by -1,
and stop **before** -1, so the last position actually visited is 0.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 4 - Lists](https://automatetheboringstuff.com/3e/chapter4.html)
* A Byte of Python
  * [Data Structures](https://python.swaroopch.com/data_structures.html)

# Instructions

Read a list of words, report on it, then add one more.

The input is:

```
line 1     N, how many words follow
next N     the words, one per line
last line  one extra word to append
```

Print exactly this:

```
count: <how many words you read>
first: <the first word>
last: <the last word>
backwards:
<the words, one per line, last to first>
after appending <the extra word> the count is <the new count>
the last item is now <the extra word>
```

So for this input:

```
3
kernel
packet
cipher
malware
```

your program prints:

```
count: 3
first: kernel
last: cipher
backwards:
cipher
packet
kernel
after appending malware the count is 4
the last item is now malware
```

Build the list with a loop and `.append()` - start with `[]` and add each word
as you read it.  Note that `count:` is the count *before* the extra word, and
the last two lines are *after* it.

```
/challenge/run ./listy.py
```
