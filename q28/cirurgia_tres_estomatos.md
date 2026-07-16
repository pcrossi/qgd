# Q28 — Cirurgia de três estômatos e aditividade do índice

## 1. Formulação geométrica

Seja $X_4$ a fatia transversal orientada na qual os defeitos elementares são
resolvidos. Escolham-se três vizinhanças disjuntas

$$
B^4_a\subset X_4,
\qquad
a=1,2,3,
$$

com bordas

$$
Y_a=\partial B^4_a\simeq S^3.
$$

A cirurgia produz o complemento perfurado

$$
X_4^\circ
=X_4\setminus
\bigcup_{a=1}^{3}\operatorname{int}(B^4_a),
$$

de modo que

$$
\partial X_4^\circ
=\bigsqcup_{a=1}^{3}(-Y_a).
$$

A variedade original é reconstruída pela colagem

$$
X_4
=X_4^\circ
\cup_{\bigsqcup Y_a}
\left(\bigsqcup_{a=1}^{3}B^4_a\right).
$$

Essa construção é a versão precisa de “três estômatos”: são três componentes
de fronteira disjuntas na fatia normal, não três partículas pontuais.

## 2. Operadores locais

Em cada $Y_a$, use o operador tangencial de Dirac--Bismut

$$
D_a
=\slashed D_{Y_a}
+\frac18B^{(a)}_{ijk}\gamma^{ijk}
-iA^{(a)}_i\gamma^i.
$$

O protótipo local já calculado fornece, para fluxo de Hopf mínimo, torção
$\beta=-3/2$ e orientação positiva,

$$
\boxed{
\operatorname{ind}_{\rm APS}D^+_{B^4_a}=1.
}
$$

Essa unidade não é imposta: ela resulta de um cruzamento espectral simples.

## 3. Fórmula de colagem APS

Sob métricas e conexões de forma produto em colares das interfaces, e usando
projetores APS complementares nos dois lados, a fórmula de colagem dá

$$
\operatorname{Ind}D^+_{X_4}
=\operatorname{Ind}D^+_{X_4^\circ}
+\sum_{a=1}^{3}
\operatorname{ind}_{\rm APS}D^+_{B^4_a}
+\mu_{\rm glue}.
$$

O termo $\mu_{\rm glue}$ contém a correção por modos zero/interseções dos
subespaços de Cauchy. Para obter aditividade direta é necessário demonstrar

$$
\operatorname{Ind}D^+_{X_4^\circ}=0,
\qquad
\mu_{\rm glue}=0.
$$

Essas condições valem, por exemplo, se o complemento não transportar carga
quiral adicional, os operadores de fronteira forem invertíveis após a
regularização admissível e os projetores dos dois lados forem exatamente
complementares. Se houver modos zero, eles devem ser tratados explicitamente;
não podem ser descartados.

Sob essas hipóteses,

$$
\boxed{
\operatorname{Ind}D^+_{X_4}
=1+1+1=3.
}
$$

## 4. Orientação e cancelamento

A soma igual a três exige que as três circulações possuam a mesma orientação:

$$
m_a=+1,
\qquad
a=1,2,3.
$$

Em geral,

$$
\operatorname{Ind}D^+_{X_4}
=\sum_{a=1}^{3}\operatorname{sgn}(m_a).
$$

Assim, configurações como $(+,+,-)$ fornecem índice líquido um. A mera
existência de três gargantas não basta: a lei de conservação da torção deve
selecionar o setor coorientado se o resultado pretendido for três.

## 5. Levantamento para a carga global

Pela colagem $\mathbb Z_6$, cada unidade primitiva de índice corresponde a

$$
A_a=6\operatorname{sgn}(m_a).
$$

Se o mapa de Gysin que insere cada defeito no background global preservar
essas três classes de forma independente, então

$$
a_4^{\rm total}
=\sum_{a=1}^{3}(i_a)_!a_4^{(a)}
$$

e, no setor coorientado,

$$
\boxed{
A_{\rm total}
=\sum_{a=1}^{3}A_a
=18.
}
$$

