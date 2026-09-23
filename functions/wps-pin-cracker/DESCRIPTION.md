<!--
STATUS: DRAFT / WORK IN PROGRESS.

Not deployed: no .init, no run script, no .eval_data, and deliberately left
out of module.yml until pin_verify.c is actually built into a suid binary.
That build step is being ported over from another dojo (a different,
already-working pattern for compiling and secret-injecting a binary at
deploy time) rather than reinvented here - see pin_verify.c in this same
directory for the verification logic itself, which IS real and does work
standalone (tested with gcc on the author's machine).

Sections marked PLACEHOLDER need real content once the build lands:
  * the exact secret-injection mechanism (currently a #define default)
  * the Instructions section's I/O contract and test data
-->

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

`wps_checksum(1337246)` returns `0`, so the full valid PIN built from that
prefix is `13372460`. Once you have confirmed digits 1-4 and are searching
digits 5-7, compute digit 8 with this instead of guessing it - that is
where the 10,000-guess second stage turns into 1,000.

## Further Reading

* [PLACEHOLDER: link to the CVE-2011-5053 writeup and a WPS PIN reference
  once this challenge is finalized]

# Instructions

[PLACEHOLDER - DRAFT, NOT YET JUDGED]

Write a Python program that recovers the secret PIN behind
`/challenge/pin_verify` and reports it, using no more than 11,000 calls to
the oracle:

1. Brute force the first four digits, trying `try_pin()` until you stop
   getting exit status `1`.
2. Brute force digits 5-7 (not digit 8 - compute that one), trying each
   candidate until you get exit status `0`.
3. Print the full 8-digit PIN you found, and/or the flag the oracle handed
   you.

This section still needs: how the flag actually reaches the judge (the
oracle prints it on success - do we grade on that appearing in your
program's own output, or on the PIN string itself?), the exact number of
calls the judge is willing to tolerate, and whether a wrong-format guess
(not 8 digits) needs handling.
