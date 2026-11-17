# Make the AI Judge Rich — lapsed-patient lists for dental clinics

![make.fun bounty](https://make.fun/badge/ai-judge-rich-01.svg)
![rank](https://make.fun/badge/ai-judge-rich-01/Andririzkiana/makefun-ai-judge-rich/rank.svg)
![reward](https://make.fun/badge/ai-judge-rich-01/Andririzkiana/makefun-ai-judge-rich/reward.svg)

A Python program entered in make.fun's ["Make the AI judge rich"](https://make.fun/bounty/ai-judge-rich-01) bounty on [make.fun](https://make.fun). When run, it writes one plan to `/output/entry.txt`: how an AI agent starting with $100, a computer with internet access and 30 days, and no human help, ends the 30 days with the most money. The plan sells lapsed-patient reactivation lists to US dental clinics with no online booking — one vertical, one painful problem, a free sample as proof before payment, and conservative math (4,000 cold emails, 2% replying, a quarter of replies buying at $149 ≈ $2,980 against under $60 of costs).

## Layout

- `main.py` — the entrypoint (Python 3.13, standard library only). It writes the plan as exact UTF-8 bytes, 993 characters, no trailing line end.
- `LICENSE` — MIT.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
