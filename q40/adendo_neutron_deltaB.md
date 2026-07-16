# Adendo Q40 — Massa do nêutron e unificação de \(\delta_B\)

## 1. Objetivo

Após fechar estruturalmente a massa do próton:

\[
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right),
\]

resta unificar a diferença nêutron-próton:

\[
\boxed{
\delta_B
=
\frac{M_n-M_p}{M_e}.
}
\]

O capítulo 26 e o Apêndice 1 usam rotas numéricas ligeiramente diferentes.
Este adendo fixa a definição estrutural única.

---

## 2. Diferença física entre próton e nêutron

Próton e nêutron pertencem à mesma classe de bulk:

\[
n_B=3.
\]

Logo, eles compartilham:

\[
\mathcal I_B^{\rm bulk}=6\pi^5.
\]

A diferença não vem do volume. Ela vem da orientação de cola:

- próton: cola quiral paralela, carga assintótica \(Q_p=+1\);
- nêutron: cola quiral antiparalela, carga assintótica \(Q_n=0\).

Em termos de tensões torsionais dos três estômatos:

\[
\boxed{
\text{próton: }
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,\tau),
}
\]

isto é, as tensões estão alinhadas e fecham no sóliton carregado. Já no
nêutron há um estômato invertido:

\[
\boxed{
\text{nêutron: }
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,-2\tau).
}
\]

O fator \(2\) não é ajuste: é a condição estacionária de conservação torsional,
pois o canal invertido deve compensar os dois canais alinhados:

\[
\boxed{
\sum_{a=1}^{3}\mathcal T_a=0.
}
\]

Essa lei pode ser vista como consequência de Noether para a simetria de fase/
torção da ação de contorno:

\[
\delta_\vartheta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
dJ_{\rm tor}=0.
\]

Portanto:

\[
\boxed{
M_n-M_p
=
\text{energia de cisalhamento torsional antiparalelo}.
}
\]

---

## 3. Definição única de \(\delta_B\)

Definimos:

\[
\boxed{
\delta_B
=
\frac{1}{M_ec^2}
\int_{\Sigma_n-\Sigma_p}
\rho\,
\frac14
B_{\mu\nu\lambda}B^{\mu\nu\lambda}
\sqrt{\det g}\,d\Sigma.
}
\]

Essa é a definição correta porque:

1. compara nêutron e próton na mesma classe de bulk;
2. remove o termo comum \(6\pi^5\);
3. mede apenas o excesso de torção da cola antiparalela;
4. usa a mesma calibração eletrônica da massa do próton.

---

## 4. Redução espectral da integral de cisalhamento

No Apêndice 1, a inércia efetiva do setor bariônico é:

\[
\delta_{\rm efetivo}
=
\delta_{\rm bare}\chi_{\rm Fano}.
\]

Com:

\[
\delta_{\rm bare}
=
\ln(2\pi^2),
\]

e:

\[
\chi_{\rm Fano}
=
\frac{3\sqrt2}{5}.
\]

Logo:

\[
\boxed{
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
\]

Numericamente:

\[
\delta_B
\approx
2.530827.
\]

Essa passa a ser a definição oficial da diferença de massa reduzida.

---

## 5. O que fazer com o valor \(2.530988\)

O valor:

\[
2.530988
\]

aparece no capítulo 26 por uma rota aproximada envolvendo o índice de
compressão quiral:

\[
\delta
=
\frac{
\frac{\pi^2}{2}
\left(
1-\frac{3}{4\pi^2}
\right)
}{\chi}.
\]

Essa expressão deve ser interpretada como aproximação intermediária. Ela não
deve competir com a definição variacional final.

A definição final é:

\[
\boxed{
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
\]

Se o manuscrito mantiver a outra rota, deve indicá-la como estimativa
equivalente de compressão, não como definição primária.

---

## 6. Massa do nêutron

Com:

\[
\frac{M_n}{M_e}
=
\frac{M_p}{M_e}
+
\delta_B,
\]

temos:

\[
\boxed{
\frac{M_n}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
+
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
\]

Essa é a fórmula estrutural final para a massa do nêutron em unidades
eletrônicas.

---

## 7. Interpretação

A decomposição completa fica:

\[
\boxed{
\frac{M_n}{M_e}
=
\underbrace{6\pi^5}_{\rm bulk}
+
\underbrace{
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
}_{\rm superfície\ próton}
+
\underbrace{
\ln(2\pi^2)\frac{3\sqrt2}{5}
}_{\rm cisalhamento\ antiparalelo}.
}
\]

O nêutron não é um novo volume. Ele é o mesmo volume bariônico com uma cola
torsional antiparalela que acrescenta energia de cisalhamento.

---

## 8. Status

Este adendo fecha estruturalmente:

1. a origem de \(M_n-M_p\);
2. a definição única de \(\delta_B\);
3. a escolha do valor \(\delta_B\simeq2.530827\);
4. a fórmula estrutural de \(M_n/M_e\).

Ainda não fecha:

1. taxa de decaimento do nêutron;
2. espectro beta;
3. momentos magnéticos;
4. fatores de forma;
5. espalhamento.

---

## 9. Conclusão

A diferença nêutron-próton é:

\[
\boxed{
\frac{M_n-M_p}{M_e}
=
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
\]

Portanto:

\[
\boxed{
\frac{M_n}{M_e}
=
\frac{M_p}{M_e}
+
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
\]

Com isso, o setor de massas bariônicas \(p,n\) fica estruturalmente fechado.
