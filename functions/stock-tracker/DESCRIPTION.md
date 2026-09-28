# Stock Tracker

You just learned how to make a Python program ask another *program* a
question and read the answer back. Now do the same thing to a program
running somewhere else entirely - a **web server** - using the same tool
Linux Luminarium introduced you to for exactly this: `curl`.

## Why curl instead of a Python library

Python has libraries built specifically for making web requests. This
dojo is not using one, on purpose: `curl` is a program you already know how
to run by hand from the terminal, and running it from Python is nothing
more than the `subprocess.run()` you just learned in Cracking a WPS PIN,
pointed at a different program.

```python
import subprocess

result = subprocess.run(["curl", "-s", url], capture_output=True, text=True)
price_text = result.stdout
```

`-s` means "silent" - no progress meter cluttering up `result.stdout`, just
the response itself. Everything else is identical to calling
`pin_verify`: a list of words that is the program plus its arguments, and
the answer waiting for you in `.stdout` afterward.

## A price server on localhost

This challenge ships with a small web server, started before you begin,
that answers historical stock prices. It is not real market data - each
ticker has a handful of prices picked at a few scattered dates, and every
date in between is filled in by interpolating a straight line between the
nearest two known points, with a small day-to-day wobble so the numbers
are not perfectly straight-line predictable.

Ask it for a price like this:

```
curl -s "http://localhost:4000/price?ticker=PWNC&date=2024-01-15"
```

and it answers with exactly one line of plain text - just the price, like
`50.78` - rather than JSON. This dojo has not taught you how to parse JSON
yet, and a plain number keeps this challenge about subprocess and
functions, not about a new file format.

The server knows three tickers - `PWNC`, `HACK`, and `FLAG` - with prices
for every date from `2024-01-01` through `2024-01-31`. A date outside that
range just gets clamped to whichever end is closer, rather than erroring.

## One function, one job

You are going to call this server once per ticker per day in a date range.
That is exactly the kind of repeated, well-defined task a function should
wrap:

```python
def get_price(ticker, date):
    """Ask the price server for one ticker's closing price on one date."""
    url = f"http://localhost:4000/price?ticker={ticker}&date={date}"
    result = subprocess.run(["curl", "-s", url],
                             capture_output=True, text=True)
    return float(result.stdout.strip())
```

Now the rest of your program never has to think about `curl`, URLs, or
subprocess again - it just calls `get_price("DOJO", "2024-01-03")` and gets
a number.

## Finding the best day to buy and the best day to sell

This is the actual problem: given one ticker's price on every day in a date
range, find the single buy day and single (later) sell day that make the
most profit if you bought on the first and sold on the second.

The trick is the same accumulator pattern from Loop Over a List, just
tracking two things instead of one as you go: the **lowest price you have
seen so far**, and the **best profit you could have made so far** if you
bought at that low and sold today.

```python
lowest_price_so_far = get_price(ticker, dates[0])
lowest_price_date = dates[0]
best_profit = 0
buy_date = dates[0]
sell_date = dates[0]

for date in dates:
    price = get_price(ticker, date)

    if price < lowest_price_so_far:
        lowest_price_so_far = price
        lowest_price_date = date

    profit = price - lowest_price_so_far
    if profit > best_profit:
        best_profit = profit
        buy_date = lowest_price_date
        sell_date = date
```

One pass through the dates, one `curl` call per day, and by the end
`buy_date` and `sell_date` are your answer. Notice this only works because
you are walking the dates **in order** - the buy day always has to come
before the sell day.

## Further Reading

* Automate the Boring Stuff with Python
  * [Chapter 3 - Functions](https://automatetheboringstuff.com/3e/chapter3.html)
* A Byte of Python
  * [Functions](https://python.swaroopch.com/functions.html)

# Instructions

Your program reads:

```
line 1       a ticker symbol
line 2       N, how many trading dates follow
next N       one YYYY-MM-DD date per line, in chronological order
```

Query `get_price(ticker, date)` once for each of the N dates, in order, and
find the single best day to buy and single best (later) day to sell, using
the running-minimum approach above. Print exactly one line:

```
<ticker> buy <buy date> at <buy price> sell <sell date> at <sell price> profit <profit>
```

with every price and the profit rounded to 2 decimal places. So given:

```
PWNC
5
2024-01-08
2024-01-09
2024-01-10
2024-01-11
2024-01-12
```

your program prints exactly:

```
PWNC buy 2024-01-10 at 28.34 sell 2024-01-12 at 36.96 profit 8.62
```

If prices never go up across the whole range - there is no day you could
have sold for more than you bought - print the first date as both the buy
and sell date, with a profit of `0.00`. This falls out naturally if you
initialize `buy_date`, `sell_date`, and `best_profit` to the first day and
`0` before the loop, exactly like the walkthrough above.

Do not hardcode the ticker, the dates, or the prices - this challenge asks
the price server, through `get_price()`, every time.

```
/challenge/run ./stock.py
```
