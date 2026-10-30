# Define and Call

In almost all programming languages you can group a collection of code together
into a function, and then you can repeatedly call that function over and over,
and from different places in the code.  Other languages may call it a subroutine
or method, these concepts are very similar.

```
def area(width, height):
    return width * height
```

Parts of a function:

* `def` and a **name**
* **argument list** in parentheses - the values it needs
* a **body**, indented with spaces or tabs (be consistent)
* Optional return statements to return a value, or exit function early

You can write a function with no return statements at all.  The function will
stop executing when you get to the end of the indented lines of code.  A
function with no `return` gives back `None`.  If your output says `None`,
that is what happened.

## Parameters are local

```
def area(width, height):
    return width * height
```

Inside `area`, `width` means whatever was passed in **for this call**.  It has
nothing to do with any `width` outside, and changing it does not affect
anything out there.

That isolation is the whole reason functions are useful.  You can read
`area()` and understand it completely without knowing anything about the rest
of the program.

## Functions can call functions

```
def describe(width, height):
    if area(width, height) > 50:
        return "big"
    else:
        return "small"
```

`describe` does not repeat the multiplication - it asks `area` to do it.  This
is how programs get built out of small understandable pieces.

## Put your defs at the top

The `def` has to have run before the call does.  In practice: all your
functions at the top of the file, the code that uses them underneath.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 4 - Functions](https://automatetheboringstuff.com/3e/chapter4.html)
* A Byte of Python
  * [Functions](https://python.swaroopch.com/functions.html)

# Instructions

Write three functions and use them.

* `area(width, height)` - returns width times height
* `perimeter(width, height)` - returns twice the width plus twice the height
* `describe(width, height)` - returns the string `big` if the area is more
  than 50, otherwise `small`

All three must **return** their answers, not print them.  `describe` should
call `area` rather than doing the multiplication itself.

Your program reads:

```
line 1     N, how many rectangles follow
next N     a line of "<width> <height>", separated by a space
```

For each rectangle print exactly three lines:

```
<w> x <h> area <the area>
<w> x <h> perimeter <the perimeter>
<w> x <h> is <big or small>
```

So for this input:

```
2
17 6
2 3
```

your program prints:

```
17 x 6 area 102
17 x 6 perimeter 46
17 x 6 is big
2 x 3 area 6
2 x 3 perimeter 10
2 x 3 is small
```

`.split()` turns `17 6` into a list of two strings, which you will need to
`int()`.  Exactly 50 counts as `small`, since the rule is "more than 50".

```
/challenge/run ./shapes.py
```
