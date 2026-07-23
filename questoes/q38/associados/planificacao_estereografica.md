# Q38 — Planificação estereográfica e leitura local de \(G\)

## 1. Objetivo

Este documento trata do fator usado nos scripts Q38 como:

\[
\Pi_{1,\rm obs}
=
\frac{\Pi_{1,\rm bulk}}{\sqrt{\pi}}.
\]

A pergunta técnica é:

\[
\boxed{
\sqrt{\pi}\text{ é derivável como jacobiano/projeção entre }S^3
\text{ e o limite local plano?}
}
\]

O ponto central é separar:

1. \(G_{\rm bulk}\): acoplamento extraído no tecido cosmológico
   \(T^5\times S^3\);
2. \(G_{\rm obs}\): valor lido por um observador local quase plano.

---

## 2. Mapa estereográfico de \(S^3\)

Para uma \(3\)-esfera de raio \(R\), a projeção estereográfica sobre
\(\mathbb R^3\) produz a métrica conforme:

\[
ds^2_{S^3}
=
\Omega(r)^2
\left(
dr^2+r^2d\Omega_2^2
\right),
\]

com:

\[
\Omega(r)
=
\frac{2R^2}{R^2+r^2}.
\]

Logo o elemento de volume é:

\[
dV_{S^3}
=
\Omega(r)^3\,d^3x.
\]

Portanto, o jacobiano local é:

\[
J_{\rm stereo}(r)
=
\Omega(r)^3
=
\left(
\frac{2R^2}{R^2+r^2}
\right)^3.
\]

Conclusão imediata:

\[
\boxed{
\text{o jacobiano estereográfico puro não é uma constante.}
}
\]

Assim, um fator constante como \(\sqrt{\pi}\) só pode aparecer após uma média,
normalização espectral, projeção de modo ou escolha de observable.

---

## 3. Volume global versus volume local

O volume total de \(S^3\) é:

\[
\operatorname{Vol}(S^3_R)=2\pi^2R^3.
\]

Em coordenada polar \(\chi\):

\[
dV_{S^3}
=
R^3\sin^2\chi\,d\chi\,d\Omega_2,
\]

e:

\[
\int_0^\pi\sin^2\chi\,d\chi
=
\frac{\pi}{2}.
\]

Esse fator \(\pi/2\) já aparece nos scripts como normalização radial da
densidade esférica.

Mas a operação:

\[
\mathcal V_{\rm radial}
\mapsto
\frac{\mathcal V_{\rm radial}}{\pi/2}
\]

é uma normalização de média radial, não uma planificação observacional.

Portanto, se além disso se divide por \(\sqrt{\pi}\), é necessário explicar
qual projeção adicional está sendo realizada.

---

## 4. Três possibilidades para o fator \(\sqrt{\pi}\)

### 4.1 Possibilidade A — fator de jacobiano médio

Pode-se tentar definir:

\[
J_{\rm flat}
=
\left\langle
J_{\rm stereo}
\right\rangle_w
\]

com peso \(w\) dado pela própria medida GDQ:

\[
w(y,\tau)
\propto
e^{2A}
\mathcal U_*
\sqrt{q_*}.
\]

Então:

\[
J_{\rm flat}
=
\frac{
\int_\gamma d\tau\int_K
J_{\rm stereo}(y)
w(y,\tau)\,d^4y
}{
\int_\gamma d\tau\int_K
w(y,\tau)\,d^4y
}.
\]

Nesse caso, para justificar o script, seria preciso provar:

\[
J_{\rm flat}=\sqrt{\pi}.
\]

Status:

\[
\boxed{
\text{possível, mas ainda não demonstrado.}
}
\]

### 4.2 Possibilidade B — fator RMS de leitura radial

Como a gravidade é lida por fluxo/campo, não apenas por volume, o fator pode
vir de uma normalização quadrática:

\[
J_{\rm flat}^{1/2}
=
\left(
\frac{\int w_{\rm flat}^2}{\int w_{S^3}^2}
\right)^{1/2}.
\]

Nesse caso, \(\sqrt{\pi}\) seria um fator RMS, não um jacobiano de volume.

Isso é compatível com o fato de o acoplamento gravitacional entrar como
coeficiente quadrático da ação efetiva:

\[
C_R\int R[h]\sqrt{-h}.
\]

Status:

\[
\boxed{
\text{fisicamente plausível; precisa ser derivado da norma do modo gravitacional.}
}
\]

### 4.3 Possibilidade C — fator de canal/impedância já misturado

O fator \(\sqrt{\pi}\) pode estar compensando, na prática, uma combinação de:

