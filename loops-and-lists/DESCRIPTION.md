# Loops and Lists

Up to now every program you have written did each thing exactly once.  That
only gets you so far.  Almost every genuinely useful program has a moment where
it says "now do that again for the next one", and that is what a **loop** is.

This module is about the two ideas that make loops worth having:

* **Loops** let you repeat work without repeating yourself.  A `for` loop over
  a range of numbers, or over the characters of a string, replaces a hundred
  copy-pasted lines with three.
* **Lists** let one variable hold many values, so you have something worth
  looping over in the first place.

You will also meet the **accumulator pattern** here.  It shows up constantly:
start with an empty thing - `0` for a total, `""` for a string, `[]` for a
list - and add to it once per trip through the loop.  Once you recognize it,
you will see it everywhere for the rest of your programming life.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 2 - Flow Control](https://automatetheboringstuff.com/3e/chapter2.html)
  * [Chapter 4 - Lists](https://automatetheboringstuff.com/3e/chapter4.html)
* A Byte of Python
  * [Control Flow](https://python.swaroopch.com/control_flow.html)
  * [Data Structures](https://python.swaroopch.com/data_structures.html)
