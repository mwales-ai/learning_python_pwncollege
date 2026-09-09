# Slicing Strings Apart

A tour of the string methods.  Keep this challenge's page - you will come back
to it.

## Cleaning up

```
>>> "   hello   ".strip()
'hello'
```

`.strip()` removes whitespace from **both ends** and leaves the middle alone.
`.lstrip()` and `.rstrip()` do one end each.  You have been using this on every
line you read from a file.

## Changing case

```
>>> "Hopper".upper()
'HOPPER'
>>> "Hopper".lower()
'hopper'
```

`.lower()` is the standard trick for comparing things case-insensitively:

```
if answer.lower() == "yes":
```

Now `Yes`, `YES` and `yes` all work.

## Taking a line apart: split()

```
>>> "the cake is a lie".split()
['the', 'cake', 'is', 'a', 'lie']
```

`.split()` with no argument splits on **any run of whitespace** and discards
empty pieces.  That is almost always what you want for words.

`.split(",")` splits on one specific character and **keeps** the empties:

```
>>> "a,,c".split(",")
['a', '', 'c']
```

That difference looks pedantic until the next challenge, where an empty cell
in a spreadsheet has to stay in its column.  Both behaviours are right - for
different jobs.

## Putting it back together: join()

`.join()` is backwards from what everyone expects.  **The separator is the
string you call it on:**

```
>>> "-".join(["a", "b", "c"])
'a-b-c'
>>> ", ".join(words)
```

Not `words.join("-")`.  Everybody writes it the wrong way round the first
time.  (The reason is that it works on any sequence, so it belongs to the
separator rather than to lists specifically.)

## Searching

```
>>> "boot: kernel".startswith("boot")
True
>>> "kernel.log".endswith(".log")
True
>>> "hello".find("l")
2
>>> "hello".find("z")
-1
```

`.find()` gives the position of the first match, or **-1** if there is none.

That -1 is a trap.  `-1` is a perfectly valid index in Python - it means the
last character - so code that does not check the result will silently work on
the wrong character instead of failing:

```
pos = line.find(":")
print(line[pos])          # if not found, prints the LAST character
```

Check for `-1`, or use `in` when you only want to know whether it is there.

`.index()` does the same job but raises a `ValueError` when it is missing.
Failing loudly is often better than a wrong answer.

## Replacing

```
>>> "the cake is a lie".replace("cake", "pie")
'the pie is a lie'
```

`.replace()` changes **every** occurrence, not just the first.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 6 - Manipulating Strings](https://automatetheboringstuff.com/3e/chapter6.html)

# Instructions

Read one line of text - it may have spaces around it - and print exactly nine
lines describing it.

```
stripped: <the line with surrounding whitespace removed>
length: <how many characters the stripped line has>
upper: <the stripped line in upper case>
lower: <the stripped line in lower case>
words: <how many words it splits into>
first word: <the first word>
joined: <the words joined back together with a single dash between them>
starts with the: <True or False - does the lower cased line start with "the">
position of e: <the position of the first "e", or -1>
```

Everything after `stripped` works on the **stripped** version, not the
original.

So for the input line `   The Analytical Engine has no pretensions`:

```
stripped: The Analytical Engine has no pretensions
length: 40
upper: THE ANALYTICAL ENGINE HAS NO PRETENSIONS
lower: the analytical engine has no pretensions
words: 6
first word: The
joined: The-Analytical-Engine-has-no-pretensions
starts with the: True
position of e: 8
```

Note `starts with the` is True even though the line begins with a capital
`The` - lower case it before you check.

```
/challenge/run ./strings.py
```
