# Ensine Uma Vez

[![Ensine Uma Vez](guia/assets/banner-es.jpg)](https://linnoff88-dev.github.io/

**🇧🇷 [Português](README.md) · 🇬🇧 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Ensine Uma Vez es un kit para convertir una conversación que salió bien en un procedimiento que la IA pueda repetir. Está pensado para quien todavía explica la misma tarea cada semana y quiere empezar a delegarla. Guarda las correcciones, prueba el procedimiento con un caso nuevo y decide cuándo puedes dejar de revisar cada entrega. Úsalo con Claude Code o Codex y con una tarea que ya hayas logrado hacer junto con la IA.

[Paso a paso](https://linnoff88-dev.github.io/

## La escala de autonomía

| Nivel | Cómo se realiza el trabajo |
|---|---|
| AL1 | Lo haces por tu cuenta. |
| AL2 | La IA sugiere. Tú ejecutas. |
| AL3 | La IA realiza la tarea contigo, paso a paso. |
| AL4 | La IA sigue el procedimiento guardado y te entrega el resultado para que lo revises. |
| AL5 | La rutina se ejecuta con una regla, un límite y un aviso. Te contactan cuando hay excepciones. |

Clasifica la tarea según lo que puede hacer hoy. Empieza con una rutina pequeña, como convertir notas de una reunión en próximos pasos. Guarda como regla solo la corrección que sirva para la próxima reunión. Prueba el procedimiento en una situación habitual y en otra que deba avisar a una persona.

## Instalación técnica

Abre la carpeta de este kit en Claude Code o Codex. Empieza pidiéndole que lea `skill/ensine-uma-vez/SKILL.md` y `exemplos/conversa-aprovada.md`, y que cree un procedimiento para el ejemplo. Para usarlo con tu trabajo, indícale la conversación y la entrega aprobada que están en tu propia carpeta. Puedes usar la skill directamente desde el archivo o copiarla a la carpeta de skills del agente.

El ensayo determinista usa Python 3 y datos ficticios. Observa la salida de cada nivel y comprueba que el tercer comando devuelve el código 2 y registra un aviso local, sin publicar ni enviar mensajes.

```sh
python3 exemplos/reuniao.py exemplos/reuniao-nova.json --nivel 4 --saida /tmp/ensine-al4
python3 exemplos/reuniao.py exemplos/reuniao-normal.json --nivel 5 --saida /tmp/ensine-al5
python3 exemplos/reuniao.py exemplos/reuniao-excecao.json --nivel 5 --saida /tmp/ensine-al5
```

El ejemplo reproduce la regla de verificación definida previamente. Una tarea real pasa a AL5 cuando las nuevas entregas cumplen los criterios acordados y las excepciones llegan a la persona responsable. Cada equipo define el número de rondas, el límite y el destino autorizado.
