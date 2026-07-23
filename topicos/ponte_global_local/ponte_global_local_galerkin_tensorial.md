# Ponte global--local — infraestrutura de Galerkin tensorial

## 1. Status e objetivo

Este documento prepara o cálculo, mas **não atribui valores físicos** a
$\lambda_\mu$, $g_\mu$, $C_a$, $C_c$ ou $C_u$. Esses números só existem após
ser fornecido um modo tensorial admissível, com background, domínio, condições
de bordo e expansão da ação oficial definidos.

O funcional reduzido auditado é

$$
\mathcal S_{\rm red}(A)-\mathcal S_0
=\lambda_\mu |A|^2+g_\mu|A|^4+h_\mu|A|^6+\cdots.
$$

O termo sêxtico é mantido porque um $g_\mu<0$ não encerra necessariamente a
análise se $h_\mu>0$ estabilizar uma bifurcação de primeira ordem.

## 2. Dados obrigatórios do modo físico

O provider a ser conectado deve calcular, em cada ponto $(r,\chi,\theta,\phi)$:

1. a densidade positiva de norma do modo;
2. as densidades quadráticas, quárticas e, quando necessárias, sêxticas;
3. sua separação nos setores `curvature`, `dilaton_gradient`,
   `dilaton_potential`, `measure_volume`, `torsion_bismut`, `constraint` e
   `boundary_interface`;
4. as três densidades de retroação quadrática do matching, associadas a
   $(a,c,u)$;
5. derivadas radiais e angulares, compatibilidade Hermitiana, projeção
   transversal a gauge e fatores da medida oficial.

O motor não inventa esses dados e rejeita setores desconhecidos.

## 3. Normalização

Com

$$
N_\mu=\int_{I\times S^3}|\mu|^2\,dV,
$$

a montagem retorna

$$
\lambda_\mu=\frac{Q_2}{N_\mu},
\qquad
g_\mu=\frac{Q_4}{N_\mu^2},
\qquad
h_\mu=\frac{Q_6}{N_\mu^3},
$$

e

$$
C_i=\frac{M_i}{N_\mu},
\qquad i\in\{a,c,u\}.
$$

Isso remove a ambiguidade de reescalar o representante tensorial por uma
constante.

## 4. Quadratura e convergência

A quadratura atual usa Gauss--Legendre separadamente em $r$, $\chi$, $\theta$
e $\phi$, com a medida angular

$$
d\Omega_3=\sin^2\chi\,\sin\theta\,d\chi\,d\theta\,d\phi.
$$

Um fator radial adicional pode ser fornecido pelo background. A rotina
`convergence_table` varia independentemente:

- a ordem radial;
- a ordem angular;
- o corte harmônico.

Um coeficiente só poderá ser citado como numericamente resolvido quando esses
três limites apresentarem platô compatível e a decomposição por setores também
convergir, não apenas a soma total.

## 5. Bifurcação de amplitude finita

Para $x=|A|^2$, os ramos estacionários não nulos satisfazem

$$
\lambda_\mu+2g_\mu x+3h_\mu x^2=0,
\qquad x>0.
$$

A estabilidade é testada pela curvatura completa

$$
\frac{d^2\mathcal S_{\rm red}}{dA^2}
=2\lambda_\mu+12g_\mu A^2+30h_\mu A^4>0.
$$

Depois disso ainda é necessário resolver simultaneamente

$$
r_i(0)+C_i|A_*|^2+\delta r_i(\delta X)=0,
$$

pois os $C_i$ isolados não garantem que a resposta do restante do background
feche o matching.

## 6. Arquivos e classificação

- `ponte_global_local_galerkin_tensorial.py`: motor de montagem;
- `teste_sintetico_galerkin_tensorial.py`: fixture analítica explicitamente
  sintética;
- este documento: contrato para inserir o modo físico futuro.

Classificação atual: **infraestrutura computacional validável**. O teste
sintético verifica quadratura, normalização, convergência harmônica e solução
da bifurcação, mas não constitui evidência física da GDQ.
