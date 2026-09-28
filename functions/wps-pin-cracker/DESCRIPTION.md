# Cracking a WPS PIN

Every function you have written so far has been code you can read. This
challenge is about a function that calls code you *cannot* read - a program
somebody else wrote, running as a separate process, that only ever answers
through its exit status. That is exactly the position a real attacker is in
against somebody else's Wi-Fi router.

## What WPS is, and why its PIN was a disaster

WPS (Wi-Fi Protected Setup) lets you join a network by typing an 8-digit PIN
printed on the router instead of the real password. Eight digits sounds
like `10^8` - a hundred million guesses, hopeless to brute force.

Two design mistakes shrunk that number by more than four orders of
magnitude:

1. **The 8th digit is not free.** It is a checksum, computed from the other
   seven with a fixed public formula. Once you know the first seven digits,
   the eighth is not a guess - you calculate it. That turns `10^8` into
   `10^7`.
2. **The router checked the PIN in two separate halves, and said which one
   failed.** During setup it validates the first four digits, and only if
   those are right does it go on to check the rest. Crucially, it reports
   failure differently for each stage - so an attacker learns "your first
   half was wrong" without ever needing a correct second half to hear it.

That second mistake is the one worth sitting with. A single 8-digit
comparison would have been all-or-nothing: **10,000,000** possibilities to
find out anything at all. Splitting the check into two stages and reporting
each one separately turned it into two much smaller independent searches:
at most **10,000** guesses to find the first four digits, and then at most
**1,000** more (digits 5-7, since digit 8 is computed, not guessed) to find
the rest. `10,000 + 1,000 = 11,000` - a search a laptop finishes in hours
instead of centuries. This is a real vulnerability, tracked as
CVE-2011-5053, and it is the reason WPS PIN mode is considered broken.

You are going to reproduce that attack against a program that behaves the
same way.

## Calling another program from Python

Every program you have written imports the tools it needs -
`import sys`, `import random`. To run an entirely separate *program* -
something that is not Python code you can import - you need a different
tool:

```python
import subprocess

result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
```

The first argument is a **list**: the program to run, followed by its
arguments, exactly the way `sys.argv` would see them on the other end.
`capture_output=True` catches its stdout and stderr instead of letting them
print to your terminal, and `text=True` gives you back `str` instead of raw
bytes - the same choice `open()` gives you.

`result` comes back with the pieces you already know how to think about:

* `result.returncode` - the exit status. `0` for success, same rule as
  Exit Codes.
* `result.stdout` - whatever the program printed, as one string.

So calling a program and reading what it said back is only two lines:

```python
result = subprocess.run(["/challenge/pin_verify", "12345678"],
                         capture_output=True, text=True)
print(result.returncode)
```

## Wrap it in a function

`subprocess.run(...)` is verbose to repeat, and you are about to call it a
lot. This is exactly the problem functions solve - give the idea a name and
a return value:

```python
def try_pin(pin):
    """Run pin_verify with one 8-digit guess. Return its exit status."""
    result = subprocess.run(["/challenge/pin_verify", pin],
                             capture_output=True, text=True)
    return result.returncode
```

Now the rest of your program can just call `try_pin("12345678")` and get a
number back, without caring how that number was produced.

## The oracle's contract

`/challenge/pin_verify` takes one argument - an 8-digit guess as a string -
and exits with:

| Exit status | Meaning |
|-------------|---------|
| `0` | The whole PIN is correct. It also prints the flag. |
| `1` | The first four digits are wrong. |
| `2` | The first four digits are right, the last four are wrong. |

That is the leak. `try_pin("00000000")` returning `1` instead of `2` tells
you *nothing* about digits 5-8 yet - but it does tell you `0000` is not the
first half, which is real information you did not have before.

## Computing the checksum digit

The 8th digit is a fixed, published formula applied to the first seven.
Treat the first seven digits as one number `n`:

```python
def wps_checksum(seven_digit_pin):
    n = seven_digit_pin * 10
    accum = 0
    accum += 3 * ((n // 10000000) % 10)
    accum += 1 * ((n // 1000000)  % 10)
    accum += 3 * ((n // 100000)   % 10)
    accum += 1 * ((n // 10000)    % 10)
    accum += 3 * ((n // 1000)     % 10)
    accum += 1 * ((n // 100)      % 10)
    accum += 3 * ((n // 10)       % 10)
    return (10 - (accum % 10)) % 10
```

`wps_checksum(1234567)` returns `0`, so `12345670` is a valid checksum PIN
built from that prefix (this is just an example - it is not the PIN you are
looking for). Once you have confirmed digits 1-4 and are searching digits
5-7, compute digit 8 with this instead of guessing it - that is where the
10,000-guess second stage turns into 1,000.

## Further Reading

* [Wikipedia: Wi-Fi Protected Setup, "Security" section](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup) -
  the real vulnerability this challenge reproduces, disclosed by Stefan
  Viehböck in December 2011
* Automate the Boring Stuff with Python
  * [Chapter 3 - Functions](https://automatetheboringstuff.com/3e/chapter3.html)

# Instructions

Write a Python program that recovers the secret 8-digit PIN behind
`/challenge/pin_verify`, using no more than 11,000 calls to the oracle:

1. Brute force the first four digits, trying `try_pin()` until you stop
   getting exit status `1`.
2. Brute force digits 5-7 (not digit 8 - compute that one with
   `wps_checksum()`), trying each candidate until you get exit status `0`.
3. Print the flag.

There is no separate judge for this challenge - `pin_verify` is the judge.
The moment you call it with the correct 8-digit PIN, it reads `/flag`
itself and prints it to its own stdout, exactly like a real attacker
getting into the network. `try_pin()` as written above only hands you back
the exit status, so once you find the PIN that scores a `0`, call
`subprocess.run()` on it one more time yourself to see what it printed:

```python
result = subprocess.run(["/challenge/pin_verify", full_pin],
                         capture_output=True, text=True)
print(result.stdout)
```

Remember `capture_output=True` hides a program's output from your screen
unless you print it yourself - this is the payoff for learning that.

```
python3 crack_pin.py
```
