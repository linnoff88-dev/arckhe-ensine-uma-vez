"""Ensaia a regra de uma rotina de reuniêo com dados fictícios e saída local."""

import argparse
from datetime import date
import json
from pathlib import Path


def prepare(meeting):
    rows = []
    issues = []
    for index, action in enumerate(meeting["acoes"], 1):
        task = action.get("tarefa") or f"Açêo {index}"
        owner = action.get("responsavel")
        deadline = action.get("prazo")
        if not isinstance(owner, str) or not owner.strip():
            issues.append(f"{task} — falta responsável confirmado")
        try:
            date.fromisoformat(deadline)
        except (TypeError, ValueError):
            issues.append(f"{task} — falta um prazo válido")
        rows.append([task, owner or "—", deadline or "—"])
    return rows, issues


def markdown_cell(value):
    return str(value).replace("\n", " ").replace("|", "\\|")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", type=Path)
    parser.add_argument("--nivel", choices=("4", "5"), required=True)
    parser.add_argument("--saida", type=Path, required=True)
    args = parser.parse_args()
    meeting = json.loads(args.entrada.read_text(encoding="utf-8"))
    rows, issues = prepare(meeting)
    if args.nivel == "5" and issues:
        name = "chamar-responsavel"
        content = "# Chamar responsável\n\n" + "\n".join(f"- {item}" for item in issues)
        status = 2
    else:
        name = "revisar" if args.nivel == "4" else "entregue"
        content = f"# {meeting['reuniao']}\n\n| Açêo | Responsável | Prazo |\n|---|---|---|\n"
        content += "\n".join("| " + " | ".join(map(markdown_cell, row)) + " |" for row in rows)
        if issues:
            content += "\n\n## Pendências\n\n" + "\n".join(f"- {item}" for item in issues)
        status = 0
    args.saida.mkdir(parents=True, exist_ok=True)
    output = args.saida / f"{args.entrada.stem}.md"
    output.write_text(f"{content}\n", encoding="utf-8")
    print(f"{name}: {output}")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
