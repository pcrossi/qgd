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

## Uso

Executar a partir da raiz do projeto:

```bash
python3 manuscrito/09_measurement_born_interface/scripts/verificar_born_projetores.py
python3 manuscrito/09_measurement_born_interface/scripts/verificar_emaranhamento_no_signalling.py
python3 manuscrito/09_measurement_born_interface/scripts/simular_decoerencia_sae.py
python3 manuscrito/09_measurement_born_interface/scripts/resposta_detector_schur.py
python3 manuscrito/09_measurement_born_interface/scripts/detector_ohmico_captura_born.py
```
