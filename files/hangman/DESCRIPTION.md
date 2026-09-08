# Hangman

Time to build an actual game.

Every Linux system ships a dictionary - a plain text file with one English
word per line.  It lives at `/usr/share/dict/words`.  Go look at it:

```
wc -l /usr/share/dict/words
head /usr/share/dict/words
shuf -n 5 /usr/share/dict/words
```

It is over a hundred thousand lines long, and it is exactly the sort of file
that is useless to open by hand and wonderful to open from a program.  Spell
checkers use it.  So do people cracking passwords.

That list is also a terrible source of hangman words - it is full of things
like `abaci` and `zwieback`.  So we built our own, and how we built it is
worth a minute of your time, because it is the kind of thing you will be able
to do yourself by the end of this dojo.

We downloaded about 124 Wikipedia articles about computing and hacking, plus
every chapter of both books recommended for this dojo.  That is roughly
818,000 words.  Then we downloaded 87 more Wikipedia articles about
everything *except* computing - cooking, sports, animals, history, music - as
a comparison pile.  Then we counted every word in both piles and asked a
simple question of each one: *how much more often does this word show up in
the computing pile than in the ordinary pile?*

Words like `which` and `other` are just as common in both, so they score
about 1 and sink to the bottom.  Words like `kernel`, `malware` and `boolean`
barely appear in the ordinary pile at all, so they rocket to the top.  The
500 words in `/challenge/words.txt` are what came out, cleaned up a bit.

That is counting words in files and looking things up - which is most of what
this module and the dictionaries module are about.  You are three challenges
away from being able to write it.

## Reading a file line by line, and counting as you go

You already know how to walk a file one line at a time.  The new trick is
keeping a count while you do it, so you can stop at the line you want:

```
line_number = 0
with open("/challenge/words.txt", "r") as f:
    for line in f:
        line_number = line_number + 1
        if line_number == 7:
            print(line)
            break
```

`break` leaves the loop immediately.  Without it you would keep reading the
other 493 lines for no reason.

## The bug you are about to hit

Every line you read from a file still has its newline character on the end.
That newline is invisible when you print it, and it absolutely counts as a
character:

```
>>> line = "hello\n"
>>> len(line)
6
>>> len(line.strip())
5
```

If your hangman board has one too many underscores, this is why.  **Strip
every line you read from a file.**

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)
* A Byte of Python
  * [Input and Output](https://python.swaroopch.com/io.html)

# Instructions

Write the game of hangman.  A word is picked, you get six wrong guesses, and
you try to reveal the word one letter at a time before you run out.

Your program reads everything with `input()`, one line at a time:

```
line 1     the path to the wordlist file
line 2     which line of that file holds the secret word (the first line is 1)
after that one guessed letter per line
```

Before any guessing, print the hidden word as underscores separated by
single spaces:

```
Word: _ _ _ _ _
```

Then, for each letter guessed, print exactly three lines:

```
<letter> is in the word!        (or)   <letter> is not in the word.
Word: h e l l _
Misses left: 4
```

* Revealed letters replace their underscore.  A letter that appears more than
  once is revealed **everywhere at once**.
* A guess that is not in the word costs one miss.  You start with 6.
* `Misses left:` is printed after every guess, right or wrong.

The game ends the moment one of two things happens, and you print one last
line and stop:

```
You win! The word was hello.
```

when every letter has been revealed, or:

```
You lose! The word was hello.
```

when your misses reach 6.  Do not print anything after that line.

Two rules to save you some head scratching:

* **Every guess is treated the same way, even a repeat.**  If you guess a
  wrong letter twice, that is two misses.  A real hangman game would say "you
  already guessed that" and let it slide - that is a nice thing to add
  afterwards, but it is not what we are checking for here.
* The input always contains exactly enough guesses to finish the game, so you
  never have to worry about running out of input.

## A complete example

If your program is given this input:

```
/challenge/words.txt
201
h
e
l
o
```

it must print exactly this:

```
Word: _ _ _ _ _
h is in the word!
Word: h _ _ _ _
Misses left: 6
e is in the word!
Word: h e _ _ _
Misses left: 6
l is in the word!
Word: h e l l _
Misses left: 6
o is in the word!
Word: h e l l o
Misses left: 6
You win! The word was hello.
```

Try it yourself first - the wordlist is readable, so you can look up line 201
and check your work.

Once it works, play it for real.  Nothing stops you from typing the guesses in
by hand instead of piping them, and nothing stops you from feeding it
`/usr/share/dict/words` and a line number of your choosing.  That is the point
of taking the path as input instead of burning it into the program.

Then make it executable and hand it to the judge:

```
chmod +x ./hangman.py
/challenge/run ./hangman.py
```
