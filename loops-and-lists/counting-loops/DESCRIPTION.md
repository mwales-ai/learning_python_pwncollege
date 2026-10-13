# ASCII Values

Every character you have ever typed is secretly a number.  Your computer
never actually stores the letter `A` - it stores `65`, and only turns it
back into a letter shape when it draws it on your screen.  Time to see that
number for yourself.

## for loops and range()

A `while` loop keeps going until something changes.  A `for` loop does
something a **known number of times**, and that turns out to be most of what
you want.

```
for i in range(5):
    print(i)
```

prints `0 1 2 3 4`, each on its own line.

## range() comes in three shapes

```
range(5)           0 1 2 3 4
range(2, 6)        2 3 4 5
range(1, 10, 2)    1 3 5 7 9
range(5, 0, -1)    5 4 3 2 1
```

* One argument: start at 0, count up to *but not including* it.
* Two arguments: start, stop.
* Three arguments: start, stop, **step**.  A negative step counts down.

## The thing that confuses everybody

**`range()` stops BEFORE the stop value.**

`range(1, 10)` is 1 through 9.  Not 10.  This looks like a design mistake for
about a week and then starts making sense, because `range(len(word))` gives
you exactly the valid positions of `word` - which is exactly what you want
below.

## Indexing into a string

You have already seen square brackets pick one item out of something -
`sys.argv[0]` is the first item of `sys.argv`.  A string works the same way.
`word[i]` gives you the single character at position `i`, counting from 0:

```
>>> word = "Hi!"
>>> word[0]
'H'
>>> word[1]
'i'
>>> word[2]
'!'
```

Combine that with `range(len(word))` and you can visit every character, one
at a time, in order:

```
for i in range(len(word)):
    print(word[i])
```

`i` takes on every valid position - `0`, `1`, `2` - and `word[i]` is the
character sitting there.  This is the loop variable being a real variable,
not just a counter ticking away in the background: you are using `i` itself
to reach into `word`.

## ord() and chr(): turning that into a number

`ord()` takes a single character and gives you back the whole number your
computer actually stores for it - its **ASCII value**.  `chr()` goes the
other direction, number back to character:

```
>>> ord("A")
65
>>> ord("a")
97
>>> ord(" ")
32
>>> chr(65)
'A'
>>> chr(97)
'a'
```

Notice `"A"` and `"a"` are 32 apart, and every letter keeps that same gap -
that is exactly how `.upper()` and `.lower()` work under the hood.

## Hex, one more time

Hex to Decimal showed you `f"{n:02X}"`: capital letters, no `0x`, padded to
at least 2 digits - exactly enough for one byte, which is exactly the size
of an ASCII value.

```
>>> f"{ord('A'):02X}"
'41'
```

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)
* [The ASCII table](https://www.asciitable.com/) - skim it once. `0`-`9` are
  consecutive, `A`-`Z` are consecutive, `a`-`z` are consecutive, and none of
  those three ranges touch each other.

# Instructions

Read one line of text and print one line **per character**:

```
<character> <decimal ASCII value> <hex ASCII value>
```

Each piece is separated by a single space.  The hex value uses the Hex to
Decimal style: capital letters, no `0x` prefix, at least 2 digits.

Use a `for` loop over `range(len(...))` and index into the string with `[i]`
to get each character - that is what this challenge is practicing.  Python
also has a shorter way to walk a string directly, but you have not been
taught it yet; you will meet it properly in Loop Over a List.

So for input `Go Hackers!`:

```
G 71 47
o 111 6F
  32 20
H 72 48
a 97 61
c 99 63
k 107 6B
e 101 65
r 114 72
s 115 73
! 33 21
```

That line that looks like it starts with two spaces is not a mistake - the
character being described on that line **is** a space, and the separator
right after it is a second space.  `  32 20` is the correct line for a
space character.

```
/challenge/run ./ascii.py
```
