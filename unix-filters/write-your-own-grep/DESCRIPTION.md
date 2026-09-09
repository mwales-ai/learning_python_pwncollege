# Write Your Own grep

You have used `grep` since Linux Luminarium.  Today you write it.

You already have every piece:

* `sys.argv[1]` - the pattern, from module 2
* `for line in sys.stdin:` - the data, from the last challenge
* `if pattern in line:` - the search, from module 3
* `sys.exit()` - the answer, from module 2

That is genuinely all `grep` is.

## Settings on the command line, data on standard input

Look at how the real one is used:

```
grep boot /var/log/messages
cat /var/log/messages | grep boot
```

The **pattern** is an argument, because it is a setting - short, and something
you want in your shell history.  The **data** is a file or a pipe, because it
might be enormous.

Keep that split and your tool works everywhere.  Put the pattern on standard
input and it can no longer be used in a pipeline at all, because the pipeline
is already using standard input for the data.

## `in` searches inside strings

```
>>> "boot" in "boot: kernel loaded"
True
>>> "boot" in "warn: disk nearly full"
False
```

Same `in` you used on lists in module 3.  On a string it asks about
**substrings**, so it matches anywhere in the line, which is exactly what
grep does.

## The exit code is the interesting part

Real `grep` exits `0` if it found something and `1` if it did not.  Try it:

```
hacker@dojo:~$ grep root /etc/passwd > /dev/null; echo $?
0
hacker@dojo:~$ grep zzzzz /etc/passwd > /dev/null; echo $?
1
```

**Exit 1 here is not an error.**  The search worked perfectly.  The answer was
"no", and that answer is delivered as a status so a script can use it:

```
grep -q "PermitRootLogin yes" /etc/ssh/sshd_config && echo "that is a problem"
```

This is the split from module 2 doing real work: **the matching lines are the
output, and whether anything matched is the status.**

To do that you need a flag that survives the loop - the accumulator pattern
with a boolean:

```
found = False
for line in sys.stdin:
    if ...:
        found = True
```

## What the real grep also does

Regular expressions, `-i` to ignore case, `-v` to invert, `-c` to count, `-n`
for line numbers, recursive directory search.  Yours does plain substring
matching, which is honestly what most people use grep for anyway.

## Further Reading

* `man grep`, now that you know what it is doing
* Automate the Boring Stuff with Python
  * [Chapter 7 - Pattern Matching with Regular Expressions](https://automatetheboringstuff.com/3e/chapter7.html)
    is where the real version goes next

# Instructions

Write a substring `grep`.

Your program is run with the pattern as its one command line argument, and the
lines to search arrive on standard input:

```
./grep.py boot
```

Print **only** the lines that contain the pattern, exactly as they came in.
Print nothing else on standard output - no count, no header.

Then exit with:

* `0` if at least one line matched
* `1` if nothing matched

So with the pattern `boot` and this input:

```
boot: kernel loaded
warn: disk nearly full
boot: starting network
info: ready
```

your program prints:

```
boot: kernel loaded
boot: starting network
```

and exits `0`.  With the pattern `zzz` on the same input it prints nothing at
all and exits `1`.

The matching is exact and case sensitive - `boot` does not match `Boot`.

Test it against the real thing:

```
cat /etc/passwd | ./grep.py root
cat /etc/passwd | grep root
```

```
/challenge/run ./grep.py
```
