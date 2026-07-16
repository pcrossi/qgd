# Q34 — Limite da rota fermiônica auxiliar e retorno ao loop geométrico

## 1. Critério de 34-0

O fechamento exige:

$$
\boxed{\text{ao menos um cálculo completo de loop derivado da ação.}}
$$

O loop $U(1)$ já calculado usa

$$
\Gamma_\tau[A]
=
\frac12\operatorname{Tr}
\int_\tau^\infty\frac{ds}{s}e^{-sL_\psi[A]},
$$

$$
L_\psi[A]
=
\slashed D_{B,A}^\dagger\slashed D_{B,A}+m^2.
$$

É necessário verificar se esse operador segue da Hessiana da ação oficial.

## 2. Espaço de campos da ação oficial

A ação fundamental depende de

$$
\mathcal S_{\rm GDQ}
=
\mathcal S_{\rm GDQ}[g,f,\bar f],
$$

com $B$ entrando, quando usado, como camada torsional constitutiva/efetiva.
As variações fundamentais são

$$
\delta g,\qquad\delta f,\qquad\delta\bar f,
$$

e eventualmente $\delta B$ na formulação efetiva declarada.

Não há variável fundamental $\psi$ ou $\bar\psi$ na ação oficial.
Consequentemente,

$$
\boxed{
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\bar\psi\,\delta\psi}
\quad\text{não está definido.}
}
$$

## 3. O que a Hessiana oficial produz

A segunda variação tem estrutura

$$
\operatorname{Hess}\mathcal S_{\rm GDQ}
:
(\delta g,\delta f,\delta\bar f,\delta B)
\longmapsto
(\delta g,\delta f,\delta\bar f,\delta B).
$$

Depois de vínculos e gauge, ela produz operadores bosônicos em tensores,
escalares e formas. Uma integral gaussiana bosônica gera

$$
\left(\det{}'H_{\rm bos}\right)^{-1/2}.
$$

O determinante fermiônico exige uma medida anticomutante ou um Pfaffiano:

$$
\det(\slashed D_{B,A}+m)
\quad\text{ou}\quad
\operatorname{Pf}(\mathcal D).
$$

O sinal e a potência do determinante não seguem apenas da fatorização formal
de um operador bosônico de segunda ordem.

## 4. Status do operador de Dirac--Bismut

A Q28 define o operador espectral

$$
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iA_\mu
\right)
$$

e usa seu índice, kernel e decomposição APS.

Entretanto, a Q4 declara

$$
S_{\rm pert}
=
S_{\rm gauge}+S_{\rm spin}+S_{\rm gf+gh}
$$

como camada perturbativa auxiliar opcional, ausente da ação oficial e sem
papel ontológico fundamental.

Portanto,

$$
\boxed{
\slashed D_{B,A}
\text{ está definido espectralmente, mas ainda não foi derivado como bloco
da Hessiana oficial.}
}
$$

## 5. Limite da rota fermiônica

No estado atual:

$$
\boxed{
\mathcal S_{\rm GDQ}[g,f,\bar f]
\not\Rightarrow
\int\bar\psi(i\slashed D_{B,A}-m)\psi
}
$$

sem uma construção intermediária. Logo, $\Pi_{\mu\nu}^{(\tau)}$ é auditoria
da redução efetiva, não loop já derivado da ação oficial.

Isso não invalida Ward, $a_4$, $a_6$ ou a saturação. Também não constitui
obstrução geral à Q34: mostra apenas que o loop fermiônico pertence à tradução
efetiva externa.

## 6. Rota fundamental correta na GDQ

O loop fundamental da GDQ é construído diretamente da Hessiana geométrica:

$$
\boxed{
\Gamma_{\rm GDQ}^{(1)}
=
\frac12
\operatorname{Tr}_{\rm phys}
\log
\left(
\operatorname{Hess}\mathcal S_{\rm GDQ}
\right).
}
$$

O traço físico atua nas perturbações

$$
(\delta g,\delta f,\delta\bar f,\delta B)
$$

depois dos vínculos, modos zero e quociente de gauge. A conexão efetiva
$A_\mu$ deve aparecer como componente geométrica da métrica/fibração, não como
campo fundamental acrescentado.

A resposta de dois pontos correta é

$$
\boxed{
\Pi_{\mu\nu}^{\rm GDQ}
=
\frac{\delta^2\Gamma_{\rm GDQ}^{(1)}}
{\delta A_\mu\,\delta A_\nu}
\bigg|_{A=0},
}
$$

onde $A$ parametriza a deformação geométrica de Hopf ou da conexão interna.

Essa cadeia permanece inteiramente na GDQ:

$$
\boxed{
\mathcal S_{\rm GDQ}
\longrightarrow
\operatorname{Hess}\mathcal S_{\rm GDQ}
\longrightarrow
\det{}'H_{\rm geom}
\longrightarrow
\Pi_{\mu\nu}^{\rm GDQ}.
}
$$

Não são necessárias variáveis Grassmann para satisfazer 34-0.

## 7. Rotas efetivas posteriores

### Rota A — modo coletivo espinorial

Construir

$$
(\delta g,\delta f,\delta B)_{\rm físico}
\longrightarrow
\psi\in\Gamma(S\otimes E_{\rm int})
$$

preservando norma, domínio, quiralidade e bordo.

### Rota B — Pfaffiano geométrico

Demonstrar que a medida reduzida possui jacobiano antissimétrico

$$
\mathcal J_{\rm red}
=
\operatorname{Pf}(\mathcal D_{B,A}).
$$

### Rota C — reconstrução operacional

Usar Osterwalder--Schrader para obter o espaço de Hilbert e demonstrar que o
setor de circulação dupla é representado por Dirac--Bismut, incluindo
estatística e medida funcional.

Nenhuma rota pode acrescentar $S_{\rm spin}$ como novo termo fundamental sem
declarar mudança da ação.

## 8. Resultado

$$
\boxed{
\text{o loop fermiônico atual é auxiliar; Q34 deve ser fechada pelo loop
geométrico da Hessiana oficial.}
}
$$

A pendência correta é calcular ao menos um bloco completo do determinante
geométrico e sua resposta à conexão emergente. A emergência espinorial pode
ser estudada depois e não bloqueia Q34.

## 9. Referências

1. questão_4.md, Seção 11: classificação de $S_{\rm pert}$ como camada
   auxiliar opcional.
2. questão_28_final.md: operador de Dirac--Bismut e índice APS.
3. D. V. Vassilevich, “Heat kernel expansion: user's manual”,
   *Physics Reports* **388** (2003) 279--360,
   DOI: 10.1016/j.physrep.2003.09.002,
   arXiv:hep-th/0306138.
4. J.-M. Bismut, “A local index theorem for non Kähler manifolds”,
   *Mathematische Annalen* **284** (1989) 681--699.
