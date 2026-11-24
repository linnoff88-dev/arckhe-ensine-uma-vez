# Ensine Uma Vez

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Ensine Uma Vez](guia/assets/banner-pt.jpg)](https://linnoff88-dev.github.io/

**ðŸ‡§ðŸ‡· [PortuguÃªs](README.md) Â· ðŸ‡¬ðŸ‡§ [English](README.en.md) Â· ðŸ‡ªðŸ‡¸ [EspaÃ±ol](README.es.md)**

## O que Ã©

Ensine Uma Vez Ã© um kit para transformar uma conversa que deu certo em um procedimento que a IA consegue repetir. Serve para quem ainda explica a mesma tarefa toda semana e quer comeÃ§ar a delegÃ¡-la. VocÃª guarda as correÃ§Ãµes, testa o procedimento com um novo caso e decide quando pode parar de revisar cada entrega. Use com Claude Code ou Codex e uma tarefa que vocÃª jÃ¡ conseguiu fazer junto com a IA.

[Passo a passo](https://linnoff88-dev.github.io/

## A escada de autonomia

| NÃ­vel | Como fica o trabalho |
|---|---|
| AL1 | VocÃª faz sozinho. |
| AL2 | A IA sugere. VocÃª executa. |
| AL3 | A IA faz a tarefa com vocÃª, passo a passo. |
| AL4 | A IA segue o procedimento salvo e entrega para vocÃª revisar. |
| AL5 | A rotina roda com regra, limite e aviso. VocÃª Ã© chamado nas exceÃ§Ãµes. |

Classifique a tarefa pelo que ela consegue fazer hoje. Comece com uma rotina pequena, como transformar notas de reuniÃ£o em prÃ³ximos passos. Guarde como regra apenas a correÃ§Ã£o que vale para a prÃ³xima reuniÃ£o. Experimente o procedimento em uma situaÃ§Ã£o comum e em outra que deve chamar uma pessoa.

## InstalaÃ§Ã£o tÃ©cnica

Abra a pasta deste kit no Claude Code ou no Codex. Comece pedindo para ler `skill/ensine-uma-vez/SKILL.md` e `exemplos/conversa-aprovada.md` e criar um procedimento para o exemplo. Para usar com seu trabalho, aponte para a conversa e a entrega aprovada na sua prÃ³pria pasta. A skill pode ser usada diretamente pelo arquivo ou copiada para a pasta de skills do agente.

O ensaio determinÃ­stico usa Python 3 e dados fictÃ­cios. Observe a saÃ­da em cada nÃ­vel e confira que o terceiro comando retorna cÃ³digo 2 e registra um aviso local, sem publicar nem enviar mensagens.

```sh
python3 exemplos/reuniao.py exemplos/reuniao-nova.json --nivel 4 --saida /tmp/ensine-al4
python3 exemplos/reuniao.py exemplos/reuniao-normal.json --nivel 5 --saida /tmp/ensine-al5
python3 exemplos/reuniao.py exemplos/reuniao-excecao.json --nivel 5 --saida /tmp/ensine-al5
```

O exemplo reproduz a regra de verificaÃ§Ã£o previamente definida. Uma tarefa real sobe para AL5 quando as entregas novas passam pelos critÃ©rios acordados e as exceÃ§Ãµes chegam atÃ© a pessoa responsÃ¡vel. Cada equipe define o nÃºmero de rodadas, o limite e o destino autorizado.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>