# Q28 — Bloco 4 — Classes características e normalização da hipercarga

## 1. Objetivo

Este bloco reduz a pendência do índice da Q28 a dados topológicos explícitos do
fibrado interno:

\[
E_{\rm int}=E_C\oplus E_W\oplus L_Y.
\]

O problema é determinar:

\[
c_2(E_C),\quad c_3(E_C),\quad c_2(E_W),\quad c_1(L_Y),
\]

e a normalização global de \(Y\).

---

## 2. Classes do setor de cor

O setor de cor é:

\[
E_C\simeq \mathbb C^3,
\qquad
G_C=SU(3).
\]

Como \(E_C\) é um fibrado \(SU(3)\):

\[
\boxed{
c_1(E_C)=0.
}
\]

O caráter de Chern é:

\[
\operatorname{ch}(E_C)
=
3
-c_2(E_C)
+\frac12c_3(E_C)
+\cdots.
\]

O terceiro caráter:

\[
c_3(E_C)
\]

é o dado que controla a assimetria quiral entre \(3\) e \(\bar3\) quando
acoplado ao operador de Dirac.

Na GDQ, a interpretação é:

\[
\boxed{
c_3(E_C)
\leftrightarrow
\text{orientação global das três câmaras/estômatos de cor.}
}
\]

---

## 3. Classes do setor fraco

O setor fraco é:

\[
E_W\simeq \mathbb C^2,
\qquad
G_W=SU(2)_L.
\]

Como \(E_W\) é um fibrado \(SU(2)\):

\[
\boxed{
c_1(E_W)=0.
}
\]

O caráter de Chern é:

\[
\operatorname{ch}(E_W)
=
2
-c_2(E_W)
+\cdots.
\]

O dado:

\[
c_2(E_W)
\]

controla o número de dubletos quirais e a possível contribuição à anomalia
global de Witten.

Na GDQ:

\[
\boxed{
c_2(E_W)
\leftrightarrow
\text{classe da circulação/Hopf quiral de posto 2.}
}
\]

---

## 4. Linha de hipercarga

A hipercarga vem de:

\[
L_Y\to N,
\qquad
G_Y=U(1)_Y.
\]

Definimos:

\[
y=c_1(L_Y).
\]

Para peso \(q\):

\[
\operatorname{ch}(L_Y^q)=e^{qy}.
\]

Logo:

\[
\operatorname{ch}(L_Y^q)
=
1+qy+\frac12q^2y^2+\frac16q^3y^3+\cdots.
\]

As potências \(q\) são as hipercargas:

\[
q=Y.
\]

O ponto importante é que \(q\) pode ser fracionário localmente, desde que o
fibrado total seja bem definido globalmente pelo quociente \(\mathbb Z_6\).

---

## 5. Quociente global e quantização de \(Y\)

O grupo global é:

\[
G_{\rm SM}^{\rm global}
=
\frac{SU(3)\times SU(2)\times U(1)_Y}{\mathbb Z_6}.
\]

Tome os centros:

\[
z_3=e^{2\pi i/3}\in Z(SU(3)),
\qquad
z_2=-1\in Z(SU(2)).
\]

O gerador de \(\mathbb Z_6\) pode ser escrito como:

\[
\zeta=
\left(
e^{2\pi i/3},
-1,
e^{i\pi Y_0}
\right),
\]

com normalização \(Y_0=1\) na convenção:

\[
Q=T_3+Y.
\]

Uma representação \((R_3,R_2)_Y\) é bem definida se:

\[
\boxed{
z_3^{t(R_3)}
z_2^{p(R_2)}
e^{i2\pi Y}
=1.
}
\]

Aqui:

1. \(t(R_3)\in\{0,\pm1\}\) é a trialidade de cor;
2. \(p(R_2)=0\) para singlete e \(1\) para dubleto;
3. \(Y\) é a hipercarga na convenção \(Q=T_3+Y\).

Essa condição fixa \(Y\) módulo inteiros para cada tipo de representação.

---

## 6. Solução para uma geração

Aplicando a condição global e exigindo cargas elétricas observáveis:

\[
Q=T_3+Y,
\]

obtém-se a família mínima:

