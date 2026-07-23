# Adendo Q40 — Ansatz explícita para \(g_p\) e \(f_p\) no bulk bariônico

## 1. Objetivo

O adendo anterior reduziu a massa de bulk do próton a:

\[
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}d\mu
=
6\pi^5,
\]

desde que exista uma solução estacionária de bulk tal que:

\[
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}\,d^5\phi
=
d\mu_{T^5_{\rm trançado}}.
\]

Agora explicitamos uma ansatz mínima para \((g_p,f_p)\) em cada câmara
fundamental do domínio bariônico.

---

## 2. Princípio físico da ansatz

A decomposição da Q40 separa:

\[
\mathcal I_p
=
\mathcal I_p^{\rm bulk}
+
\mathcal I_p^{\partial}.
\]

Logo, o bulk deve representar apenas a célula inercial homogênea. As
singularidades, torções concentradas, holonomias e correções de garganta ficam
em:

\[
\mathcal I_p^{\partial}.
\]

Portanto, em cada câmara fundamental \(\mathcal F_a\), a ansatz de bulk deve
ser a mais simples possível:

1. métrica plana induzida;
2. potencial de Perelman constante;
3. medida uniforme;
4. torção nula no interior;
5. torção/holonomia concentrada nas identificações de fronteira.

Isso é compatível com a ideia:

\[
\boxed{
\text{volume = bulk homogêneo;}
\qquad
\text{torção = fronteira/transgressão.}
}
\]

---

## 3. Câmara fundamental

Cada folha/estômato do bárion possui uma câmara:

\[
\mathcal F_a
=
[0,2\pi]_{\phi_1}
\times
[0,\pi]_{\phi_2}
\times
[0,\pi]_{\phi_3}
\times
[0,\pi]_{\phi_4}
\times
[0,\pi]_{\phi_5}.
\]

O domínio trançado é a união de três folhas:

\[
T^5_{\rm trançado}
=
\bigsqcup_{a=1}^{3}\mathcal F_a.
\]

O volume de cada câmara é:

\[
\operatorname{Vol}(\mathcal F_a)
=
2\pi^5.
\]

Logo:

\[
\operatorname{Vol}(T^5_{\rm trançado})
=
3(2\pi^5)
=
6\pi^5.
\]

---

## 4. Métrica de bulk

Em cada câmara, adotamos a métrica induzida:

\[
\boxed{
g_p^{(a)}
=
\sum_{A=1}^{5}d\phi_A^2.
}
\]

Em componentes:

\[
\boxed{
(g_p^{(a)})_{AB}
=
\delta_{AB}.
}
\]

Assim:

\[
\sqrt{\det g_p^{(a)}}=1.
\]

Essa métrica não afirma que o bulk oficial da GDQ seja \(T^5\). O bulk oficial
continua sendo o domínio Hermitiano da ação. Aqui \(T^5_{\rm trançado}\) é a
subvariedade/ciclo interno efetivo usado para a calibração bariônica de massa.

---

## 5. Potencial de Perelman no bulk

Escolhemos:

\[
\boxed{
f_p^{(a)}=f_0=\text{constante}.
}
\]

Então:

\[
\nabla_A f_p=0,
\]

\[
\nabla_A\nabla_B f_p=0.
\]

A densidade:

\[
\rho_p=e^{-f_0}
\]

é constante dentro da câmara.

Como a energia está sendo expressa em unidades eletrônicas, a constante é
absorvida na normalização:

\[
\Theta_p\,\mathcal U_p=1.
\]

Equivalentemente, pode-se escolher:

\[
\boxed{
\mathcal U_p=e^{-f_0}=1
}
\]

na medida reduzida, deixando qualquer fator global de densidade incorporado à
calibração \(E_0=M_ec^2\).

---

## 6. Verificação da equação de solíton

A equação de bulk que precisa ser satisfeita é:

\[
\mathcal R_{AB}
+\nabla_A\nabla_B f
=
\lambda_B g_{AB}.
\]

