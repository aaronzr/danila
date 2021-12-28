# danila
Tools for using Danila Miner (https://tonwhales.com/docs/miners/danila) with vast.ai

I need to invoke my miner with extra Docker arguments intended for an overclock script, e.g., of the form <c>POWER_LIMIT=<max_watts></c>.  With a miner such as NBMiner, this is no problem, since all NBminer arguments are prefaced by a flag (see https://github.com/NebuTech/NBMiner).  NBminer ignores strings before the first flag, so I can pass my OC args as such strings.  Danila miner does not use flags, so it interprets ALL strings as meaningful arguments.  Therefore, I wrote a python script that trims all arguments that begin with a capital letter and feeds the rest to danila-miner.
