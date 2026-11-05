# Anagram Finder

An **anagram** is a word made by rearranging the letters of another word,
using every letter exactly once.  `listen` and `silent` are anagrams - same
six letters, different order.

## Lists, finally

A **list** holds many things under one name, in order.  `[]` is an empty one,
which is usually where you start:

```
>>> matches = []
>>> matches.append("enlist")
>>> matches.append("silent")
>>> matches
['enlist', 'silent']
```

`.append()` adds one item to the **end**.  It changes the list in place and
hands back `None` - so `matches = matches.append(x)` destroys your list.  Just
call it, do not assign the result.

Indexing a list works exactly like indexing a string, which you already know
from Is It a Palindrome?: `matches[0]` is the first item, `matches[-1]` is the
last, and asking for a position past the end is an `IndexError`.

## Turning a line into words: split()

```
>>> "the cake is a lie".split()
['the', 'cake', 'is', 'a', 'lie']
```

`.split()` with no argument breaks a string into a list of words, splitting on
any whitespace.  That is exactly what you need to turn one line of
space-separated words into something you can loop over.

## Checking letters, not order: sorted()

Two words are anagrams exactly when they have the same letters, just in a
different order.  "Same letters" is easy to check once you stop caring about
order - and **not caring about order is what sorting is for**:

```
>>> sorted("listen")
['e', 'i', 'l', 'n', 's', 't']
>>> sorted("silent")
['e', 'i', 'l', 'n', 's', 't']
```

`sorted()` works on a string the same way it works on a list - it hands back
the items (here, the individual characters) rearranged smallest to largest.
Two words are anagrams exactly when their sorted letters match:

```
>>> sorted("listen") == sorted("silent")
True
>>> sorted("listen") == sorted("cat")
False
```

Notice you get the length check for free.  `cat` only has three letters, so
its sorted list cannot possibly equal `listen`'s six-letter one - `==` on two
lists already checks both length and contents, no special case needed.

## Two ways to sort

`sorted(word)` is a **function**.  It leaves `word` alone and hands you back a
brand new, sorted list - which is exactly what you want above, since you still
need the original word afterward.

Lists also have a `.sort()` **method**, which sorts the list **in place**
instead:

```
>>> matches = ["silent", "enlist"]
>>> matches.sort()
>>> matches
['enlist', 'silent']
```

Same gotcha as `.append()`: `.sort()` changes the list and returns `None`, so
`matches = matches.sort()` throws your list away.  Use `sorted()` when you
need the original untouched; use `.sort()` when you already have your own
list of results and just want it in order before printing.

## Putting it back together: join()

`.join()` is backwards from what everyone expects.  **The separator is the
string you call it on:**

```
>>> ", ".join(["enlist", "silent"])
'enlist, silent'
```

Not `matches.join(", ")`.  It works on any sequence of strings, which is why
it belongs to the separator rather than to the list.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 4 - Lists](https://automatetheboringstuff.com/3e/chapter4.html)
* A Byte of Python
  * [Data Structures](https://python.swaroopch.com/data_structures.html)

# Instructions

Read a number of test cases.  Each one is a single line of space-separated
words.  The **first** word on the line is the one to check; figure out which
of the **other** words on that line are anagrams of it.

The input is:

```
line 1     T, how many test cases follow
next T     one line each, space-separated words
```

For each test case, print one line:

```
<first word>: <the matching words, sorted alphabetically, separated by ", ">
```

So for this input:

```
2
listen enlist banana silent
cat cot act scat
```

your program prints:

```
listen: enlist, silent
cat: act
```

`banana` and `cot`/`scat` are not anagrams of `listen` and `cat` - they do not
have the same letters, so leave them out.  If **no** word on a line is an
anagram of the first one, still print the line, just with nothing after the
colon.

Build the list of matches with `.append()` as you find them, put it in order
with `.sort()`, then glue it into one line with `", ".join(...)`.

```
/challenge/run ./anagrams.py
```
