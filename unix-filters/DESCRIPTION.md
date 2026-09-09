# Unix Filters

This is the module the whole dojo has been walking towards.

A **filter** is a program that reads from standard input, writes to standard
output, and does one job.  That is the entire idea, and it is the reason Linux
is built the way it is.  Because every tool follows that one convention, any
tool can be plugged into any other:

```
cat access.log | grep " 404 " | ./count.py
```

Nobody who wrote `cat`, or `grep`, or your program had to know about the
others.  They agreed on one thing - text in, text out - and that agreement is
worth more than any individual feature.

You already have every piece you need:

* the `for line in f:` loop, from the files module - `sys.stdin` is just
  another file
* `sys.argv`, from module 2 - settings come from the command line
* standard error, from module 2 - complaints go there, never into the pipe
* exit codes, from module 2 - how a filter answers a yes/no question

In this module you will rebuild `grep` and `wc`, write something that sits in
the middle of a pipeline, and take the FizzBuzz you wrote in module 4 and turn
it from a program that makes up its own data into one that processes somebody
else's.

## The rules of being a good filter

1. **Read standard input.**  Do not ask where the data is; it is being handed
   to you.
2. **Write the answer, and only the answer, to standard output.**  A banner, a
   prompt or a progress message on stdout is data as far as the next program
   is concerned, and it will be counted, sorted, or searched along with
   everything else.
3. **Put everything else on standard error.**  Warnings, skipped lines,
   "processing file 3 of 10".
4. **Do not die because one line was bad.**  Complain and carry on.  A tool
   that quits on line 900,000 of a million line file, having printed nothing,
   is useless.
5. **Report success or failure with your exit code**, so a script can act on
   it.

Follow those five and your program is a real Unix tool, indistinguishable from
the ones that shipped with the system.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)
* Linux Luminarium's pipes and redirection material is the other half of this
  module.  This is where it pays off.
