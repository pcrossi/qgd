---
title: "Checklist operacional — Capítulo 5"
---

# Checklist operacional — Capítulo 5

Este checklist segue o protocolo metodológico do Capítulo 27.

O capítulo deve ser pedagógico: abrir a primeira variação da ação oficial e
mostrar quais equações seguem diretamente dela, sem transformar a GDQ em
mecânica quântica ordinária.

## 1. Objetivo do capítulo

O Capítulo 5 deve demonstrar:

1. como a variação de $\mathcal U\mathcal L_0dV_g$ deve ser feita;
2. como $f$ se reescreve em $\rho$ e $S_R$;
3. por que a variação em fase produz corrente conservada;
4. por que a variação em densidade produz o operador de Bohm;
5. por que a variação métrica produz uma equação ponderada, não Einstein
   renomeado;
6. como Noether aparece explicitamente;
7. como os momentos de bordo entram;
8. o que é direto da ação oficial e o que depende da reconstrução física;
9. por que $\Pi_{S_R}=\rho$ não é identidade off shell universal.

Status do capítulo: **fechado para a primeira variação de bulk e condicional
para a dinâmica canônica de laboratório**.

## 2. Situação do corpo principal

| Seção | Status | Observação |
|---|---|---|
| `05.1` | pronta em primeira versão | Explica regra do produto, integração por partes e separação bulk/bordo. |
| `05.2` | pronta em primeira versão | Reescreve a ação em $\rho$ e $S_R$. |
| `05.3` | pronta em primeira versão | Deriva corrente de fase e conservação de fluxo. |
| `05.4` | pronta em primeira versão | Deriva operador de amplitude/Bohm e HJ-Bohm como redução. |
| `05.5` | pronta em primeira versão | Deriva equação métrica ponderada. |
| `05.6` | pronta em primeira versão | Prova Noether e discute vínculos/bordos. |
| `05.7` | pronta condicionalmente | Separa o demonstrado da reconstrução canônica posterior. |

## 3. Notas chamadas e função lógica

| Nota | Função |
|---|---|
| `Derivação da corrente de fase` | Cálculo compacto da variação em $S_R$. |
| `Da energia de amplitude ao termo de Bohm` | Identidade variacional que reconhece o operador de Bohm em redução física. |
| `Auditoria do termo canonico rho d_t S_R` | Mostra que $\Pi_{S_R}=\rho$ não é identidade off shell da ação oficial. |
| `Primeira variação da ação GDQ - estrutura completa` | Apoio algébrico global à primeira variação. |
| `Bem-postura do fluxo geométrico GDQ em gauge` | Demonstra parabolicidade forte, existência local, unicidade, dependência contínua e continuação do fluxo em $\tau$ após gauge. |

Avaliação: as notas sustentam as afirmações fortes e preservam a distinção
entre bulk GDQ e setor Madelung.

## 4. Resultados consolidados incorporados

O capítulo incorpora, em forma autocontida, os seguintes blocos técnicos:

1. conservação da corrente de fase;
2. equação de Hamilton--Jacobi--Bohm como redução do setor de densidade;
3. variação métrica ponderada;
4. relação constitutiva entre $\rho$ e $\mathcal U$;
5. decomposição do campo complexo em fase e densidade;
6. distinção entre bulk GDQ e representação de Madelung;
7. difusão e fluxo como linguagem de redução, não como ação substituta;
8. análise do termo canônico $\rho\,\partial_tS_R$.
9. bem-postura local do fluxo geométrico em $\tau$ após gauge.

Notas principais chamadas pelo capítulo:

- [[../notes/equations/index|Equações de movimento e leis de conservação]];
- [[../notes/action/Primeira variação da ação GDQ - estrutura completa|Primeira variação da ação GDQ — estrutura completa]].

## 5. Resultados diretos da ação oficial

Diretamente demonstrado:

1. a transformação $f\leftrightarrow(\rho,S_R)$ em setor $\rho>0$;
2. $\delta_{S_R}\mathcal U=0$;
3. $\delta_\rho\mathcal U=\mathcal U\,\delta\rho/\rho$;
4. corrente de fase:

$$
\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U g^{\mu\bar\nu}\partial_{\bar\nu}S_R;
$$

5. conservação on shell:

$$
\nabla_\mu\widehat J_S^\mu=0;
$$

6. equação de densidade com razão $\Delta_g\sqrt\rho/\sqrt\rho$;
7. equação métrica ponderada com derivadas de $\mathcal U$;
8. identidade de Noether off shell;
9. momentos normais e condições de bordo oriundos da própria variação.

## 6. Resultados condicionais ou reduzidos

