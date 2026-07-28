---
title: "Scripts transversais do manuscrito"
---

# Scripts transversais do manuscrito

## Auditoria transversal

O script `auditoria_transversal.py` verifica:

- os 28 capítulos, seus índices e checklists;
- links Wiki e Markdown locais;
- convenções matemáticas do Quartz;
- dependências de arquivos históricos;
- sinais constitutivos suspeitos;
- preservação literal da ação oficial;
- sintaxe dos scripts Python;
- cobertura bibliográfica;
- citação nominal dos scripts em seus capítulos.

Execução:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 manuscrito/scripts/auditoria_transversal.py
```

Saída:

- [`auditoria_transversal_final.md`](../notes/editorial/auditoria_transversal_final.md)

O verificador certifica integridade documental e sintática. Ele não decide a
validade física das hipóteses ou a correção de uma prova analítica.
