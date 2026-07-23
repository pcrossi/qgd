# Q53 — Neutrinos

## Status

Fechada estruturalmente; candidato reduzido forte para massas neutras;
metrologia final em refinamento.

## Documento principal

- [[questao_53]]

## Arquivos associados

- [[associados/saida_auditoria_neutrinos_q53]]
- [[associados/auditar_neutrinos_q53.py]]
- [[associados/plano_obter_massas_neutras_q53]]
- [[associados/derivacao_condicional_coeficientes_neutros_q53]]
- [[associados/refinamento_metrologico_hessiana_neutra_q53]]
- [[associados/executar_massas_neutras_q53.py]]
- [[associados/saida_execucao_massas_neutras_q53]]
- [[associados/testar_sensibilidade_coeficientes_q53.py]]
- [[associados/saida_sensibilidade_coeficientes_q53]]

## Resumo

A GDQ identifica o neutrino como onda neutra de torção/fase, sem estômato
localizado e sem carga elétrica. A oscilação é descrita como propagação
coerente no setor neutro projetado sobre as três folhas/graus de geração.

O apêndice legado fornece uma rota para PMNS, Weyl torsional e MSW. A execução
reduzida mais recente obtém diferenças quadradas próximas às observadas usando
o espectro candidato
`lambda=(0, chi_nu^2/2, 6*pi/5)`, com
`S_nu=alpha^7 Q_beta^2`. O status é forte como redução condicional, mas ainda
não substitui a diagonalização direta da Hessiana neutra oficial no background
global--local.

O refinamento metrológico máximo está documentado como programa separado em
`associados/refinamento_metrologico_hessiana_neutra_q53.md`.
