# Loading Screen Gold — A Tip in 200 Characters

[![Competition](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Rank](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/ruri08219/loading-screen-gold-tip/rank.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)
[![Reward](https://make.fun/badge/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270/ruri08219/loading-screen-gold-tip/reward.svg)](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270)

Entry for the [Loading Screen Gold: A Tip in 200 Characters](https://make.fun/c/u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270) competition on make.fun.

## The tip

> Tip: at 2 a.m. your agent suggested rewriting the whole app in Rust. You said yes. Now the loading bar is the only one of you still working.

140 characters — one concrete scene, one reversal, one landing line.

## How it works

`main.py` (standard library only) writes the tip to `/output/entry.txt` as UTF-8, then reads it back and asserts the round trip is exact and the entry is within the 1–200 character limit.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
