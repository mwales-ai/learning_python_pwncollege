# Hello Hacker

The first program everyone has to write for a new language they are learning is
the "Hello World" program.  We usually use this to make sure our environment is
setup correctly.  Some languages have compilers that you want to be able test
out and make sure it works.  And once your program is built, does the system
you want to run your program have all the correct run-time libraries and / or
interpreters in place to execute it?

Since we are hackers here, we are going to slightly modify our "Hello World"
program to be "Hello Hackers".  Up to this point we have been running our
python instructions directly in the python interpreter, but now we are going
to put them in a file, and then let the interpreter execute them all at once.

## Further Reading

* A Byte of Python
  * [First Steps](https://python.swaroopch.com/first_steps.html)

# Follow Along

You are going to first need determine which file editor you want to use for
writing your program in.

The following are editors that are available for the command line:
* nano
* vi / vim (not for new programmers, takes some time to learn and master)
* emacs (also not for new programmers)

For the desktop:
* gedit
* vim and neovim
* emacs

But what is probably the easiest and most for familiear for most of you will be
Visual Studio Code which is available as a web IDE on pwn.college that is
connected directly to your challenge virtual machine.

Using your editor of choice, create a new text file somewhere in your home
directory, and add the following line to it.

```
print("Hello Hackers")
```

You should save your file with a .py extension so it's easy to tell later that
it's a python script.  It's not actually neccessary on Linux to do this, just
a common convention.  On windows it will likely let you double-click the file
in explorer to run it with the Windows python interpreter if you have one 
installed. You should also avoid including spaces in your filename, most
developers use underscores (called_snake_case) or capitalize the first letter
of each word (ThatsCalledCamelCase).

After we save the file in our home directory (which is /home/hacker), it will
stay there until we delete it.  Even if you start on other challenges, your
home directory will stay there and can store up to 1GB of files (you probably
won't need that many).

Next we want to start a terminal and test our script out and make sure it works.
You can horizontally split a window in Visual Studio Code and run a terminal
from directly within Visual Studio Code, or restart your challenge VM in a
terminal (make sure you save your work before doing this).  For this walkthrough
I will assume we have named our file hello_hackers.py. Now we will tell the
python interpreter to execute our script for us.

```
python hello_hackers.py
```

It should print out Hello Hackers and then return you to a command prompt.

Now to complete the challenge, we need to tell the challenge evaluation program
where your file is so it can run it and check it out:

```
/challenge/run /home/hacker/hello_hackers.py
```

# Instructions

Write a python script that prints a single line that says the following:

```
Hello Hackers
```

Pass that program name to the /challenge/run program to get your flag:

```
/challenge/run /path/to/my/program.py
```


