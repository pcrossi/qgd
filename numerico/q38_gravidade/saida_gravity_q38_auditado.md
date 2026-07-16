# Saída do solver auditado Q38

## 1. Constantes usadas

\[
\alpha_{\rm geom}=0.007297348130,
\qquad
S_{\rm inst}=\frac1{2\alpha}=68.51804122.
\]

\[
\chi_{\rm Fano}^{\rm bulk}
=
\frac{3\sqrt2}{5}
=0.848528137424,
\qquad
\sqrt\pi=1.772453850906.
\]

\[
\frac{\chi_{\rm Fano}^{\rm bulk}}{\sqrt\pi}
=0.478730736482.
\]

Valor observado usado apenas como comparação final:

\[
\Pi_1^{\rm obs}
=
\frac{GM_p^2}{\hbar c}
=5.90615307e-39.
\]

## 2. Tabela de auditoria

| Cenário | Contorno | chi_Fano | J_flat | V_eff | Pi_obs | Erro | Classificação |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | :--- |
| A_dirichlet_bulk_sem_planificacao | dirichlet_fixed_instanton | 8.48528137e-01 | 1.00000000e+00 | 1.74981762e-30 | 5.89039596e-39 | 0.2668% | teste: Fano bulk, sem leitura plana |
| B_dirichlet_bulk_com_sqrtpi | dirichlet_fixed_instanton | 8.48528137e-01 | 1.77245385e+00 | 1.74981762e-30 | 3.32330004e-39 | 43.7316% | hipotese: Fano bulk + planificacao separada sqrt(pi) |
| C_v2_misturado_reproduzido | dirichlet_fixed_instanton | 4.78730736e-01 | 1.77245385e+00 | 1.74981762e-30 | 5.89039596e-39 | 0.2668% | auditoria: chi=Fano/sqrt(pi) e depois divide por sqrt(pi) |
| D_script_sem_planificacao_final | dirichlet_fixed_instanton | 4.78730736e-01 | 1.00000000e+00 | 1.74981762e-30 | 1.04404550e-38 | 76.7725% | controle: Fano ja planificado sem divisao final |
| E_neumann_regular_media_fixa | neumann_regular_mean_fixed | 8.48528137e-01 | 1.00000000e+00 | 1.74981762e-30 | 5.89039596e-39 | 0.2668% | teste: Neumann regular reduz ao modo constante |
| F_robin_balanceado_media_fixa | robin_impedance_balanced | 8.48528137e-01 | 1.00000000e+00 | 1.74981762e-30 | 5.89039596e-39 | 0.2668% | teste: Robin balanceado reduz ao modo constante |

## 3. Notas de contorno

- `A_dirichlet_bulk_sem_planificacao`: Dirichlet instantônico resolvido por BVP.
- `B_dirichlet_bulk_com_sqrtpi`: Dirichlet instantônico resolvido por BVP.
- `C_v2_misturado_reproduzido`: Dirichlet instantônico resolvido por BVP.
- `D_script_sem_planificacao_final`: Dirichlet instantônico resolvido por BVP.
- `E_neumann_regular_media_fixa`: Neumann regular possui modo zero; média fixada em S_inst para comparação.
- `F_robin_balanceado_media_fixa`: Robin balanceado com fonte j=lambda*S_inst; perfil regular constante.

## 4. Conclusões

1. Com a EDO reduzida de vácuo, todos os contornos regulares sem fonte efetiva
   colapsam no perfil constante. Portanto, este solver ainda não é uma prova
   dinâmica do dilaton.

2. O cenário `A_dirichlet_bulk_sem_planificacao` já fica próximo do valor
   observado, com erro da ordem de \(10^{-1}\%\). Isso corresponde ao uso
   de \(\chi_{\rm Fano}^{\rm bulk}\) sem fator plano separado.

3. O cenário `B_dirichlet_bulk_com_sqrtpi` mostra que aplicar
   \(J_{\rm flat}=\sqrt\pi\) como fator independente desloca fortemente
   o resultado. Logo, \(\sqrt\pi\) não pode ser aplicado de forma ingênua
   após usar o Fano bulk.

4. O cenário `C_v2_misturado_reproduzido` confirma a auditoria: usar
   \(\chi_{\rm Fano}/\sqrt\pi\) e depois dividir por \(\sqrt\pi\)
   cancela a planificação e retorna ao cenário bulk.

5. Para fechar Q38, falta substituir o modo fenomenológico
   \(S_{\rm inst}=1/(2\alpha)\) por uma sela derivada da ação reduzida
   euclidiana da GDQ e calcular \(J_{\rm flat}\) pela norma do modo
   gravitacional ou por média ponderada.
