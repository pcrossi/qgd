# Q44 — Auditoria dos scripts de dupla fenda

## Objeto auditado

Arquivo legado:

- `src/plot_dupla_fenda.py`

Figura produzida:

- `figs/dupla_fenda_comparacao.png`

## Classificação numérica

O script é uma visualização analítica de um modelo reduzido assumido, não uma
simulação completa da GDQ.

Classificação conforme o protocolo numérico:

1. comparação fenomenológica;
2. teste de consistência da redução paraxial;
3. visualização de correspondência com Fraunhofer.

Não é:

1. evolução da ação oficial;
2. solução da Hessiana física;
3. evolução de métrica;
4. previsão cega de decoerência;
5. teste completo de detector/aparelho.

## Equação efetivamente usada

O script usa dois pacotes gaussianos paraxiais em fundo fixo e calcula:

$$
\rho(x,y)=|\psi_1(x,y)+\psi_2(x,y)|^2.
$$

Na linguagem GDQ, isso deve ser lido como uma solução reduzida do setor
Madelung em fundo estacionário, com:

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

O script não resolve diretamente:

$$
\delta \mathcal S_{\rm GDQ}=0
$$

para os campos completos $(g,J,H,f,\mathcal U)$.

## Métrica

A métrica é mantida fixa e plana. Logo, qualquer legenda dizendo "GDQ exata" ou
"Perelman exato" deve ser suavizada para:

$$
\text{modelo reduzido GDQ/Madelung em fundo fixo}.
$$

## O que o gráfico mostra corretamente

O gráfico mostra:

1. interferência por duas fontes coerentes;
2. correção de campo próximo em relação ao limite de Fraunhofer;
3. aproximação assintótica ao padrão usual no campo distante;
4. mínimos não estritamente nulos para gaussianas finitas fora do eixo.

## O que o gráfico não prova

O gráfico não prova:

1. evolução métrica de Perelman--Bismut;
2. retroação do nó topológico sobre o background;
3. destruição de franjas por detector;
4. fator de decoerência derivado;
5. diferença experimental exclusiva da GDQ.

## Correção recomendada de linguagem

Trocar:

$$
\text{GDQ exato - Perelman}
$$

por:

$$
\text{GDQ reduzida - Madelung em fundo fixo}
$$

e trocar:

$$
\text{MQ clássica}
$$

por:

$$
\text{limite de Fraunhofer}.
$$

## Próximo script correto

Um script forte para Q44 deve resolver ao menos o problema reduzido:

$$
\begin{cases}
\partial_t\rho+\nabla\cdot(\rho\nabla S_R/m)=0,\\
\partial_tS_R+\frac{|\nabla S_R|^2}{2m}
+V_{\rm app}+Q[\rho]=0,
\end{cases}
$$

com:

$$
Q[\rho]=-\frac{\hbar^2}{2m}\frac{\Delta\sqrt\rho}{\sqrt\rho},
$$

domínio com barreira e duas fendas, e condição de detector modelada como
impedância de bordo derivada:

$$
\mathsf R_{\rm det}
=
\text{DtN}_{\rm aparelho}
$$

ou como fonte externa clássica explicitamente declarada.
