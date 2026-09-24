<!--
STATUS: DRAFT / WORK IN PROGRESS.

Not deployed: no .init, no run script, no .eval_data, and deliberately left
out of module.yml. The price server itself now exists and works: st_server
is a small C program (source and build files in the solutions repo, built
against mwales/pwncollege_base:beta05 via podman so it links the same
libraries the challenge VM has) answering GET /price?ticker=SYM&date=DATE
as a plain-text price. The compiled binary lives right next to this file.
A golden solution.py (curl + subprocess, in the solutions repo) has been
run against it for all three seeded tickers and produces sensible buy/sell
picks.

Still needed before this is judgeable:
  * .init to start st_server in the background before the student's script
    runs, and run/.eval_data for the actual judge
  * the Instructions section's exact input/output contract and test data
-->

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

[PLACEHOLDER: the real ticker list is `PWNC`, `HACK`, and `FLAG`, covering
2024-01-01 through 2024-01-31 - confirm these are the ones the finished
challenge should actually quiz the student on before this ships.]

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

* [PLACEHOLDER: link to how the "best time to buy and sell stock" problem
  is normally described, once this challenge is finalized]

# Instructions

[PLACEHOLDER - DRAFT, NOT YET JUDGED]

You will be given one or more stock tickers, each with a range of trading
dates. For each ticker, query the price server once per date in its range,
using `get_price()`, and work out the single best day to buy and single
best (later) day to sell.

The overall shape of the task, once the server and real data exist:

1. Read a ticker symbol and its list of trading dates.
2. Call `get_price(ticker, date)` for each date in order.
3. Track the best buy day / sell day pair using the running-minimum
   approach above.
4. Print the ticker, the buy date, the sell date, and the profit.

This section still needs: the exact input format (dates given directly, or
a count-and-then-dates shape like Build a Toolbox's rectangles), whether
multiple tickers appear in one run, the precise output line format, and
what happens if the best "profit" would be zero or negative (never sell).
