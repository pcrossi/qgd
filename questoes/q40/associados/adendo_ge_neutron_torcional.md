# Q40 — Adendo: derivação torsional de \(G_E^n\)

## 1. Problema

O nêutron tem carga total nula:

\[
G_E^n(0)=0.
\]

Mas sua densidade elétrica efetiva não precisa ser localmente nula. Na GDQ, o
nêutron é o mesmo bulk bariônico do próton com cola torsional antiparalela.
Essa cola desloca radialmente as contribuições efetivas positiva e negativa.

O objetivo é escrever \(G_E^n\) sem usar o raio experimental do nêutron como
entrada.

---

## 2. Energia de cisalhamento como amplitude de polarização

A diferença nêutron-próton é:

\[
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
\]

Ela mede o excesso de energia de cisalhamento torsional antiparalelo. A
projeção elétrica desse cisalhamento deve vir multiplicada pela admitância
eletro-geométrica \(\alpha\). Portanto, a amplitude líder da polarização é:

\[
\boxed{
A_n=\alpha\delta_B\mathcal P_E.
}
\]

No fechamento mínimo:

\[
\boxed{
\mathcal P_E=1,
\qquad
A_n=\alpha\delta_B.
}
\]

Esse coeficiente não é ajustado ao raio do nêutron; ele vem da mesma estrutura
que já fixa a diferença de massa e o momento magnético.

---

## 3. Deslocamento angular produzido pela cola

A cola antiparalela separa as duas componentes elétricas efetivas por uma
escala angular de ordem eletro-geométrica:

\[
\boxed{
\chi_\pm
=
\epsilon_{\rm eff}
\left(1\pm\frac{\alpha_{\rm tor}}{2}\right).
}
\]

No fechamento líder:

\[
\boxed{
\alpha_{\rm tor}=\alpha.
}
\]

A casca negativa é a mais periférica:

\[
\chi_->\chi_+.
\]

Isso força o sinal negativo do raio quadrático elétrico.

---

## 4. Densidade elétrica mínima

A densidade efetiva é:

\[
\boxed{
\rho_E^n(\chi)d\chi
=
A_n[
\delta(\chi-\chi_+)
-
\delta(\chi-\chi_-)
]d\chi.
}
\]

Logo:

\[
\int\rho_E^n d\chi
=
A_n(1-1)=0.
\]

Portanto:

\[
\boxed{
G_E^n(0)=0.
}
\]

---

## 5. Fator de forma elétrico do nêutron

A coordenada radial eletromagnética observável é:

\[
r_{\rm obs}(\chi)=C_rR_B\chi.
\]

Então:

\[
\boxed{
G_E^n(q^2)
=
A_n[
j_0(qC_rR_B\chi_+)
-
j_0(qC_rR_B\chi_-)
].
}
\]

Substituindo o fechamento líder:

\[
\boxed{
G_E^n(q^2)
=
\alpha\delta_B
\left[
j_0(qr_p(1-\alpha/2))
-
j_0(qr_p(1+\alpha/2))
\right],
}
\]

pois:

\[
r_p=C_rR_B\epsilon_{\rm eff}.
\]

---

## 6. Raio quadrático elétrico

Expandindo:

\[
j_0(qr)=1-\frac{q^2r^2}{6}+O(q^4).
\]

Então:

\[
G_E^n(q^2)
=
-\frac{q^2}{6}
A_n(r_+^2-r_-^2)
+O(q^4).
\]

Assim:

\[
\boxed{
\langle r_n^2\rangle
=
A_n(r_+^2-r_-^2).
}
\]

No fechamento líder:

\[
r_\pm=r_p(1\pm\alpha/2).
\]

Logo:

\[
r_+^2-r_-^2
=
r_p^2[
(1-\alpha/2)^2-(1+\alpha/2)^2
]
=
-2\alpha r_p^2.
\]

Portanto:

\[
\boxed{
\langle r_n^2\rangle_{\rm líder}
=
-2\alpha^2\delta_B r_p^2.
}
\]

Essa é uma previsão líder de polarização de borda. Ela fixa corretamente:

1. carga total nula;
2. sinal negativo;
3. escala eletro-geométrica controlada por \(\alpha^2\delta_B\);
4. dependência no raio de superfície do próton.

---

## 7. Por que isso ainda não é o \(G_E^n\) fenomenológico completo

O fechamento por duas cascas é o termo líder. Ele representa apenas a separação
mínima induzida pela cola antiparalela.

O \(G_E^n\) completo exige substituir:

\[
\delta(\chi-\chi_\pm)
\longrightarrow
w_\pm^{\rm tor}(\chi),
\]

onde \(w_\pm^{\rm tor}\) vêm do perfil torsional \(H_n(\chi)\):

