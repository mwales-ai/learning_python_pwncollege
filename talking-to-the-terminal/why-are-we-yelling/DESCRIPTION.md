# Why Are We Yelling?

For this next challenge we want to use some string methods and demonstrate
how to use them.

## String functions

Python has some incredibly powerful
[methods for manipulating strings](https://docs.python.org/3/library/stdtypes.html#string-methods) 
built into the language.  Here is a quick list of some methods that we could
use already with python skills we have acquired so far:

* `capitalize()`: returns a copy of string with first letter capitalized
* `center(width, fill_char)`: returns a string that is centered between the
  fill_char, and width number of characters long
* `lower()`: returns a copy of string with all characters converted to lower
  case
* `upper()`: returns a copy of string with all characters converted to upper
  case
* `replace(old, new)`: returns a copy of string with any substring old,
  replaced by a new substring of text
* `strip()`: returns a copy of string with the whitespace characters from
  beginning and the end removed
* `title()`: returns a copy of the string with the first character of each
  word uppercase, and the remaining all lowercase

If any of these aren't obvious, check out the detailed help information at the
link above or just try them out and play around with them.

## String immutability

This may not make a lot of sense yet, but we will introduce it here, and then
this topic will come back when we get to lists and some more advanced features
of python. But you surely at some point will have a bug in your python because
you forgot about this.

Strings in python are what we call _immutable_.  You can not change the
contents of what is in a string. So all the example functions above say they
return a copy of a string that has the changes. Later on as we learn about
python, we learn about lists, and the contents of lists we can change, so
they are considered _mutable_.

* immutable: constant, does not change
* mutable: can be changed

Lets demonstrate with some examples from the python shell:

```
>>> test_string = "we always say hello hackers"
>>> print(test_string)
we always say hello hackers
>>> all_upper = test_string.upper()
>>> print(test_string)
we always say hello hackers
>>> print(all_upper)
WE ALWAYS SAY HELLO HACKERS
>>> all_upper.title()
'We Always Say Hello Hackers'
>>> print(all_upper)
WE ALWAYS SAY HELLO HACKERS
>>> print(all_upper.lower())
we always say hello hackers
>>> 
```

If we do want to change our string variable, we can set it's value to the
new string returned from a function.

```
>>> test_string = "we always say hello hackers"
>>> test_string = test_string.upper()
>>> print(test_string)
WE ALWAYS SAY HELLO HACKERS
```

# Instructions

For this next challenge we are going to read in single line of text from
standard input, and then turn it into very profane yelling text.  We will
convert all the characters to upper case _LIKE WE ARE YELLING_.  To make it
profane, we will use [unnecessary censorship](https://www.youtube.com/watch?v=Sc7J1w5Mxmk).
We will replace all vowels with `*` characters so it looks like a profanity
that was censored.

For example, if we sent your program the following text:

```
I saw a duck eating a cake at a slot machine in vegas
```

Your program should output:

```
* S*W * D*CK **T*NG * C*K* *T * SL*T M*CH*N* *N V*G*S
```

You can test your program by executing the following:

```
cat /challenge/sample.txt | ./your_script.py
```

When it works, run give it to the evaluation script to try out:

```
/challenge/run ./your_script.py
```

Make sure your script is executable permission and has proper shebang line!
