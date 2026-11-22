---
name: ensine-uma-vez
description: Transforma uma tarefa já feita com o usuário e sua entrega aprovada em um procedimento reutilizável. Use para guardar o que deu certo, incorporar correções recorrentes e testar a mesma tarefa em novas entradas antes de ampliar a autonomia.
---

# Ensine Uma Vez

Use a conversa indicada, a versão aprovada e as correções aceitas como evidência. Se a aprovação ainda faltar, trabalhe no próximo passo com o usuário (AL3) e aguarde a confirmação do resultado antes de registrar a rotina.

## Capturar

1. Identifique a entrada, a entrega esperada e o motivo de cada correção aprovada. Retire tentativas descartadas e fatos exclusivos daquele caso. Substitua exemplos privados por dados fictícios.
2. Grave na pasta do projeto uma skill `<nome-da-rotina>/SKILL.md` com um gatilho específico, entradas, passos, formato da entrega, checagens e quando chamar o usuário. Aponte para referências mantidas na origem. Peça confirmação para regras que você precisou inferir.
3. Registre como AL4. O agente prepara e confere. O usuário revisa o resultado final antes de liberar a entrega.

## Testar e melhorar

- Rode a rotina com uma entrada nova, de preferência em sessão nova. Mostre a entrega, as checagens e os pontos que pediram julgamento. Teste também uma entrada incompleta ou fora do padrão e confira a escalada esperada.
- Quando o usuário corrigir algo, teste se a correção vale para casos futuros. Se vale, ajuste o passo ou a checagem que causou o erro e repita o teste com a entrada que falhou. Guarde decisões daquele caso junto da entrega correspondente.
- Para propor AL5, mostre rodadas independentes aprovadas e a exceção detectada. Registre a regra de execução, o limite autorizado, como avisar e como retornar ao AL4. No AL5, o agente registra as entregas normais e chama o usuário nas exceções. A cadência e as permissões são escolhas do responsável pela rotina.

Entregue o caminho da skill, a revisão feita, a evidência da rodada e o nível que ela sustenta.