1. projeção estereográfica;
2. impedância de Fano;
3. normalização radial \(\pi/2\);
4. passagem entre bulk cosmológico e canal plano.

Nesse caso, ele não deve ser mantido como “planificação pura”. Deve ser
decomposto:

\[
\sqrt{\pi}
=
J_{\rm stereo}^{\rm eff}
Z_{\rm Fano}^{\rm eff}
N_{\rm radial}^{\rm eff}.
\]

Status:

\[
\boxed{
\text{possível, mas exige reescrever o solver com fatores separados.}
}
\]

---

## 5. Consequência para o solver V2

O solver V2 usa a cadeia:

\[
V_{\rm eff}
\to
\Pi_{1,\rm bulk}
\to
\Pi_{1,\rm obs}
=
\Pi_{1,\rm bulk}/\sqrt{\pi}.
\]

Para deixá-lo rigoroso, a cadeia deve ser reescrita como:

\[
V_{\rm eff}^{\rm Ein}
\to
C_R^{\rm bulk}
\to
G_{\rm bulk}
\to
G_{\rm obs}
=
\mathcal P_{\rm flat}[G_{\rm bulk}],
\]

onde:

\[
\mathcal P_{\rm flat}
\]

é um operador geométrico de projeção, não apenas uma divisão escalar escolhida
após a comparação.

---

## 6. Critério de fechamento

Para fechar o fator de planificação, deve-se calcular um dos objetos abaixo.

### Critério 1 — jacobiano médio

\[
J_{\rm flat}
=
\frac{
\int_\gamma d\tau\int_K
J_{\rm stereo}(y)
e^{2A}\mathcal U_*\sqrt{q_*}\,d^4y
}{
\int_\gamma d\tau\int_K
e^{2A}\mathcal U_*\sqrt{q_*}\,d^4y
}
\]

e mostrar:

\[
J_{\rm flat}=\sqrt{\pi}.
\]

### Critério 2 — norma do modo gravitacional

Definir o modo gravitacional zero \(\psi_G(y)\) e calcular:

\[
N_G^{S^3}
=
\int_K
|\psi_G(y)|^2
e^{2A}\mathcal U_*\sqrt{q_*}\,d^4y.
\]

Depois comparar com a norma plana local:

\[
N_G^{\rm flat}.
\]

O fator de leitura seria:

\[
J_{\rm flat}
=
\left(
\frac{N_G^{S^3}}{N_G^{\rm flat}}
\right)^{1/2}.
\]

Se:

\[
J_{\rm flat}=\sqrt{\pi},
\]

então o fator do script está derivado.

### Critério 3 — complemento de Schur de contorno

Se o fator mistura planificação e impedância, calcular:

\[
Z_{\rm eff}
=
Z_0-J^\dagger K^{-1}J
\]

para o modo gravitacional de contorno. Então:

\[
J_{\rm flat}
=
Z_{\rm eff}^{-1}
\]

ou uma função simples dele.

---

## 7. Veredito atual

\[
\boxed{
\sqrt{\pi}\text{ ainda não está derivado.}
}
\]

Mas ele não deve ser descartado. Ele deve ser tratado como:

\[
\boxed{
\text{fator efetivo de projeção bulk}\to\text{observador local, a ser decomposto.}
}
\]

A rota mais limpa é pelo critério 2: norma do modo gravitacional. Isso liga
diretamente a planificação ao coeficiente quadrático \(C_R\), sem depender de
intuição visual da projeção estereográfica.

---

## 8. Próximo passo

O próximo documento deve atacar a decomposição de \(\chi_{\rm Fano}\), porque
o solver V2 usa um valor numérico conflitante:

\[
0.4791
\quad\text{versus}\quad
\frac{3\sqrt2}{5}\approx0.848528.
\]

Produto:

\[
\boxed{
\texttt{questoes/q38/associados/fano_impedancia_gravitacional.md}
}
\]

Objetivo:

1. decidir se \(\chi_{\rm Fano}\) é admitância, impedância ou fator de
   transmissão;
2. derivar sua entrada em \(\mathcal V_{\rm eff}^{(G)}\);
3. impedir que o fator de Fano seja usado como correção pós-ajuste.

Continuação criada:

\[
\boxed{
\texttt{questoes/q38/associados/fano\_impedancia\_gravitacional.md}
}
\]

Resultado importante:

\[
0.4791\approx\frac{3\sqrt2/5}{\sqrt{\pi}}.
\]

Logo, o solver V2 provavelmente misturou Fano e planificação no mesmo fator.
