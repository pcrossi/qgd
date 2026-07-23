---
title: "Scripts — Capítulo 2"
---

# Scripts — Capítulo 2

Estes scripts são verificações simbólicas ou ilustrações pedagógicas ligadas ao
Capítulo 2. Eles não são previsões físicas e não substituem as provas do texto.

## Scripts

1. `verificar_dimensao_kernel.py`
   - Classificação: teste simbólico/ilustração dimensional.
   - Verifica que, para dimensão real $d=2n=8$, o kernel plano usa potência
     $d/2=n=4$.
   - Saída: `saida_verificar_dimensao_kernel.md`.

2. `verificar_decomposicao_f_symbolic.py`
   - Classificação: teste simbólico de identidade constitutiva.
   - Verifica a equivalência entre $f$, $\bar f$, $\rho$, $S_I$ e $S_R$.
   - Saída: `saida_verificar_decomposicao_f_symbolic.md`.

3. `verificar_reflexao_lorentziana.py`
   - Classificação: ilustração linear da reconstrução lorentziana.
   - Mostra que a reflexão em uma forma-relógio unitária transforma uma métrica
     euclidiana positiva em uma métrica efetiva de assinatura $(-,+,+,+)$.
   - Saída: `saida_verificar_reflexao_lorentziana.md`.

4. `verificar_mapa_perelman_madelung.py`
   - Classificação: teste simbólico/numérico de identidade constitutiva.
   - Verifica o mapa direto/inverso em $\rho>0$, registra a singularidade em
     $\rho=0$ e mostra que superposição é linear em $\Psi$, não em
     $(\rho,S_R)$.
   - Saída: `saida_verificar_mapa_perelman_madelung.md`.

## Uso

Executar a partir desta pasta ou diretamente:

```bash
python3 verificar_dimensao_kernel.py
python3 verificar_decomposicao_f_symbolic.py
python3 verificar_reflexao_lorentziana.py
python3 verificar_mapa_perelman_madelung.py
```
