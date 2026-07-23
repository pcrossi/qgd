# Adendo Q40 — Cola global e termo de superfície torsional

## 1. Objetivo

Os adendos anteriores fecharam a parte de bulk:

\[
\mathcal I_p^{\rm bulk}=6\pi^5.
\]

Falta agora justificar o termo de superfície:

\[
\boxed{
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
\]

Este adendo fornece a estrutura de cola global das três câmaras bariônicas e a
interpretação variacional da torção como termo de superfície.

---

## 2. Três câmaras e a cobertura bariônica

O domínio de bulk foi escrito como:

\[
T^5_{\rm trançado}
=
\bigsqcup_{a=1}^{3}\mathcal F_a,
\]

com:

\[
\operatorname{Vol}(\mathcal F_a)=2\pi^5.
\]

Cada câmara \(\mathcal F_a\) representa uma folha associada a um estômato. O
bárion físico não é a soma desconexa dessas folhas. Ele é obtido pela
identificação de suas fronteiras internas por mapas de transição:

\[
\boxed{
\Psi_{ab}:\partial\mathcal F_a\to\partial\mathcal F_b.
}
\]

Esses mapas carregam a holonomia que transforma a união desconexa em um nó
bariônico.

---

## 3. Dados de cola

Definimos os dados de cola por:

\[
\mathfrak G_p
=
\{\,\mathcal F_a,\Psi_{ab},\mathcal A_{ab},B_{ab}\,\}_{a,b=1}^{3},
\]

onde:

1. \(\mathcal F_a\) são as três câmaras planas de bulk;
2. \(\Psi_{ab}\) são as identificações de fronteira;
3. \(\mathcal A_{ab}\) é a conexão de Bismut/Chern induzida na interface;
4. \(B_{ab}\) é a torção de Cartan localizada na cola.

No interior:

\[
B^{(a)}=0.
\]

Nas interfaces:

\[
B_{ab}\neq0.
\]

Portanto:

\[
\boxed{
\text{a torção não altera o volume de bulk; ela vive na cola.}
}
\]

---

## 4. Termo de transgressão

A diferença entre duas conexões em câmaras vizinhas produz uma forma de
transgressão:

\[
\mathcal T_{ab}
=
\operatorname{CS}(\mathcal A_b)
-
\operatorname{CS}(\mathcal A_a)
-
d\,Q(\mathcal A_a,\mathcal A_b).
\]

De modo esquemático:

\[
d\mathcal T_{ab}
=
\operatorname{Tr}(R_b\wedge R_b)
-
\operatorname{Tr}(R_a\wedge R_a).
\]

Ao integrar sobre o domínio regularizado:

\[
\int_{\Sigma_p^\circ}d\mathcal T
=
\int_{\partial\Sigma_p^\circ}\mathcal T.
\]

Assim:

\[
\boxed{
\mathcal I_p^{\partial}
=
\alpha
\int_{\partial\Sigma_p^\circ}
\mathcal T_{\rm eff}.
}
\]

O fator \(\alpha\) entra como admitância eletro-geométrica da fronteira: ele
converte holonomia torsional em energia inercial observável na unidade
eletrônica.

---

## 5. Parte Chern--Simons: \(3\pi/2\)

Cada estômato carrega uma rotação fundamental de meia-volta na fibra de fase:

\[
\Delta\theta_a=\frac{\pi}{2}.
\]

Essa é a mesma estrutura que apareceu repetidamente na teoria: spin como
circulação/holonomia de meia unidade. Para três estômatos:

\[
\sum_{a=1}^{3}\Delta\theta_a
=
3\frac{\pi}{2}
=
\boxed{\frac{3\pi}{2}}.
\]

Logo:

\[
\boxed{
S_{\rm CS}^{(3)}
=
\int_{\partial\Sigma_p^\circ}\operatorname{CS}(\mathcal A)
=
\frac{3\pi}{2}.
}
\]

Interpretação: este termo é a holonomia global necessária para colar três
câmaras planas em um nó bariônico com carga inteira \(Q_p=+1\) e spin global
\(1/2\).

---

## 5.1 Alinhamento no próton e compensação no nêutron

A integral de Cauchy que define a carga fixa índices inteiros. Ela não impõe,
por si, cargas fracionárias fundamentais. A diferença entre próton e nêutron
entra pela orientação torsional dos três estômatos.

No próton, os três estômatos estão alinhados:

\[
\boxed{
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,\tau).
}
\]

