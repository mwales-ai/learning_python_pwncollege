# Tippy Tipper

So you made this cool program to help you calculate tips in the shebang
challenge.  But it seems kind of a pain in the butt to have to edit your script
each time you have to adust the amount of the bill you have to use your
program.  Wouldn't it be more useful if you could ask the user to give you
the data when you run the program.  Having values like that build into the
source code of a program is called hard-coding or having hard-coded constants.

Lets change that program up a little bit so that we can have the user give us
some information about the subtotal, and then we can have a more useful
interactive application

# Knowledge Upgrade

## `input` function

Python has an `input` function that can be used to get data from the user.  When
the user responds and then presses enter, the `input()` function will take the
data from the user and store it into a string for us.

```python
my_var = input()
```

Will wait for the user to enter some text and then press enter.  The variable
will then get a string of all the characters the user entered (it doesn't get
the newline character). The variable in our example is named `my_var`, but you
can give the variable any name that python allows for variables.

```python
my_var = input("Enter your name: ")
```

The input function can also take an argument for the prompt.  It outputs the
prompt and then on the same line waits for the user to type in their response.

## Conversion functions

The following functions are helpful for converting data from one data type
to another.  For example, take a look at this following example from the
python shell.

```
>>> user_value = input("Give me a number: ")
Give me a number: 5
>>> user_value * 5
'55555'
>>> int(user_value) * 5
25
>>> float(user_value) * 5
25.0
>>> 
```

While those all look kinda similar, some of them had very different results.
Multiplying a string by an integer causes string-replication.  If we convert
the string to an integer or floating point data type we get mathematical
multiplications of the values like we expect.

The following is a list of some other useful python functions:

* `str(value)`: for converting numerical values to strings
* `int(value)`: for converting strings to integers
* `float(value)`: for converting strings to non-whole floating point numbers
* `round(value, num_decimal_places)`: for rounding floating point numbers
* `abs(value)`: for getting the absolute value of a number

## Further Reading

* A Byte of Python
  * [First Steps](https://python.swaroopch.com/first_steps.html)
* Automate the Boring Stuff with Python
  * [Chapter 1](https://automatetheboringstuff.com/3e/chapter1.html)

# Instructions

Update your program from the shebang challenge for calculating tips.  Now
prompt the user for the different values that we had hardcoded for subtotal,
tax rate, and tip percentage.  Then using the same output format, calculate
what the total bill.

Your prompts need to look exactly like the following (and in this order).

```
What is the subtotal amount?
100.0
What is the tax amount?
10.0
What is the tip amount?
20.0
```

Then output the results (including repeating the values that the user just
gave you.)

```
SUBTOTAL = 100.0
TAX      = 10.0
TIP      = 20.0
TOTAL    = 130.00
```

Test your result by executing the evaluation script and pass it your program
that you wrote.

```console
/challenge/run ./my_solution.py
```
