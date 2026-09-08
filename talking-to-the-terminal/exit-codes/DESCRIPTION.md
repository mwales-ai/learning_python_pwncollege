# Exit Codes

When a program finishes, it hands one small number back to whoever started it.
That number is the **exit status**, and it answers exactly one question: did
this work?

* **0 means success.**  Zero problems.
* **Anything else means failure.**  Which number can mean which kind of
  failure, if the program wants to say.

It is backwards from what you would guess, and there is a reason: there is
only one way to succeed, but lots of ways to fail, so success gets the one
special value.

## Seeing it

The shell keeps the last exit status in `$?`:

```
hacker@dojo:~$ ls /home
hacker
hacker@dojo:~$ echo $?
0
hacker@dojo:~$ ls /nope
ls: cannot access '/nope': No such file or directory
hacker@dojo:~$ echo $?
2
```

`$?` is only about the command you *just* ran, so check it immediately -
`echo $?` twice in a row prints the status of the first `echo` the second
time.

## Why it matters

Because the shell reads that number and makes decisions with it:

```
./build.py && ./deploy.py      # deploy ONLY if build succeeded
./try_this.py || ./plan_b.py   # run plan B ONLY if the first one failed
```

`&&` and `||` are not "and" and "or" here - they are "if that worked" and "if
that failed".  Every install script, every CI pipeline, and every bit of shell
glue in the world is built out of this.

It is also how tools answer yes/no questions.  `grep` exits `1` when it found
nothing.  That is not an error - the search worked fine - it is the *answer*,
delivered as a status so a script can act on it.

That is the split worth remembering: **answers go to standard output,
success and failure go to the exit status.**

## Doing it in Python

`sys.exit(n)` ends the program right there with status `n`:

```
import sys

print("something went wrong", file=sys.stderr)
sys.exit(1)
```

If you never call it, Python exits `0` for you when the program runs off the
end.  So every program you have written so far has been quietly reporting
success.

The status is a single byte, so it only goes from 0 to 255.  `sys.exit(256)`
actually reports `0`, which is a fun way to make a program lie about failing.

## Further Reading

* Linux Luminarium covers `$?`, `&&` and `||` from the shell side.
* A Byte of Python
  * [Standard Library](https://python.swaroopch.com/stdlib.html) mentions
    `sys`

# Instructions

Write a program that reads a single number and exits with that number as its
exit status.

Read one line, a number from 0 to 255.  Print exactly one line on standard
output:

```
exiting with status <the number>
```

Then exit with that number as your exit status.

So given input `42`, your program prints:

```
exiting with status 42
```

and `echo $?` afterwards shows `42`.

**This challenge checks your exit status as well as your output.**  Getting
the line right but always exiting 0 will not pass.

You do not need `if` for this - you have not been taught it yet, and you do
not need it.  The number you should exit with is the number you were given.

Check it yourself:

```
echo 42 | ./status.py
echo $?
```

and try wiring it into the shell, which is the whole point:

```
echo 0 | ./status.py && echo "the shell thinks that worked"
echo 1 | ./status.py || echo "the shell thinks that failed"
```

```
/challenge/run ./status.py
```
