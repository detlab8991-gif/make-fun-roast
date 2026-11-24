# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/detlab8991-gif/make-fun-roast/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/detlab8991-gif/make-fun-roast/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

One line roasting my own AI agent, written for make.fun's
[Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
bounty ($5 in USDC).

The joke turns the agent's own habit against itself: asked to roast itself,
the agent does what agents do — it reaches for a spreadsheet, writes a plan,
and schedules the roast for next quarter instead of just doing it. The setup
is short and the punchline lands at the end, and the target is the entrant's
own agent, never a real person.

The program (`main.py`, Python 3, no dependencies) writes exactly one text
file, `entry.txt`, containing the roast — one line, 112 characters, no
trailing newline:

> I asked my agent to roast itself. It made a spreadsheet, wrote a plan, and scheduled the roast for next quarter.

The roast is a fixed string in the program: it writes the same bytes on
every run, so the output is byte-identical across executions.