A torção se fecha globalmente no sóliton carregado. Por isso o resíduo global é:

\[
Q_p=+1.
\]

No nêutron, um estômato está invertido. Para que a configuração neutra seja
estacionária, a torção invertida deve compensar simultaneamente os dois
estômatos alinhados:

\[
\boxed{
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,-2\tau).
}
\]

Logo:

\[
\boxed{
\sum_{a=1}^{3}\mathcal T_a=0.
}
\]

Essa é a lei de compensação torsional estacionária. Ela pode ser vista como a
forma de fronteira da conservação de Noether:

\[
\delta_\vartheta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
dJ_{\rm tor}=0.
\]

Assim, o nêutron não precisa ser interpretado como soma fundamental de cargas
fracionárias. Ele é uma configuração de resíduo global nulo com tensões
torsionais internas compensadas.

---

## 6. Correção espectral de garganta: \(3/(4\pi^3)\)

Além da holonomia de fase, cada estômato possui uma garganta de interface.

A unidade espectral mínima da garganta é normalizada pelo volume da esfera de
fase local \(S^3\) e pelo ciclo angular \(S^1\):

\[
\lambda_{\rm throat}^{(1)}
=
\frac{1}{\operatorname{Vol}(S^3)\operatorname{Vol}(S^1)}.
\]

Como:

\[
\operatorname{Vol}(S^3)=2\pi^2,
\qquad
\operatorname{Vol}(S^1)=2\pi,
\]

temos:

\[
\lambda_{\rm throat}^{(1)}
=
\frac{1}{(2\pi^2)(2\pi)}
=
\frac{1}{4\pi^3}.
\]

Para três estômatos:

\[
\boxed{
\lambda_{\rm throat}^{(3)}
=
\frac{3}{4\pi^3}.
}
\]

Esse termo mede a impedância mínima da garganta: mesmo com bulk plano, a cola
tem um custo espectral finito.

---

## 7. Termo total de superfície

Somando holonomia e garganta:

\[
\int_{\partial\Sigma_p^\circ}\mathcal T_{\rm eff}
=
S_{\rm CS}^{(3)}
+
\lambda_{\rm throat}^{(3)}.
\]

Logo:

\[
\int_{\partial\Sigma_p^\circ}\mathcal T_{\rm eff}
=
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}.
\]

Multiplicando pela admitância eletro-geométrica:

\[
\boxed{
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
\]

---

## 8. Massa do próton

Com:

\[
\mathcal I_p^{\rm bulk}=6\pi^5,
\]

e:

\[
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right),
\]

obtemos:

\[
\boxed{
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
\]

Essa é a fórmula bariônica de massa do próton em unidades eletrônicas.

---

## 9. Status lógico

Com este adendo, ficam fechados estruturalmente:

1. o termo de volume;
2. a origem do fator \(6\pi^5\);
3. a cola global por três câmaras;
4. a torção como transgressão de superfície;
5. a origem de \(\frac{3\pi}{2}\);
6. a origem de \(\frac{3}{4\pi^3}\);
7. a fórmula de massa do próton.

O que ainda não fica fechado neste adendo:

1. momentos magnéticos;
2. raio;
3. fatores de forma;
4. espectro excitado;
5. espalhamento;
6. estabilidade completa contra todos os canais.

Esses são observáveis bariônicos posteriores, não a massa de bulk/superfície.

---

## 10. Conclusão

A decomposição bariônica fica:

\[
\boxed{
\frac{M_p}{M_e}
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
}_{\rm superfície/torsão}.
}
\]

Assim, a analogia com Gamow torna-se precisa:

\[
\boxed{
\text{massa do próton}
=
\text{volume interno}
+
\text{superfície torsional}.
}
\]

Mas os coeficientes não são fenomenológicos: eles vêm da geometria do domínio,
da holonomia dos três estômatos e da impedância espectral mínima das
gargantas.
