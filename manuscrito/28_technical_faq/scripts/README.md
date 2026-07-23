---
title: "Scripts — Capítulo 28"
---

# Scripts — Capítulo 28

Este capítulo não introduz solver físico novo. Os scripts são verificadores
editoriais e conceituais autocontidos.

## Scripts

- `faq_status_matrix.py`: gera uma matriz de objeções, respostas, status e
  ação recomendada.
- `check_no_historical_refs.py`: verifica se o capítulo não referencia arquivos
  históricos externos ao manuscrito.
- `check_overclaim_terms.py`: procura expressões que poderiam sugerir
  fechamento indevido ou troca da ação oficial.
- `comparacoes_metrologicas_faq.py`: regenera a tabela curta de comparações
  metrológicas preservadas neste FAQ.

## Como executar

```bash
python3 faq_status_matrix.py
python3 check_no_historical_refs.py
python3 check_overclaim_terms.py
python3 comparacoes_metrologicas_faq.py
```

As saídas Markdown ficam nesta mesma pasta.
