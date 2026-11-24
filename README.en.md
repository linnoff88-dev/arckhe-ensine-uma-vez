# Ensine Uma Vez

[![Ensine Uma Vez](guia/assets/banner-en.jpg)](https://linnoff88-dev.github.io/

**🇧🇷 [Português](README.md) · 🇬🇧 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

Ensine Uma Vez is a kit for turning a conversation that went well into a procedure AI can repeat. It is for people who still explain the same task every week and want to start delegating it. You save the corrections, test the procedure with a new case, and decide when you can stop reviewing every deliverable. Use it with Claude Code or Codex and a task you have already completed with AI.

[Step-by-step guide](https://linnoff88-dev.github.io/

## The autonomy ladder

| Level | What the work looks like |
|---|---|
| AL1 | You do it on your own. |
| AL2 | AI suggests. You execute. |
| AL3 | AI does the task with you, step by step. |
| AL4 | AI follows the saved procedure and gives you the result to review. |
| AL5 | The routine runs with rules, limits, and alerts. You are called in for exceptions. |

Classify the task by what it can do today. Start with a small routine, such as turning meeting notes into next steps. Save only the correction that applies to the next meeting as a rule. Try the procedure in a typical situation and another one that should call a person.

## Technical setup

Open this kit’s folder in Claude Code or Codex. Start by asking it to read `skill/ensine-uma-vez/SKILL.md` and `exemplos/conversa-aprovada.md`, then create a procedure for the example. To use it with your own work, point to the conversation and approved deliverable in your own folder. You can use the skill directly from the file or copy it into the agent’s skills folder.

The deterministic trial uses Python 3 and fictional data. Check the output at each level and confirm that the third command returns code 2 and records a local alert without publishing or sending messages.

```sh
python3 exemplos/reuniao.py exemplos/reuniao-nova.json --nivel 4 --saida /tmp/ensine-al4
python3 exemplos/reuniao.py exemplos/reuniao-normal.json --nivel 5 --saida /tmp/ensine-al5
python3 exemplos/reuniao.py exemplos/reuniao-excecao.json --nivel 5 --saida /tmp/ensine-al5
```

The example reproduces the previously defined verification rule. A real task advances to AL5 when new deliverables pass the agreed criteria and exceptions reach the responsible person. Each team defines the number of rounds, the limit, and the authorized destination.
