# Birthday Banner

Lets practice some more python string handling features for this challenge.

## Strip Replication

The string replication feature in python is pretty unique, not many languages
have such a feature as built-in to the language as it is for python.  Incase
you forgot what string replication is, lets review.

I can replicate a string by multiplying it by an integer.  For example, we
can demonstrate in the python shell:

```
>>> "he" + "llo" * 3 + " hackers" + "!" * 5
'hellollollo hackers!!!!!'
```

The multiplication operations are all evaluated first, and then the strings
are added together using the addition operation (string concatenation)

## String length

You can use the `len()` function on many different containers you will use in
python.  When you pass the `len()` function a string, it will return the length
of it to you.

Example:

```
>>> test = "test string"
>>> len(test)
11
>>> len("how about now?")
14
>>> 
```

Unlike most of the string methods we showed you in the last module, this is a
function, notice the way you call it will be a little different:

```
>>> test.length()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'length'
>>> 
```

## Math Operations

If you are just multiplying numbers together, most of the operations are pretty
obvious for python, but there are some that have a little bit of nuance as
to how they work (or syntax for using).

```
| Operator | Operation           | Result Type                   | Example       |
|----------|---------------------|-------------------------------|---------------|
|    +     | Addition            | Float if either term is float | 2 + 1.0 = 3.0 |
|    -     | Subtraction         | Float if either term is float | 5 - 6 = -1    |
|    *     | Multiplication      | Float if either term is float | 8 * 4 = 32    |
|    /     | Division            | Float always                  | 4 / 2 = 2.0   |
|    //    | Int Division        | Integer (floored)             | 11 // 4 = 2   |
|    %     | Modulus / Remainder | Integer                       | 11 % 4 = 3    |
|    **    | Exponent            | Float if either term is float | 3 ** 3 = 27   |
```

Take notice that when you do integer division, the result is _NOT_ rounded to the
closest integer value (like you would normally do in math class).  The integer
division operation in python just drops off the decimal / fractional part.


# Further Reading
 
* A Byte of Python
  * [Operators and Expressions](https://python.swaroopch.com/op_exp.html)
* Automate the Boring Stuff with Python
  * [Chapter 1](https://automatetheboringstuff.com/3e/chapter1.html)

# Instructions

We are going to create a program that will make centered birthday banners for our
terminal.

Our program should accept the name of a person using the `input()` function.  It
should then print 3 lines of text out.  The first line of text it should output
is 80 `*` characters.  The last line of the program will be the same as the first
line.

For the middle line, we want to center `Happy Birthday Person Name` inbetween
`*` characters.  The width of the line should be 80 characters.  There should be
a single space between `*`s and the text that is centered.  The words should be 
in title case (the beginning letter of each word is capitalized).

Here is an example, if we enter the name `zardus n adam d.`.

```
********************************************************************************
*********************** Happy Birthday Zardus N Adam D. ************************
********************************************************************************
```

If the amount of `*`s you need for centering aren't exactly equal because of an
odd amount of characters in the banner text, then maek the left side group of
`*`s one shorter than the right side. The example above does this.


When you have completed your program, give it to the evaluation script to try 
out:

```
/challenge/run ./your_script.py
```

Your output has to match the expected output exactly to get the flag!
