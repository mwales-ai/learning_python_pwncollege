# Say My Name

So far your programs have said the same thing every time.  Time to let them
listen.

## input()

`input()` reads one line of text from standard input and hands it back to you:

```
>>> name = input()
Grace Hopper
>>> name
'Grace Hopper'
```

Three things to know about it:

* It reads **one line**.  Want two lines?  Call it twice.
* It strips the newline off the end for you, so you get `'Grace Hopper'` and
  not `'Grace Hopper\n'`.
* It **always gives you a string**, even if the person typed digits.  That
  will matter enormously in the next challenge.

## Where does input come from?

When you run your program in a terminal, `input()` waits for you to type.
But it does not have to be you.  Standard input can just as easily come from
a file or from another program:

```
./greet.py                       <- you type it
echo "Grace Hopper" | ./greet.py <- another program types it
./greet.py < names.txt           <- a file types it
```

Your program cannot tell the difference and does not care.  That is exactly
why this is worth learning early: the judge is going to feed your program its
input this way, and so will every pipeline you ever build.

If you run your program and it just sits there doing nothing, it is not
frozen - it is waiting for input.  Type a line and press enter.  `Ctrl-D`
tells it there is no more input coming.

## Do not use a prompt

```
name = input("What is your name? ")
```

Do not do this here.  That prompt is printed to standard output, right in
front of your answer, and the judge is reading standard output:

```
Line 1 = What is your name? Hello, Grace Hopper!
stdout line 1 is incorrect
```

Call `input()` with nothing in the brackets.

## Further Reading

* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)
* Automate the Boring Stuff with Python
  * [Chapter 1 - Python Basics](https://automatetheboringstuff.com/3e/chapter1.html)

# Instructions

Write a program that reads two lines:

```
line 1     a person's name
line 2     a place
```

and prints exactly two lines:

```
Hello, <name>!
Welcome to <place>.
```

So if your program is given this input:

```
Grace Hopper
the Wildcat Computer Science Club
```

it must print:

```
Hello, Grace Hopper!
Welcome to the Wildcat Computer Science Club.
```

Mind the punctuation - the exclamation mark on the first line and the full
stop on the second are part of the answer.

Try it by hand first, then:

```
/challenge/run ./greet.py
```
