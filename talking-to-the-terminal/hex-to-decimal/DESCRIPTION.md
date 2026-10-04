# Hex to Decimal

You are going to see hexadecimal everywhere in security work: memory
addresses, hex dumps, colour codes, MAC addresses, hashes, byte values in a
packet.  It is worth ten minutes now.

## Why hex exists

Computers work in bits.  Writing out bits gets unreadable fast:

```
11011110 10101101 10111110 11101111
```

Decimal does not help, because ten is not a power of two and the digits do not
line up with anything.  But **sixteen is two to the fourth**, so one hex digit
is exactly four bits, and **one byte is exactly two hex digits**:

```
1101 1110  1010 1101  1011 1110  1110 1111
   d    e     a    d     b    e     e    f
```

That is why `deadbeef` is one of the most famous constants in computing, and
why a colour like `#ff8800` is three bytes: red `ff`, green `88`, blue `00`.

Hex digits go `0 1 2 3 4 5 6 7 8 9 a b c d e f`, so `a` is 10 and `f` is 15.
Case does not matter: `ff` and `FF` are the same number.

## Text to number: int() has a second argument

You already know `int("31")` gives `31`.  What almost nobody is taught is that
`int()` takes a **base**:

```
>>> int("1f", 16)
31
>>> int("ff", 16)
255
>>> int("deadbeef", 16)
3735928559
```

It is relaxed about how you write it - an `0x` prefix is fine, and so is
either case:

```
>>> int("0xDEAD", 16)
57005
>>> int("dead", 16)
57005
```

So you do not have to strip anything off.  Just pass the text and the base.

The base does not have to be 16.  `int()` accepts any base from `2` up to
`36`, so the same function reads binary, octal, or anything else:

```
>>> int("11011110", 2)
222
>>> int("755", 8)
493
```

## Number to text: hex() and format specifiers

`hex()` goes the other direction and includes the `0x`:

```
>>> hex(255)
'0xff'
>>> hex(4096)
'0x1000'
```

Inside an f-string you can ask for hex without the prefix.  `X` gives capital
letters, `x` gives lower case:

```
>>> n = 255
>>> f"{n:x}"
'ff'
>>> f"{n:X}"
'FF'
>>> f"{n:02X}"
'FF'
```

That `02` is a **minimum** width, padded with zeros - it is how you make a
single byte always show as two digits:

```
>>> f"{10:02X}"
'0A'
>>> f"{4096:02X}"
'1000'
```

It does not truncate.  `4096` needs four digits, so it gets four.

## Octal, the same way

Octal (base 8) works exactly like hex, just with three bits per digit
instead of four.  `oct()` converts to text, prefix and all; `o` in an
f-string drops the prefix:

```
>>> oct(493)
'0o755'
>>> f"{493:o}"
'755'
```

You will recognize `755` - Linux file permissions are octal for exactly
this reason: three bits per digit line up perfectly with the three
read/write/execute permission bits.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 1 - Python Basics](https://automatetheboringstuff.com/3e/chapter1.html)
* Try `man ascii` in your terminal - the table is in hex for a reason.

# Instructions

Read two lines:

```
line 1     the base the second line is written in (2 through 36)
line 2     a number, written as text in that base (0x prefix allowed for hex)
```

Convert it, and print exactly three lines:

```
OCTAL   = <the value in octal, no 0o prefix>
DECIMAL = <the value in decimal>
HEX     = <the value in hex, capital letters, no 0x prefix>
```

So for input `16` and `deadbeef`:

```
OCTAL   = 33653337357
DECIMAL = 3735928559
HEX     = DEADBEEF
```

And for `8` and `755`:

```
OCTAL   = 755
DECIMAL = 493
HEX     = 1ED
```

That second example is not a coincidence - `755` is already valid octal, so
converting it to octal is the identity.  A good way to catch yourself
reading the base argument backwards.

```
/challenge/run ./hex.py
```
