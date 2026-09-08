# Loop Over a List

You can loop over a list by position:

```
for i in range(len(numbers)):
    print(numbers[i])
```

But when you do not actually need the position, there is a much better way:

```
for value in numbers:
    print(value)
```

That gives you the **items themselves**, one at a time.  No `range()`, no
`len()`, no indexing, and nothing to get off by one.  It also reads like
English.  Use this one unless you specifically need to know *where* you are.

It works on strings too, which is how you will take a word apart in the next
challenge:

```
for ch in "cat":
    print(ch)
```

## The accumulator pattern

This is the real content of this challenge, and it is one of the half dozen
patterns you will use for the rest of your life.

**Create a variable before the loop.  Update it once per item.  Use it after
the loop.**

```
total = 0
for value in numbers:
    total = total + value
print(total)
```

`total` has to exist *before* the loop, because you cannot add to something
that does not exist yet.  And it has to be *outside* the loop, because a
variable created inside gets reset every time round - that is why a broken
version reports the last number instead of the sum.

You have already met this shape twice without it being named: the birthday
banner built up a string, and the guessing game counted guesses.  Same
pattern, different starting value:

| Building a | Start with |
|------------|-----------|
| total | `0` |
| string | `""` |
| list | `[]` |
| count | `0` |

## Finding the largest: the seeding trap

Finding the biggest item looks like the same thing:

```
largest = 0
for value in numbers:
    if value > largest:
        largest = value
```

That is **wrong**, and it is wrong in a way that works fine right up until it
does not.  Give it `[-5, -10, -1]` and it says the largest is `0` - a number
that is not even in the list.

The fix is to start from something that is genuinely a candidate.  The first
item always is:

```
largest = numbers[0]
```

Ask yourself what your accumulator should be before you have seen anything.
For a sum, "nothing yet" really is 0.  For a maximum, there is no such value,
so use the first item.

## You will not write this again

Python already has these:

```
>>> sum(numbers)
>>> max(numbers)
>>> min(numbers)
```

In real code, use them.  We are writing the loops by hand exactly once, so
that the pattern is yours - because the moment you need something Python does
*not* have a built-in for, you will write this loop again from memory.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 4 - Lists](https://automatetheboringstuff.com/3e/chapter4.html)
* A Byte of Python
  * [Data Structures](https://python.swaroopch.com/data_structures.html)

# Instructions

Read a list of numbers and print some statistics about them.

The input is:

```
line 1     N, how many numbers follow
next N     the numbers, one per line
```

Print exactly five lines:

```
count: <how many numbers>
total: <all of them added up>
largest: <the biggest>
smallest: <the smallest>
average: <the total divided by the count, to two decimal places>
```

For this input:

```
4
7
3
9
1
```

your program prints:

```
count: 4
total: 20
largest: 9
smallest: 1
average: 5.00
```

Notes:

* The average is printed to **exactly two decimal places**, so 5 comes out as
  `5.00`.  An f-string does this for you: `f"{average:.2f}"`.
* Use `/` for the average, not `//`.  Integer division would throw away the
  fraction you are being asked for.
* Some of the test cases are **all negative numbers**.  If you seed `largest`
  with 0, they will catch you.

Write the loops yourself for this one rather than using `sum()`, `max()` and
`min()` - after this challenge, use the built-ins.

```
/challenge/run ./stats.py
```
