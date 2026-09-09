# Lookup Tables

Remember the Secret Decoder Ring?  You had two parallel strings and, for every
single character of every message, you searched one of them with `.index()`.

Let us do it properly.

## Dictionaries

```
>>> decode = {}
>>> decode["4"] = "a"
>>> decode["3"] = "e"
>>> decode
{'4': 'a', '3': 'e'}
>>> decode["4"]
'a'
```

`{}` is an empty dictionary.  `d[key] = value` puts something in - or replaces
what was there.  `d[key]` gets it back.

Keys can be strings, numbers, or most other unchangeable things.  Values can be
anything.  Each key appears once.

## KeyError, and the two ways round it

```
>>> decode["z"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'z'
```

Asking for a key that is not there is an error.  Two ways to deal with it:

```
if ch in decode:              # check first
    ...

decode.get(ch, ch)            # or give a default
```

`.get(key, default)` returns the value if the key is there, and the default if
it is not.  For this challenge that is *exactly* what you want, because the
rule is "translate it, or leave it alone":

```
plain = plain + decode.get(ch, ch)
```

One line, no `if`, no `.index()`, and no possible `ValueError`.  Compare that
to the decoder ring.

Note that `in` on a dictionary checks the **keys**, not the values.  That
catches people.

## Looping

```
for key in d:                 # keys
for key, value in d.items():  # both at once
```

`.items()` is the one you will use most.

## Direction, again

The key you are given describes **encoding**: original on the left, what it
became on the right.  You are **decoding**, so the thing that arrives in the
message is what you look up.

That means the dictionary goes in backwards:

```
decode[substituted] = original
```

Getting this inverted is the same mistake as last time.  If your output is
gibberish, this is why.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 5 - Dictionaries and Structuring Data](https://automatetheboringstuff.com/3e/chapter5.html)

# Instructions

Decode secret messages again - with a dictionary this time.

The key now arrives as pairs, one per line, instead of two long strings:

```
line 1      N, how many mappings follow
next N      "<original>=<substituted>", one per line
next line   M, how many messages follow
next M      the encoded messages
```

For each message, print the decoded version on its own line.

As before, the key describes how the message was **encoded**, so decoding
means going the other way.  Any character not mentioned in the key was never
changed - leave it alone.

So for this input:

```
5
a=4
e=3
i=1
o=0
u=7
2
d1ct10n4r13s 4r3 l00k7p t4bl3s
k3ys 4nd v4l73s
```

your program prints:

```
dictionaries are lookup tables
keys and values
```

`.split("=")` turns `a=4` into `['a', '4']`.

When it works, open your old Secret Decoder Ring solution next to this one and
compare the two decode loops.  That difference is the entire reason
dictionaries exist.

```
/challenge/run ./decode.py
```
