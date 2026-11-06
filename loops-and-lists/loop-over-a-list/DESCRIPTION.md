# Olympic Scorecard

Some Olympic events - diving and gymnastics among them - use a panel of
judges, and to keep any one judge from swaying the result, the rule is
simple: **throw out the lowest score and the highest score**, then average
what is left.

ASCII Values already showed you this, on a string: `for char in word:`
hands you each item directly, no `range()`, no `len()`, no indexing. The
exact same syntax works on a real `list`:

```
for score in scores:
    print(score)
```

Compare that to looping by position, which still works but is more
machinery than you need when you do not actually care *where* you are:

```
for i in range(len(scores)):
    print(scores[i])
```

Use the direct form unless you specifically need the position - and now
you have seen it do the same job on a string and on a list, which is
exactly the point: **a list is the general case, and a string was a
preview of it.**

## The accumulator pattern

This is one of the half dozen patterns you will use for the rest of your
life.

**Create a variable before the loop.  Update it once per item.  Use it after
the loop.**

```
total = 0
for score in scores:
    total = total + score
print(total)
```

`total` has to exist *before* the loop, because you cannot add to something
that does not exist yet.  And it has to be *outside* the loop, because a
variable created inside gets reset every time round - that is why a broken
version reports the last score instead of the sum.

You have already met this shape twice without it being named: the birthday
banner built up a string, and the guessing game counted guesses.  Same
pattern, different starting value:

| Building a | Start with |
|------------|-----------|
| total | `0` |
| string | `""` |
| list | `[]` |
| count | `0` |

## Finding the highest: the seeding trap

Finding the highest score looks like the same thing:

```
highest = 0
for score in scores:
    if score > highest:
        highest = score
```

That is **wrong**, and it is wrong in a way that works fine right up until it
does not.  A score of exactly `0` would never be beaten by anything smaller,
and a figure skating program that gets every judge's score **negative** -
deductions can do that in some scoring systems - would report `0` as its
highest, a number no judge actually gave.

The fix is to start from something that is genuinely a candidate.  The first
item always is:

```
highest = scores[0]
```

Ask yourself what your accumulator should be before you have seen anything.
For a sum, "nothing yet" really is 0.  For a highest-score search, there is
no such value, so use the first item.

## You will not write this again

Python already has these:

```
>>> sum(scores)
>>> max(scores)
>>> min(scores)
```

In real code, use them.  You just hand-wrote the seeding trap once, so the
pattern is yours - from here on, reach for the built-ins.

## Dropping the extremes: sort, then slice

`sorted()` already showed up in Anagram Finder, sorting the letters of a
word.  It works exactly the same way on a list of numbers:

```
>>> sorted([9.5, 9.3, 9.7, 9.2])
[9.2, 9.3, 9.5, 9.7]
```

Once a list is sorted, the lowest score is sitting at index `0` and the
highest is at index `-1`.  That means you can throw both away with a
**slice** - a piece cut out of a list:

```
>>> numbers = [10, 20, 30, 40, 50]
>>> numbers[1:4]
[20, 30, 40]
>>> numbers[1:-1]
[20, 30, 40]
```

`list[start:stop]` gives you everything from `start` up to but not
including `stop` - the same "stops before the end" rule `range()` taught
you.  `numbers[1:-1]` reads as "everything except the first item and the
last item", which is exactly "drop the lowest and the highest" once the
list is sorted:

```
>>> scores = [9.5, 9.3, 9.7, 9.2, 9.6]
>>> sorted(scores)[1:-1]
[9.3, 9.5, 9.6]
```

Notice this drops **one** instance of the lowest and **one** of the highest,
even if two judges happened to give the exact same score - which is the
correct Olympic rule, and you got it for free without writing any `if`
statement to handle ties.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 4 - Lists](https://automatetheboringstuff.com/3e/chapter4.html)
* A Byte of Python
  * [Data Structures](https://python.swaroopch.com/data_structures.html)

# Instructions

Read a list of judges' scores for one routine.  Drop the lowest score and
the highest score, print what is left, then print the average of what is
left.

The input is:

```
line 1     N, how many scores follow
next N     the scores, one per line
```

There are always **at least 3** scores, so there is always at least one
left after dropping the two extremes.

Print:

```
remaining:
<the scores that were not dropped, one per line, lowest to highest>
average: <their average, to exactly two decimal places>
```

So for this input:

```
5
9.5
9.3
9.7
9.2
9.6
```

your program prints:

```
remaining:
9.3
9.5
9.6
average: 9.47
```

Notes:

* Sort the scores, then slice off the first and last with `[1:-1]` - that
  is both the lowest and highest dropped in one line, ties handled
  correctly with no extra code.
* The average is printed to **exactly two decimal places**, so `6` comes out
  as `6.00`.  An f-string does this for you: `f"{average:.2f}"`.
* Use `/` for the average, not `//`.  Integer division would throw away the
  fraction you are being asked for.
* `sum()` and `len()` are exactly what the built-ins section above was
  telling you to reach for - use them on the **remaining** scores, not the
  original list.

```
/challenge/run ./scorecard.py
```
