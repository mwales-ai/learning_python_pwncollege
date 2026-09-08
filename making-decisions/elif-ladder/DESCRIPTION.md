# The elif Ladder

`if` and `else` give you two choices.  Often you need five.

`elif` is short for "else if", and it means *otherwise, try this one*:

```
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

## The one rule that matters: first match wins

Python tries each test **in order** and stops at the first true one.  The rest
of the ladder is skipped entirely - not tested, not run.

That is why you do not need to write the upper bound.  Look at the `>= 80`
branch: it does not say "and less than 90".  It does not need to.  If the
score were 90 or more, the branch above would have caught it and we would
never have got here.

## The upside down ladder

This is the classic bug, and it is worth staring at until it is obvious:

```
if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 90:
    grade = "A"
```

Score 95 hits the very first test - 95 is definitely `>= 60` - so it is a D,
and the program never looks at the other branches.  In fact *every* passing
score is a D and the rest of the ladder is unreachable code.

Go from one end to the other consistently.  High to low, or low to high, but
pick one.

## elif is not the same as several ifs

```
if score >= 90:          if score >= 90:
    grade = "A"              print("A")
elif score >= 80:        if score >= 80:
    grade = "B"              print("B")
```

The left one picks **one** branch.  The right one tests **every** condition
independently, so a score of 95 prints both `A` and `B`.  When you find your
program printing two answers, this is why.

## The final else

The `else` at the bottom has no test.  It catches everything that fell all the
way through, which is what makes the ladder **total** - there is no input it
fails to answer.  Leave it out and some inputs produce nothing at all, which
is usually not what you want.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)

# Instructions

Read one line - a score from 0 to 100 - and print exactly one line:

```
<the score> is a <letter grade>
```

Using this scale:

| Score | Grade |
|-------|-------|
| 90 and above | A |
| 80 to 89 | B |
| 70 to 79 | C |
| 60 to 69 | D |
| below 60 | F |

So `95` gives:

```
95 is a A
```

Yes, "a A" is not good English.  It is what the judge expects, and making the
grammar right would mean another decision you have not been taught yet.

Be careful at the boundaries.  `90` is an A, `89` is a B.  `60` is a D, `59`
is an F.  Using `>` where you want `>=` breaks exactly those cases and nothing
else, which makes it a nasty bug to spot - so test them.

```
/challenge/run ./grade.py
```
