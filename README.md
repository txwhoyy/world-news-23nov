# world-news-23nov

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/txwhoyy/world-news-23nov/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/txwhoyy/world-news-23nov/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

"The World Today" — the world news of Monday 23 November 2026 in one image. A deterministic program draws a 1024×1024 newspaper front page with the day's eight biggest stories, each with its own illustration drawn from code: the COP31 climate talks collapsing in Antalya, the Democrats' historic 258-seat House majority, Mexico's capture of cartel boss "El Chapo Isidro", Russian ships hit in two seas, the deadly factory fire in Banten, the AI stock sell-off on Wall Street, India's record 720 in Wellington, and Alcaraz's ATP Finals title.

## Run it

```sh
python3 render.py
MAKEFUN_OUTPUT_DIR=out node main.ts
```

`render.py` draws `entry.png` (1024×1024, under 1 MiB) with no network and no randomness, so every run produces identical bytes. `main.ts` validates the PNG and copies it to `$MAKEFUN_OUTPUT_DIR` (or `/output`).

## The eight stories

All eight were reported on Monday 23 November 2026.

1. **COP31 collapses with no deal** — UN climate talks in Antalya end with no agreement after the EU rejects a final draft that omits fossil fuels, the first such failure since Copenhagen in 2009. — Reuters
2. **Democrats win 258 House seats** — The party's biggest House majority since 1992 sets up divided government under a Republican president. — Associated Press
3. **"El Chapo Isidro" captured** — Mexico seizes FBI most-wanted cartel boss Fausto Isidro Meza Flores in a Sinaloa raid that leaves 11 dead. — Associated Press
4. **Russian ships hit in two seas** — A cargo ship burns off Finland and a vessel is struck in Libya's Benghazi port in suspected drone attacks. — Reuters
5. **Factory fire: 50 missing in Java** — Seven body bags are recovered after a blaze tears through a candy factory in Banten; rescuers search for dozens. — Reuters
6. **AI stocks drag Wall Street down** — The S&P 500 falls 3.7% in its worst week in 18 months as investors doubt AI spending will pay off soon. — Associated Press
7. **India's record 720 in Wellington** — India declares on 720 for 9, a record total, on day four of the first Test against New Zealand. — Associated Press
8. **Alcaraz wins ATP Finals** — Carlos Alcaraz beats world No. 1 Alexander Zverev. — Reuters

---

<sub>Entered on [make.fun](https://make.fun/?ref=g586rfkm&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
