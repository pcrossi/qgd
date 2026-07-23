---
title: "Scripts — Capítulo 4"
---

# Scripts — Capítulo 4

Estes scripts são verificações simbólicas ou ilustrações pedagógicas ligadas ao
Capítulo 4. Eles não substituem as notas analíticas nem constituem previsões
físicas.

## Scripts

1. `verificar_dimensao_acao_normalizada.py`
   - Classificação: teste simbólico dimensional.
   - Verifica a neutralidade dimensional do integrando em coordenadas
     normalizadas e separa $\Lambda_C$ adimensional de escalas físicas.
   - Saída: `saida_verificar_dimensao_acao_normalizada.md`.

2. `verificar_variacao_medida.py`
   - Classificação: teste simbólico de identidade constitutiva.
   - Verifica $\delta\mathcal U/\mathcal U=-\delta(f+\bar f)/2$ para métrica
     fixa e $z_\tau$ fixo.
   - Saída: `saida_verificar_variacao_medida.md`.

3. `verificar_projetor_fisico_linear.py`
   - Classificação: ilustração linear de quociente físico.
   - Constrói um projetor que remove modos de gauge e vínculos num modelo
     finito.
   - Saída: `saida_verificar_projetor_fisico_linear.md`.

4. `verificar_polarizacao_heat_kernel_toy.py`
   - Classificação: ilustração heat-kernel.
   - Mostra saturação ultravioleta em um integral heat-kernel simples.
   - Saída: `saida_verificar_polarizacao_heat_kernel_toy.md`.

5. `verificar_kernel_calor_propagador.py`
   - Classificação: verificação simbólica/numérica de consistência.
   - Verifica o propagador plano $G_\tau=e^{-\tau p_E^2}/(p_E^2+m^2)$ e a
     separação correta entre Hessiana e gerador de calor.
   - Saída: `saida_verificar_kernel_calor_propagador.md`.

6. `verificar_hessiana_escalar_reduzida.py`
   - Classificação: verificação simbólica/numérica de consistência.
   - Monta $L_\varphi=2(-\Delta)$ em domínio periódico e compara os primeiros
     autovalores com $2k^2$.
   - Saída: `saida_verificar_hessiana_escalar_reduzida.md`.

7. `verificar_separacao_escalas.py`
   - Classificação: teste numérico/simbólico de consistência.
   - Separa $\Lambda_C$, $\widehat\Lambda_\tau$, massas e escalas setoriais.
   - Mostra por ordem de grandeza que $m_e$ e $1$ GeV não podem ser cortes
     gaussianos duros universais.
   - Saída: `saida_verificar_separacao_escalas.md`.

8. `verificar_loop_geometrico_fase_t4.py`
   - Classificação: teste numérico/simbólico de consistência.
   - Reproduz o loop geométrico da fase toroidal.
   - Verifica $\Pi(0)=0$, transversalidade de Ward e saturação UV.
   - Saída: `saida_verificar_loop_geometrico_fase_t4.md`.

9. `verificar_kernels_covariantes_calibre.py`
   - Classificação: teste numérico/simbólico de consistência.
   - Compara kernels covariantes admissíveis.
   - Mostra que Ward é preservada por covariância, embora coeficientes
     numéricos dependam da resolução espectral escolhida.
   - Saída: `saida_verificar_kernels_covariantes_calibre.md`.

10. `verificar_ausencia_polo_landau_u1.py`
    - Classificação: avaliação direta e teste de consistência.
    - Avalia $\Pi_\tau(q^2)$, verifica $\Pi(0)=0$, Ward, saturação UV e
      recuperação do limite logarítmico em baixa energia.
    - Saída: `saida_verificar_ausencia_polo_landau_u1.md`.

11. `verificar_varredura_multiespecie_landau.py`
    - Classificação: teste de consistência.
    - Varre a condição multiespécie $\Pi_{\rm EM}(\infty)=1$ sem tratar a
      raiz como previsão de escala física.
    - Saída: `saida_verificar_varredura_multiespecie_landau.md`.

12. `verificar_gap_colar_em.py`
    - Classificação: avaliação direta e teste de convergência.
    - Mostra que o colar Neumann local tem $\lambda_1=\pi^2/L^2\to0$.
    - Saída: `saida_verificar_gap_colar_em.md`.

13. `verificar_fechamento_torcao_reynolds.py`
    - Classificação: avaliação simbólico-numérica de cadeia constitutiva.
    - Verifica $\operatorname{Re}_{\rm Q}=\alpha$ e a equação estacionária
      radial que fornece $\tau_{\rm EM}>0$.
    - Saída: `saida_verificar_fechamento_torcao_reynolds.md`.

## Uso

```bash
python3 verificar_dimensao_acao_normalizada.py
python3 verificar_variacao_medida.py
python3 verificar_projetor_fisico_linear.py
python3 verificar_polarizacao_heat_kernel_toy.py
python3 verificar_kernel_calor_propagador.py
python3 verificar_hessiana_escalar_reduzida.py
python3 verificar_separacao_escalas.py
python3 verificar_loop_geometrico_fase_t4.py
python3 verificar_kernels_covariantes_calibre.py
python3 verificar_ausencia_polo_landau_u1.py
python3 verificar_varredura_multiespecie_landau.py
python3 verificar_gap_colar_em.py
python3 verificar_fechamento_torcao_reynolds.py
```
