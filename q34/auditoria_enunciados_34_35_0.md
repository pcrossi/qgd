# Auditoria de fechamento segundo bkp/34-0.md e bkp/35-0.md

## 1. Regra

Os enunciados originais prevalecem sobre ampliações posteriores do programa.
Um cálculo útil pode permanecer válido sem satisfazer integralmente o critério
de fechamento da questão.

## 2. Questão 34

O critério original é:

$$
\boxed{\text{ao menos um cálculo completo de loop derivado da ação.}}
$$

### Respondido

1. gauge de fundo;
2. determinante de Faddeev--Popov;
3. fantasmas como representação auxiliar;
4. Ward no loop $U(1)$;
5. Slavnov--Taylor estrutural;
6. termos locais $a_4$ e $a_6$;
7. coeficientes de grupo e extensão Bismut formal;
8. beta-função como tradução perturbativa externa.

### Critério mínimo posteriormente satisfeito

O loop fermiônico efetivo começa em

$$
\Gamma_\tau[A]
=
\frac12\operatorname{Tr}
\int_\tau^\infty\frac{ds}{s}e^{-sL_\psi[A]},
$$

mas não precisa ser promovido. A cadeia GDQ foi posteriormente executada no
setor de fase toroidal:

$$
\boxed{
\mathcal S_{\rm GDQ}
\longrightarrow
\operatorname{Hess}_\chi\mathcal S_{\rm GDQ}
\longrightarrow
\det{}'H_{\rm geom}
\longrightarrow
\Pi_{\mu\nu}^{\rm GDQ}.
}
$$

Ver q34/loop_geometrico_fase_t4.md. O teste quantitativo entre três classes de
kernels covariantes foi executado em q34/teste_kernels_covariantes.md. Ward,
$\Pi(0)=0$, monotonicidade, finitude e saturação são invariantes. A amplitude
saturada não é universal quando o kernel representa outra resolução física;
o kernel canônico é o semigrupo da Hessiana oficial.

### Status

$$
\boxed{
\text{Q34 fechada no setor geométrico declarado de 34-0.}
}
$$

## 3. Questão 35

### Respondido

1. função efetiva de escala definida pela polarização;
2. diagrama fermiônico $U(1)$ calculado;
3. operadores vetor--jacobiano auditados por $a_4/a_6$;
4. esquema de tempo próprio/heat kernel covariante com subtração em $q^2=0$;
5. antiga beta-função cúbica rejeitada por estabilidade incorreta;
6. saturação demonstrada para $\tau_{\rm EM}>0$;
7. origem estrutural positiva de $\tau_{\rm EM}$ formulada pela ponte
   torsão--Reynolds.

### Delimitação posterior do escopo

O enunciado 35-0 também solicitava comparação com o running observado. O
cálculo até

$$
\alpha_{\rm IR}^{-1}\simeq137
\longrightarrow
\alpha_{\rm LHC}^{-1}\simeq128.
$$

não foi executado. Por decisão explícita do usuário em 2026-07-12, $1/128$
foi retirado do programa atual. Essa delimitação impede chamar o resultado de
resposta fenomenológica completa a todas as perguntas de 35-0, mas não reabre
a demonstração geométrica de ausência do polo.

### Status

$$
\boxed{
\text{Q35 fechada condicionalmente no setor }U(1)\text{ no escopo adotado.}
}
$$

## 4. Consequência para o backlog

As extensões posteriores são:

1. Q35: calibrar $\Lambda_C$ em unidades físicas e testar a equação de gap,
   sem reabrir o fechamento condicional;
2. Q34: manter Bismut, fundos topológicos e setores não abelianos como
   extensões posteriores, sem reabrir o fechamento declarado.

Os cálculos $U(1)$, $a_4$, $a_6$ e Bismut permanecem válidos como auditoria
externa e preparação técnica.