| Campo | \(t(R_3)\) | \(p(R_2)\) | \(Y\) |
|---|---:|---:|---:|
| \(Q_L\) | \(1\) | \(1\) | \(1/6\) |
| \(u_R^c\) | \(-1\) | \(0\) | \(-2/3\) |
| \(d_R^c\) | \(-1\) | \(0\) | \(1/3\) |
| \(L_L\) | \(0\) | \(1\) | \(-1/2\) |
| \(e_R^c\) | \(0\) | \(0\) | \(1\) |
| \(\nu_R^c\) opcional | \(0\) | \(0\) | \(0\) |

Portanto, as hipercargas são consequência de três exigências:

1. representação global bem definida no quociente \(\mathbb Z_6\);
2. relação geométrica de carga:
   \[
   Q=T_3+Y;
   \]
3. neutralidade/carga inteira dos estados compostos observáveis.

---

## 7. Caráter de Chern da geração

Formalmente, uma geração pode ser escrita como:

\[
\mathcal E_{\rm gen}
=
(E_C\otimes E_W\otimes L_Y^{1/6})
\oplus
(E_C^*\otimes L_Y^{-2/3})
\oplus
(E_C^*\otimes L_Y^{1/3})
\oplus
(E_W\otimes L_Y^{-1/2})
\oplus
L_Y.
\]

Logo:

\[
\operatorname{ch}(\mathcal E_{\rm gen})
=
\operatorname{ch}(E_C)\operatorname{ch}(E_W)e^{y/6}
+\operatorname{ch}(E_C^*)e^{-2y/3}
+\operatorname{ch}(E_C^*)e^{y/3}
+\operatorname{ch}(E_W)e^{-y/2}
+e^y.
\]

Essa expressão é o dado que deve entrar no índice.

---

## 8. Cancelamento topológico das anomalias

As anomalias são os termos de grau seis do caráter de Chern efetivo.

Para a geração acima:

\[
\left[\operatorname{ch}(\mathcal E_{\rm gen})\right]_{6}
\]

tem coeficientes proporcionais às somas:

\[
[SU(3)]^2U(1),\quad
[SU(2)]^2U(1),\quad
[U(1)]^3,\quad
\text{grav}^2U(1).
\]

Como essas somas foram calculadas em `q28/espectro_hipercarga_anomalias.md` e
se anulam, temos:

\[
\boxed{
\left[\operatorname{ch}(\mathcal E_{\rm gen})\right]_{\rm anom}=0.
}
\]

Interpretação GDQ:

\[
\boxed{
\text{o espectro de uma geração é exatamente a combinação que torna a cola quântica global consistente.}
}
\]

---

## 9. Índice com três gerações

Com a contagem topológica:

\[
N_{\rm ger}=3,
\]

o fibrado total de matéria é:

\[
\mathcal E_{\rm matter}
=
\mathbb C^3_{\rm gen}
\otimes
\mathcal E_{\rm gen}.
\]

Então:

\[
\operatorname{ch}(\mathcal E_{\rm matter})
=
3\,\operatorname{ch}(\mathcal E_{\rm gen}).
\]

O índice esperado é:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
\int_{\mathcal I}
\widehat A(T\mathcal I)
\,3\,\operatorname{ch}(\mathcal E_{\rm gen})
+
\eta_{\partial}.
}
\]

Se a condição APS dos estômatos seleciona os três setores geracionais estáveis,
então:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
3\,\mathcal E_{\rm gen}.
}
\]

---

## 10. O que este bloco fecha

Este bloco fecha estruturalmente:

1. a forma das classes características relevantes;
2. a origem global das hipercargas;
3. a expressão de \(\mathcal E_{\rm gen}\) como fibrado;
4. o cancelamento de anomalias como cancelamento do termo anômalo do caráter de
   Chern;
5. a incorporação do fator de três gerações no índice.

---

## 11. O que ainda falta

Ainda falta calcular geometricamente, no background oficial da GDQ:

1. os valores integrais concretos de \(c_2(E_C),c_3(E_C),c_2(E_W),y=c_1(L_Y)\);
2. o termo de borda \(\eta_{\partial}\);
3. a projeção quiral \(P_L\) induzida por torção;
4. as normas que geram \(g_s,g,g'\).

Status:

\[
\boxed{
\text{hipercarga e classes características foram estruturadas; resta avaliação topológica concreta.}
}
