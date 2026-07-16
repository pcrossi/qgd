# Q34 — Teste quantitativo de kernels geométricos covariantes

## 1. Pergunta

O enunciado 34-0 exige independência do regulador. Na GDQ é necessário
distinguir:

1. independência da identidade de calibre;
2. independência numérica dos coeficientes efetivos.

Se o kernel é uma função do operador físico,

$$
K(H),
$$

então

$$
H[A^g]=g^{-1}H[A]g
\quad\Longrightarrow\quad
K(H[A^g])=g^{-1}K(H[A])g.
$$

Logo, o traço é gauge-invariante para toda função admissível. Isso não implica
que duas funções diferentes representem a mesma resolução física.

## 2. Família testada

Defina

$$
\mathcal E_K(z)
=
\int_1^\infty\frac{du}{u}K(zu).
$$

Foram usados três perfis positivos e inteiros:

### Kernel canônico

$$
K_0(z)=e^{-z},
\qquad
\mathcal E_0(z)=E_1(z).
$$

### Mistura convexa

$$
K_{\rm mix}(z)
=
\frac12e^{-z}
+\frac12e^{-2z},
$$

$$
\mathcal E_{\rm mix}(z)
=
\frac12E_1(z)
+\frac12E_1(2z).
$$

### Deformação inteira

$$
K_+(z)=e^{-z}(1+z),
$$

$$
\mathcal E_+(z)=E_1(z)+e^{-z}.
$$

Todos transformam por conjugação quando aplicados a $H_n[A]$.

## 3. Polarização

Para cada perfil:

$$
\Pi_K(Q^2)
=
\frac{q_n^2}{16\pi^2}
\int_0^1dx\,(1-2x)^2
\left[
\mathcal E_K(\eta)
-\mathcal E_K\!\left(
\eta+s_0x(1-x)Q^2
\right)
\right].
$$

A subtração fornece

$$
\Pi_K(0)=0.
$$

O tensor é sempre

$$
\Pi_{\mu\nu}^K
=
(Q_\mu Q_\nu-Q^2\delta_{\mu\nu})\Pi_K,
$$

portanto

$$
\boxed{Q^\mu\Pi_{\mu\nu}^K=0}
$$

para os três kernels.

## 4. Limite ultravioleta

Cada perfil satura em

$$
\boxed{
\Pi_K(\infty)
=
\frac{q_n^2}{48\pi^2}\mathcal E_K(\eta).
}
$$

Os limites são finitos, mas não idênticos. Isso é esperado: os perfis
representam resoluções espectrais diferentes.

## 5. Critério de independência

O teste sustenta:

$$
\boxed{
\text{Ward, ausência de massa e finitude são independentes do kernel
covariante.}
}
$$

Mas exclui a afirmação mais forte:

$$
\boxed{
\text{os coeficientes numéricos não são universais sob troca arbitrária de
kernel.}
}
$$

Assim, na GDQ o heat kernel canônico não deve ser chamado de regulador
arbitrário. Ele precisa ser selecionado como o semigrupo do operador físico:

$$
K_0(sH)=e^{-sH}.
$$

## 6. Consequência para 34-0

A independência relevante para calibre está demonstrada: toda função
covariante preserva Ward. A independência numérica completa não existe e não
deve ser prometida.

O fechamento correto é:

$$
\boxed{
\text{Q34 responde à independência do regulador como independência de calibre,
não como igualdade entre resoluções físicas distintas.}
}
$$

## 7. Referência

D. V. Vassilevich, “Heat kernel expansion: user's manual”,
*Physics Reports* **388** (2003) 279--360,
DOI: 10.1016/j.physrep.2003.09.002,
arXiv:hep-th/0306138. A referência sustenta o uso de funções do operador de
tipo Laplace e a expansão por heat kernel.
