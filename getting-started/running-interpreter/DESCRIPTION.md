# Running the interpreter

Normally before you can do anything with Python, you would need to install
Python.  Python fortunately is a free application.  It was originally written
by Guido van Russom, but it is now maintained by the Python Software
Foundations.  For pwn.college (and in fact my Linux distributions), Python is
already installed.

To start with, we are going to play around a bit in the Python interpreter.
This is an application that lets you enter Python instructions and it will
immediately execute them after you hit enter.  This is great for trying out
different Python commands to see how something works.

Normally, you will start the Python interpreter by running the application:

```console
python
```

or 

```console
python3
```

Some Linux distributions will also have the Python version 2 interpreter that
can be started, usually by explicitly telling the system you want to run the
older interpreter

```console
python2
```

For pwn.college, we are going to focus on using Python 3 since that is what all
students should learn and use for their programs.

For this challenge I'm going start the interpreter for you when you run the
challenge command

```console
/challenge/run
```

I'm going to load the flag for you into a Python variable.  You will just need
to print the contents of the variable.  We'll explain more of this later, but
for now, follow the instructions in the instructions section.

## Further Reading

* A Byte of Python
  * [About Python](https://python.swaroopch.com/about_python.html)
  * [First Steps](https://python.swaroopch.com/first_steps.html)
* Automate the Boring Stuff with Python
  * [Introduction](https://automatetheboringstuff.com/3e/chapter0.html)
  * [Chapter 1](https://automatetheboringstuff.com/3e/chapter1.html)

## Follow Along Example

Start the Python interpreter using my script (normally you would just type Python
into the terminal)

```console
/challenge/run
```

It should have print out a short banner message about which version of Python
you are running and then left you at a prompt that looks like the following:

```
>>>
```

Now you are in the Python interpreter.  You can type in Python commands here.  Lets
try to have it do some math.  Type in the following expression:

```python
8 * 43.2
```

The expression is immediately evaluated when you hit enter and then the answer is
printed out.

We can also create variables in Python that will store values and things for
us.  We are going to create a variable and store our expression result in it.
First we have to come up with a name for our variable.

Rules for variable names:

* No spaces
* Only letters, numbers, and underscores
* Can't begin with a number
* It can't be a Python keyword (Python already has a bunch of names reserved)

For our example, lets name the variable leet, and assign it the value of 1337.
Spaces and white space only matter at the beginning of a Python command, for now,
don't put any spaces before your instructions.  Any spaces or whitespace after
the first text normally don't matter.


```python
leet = 1337
```

We don't see anything output after this instruction, except the next prompt.  Our
value 1337 was assigned to the variable leet.  We can see the value of leet by
just evaluating leet by itself

```python
leet
```

Now 1337 is printed in the terminal.  For this challenge, I have already loaded
a variable with the flag, and you just need get the variable contents to be
printed out.

One last thing, when you want to exit the interpreter, you have to call the exit
function. Don't forget the parentheses when you call the exit function.

```python
exit()
```

# Instructions

For this challenge start the python interpreter by calling `/challenge/run`.
We normally don't need to start the interpreter this way, this is unique for a
few pwn.college challenges.

Once you are in the python interpreter, print the contents of the variable
named `flag4me` to reveal the flag.

