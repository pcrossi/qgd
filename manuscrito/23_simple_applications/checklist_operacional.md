---
title: "Checklist operacional — Capítulo 23"
---

# Checklist operacional — Capítulo 23

## Construções analíticas

| Bloco | Prova humana | Certificação |
|---|---|---|
| poço ideal e circulação | `23.2`, nota `poco_oscilador_reducao` | `SimpleApplications.lean` |
| oscilador gaussiano | `23.3`, nota `poco_oscilador_reducao` | `SimpleApplications.lean` |
| parede Schur/DtN | `23.4`, nota `impedancia_parede_schur` | `DetectorDtNSchur.lean` |
| saturação de Hartman | `23.5`, nota `hartman_comprimento_proprio` | `TransportInterference.lean` |
| Casimir ideal | `23.6`, nota `casimir_hessiana_contorno` | `SimpleApplications.lean` |
| rotor e distorção | `23.7`, nota `rotor_molecular_hessiana` | `SimpleApplications.lean` |

## Scripts preservados

| Script | Classificação |
|---|---|
| `poco_oscilador_reducao.py` | correspondência e convergência |
| `poco_impedancia_gdq.py` | consistência Robin/DtN contra barreira direta |
| `hartman_saturacao.py` | avaliação direta de fórmula reduzida |
| `casimir_ideal.py` | avaliação numérica do limite ideal |
| `casimir_zeta_derivacao.py` | verificação simbólica do coeficiente |
| `rotor_distorcao_symbolic.py` | verificação simbólica da eliminação radial |
| `rotor_molecular_reduzido.py` | comparação fenomenológica com dados externos |

## Limites preservados

- Parede, placas e moléculas reais exigem seus backgrounds e Hessianas.
- O coeficiente de Casimir é universal somente no contorno ideal declarado.
- Hartman não implica propagação causal superluminal.
- Os dados de CO usados no teste do rotor são externos.
- Nenhum desses operadores substitui a ação oficial da GDQ.
