# Is It a Palindrome?

A **palindrome** is a word or phrase that reads the same forwards and
backwards - `racecar`, `level`, `noon`.  To check one, you need two new
ideas: pulling a single item out of a list by position, and walking
toward the middle from both ends at once.

## A string is a list of characters

This module is called Loops *and Lists* for a reason, and here is your
first look at why they go together: a string already behaves like a
list.  Not a list of words - a list where each **character** is one
item, sitting at a position, counting from `0`.  The standard list
operations work on it right now, before you have even met the `list`
type by name.

**Indexing** - square brackets pick out one item by position:

```
>>> word = "cake"
>>> word[0]
'c'
>>> word[1]
'a'
>>> word[3]
'e'
```

`word[0]` is always the first item, never the second - the same
zero-counting rule every list uses.  Ask for a position that does not
exist - `word[4]` on a 4-item list - and you get an `IndexError`:
walking off the end of the list.

**Length** - `len()` tells you how many items are in the list, the exact
same function you would call on a real `list` later.  The *last* item
sits at position `len(word) - 1`, **not** `len(word)` - a 4-item list has
positions `0`, `1`, `2`, `3`, and position `4` does not exist:

```
>>> word = "cake"
>>> len(word)
4
>>> word[len(word) - 1]
'e'
```

That off-by-one is exactly the same shape as `range()` stopping before its
stop value - the length and the last valid position are never the same
number.

(One real difference, for when you meet actual `list`s: those let you
change one item in place.  A string does not - once it exists, none of
its characters can be swapped out.  You are only ever *reading*
characters in this challenge, so that difference does not come up yet.)

## Checking from both ends at once

The plan: keep one position creeping in from the left and another creeping
in from the right, comparing the characters at each, until they meet in
the middle.

```python
is_palindrome = True
left = 0
right = len(word) - 1

while left < right:
    if word[left] != word[right]:
        is_palindrome = False
        break
    left = left + 1
    right = right - 1
```

`is_palindrome` starts out `True` - innocent until proven otherwise.  The
loop only ever has the power to set it `False`, the moment it finds one
mismatched pair, and `break` stops checking immediately - there is no
point comparing the rest once you already know the answer.

Walk `"noon"` through it by hand: `left=0, right=3` compares `n` and `n` -
match, so nothing changes.  `left=1, right=2` compares `o` and `o` - match
again.  Now `left` is not less than `right`, so the loop stops on its own,
`is_palindrome` is still `True`, and `"noon"` is a palindrome.  Walk
`"hello"` through it and `left=0, right=4` compares `h` and `o`
immediately - a mismatch, `is_palindrome` becomes `False`, and `break`
ends it right there without ever looking at the middle.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 3 - Loops](https://automatetheboringstuff.com/3e/chapter3.html)
* A Byte of Python
  * [Sequences](https://python.swaroopch.com/data_structures.html#sequence)

# Instructions

Read one line - a word or a short phrase - and decide whether it is a
palindrome: does it read the same forwards and backwards, character for
character, exactly as given?

Print exactly one line:

```
<the input> is a palindrome
```

or

```
<the input> is not a palindrome
```

So for `racecar`:

```
racecar is a palindrome
```

and for `python`:

```
python is not a palindrome
```

This checks the **exact** characters you were given - no changing case, no
removing spaces or punctuation.  `"wow mom wow"` is a palindrome exactly as
written (the spaces themselves sit in mirrored positions); `"Racecar"`
with a capital `R` is not, because `R` and `r` are different characters.
Real-world palindrome checkers usually do clean the input up first - you
will have the string tools to do that soon, but not yet.

Use indexing and a loop to compare characters from both ends inward.  Do
not just compare `word` to a reversed copy of itself - the point of this
challenge is the two-pointer walk, not finding the one builtin that skips
it.

```
/challenge/run ./palindrome.py
```
