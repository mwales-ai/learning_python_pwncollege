# Word Game

A word-guessing game, five letters at a time, with colored feedback on
every guess telling you how close it was.  If that sounds familiar, it is
the same idea as the popular word game Wordle - with one real simplification
explained below, so do not expect it to feel identical.

## Two word lists

```
ls /challenge/
```

shows you `word-bank.txt` and `valid-words.txt`.  Both are plain text, one
five-letter word per line:

* `word-bank.txt` - about 2,300 common words.  Every puzzle's **solution**
  comes from this list.
* `valid-words.txt` - about 13,000 words, `word-bank.txt` included.  A
  **guess** has to be somewhere in this much bigger list, or it is not a
  real word and should not be accepted.

That split is deliberate, and it is the real reason there are two files
instead of one: the solution should be a word most people actually know,
but you should be allowed to *guess* far more obscure words than that while
you are narrowing things down.

## Coloring your output with ANSI escape codes

Your terminal understands a handful of special character sequences that
change the color of whatever gets printed next, rather than printing
visible characters themselves.  They all start with the same two
characters - the escape character, written `\033` in a Python string,
followed by `[` - then a number, then the letter `m`:

| Code | Color |
|------|-------|
| `\033[31m` | red |
| `\033[32m` | green |
| `\033[33m` | yellow |
| `\033[34m` | blue |
| `\033[35m` | magenta |
| `\033[36m` | cyan |
| `\033[0m`  | **reset** - back to the default color |

A color code does not just color one character - it colors *everything*
printed after it, until something resets it.  Forget the reset and the
color bleeds into every line that follows for the rest of the program.
Here is the whole idea in one line:

```python
print("\033[32mHello\033[0m, world!")
```

That prints `Hello` in green, then `, world!` in your terminal's normal
color, because the reset code sits right between them.  Try it - run it in
a real terminal, not just read it, since a plain text file cannot show you
color.

That is the only example you are getting.  Figuring out how to color just
the *letters that need it* - some letters colored, others plain, all on
one line - is your job, not a function we hand you.

## Further Reading

* [Wikipedia: ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code) -
  the "Colors" section under SGR (Select Graphic Rendition) has the full
  table; this challenge only needs eight of them.
* Automate the Boring Stuff with Python
  * [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/3e/chapter9.html)

# Instructions

Write a word-guessing game.  Your program is given a puzzle number on the
**command line**:

```
/challenge/run ./wordgame.py 2024
```

Load `/challenge/word-bank.txt`, and pick the solution with:

```
puzzle_number % len(word_bank)
```

The same puzzle number always picks the same word - that is what
"deterministic" means here - and the modulo keeps it a valid index no
matter how large the number on the command line is.

Then read guesses from standard input, one per line, until you have had
**six** of them or you guess correctly, whichever comes first.

For each guess:

* If it is not somewhere in `/challenge/valid-words.txt`, print a message
  to **stderr** saying so and exit with status **1** immediately - do not
  read any more guesses, and do not let an invalid guess use up one of the
  six tries.
* Otherwise, print the guess once, colored letter by letter:
  * **Green** if that letter is in the **same position** in the solution.
  * **Yellow** if that letter is somewhere else in the solution, just not
    that position.
  * No color at all if the letter is not in the solution anywhere.
* If the guess exactly matches the solution, print
  `You win! The word was <solution>.` and stop.

If all six guesses are used without a win, print
`You lose! The word was <solution>.`

**The simplification promised above:** real Wordle keeps track of how many
of each letter are still "available" to color, so a guess with two of the
same letter cannot both show yellow if the solution only has one of that
letter. This version does not bother - check each letter of the guess
against the solution on its own, with no memory of letters already claimed
by an earlier position in the same guess. It is not quite real Wordle, but
it is a lot less code, and nobody asked you to clone it exactly.

Your program must still work when its output is piped somewhere that is
not a color-capable terminal - the judge is reading it exactly that way,
raw escape codes and all, which is also exactly how it is checking that
your colors are right.

```
/challenge/run ./wordgame.py 2024
```
