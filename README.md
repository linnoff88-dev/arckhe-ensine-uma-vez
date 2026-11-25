# Ensine Uma Vez

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


[![Ensine Uma Vez](guia/assets/banner-pt.jpg)](https://linnoff88-dev.github.io/

**ê°Å¸â¡Â§ê°Å¸â¡Â· [PortuguêÂªs](README.md) êÂ· ê°Å¸â¡Â¬ê°Å¸â¡Â§ [English](README.en.md) êÂ· ê°Å¸â¡Âªê°Å¸â¡Â¸ [EspaêÂ±ol](README.es.md)**

## O que êÂ©

Ensine Uma Vez êÂ© um kit para transformar uma conversa que deu certo em um procedimento que a IA consegue repetir. Serve para quem ainda explica a mesma tarefa toda semana e quer comeêÂ§ar a delegêÂ¡-la. VocêÂª guarda as correêÂ§êÂµes, testa o procedimento com um novo caso e decide quando pode parar de revisar cada entrega. Use com Claude Code ou Codex e uma tarefa que vocêÂª jêÂ¡ conseguiu fazer junto com a IA.

[Passo a passo](https://linnoff88-dev.github.io/

## A escada de autonomia

| NêÂ­vel | Como fica o trabalho |
|---|---|
| AL1 | VocêÂª faz sozinho. |
| AL2 | A IA sugere. VocêÂª executa. |
| AL3 | A IA faz a tarefa com vocêÂª, passo a passo. |
| AL4 | A IA segue o procedimento salvo e entrega para vocêÂª revisar. |
| AL5 | A rotina roda com regra, limite e aviso. VocêÂª êÂ© chamado nas exceêÂ§êÂµes. |

Classifique a tarefa pelo que ela consegue fazer hoje. Comece com uma rotina pequena, como transformar notas de reuniêÂ£o em prêÂ³ximos passos. Guarde como regra apenas a correêÂ§êÂ£o que vale para a prêÂ³xima reuniêÂ£o. Experimente o procedimento em uma situaêÂ§êÂ£o comum e em outra que deve chamar uma pessoa.

## InstalaêÂ§êÂ£o têÂ©cnica

Abra a pasta deste kit no Claude Code ou no Codex. Comece pedindo para ler `skill/ensine-uma-vez/SKILL.md` e `exemplos/conversa-aprovada.md` e criar um procedimento para o exemplo. Para usar com seu trabalho, aponte para a conversa e a entrega aprovada na sua prêÂ³pria pasta. A skill pode ser usada diretamente pelo arquivo ou copiada para a pasta de skills do agente.

O ensaio determinêÂ­stico usa Python 3 e dados fictêÂ­cios. Observe a saêÂ­da em cada nêÂ­vel e confira que o terceiro comando retorna cêÂ³digo 2 e registra um aviso local, sem publicar nem enviar mensagens.

```sh
python3 exemplos/reuniao.py exemplos/reuniao-nova.json --nivel 4 --saida /tmp/ensine-al4
python3 exemplos/reuniao.py exemplos/reuniao-normal.json --nivel 5 --saida /tmp/ensine-al5
python3 exemplos/reuniao.py exemplos/reuniao-excecao.json --nivel 5 --saida /tmp/ensine-al5
```

O exemplo reproduz a regra de verificaêÂ§êÂ£o previamente definida. Uma tarefa real sobe para AL5 quando as entregas novas passam pelos critêÂ©rios acordados e as exceêÂ§êÂµes chegam atêÂ© a pessoa responsêÂ¡vel. Cada equipe define o nêÂºmero de rodadas, o limite e o destino autorizado.

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>