Consequentemente,

$$
\boxed{
N_G=\frac{A_{\rm total}}6=3.
}
$$

Esse é o homomorfismo local--global procurado. Ele prova a implicação

$$
\boxed{
\text{três estômatos primitivos, independentes e coorientados}
\Longrightarrow N_G=3.
}
$$

## 6. Conteúdo fermiônico

O levantamento de representações já construído associa a cada unidade de
índice uma cópia de

$$
\mathcal E_{\rm gen}
=(3,2)_{1/6}
\oplus(\bar3,1)_{-2/3}
\oplus(\bar3,1)_{1/3}
\oplus(1,2)_{-1/2}
\oplus(1,1)_1.
$$

Essa soma possui quinze componentes de Weyl. Condicionalmente às hipóteses de
cirurgia,

$$
\operatorname{Ind}_{\rm total}
=3\mathcal E_{\rm gen},
$$

totalizando quarenta e cinco componentes de Weyl quirais. Isso não inclui
automaticamente neutrinos direitos; eles exigiriam um setor adicional.

## 7. Modos e mistura de sabor

Se $\psi_a^{(u)}$, $\psi_a^{(d)}$, $\psi_a^{(e)}$ e $\psi_a^{(\nu)}$ são os
modos normalizados localizados nas três gargantas, a Hessiana oficial reduzida
define matrizes de overlap

$$
(M_s)_{ab}
=\left\langle
\psi_a^{(s)},
\mathcal O_{\rm Hess}^{(s)}\psi_b^{(s)}
\right\rangle_{\mathcal U},
\qquad
s=u,d,e,\nu.
$$

Os elementos diagonais controlam as escalas próprias; os não diagonais medem
o tunelamento geométrico entre estômatos. Entretanto, as matrizes físicas de
mistura não são um único overlap. Elas são os desalinhamentos

$$
V_{\rm CKM}=U_u^\dagger U_d,
$$

$$
U_{\rm PMNS}=U_e^\dagger U_\nu,
$$

onde $U_s$ diagonaliza o setor correspondente. Assim, três estômatos fornecem
a arquitetura de matrizes $3\times3$, mas não determinam automaticamente seus
ângulos e fases.

Não se deve afirmar que elétrons oscilam livremente em múons ou taus. A
oscilação coerente observada é a de sabores de neutrinos; CKM descreve o
desalinhamento dos setores de quarks nas correntes fracas.

## 8. Hierarquia de massas

A igualdade dos índices locais não implica igualdade de massas. Depois da
cirurgia, a Hessiana global possui a forma efetiva

$$
H_{ab}
=E_a\delta_{ab}+T_{ab},
$$

onde $E_a$ depende dos perfis locais de curvatura, torção e dilatão, e
$T_{ab}$ mede a comunicação pelo complemento $X_4^\circ$. Uma quebra dinâmica
da simetria de permutação pode separar os autovalores.

Isso torna uma hierarquia possível, mas não a calcula. Os valores de massa
exigem resolver o background de três centros pela ação oficial e avaliar sua
Hessiana.

## 9. O que a cirurgia prova e o que permanece assumido

### Provado condicionalmente

$$
3\text{ componentes primitivas coorientadas}
\Longrightarrow
\operatorname{Ind}=3
\Longrightarrow
A=18.
$$

### Ainda não derivado

1. por que a cosmologia cria exatamente três estômatos;
2. por que eles são coorientados;
3. por que o complemento tem índice zero e $\mu_{\rm glue}=0$;
4. por que esses estômatos geracionais são os mesmos três defeitos usados no
   modelo bariônico;
5. os overlaps, massas e parâmetros CKM/PMNS.

## 10. Status

A cirurgia é uma formulação válida e encerra a **aditividade**. Se a topologia
com três estômatos for tomada como condição ambiental inicial, então a GDQ
produz rigorosamente três cópias do multiplet quiral já derivado. Nesse caso,

$$
\boxed{
A=18
}
$$

é consequência da condição inicial de três defeitos, não uma previsão do
número de defeitos pela ação oficial.