\[
\rho_E^n(\chi)
\propto
\alpha\,
\frac{d}{d\chi}
\left(e^{-f_n(\chi)}H_n(\chi)\right).
\]

Essa etapa pertence ao programa fenomenológico de espalhamento, não ao
fechamento estrutural da Q40.

---

## 8. Fechamento estendido: cola dupla torsional

O fechamento líder mínimo subestima a polarização elétrica do nêutron porque
mantém apenas a admitância eletro-geométrica local \(\alpha\delta_B\). Para o
fator de forma elétrico completo de borda, a amplitude relevante é a projeção
torsional espacial que já aparece no momento magnético:

\[
\boxed{
A_n^{(2)}
=
|\mu_n|
=
\frac34\delta_B
\left(
1+\alpha\frac{3\sqrt2}{4}
\right).
}
\]

A separação efetiva das duas interfaces antiparalelas não é apenas \(\alpha\).
Ela recebe o comprimento global da cola:

\[
\boxed{
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2).
}
\]

Logo:

\[
\boxed{
r_+^{(2)}
=
r_p
\left(
1-\frac{\alpha_{\rm tor}^{(2)}}{2}
\right),
\qquad
r_-^{(2)}
=
r_p
\left(
1+\frac{\alpha_{\rm tor}^{(2)}}{2}
\right),
}
\]

com a componente positiva na posição interna e a componente negativa na posição
externa. O fator de forma estendido é:

\[
\boxed{
G_{E,\rm ext}^n(q^2)
=
|\mu_n|
\left[
j_0(qr_+^{(2)})
-
j_0(qr_-^{(2)})
\right].
}
\]

Assim:

\[
\boxed{
\left\langle r_n^2\right\rangle_{\rm ext}
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2
\approx
-0.11772\,{\rm fm}^2.
}
\]

Esse valor não usa o raio elétrico experimental do nêutron como entrada. Ele
usa apenas \(\mu_n\), \(r_p\), \(\alpha\) e \(\ln(2\pi^2)\), todos já fixados
em outros observáveis da Q40.

---

## 9. Perfil suave por núcleo de calor de superfície

Para remover a idealização de cascas delta, substituímos:

\[
\delta(\chi-\chi_\pm)
\longrightarrow
K_\sigma(\xi,\xi_\pm),
\]

onde:

\[
K_\sigma(\xi,\xi_0)
=
\frac{1}{\sqrt{2\pi}\sigma_r}
\exp\left[
-\frac{(\xi-\xi_0)^2}{2\sigma_r^2}
\right],
\qquad
\int_{-\infty}^{+\infty}K_\sigma d\xi=1.
\]

Aqui:

\[
\xi=r-r_p=C_rR_B(\chi-\epsilon_{\rm eff}).
\]

Essa é uma coordenada local da camada de superfície. Ela é necessária porque a
componente positiva fica ligeiramente no lado interno do estômato, enquanto a
componente negativa fica no lado externo. Tratar essa camada como densidade de
bulk em \([\epsilon_{\rm eff},\pi]\) introduziria um corte artificial.

A largura líder é:

\[
\boxed{
\sigma_\chi
=
\frac12\epsilon_{\rm eff}\alpha_{\rm tor}^{(2)},
\qquad
\sigma_r
=
C_rR_B\sigma_\chi
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
}
\]

O fator de forma suave fica:

\[
\boxed{
G_{E,\rm suave}^n(q^2)
=
|\mu_n|
\int_{-\infty}^{+\infty}
\left[
K_\sigma(\xi,\xi_+^{(2)})
-
K_\sigma(\xi,\xi_-^{(2)})
\right]
j_0(q(r_p+\xi))\,d\xi .
}
\]

Esse perfil preserva:

\[
G_{E,\rm suave}^n(0)=0,
\]

e preserva a inclinação de baixa energia porque as duas larguras são iguais e
a variância comum cancela na diferença:

\[
\left\langle r_n^2\right\rangle_{\rm suave}
=
|\mu_n|(r_+^2-r_-^2)
\]

no modelo local de superfície, pois a variância comum das duas gaussianas se
cancela exatamente na diferença.

---

## 10. Status

Com o fechamento estendido e o perfil suave, \(G_E^n\) está resolvido no nível
estrutural de baixa energia:

1. carga total nula;
2. sinal negativo;
3. escala correta do raio quadrático;
4. curva suave líder em \(q^2\).

O perfil \(H_n(\chi)\) foi resolvido no adendo variacional como núcleo de calor
de Perelman na camada de superfície. A pendência restante é comparar a curva
inteira de espalhamento com dados e acrescentar correções de sonda/magnetização,
não obter a normalização ou a inclinação.