Dependem da reconstrução física:

1. identificação da equação de continuidade local do laboratório;
2. normalização cinética com massa física;
3. termo canônico $\rho\partial_tS_R$;
4. condição $\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}$;
5. forma canônica completa de Madelung;
6. interpretação probabilística operacional de eventos medidos.

A condição canônica exige uma polarização física:

$$
p_\rho=0,
\qquad
\Pi_{S_R}=\sqrt h\rho.
$$

Essa polarização não altera a ação oficial. Ela seleciona o setor físico
hidrodinâmico ordinário dentro do espaço maior de dados GDQ.

## 7. O que não deve ser afirmado neste capítulo

Não afirmar que:

1. GDQ é apenas mecânica quântica em variáveis de Madelung;
2. $\Pi_{S_R}=\rho$ vale off shell;
3. Perelman seleciona sozinho o setor canônico;
4. a equação de Bohm no laboratório está completa sem a ponte global–local;
5. toda solução da ação oficial é matéria observável;
6. vínculos de aparelho podem ser inseridos sem declaração variacional.

## 8. Scripts numéricos e simbólicos

Scripts obrigatórios para fechamento do Capítulo 5: **nenhum**.

Motivo: o capítulo é variacional e analítico. As verificações mais úteis são
simbólicas ou ilustrativas.

Scripts opcionais criados em [[scripts/README|scripts/]]:

1. [[scripts/verificar_corrente_fase_1d.py|verificar_corrente_fase_1d.py]]  
   Verificar em malha 1D que uma corrente constante satisfaz divergência nula
   e que fluxo lateral altera a carga integrada.

2. [[scripts/verificar_bohm_fisher_variacao.py|verificar_bohm_fisher_variacao.py]]  
   Checar numericamente a variação da energia de Fisher e o operador
   $\Delta\sqrt\rho/\sqrt\rho$.

3. [[scripts/verificar_noether_shift_fase.py|verificar_noether_shift_fase.py]]  
   Ilustrar que uma Lagrangiana dependente apenas de $\partial S_R$ é
   invariável sob $S_R\mapsto S_R+S_0$.

4. [[scripts/verificar_polarizacao_canonica_toy.py|verificar_polarizacao_canonica_toy.py]]  
   Mostrar a saturação de Cauchy–Schwarz/Routh para
   $\Pi=(Q_S/N_\rho)\rho$ em um toy model positivo.

5. [[scripts/verificar_simbolo_parabolico_gdq.py|verificar_simbolo_parabolico_gdq.py]]  
   Verificar pontualmente que o símbolo principal em gauge é
   $\sigma_{\rm pr}(\xi)=|\xi|_g^2I$ e é positivo para métrica riemanniana.

Classificação: teste simbólico/ilustração pedagógica, não previsão física.

## 9. Pontos didáticos a revisar na leitura final

Antes de considerar o Capítulo 5 editorialmente pronto:

1. garantir que as derivações longas continuem legíveis;
2. verificar se cada equação tem hipótese próxima;
3. separar claramente “bulk GDQ” de “laboratório Madelung”;
4. reforçar que bordos são parte da variação;
5. manter o resultado $\Pi_{S_R}\ne\rho$ off shell como ponto de rigor, não
   como problema insolúvel;
6. ligar o que fica condicional ao Capítulo 6 e à teoria da medida;
7. conferir links e renderização Quartz.

## 10. Veredito operacional

O Capítulo 5 está **estruturalmente montado e matematicamente central**.

Ele fecha:

1. corrente de fase;
2. operador de densidade/Bohm no bulk;
3. equação métrica ponderada;
4. Noether;
5. papel dos bordos.

Ele deixa condicional:

1. o termo canônico de Madelung;
2. a polarização física de laboratório;
3. a seleção dinâmica/operacional do setor medido.

Essas condições são tratadas na ponte global–local e na teoria da medida, sem
reabrir a primeira variação da ação oficial.

## Revisão didática de 2026-07-19

O Capítulo 5 foi conferido na fase de revisão científica/didática. O checklist
foi ajustado para remover dependências de rastreabilidade histórica: os blocos
técnicos agora aparecem como resultados incorporados ao manuscrito e não como
referências externas. Foi criado o índice interno
[[../notes/equations/index|Equações de movimento e leis de conservação]], que
lista as notas chamadas sobre corrente de fase, termo de Bohm e polarização
canônica.

Os quatro scripts do capítulo devem permanecer como verificações pedagógicas:
corrente de fase em 1D, variação Fisher--Bohm, simetria global da fase e
polarização canônica toy. Nenhum deles é previsão metrológica.
