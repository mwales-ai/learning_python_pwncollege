# Run It Yourself

Last time you ran your program by handing it to Python:

```
python hello_hackers.py
```

That works, but it is not how the programs on your computer work.  You do not
type `elf-loader firefox`.  You just run `firefox`.  Your program can work the
same way, and it takes exactly two things.

## Thing one: the shebang

The very first line of your file needs to be this, and it has to be the
*first* line - not the second, not after a blank line, not after a comment:

```
#!/usr/bin/env python3
```

That is called a **shabang**, **shebang**, or **hash bang** (feel free to look
at a person funny if the call it hash bang....). It's named from "sharp" `#`
and "bang" `!`.  When Linux is asked to run a file, it peeks at the first two
bytes.  If they are `#!`, it reads the rest of that line and uses it as the
program to run your file with.

`/usr/bin/env python3` means "go find whichever python3 is on the PATH".  You
will also see people write `#!/usr/bin/python3`, which names one exact
interpreter.  The `env` version is more portable, which is why we use it.

To Python that line is just a comment, because it starts with `#`.  It is
there for Linux, not for Python.

## Thing two: permission to run

A file has separate permissions for reading, writing, and **executing**.  A
text file you just created is not executable, and Linux will refuse:

```
hacker@dojo:~$ ./myprogram.py
bash: ./myprogram.py: Permission denied
```

`chmod +x` turns the execute bit on:

```
chmod +x myprogram.py
```

Have a look before and after with `ls -l`.  Those `x` characters are the
difference:

```
-rw-r--r--  1 hacker hacker  52 Jan  1 10:00 myprogram.py     <- before
-rwxr-xr-x  1 hacker hacker  52 Jan  1 10:00 myprogram.py     <- after
```

## Why `./`?

Once it is executable you run it like this:

```
./myprogram.py
```

Not `myprogram.py`.  The `./` means "the file called myprogram.py **in this
directory**".  Without it, the shell only looks in the directories on your
`PATH`, and the current directory is deliberately not one of them.

That is a security decision, and a good one.  If `.` were on your PATH,
anybody who could drop a file named `ls` into a directory could get you to run
their program the next time you typed `ls` in it.

## Further Reading

* Linux Luminarium covers `chmod` and `PATH` in more depth - this is the same
  material from the other side.

# Instructions

Write a program that prints exactly this one line:

```
I am a real program now
```

But this time you must be able to run it **without typing python**.  Give it a
shebang line, make it executable, and check that this works:

```
./myprogram.py
```

If you see `Permission denied`, you have not run `chmod +x` yet.  If you see
something about `exec format error` or the file being opened in an editor, the
shebang line is missing or is not the first line of the file.

Then hand it to the judge:

```
/challenge/run ./myprogram.py
```

From now on every challenge in this dojo is run this way, so get comfortable
with it.  The judge runs your program directly, exactly like the shell does,
and it will tell you if the shebang or the execute bit is missing.
