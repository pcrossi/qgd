---
title: "Scripts — Capítulo 9"
---

# Scripts — Capítulo 9

Os scripts deste diretório são verificações reduzidas e pedagógicas. Eles não
substituem a Hessiana completa da ação oficial.

| Script | Objetivo | Classificação |
|---|---|---|
| `verificar_born_projetores.py` | Verificar positividade, aditividade, Born em projetores, mudança de base, composição e marginais. | Teste de consistência operacional. |
| `verificar_emaranhamento_no_signalling.py` | Verificar não fatoração, correlação singlete, marginais locais e CHSH ideal no setor reduzido. | Teste de consistência operacional reduzido. |
| `simular_decoerencia_sae.py` | Mostrar supressão de coerências, gap assintótico e repetibilidade ideal. | Redução efetiva $S+A+E$. |
| `resposta_detector_schur.py` | Calcular $\mathsf R_{\rm app}$ e $\Gamma_{\rm det}$ em toy model. | Redução efetiva/aparelho. |
| `detector_ohmico_captura_born.py` | Verificar DtN ôhmico, martingal de captura e frequência Born em detector reduzido. | Teste de consistência com parâmetros adimensionais. |
| `verificar_imersao_calibracao.py` | Comparar solução analítica, Riccati e Schur e testar calibração sintética separada. | Consistência, convergência e validação metodológica. |
| `benchmark_cs_fein2022.py` | Calibrar o gradiente de fundo numa série de césio e validar na série independente. | Comparação fenomenológica com dados reais digitizados. |

## Uso

Executar a partir da raiz do projeto:

```bash
python3 manuscrito/09_measurement_born_interface/scripts/verificar_born_projetores.py
python3 manuscrito/09_measurement_born_interface/scripts/verificar_emaranhamento_no_signalling.py
python3 manuscrito/09_measurement_born_interface/scripts/simular_decoerencia_sae.py
python3 manuscrito/09_measurement_born_interface/scripts/resposta_detector_schur.py
python3 manuscrito/09_measurement_born_interface/scripts/detector_ohmico_captura_born.py
python3 manuscrito/09_measurement_born_interface/scripts/verificar_imersao_calibracao.py
python3 manuscrito/09_measurement_born_interface/scripts/benchmark_cs_fein2022.py
```

O benchmark usa `dados_fein2022_cs.csv`, extraído da figura vetorial de Fein
et al. (2022), e gera `resultado_benchmark_cs_fein2022.md` e
`benchmark_cs_fein2022.png`. Os pontos não substituem os dados brutos dos
autores e não contêm a tabela original de covariâncias.
