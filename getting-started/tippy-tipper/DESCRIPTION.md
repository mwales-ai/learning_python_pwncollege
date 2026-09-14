# Tippy Tipper

Anyone who has split a restaurant bill has done this math: take the subtotal,
work out the tax, work out the tip, and add it all up.  It is a good first
`input()` program, because the numbers are familiar and you can check your
program's answers with a calculator.

If you wrote this as a program with the subtotal typed directly into the
source code - `subtotal = 45.20` sitting right there in the script - that
value is called **hard-coded**.  It works fine once, but the moment somebody
wants to check a different bill they have to go edit your source code, which
defeats the point of writing a program at all.

Let's write a version that asks the user for the numbers instead of having
them hard-coded.

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

Write an interactive tip calculator.

Ask the user for the subtotal of a bill, then for the tax rate and the tip
rate - **both given as percentages**, like `10` meaning 10%.  Your prompts
need to look exactly like the following, and in this order:

```
What is the subtotal amount?
80.0
What is the tax amount?
10.0
What is the tip amount?
20.0
```

Then print a four line breakdown:

```
SUBTOTAL = 80.0
TAX      = 8.0
TIP      = 16.0
TOTAL    = 104.00
```

Look closely at where those numbers come from, because this is the part
people get wrong: **`TAX` and `TIP` are dollar amounts, not the percentages
you were just given.**

* `TAX` is the subtotal times the tax percentage, divided by 100.  10% tax
  on an $80.00 subtotal is $8.00.
* `TIP` is the subtotal times the tip percentage, divided by 100.  20% tip
  on $80.00 is $16.00.
* `TOTAL` is the subtotal plus `TAX` plus `TIP`.

Printing the tax and tip numbers back unchanged will look correct by
accident when the subtotal happens to be `100.0` - `10%` of `100` is `10` -
but it is wrong for every other subtotal, which is exactly what the judge
will test.

Try your program by hand first and check the math yourself.  Then hand it to
the judge, which runs it three times with different random amounts:

```console
/challenge/run ./my_solution.py
```