Para a métrica plana:

\[
\mathcal R_{AB}=0.
\]

Para \(f=f_0\) constante:

\[
\nabla_A\nabla_B f=0.
\]

Logo:

\[
0=\lambda_B \delta_{AB}.
\]

Portanto:

\[
\boxed{
\lambda_B=0.
}
\]

E a equação é satisfeita:

\[
\boxed{
\mathcal R_{AB}
+\nabla_A\nabla_B f
=
0
=
\lambda_B g_{AB}.
}
\]

Isso mostra que cada câmara fundamental é um solíton estacionário plano de
bulk. O conteúdo físico não trivial do bárion não está no interior homogêneo
da câmara, mas nas identificações e transgressões de fronteira.

---

## 7. Medida reduzida

Com:

\[
\sqrt{\det g_p^{(a)}}=1,
\qquad
\mathcal U_p=1,
\qquad
\Theta_p=1,
\]

temos:

\[
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}\,d^5\phi
=
d^5\phi.
\]

Assim, em uma câmara:

\[
\mathcal I_{\mathcal F}^{\rm bulk}
=
\int_{\mathcal F}d^5\phi
=
2\pi^5.
\]

Em três câmaras:

\[
\mathcal I_p^{\rm bulk}
=
\sum_{a=1}^{3}
\int_{\mathcal F_a}d^5\phi
=
3(2\pi^5)
=
\boxed{6\pi^5}.
\]

---

## 8. Onde entra a torção?

Nesta ansatz:

\[
B_{ABC}=0
\quad
\text{no interior de cada }\mathcal F_a.
\]

Mas:

\[
B\neq0
\quad
\text{nas identificações/fronteiras dos estômatos.}
\]

Isso é exatamente a separação necessária:

\[
\boxed{
\text{bulk plano homogêneo}
\Rightarrow
6\pi^5;
}
\]

\[
\boxed{
\text{torção de fronteira}
\Rightarrow
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
\]

A torção não precisa contaminar a densidade de volume. Ela atua por
transgressão:

\[
\int_{\Sigma^\circ}d\mathcal T_{\rm top}
=
\int_{\partial\Sigma^\circ}\mathcal T_{\rm top}.
\]

---

## 9. Status da ansatz

Esta ansatz fecha a verificação local de bulk:

\[
\boxed{
g_{AB}=\delta_{AB},
\qquad
f=f_0,
\qquad
\lambda_B=0.
}
\]

Ela prova que existe uma solução-modelo por câmara que satisfaz a equação de
solíton no interior:

\[
\mathcal R_{AB}+\nabla_A\nabla_Bf=0.
\]

Ela também mostra que:

\[
\boxed{
\mathcal I_p^{\rm bulk}=6\pi^5.
}
\]

O que ainda falta não é mais a parte volumétrica, mas a cola global:

1. especificar as identificações entre as três câmaras;
2. escrever a conexão de Bismut/Cartan nas fronteiras;
3. calcular a transgressão torsional;
4. obter o termo:

   \[
   \alpha
   \left(
   \frac{3\pi}{2}
   +
   \frac{3}{4\pi^3}
   \right).
   \]

---

## 10. Conclusão

A solução de bulk mínima da Q40 é:

\[
\boxed{
\mathcal F_a:
\quad
g_p^{(a)}=\delta_{AB}d\phi^A d\phi^B,
\qquad
f_p^{(a)}=f_0,
\qquad
B^{(a)}=0.
}
\]

Ela satisfaz:

\[
\boxed{
\mathcal R_{AB}+\nabla_A\nabla_Bf=0.
}
\]

E produz:

\[
\boxed{
\mathcal I_p^{\rm bulk}
=
\sum_{a=1}^{3}\operatorname{Vol}(\mathcal F_a)
=
6\pi^5.
}
\]

Portanto, a parte de volume da massa bariônica fica fechada no nível da
ansatz estacionária de bulk. A próxima falta real é a derivação do termo de
superfície torsional.
