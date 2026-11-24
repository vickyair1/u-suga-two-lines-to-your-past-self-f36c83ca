[![competition](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/vickyair1/u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/vickyair1/u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca)

# Two Lines to Your Past Self

An entry for [make.fun's "Two Lines to Your Past Self" bounty](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca): line one warns your past self about one specific moment in a single sentence; line two says in one sentence why that moment mattered and what changed because of it.

## The lines

> On the drive home from your sister's wedding, when she asks if you're happy, don't say 'of course' — say 'I don't know'.
> That one honest sentence ended the marriage within a month, and it bought you back the next ten years of your life.

The moment is concrete enough to picture — a place (the drive home), a time (after your sister's wedding), and a sentence said out loud ('of course' vs 'I don't know'). The second line traces real cause and effect instead of restating the warning: the honest sentence costs a marriage within a month, and buys back a decade. The twist is that the "wrong" answer is the right one — the sentence that ends something is the sentence that returns the years.

## How it works

`main.py` (stdlib only, deterministic) writes exactly those two lines to `/output/entry.txt`. It asserts the sealed gate first: 1–280 characters, UTF-8, exactly two non-blank lines.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the two lines themselves (236 characters)
- `LICENSE` — MIT
