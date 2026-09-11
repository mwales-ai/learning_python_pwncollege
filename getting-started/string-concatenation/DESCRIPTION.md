# More of the Python interpeter

The variables in python can store numbers, sequences of characters (which we
will usually just call [strings](https://docs.python.org/3/library/string.html)),
lists of objects, and so forth.  And you will learn how all this works in future
challenges.

For this next challenge we are going to use some variables that have strings
stored within them already. We are going to concatenate 2 strings into a single
longer string, and then call a function with the resulting string to discover
the flag.

## Further Reading

* A Byte of Python
  * [First Steps](https://python.swaroopch.com/first_steps.html)
* Automate the Boring Stuff with Python
  * [Chapter 1](https://automatetheboringstuff.com/3e/chapter1.html)

# Follow Along Example

You can start this challenge by starting up our specially prepared Python shell
by executing the following instruction in a terminal.

```console
/challenge/run
```

We have split up the flag and stored it in a secret encoded form in 2 different
variables in your shell. Lets take a look at the two secret encoded strings
(we normally call encoded data ciphertext).


```
ct1
ct2
```

We first need to concatenate the two strings.  [Concatenation](https://www.w3schools.com/python/gloss_python_string_concatenation.asp)
simple means we are going 2 join.  This is easy to understand with an
example:

```
>>> p = "pwn"
>>> c = "college"
>>> d = "."
>>> school = p + d + c
>>> school
'pwn.college'
```

Lets now join our 2 encoded cipher texts into a single ciphertext.

```python
single_ct = ct1 + ct2
```

To look at the result:

```
single_ct
```

Another thing we can do with the Python interpreter is we can call functions.
One of the functions built into Python is the `len` function, which will
calculate how many characters are in a string.  For example, if we wanted 
to know the length of the school variable:

```
>>> len(school)
11
```

There is a custom function that is available in the challenge shell that
can decrypt the secret message and show you the flag.  The function is
called `secret_decoder`.

You need to call it and pass it your `single_ct` variable to decode the 
secret message and get the flag.

```python
secret_decoder(single_ct)
```

# Instructions

For this challenge start the python interpreter by calling `/challenge/run`.
We normally don't need to start the interpreter this way, this is unique for a
few pwn.college challenges.

Join the 2 strings stored in the variables `ct1` and `ct2`.  The decode the flag
by passing that combined string to the `secret_decoder` function.


