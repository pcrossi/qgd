# Adendo Q40 — Decomposição volume–superfície da massa bariônica

## 1. Motivação

A fórmula bariônica usada no manuscrito tem a forma:

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
\right).
\]

Essa estrutura sugere uma decomposição física clara:

\[
\boxed{
\text{massa bariônica}
=
\text{energia de volume}
+
\text{energia de superfície/fronteira}.
}
\]

Isso lembra a lógica de Gamow e do modelo de gota nuclear: há um termo de
volume, associado ao interior da configuração, e termos de superfície,
associados à fronteira finita do objeto. Mas, na GDQ, a origem não deve ser
fenomenológica. A decomposição deve vir da ação geométrica:

\[
\boxed{
\mathcal S_{\rm GDQ}
\quad\Longrightarrow\quad
E_B
=
E_{\rm bulk}
+
E_{\partial}.
}
\]

O objetivo deste adendo é mostrar como essa decomposição deve ser entendida
para a Questão 40.

---

## 2. Tese técnica

A proposta de fechamento é:

\[
\boxed{
\frac{M_B}{M_e}
=
\mathcal I_B^{\rm bulk}
+
\mathcal I_B^{\partial}.
}
\]

Para o próton:

\[
\boxed{
\mathcal I_p^{\rm bulk}
=
6\pi^5
}
\]

e:

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

Assim:

\[
\boxed{
\frac{M_p}{M_e}
=
\mathcal I_p^{\rm bulk}
+
\mathcal I_p^{\partial}.
}
\]

O ponto decisivo é que \(6\pi^5\) não deve ser lido como "um número próximo"
de \(M_p/M_e\). Ele deve ser lido como o termo de bulk da energia
adimensional do sóliton bariônico quando a energia eletrônica foi escolhida
como unidade metrológica:

\[
E_0=M_ec^2.
\]

---

## 3. Energia estática reduzida

No setor estacionário:

\[
\partial_\tau g=0,
\qquad
\partial_\tau f=0,
\qquad
\partial_\tau B=0,
\]

a ação oficial deve induzir uma energia efetiva:

\[
E[g,f,B]
=
E_0
\int_{\Sigma}
\mathcal H_{\rm GDQ}(g,f,B)
\mathcal U\sqrt{\det g}\,d\Sigma.
\]

Para uma classe solitônica \(\mathcal C\), definimos:

\[
\mathcal I_{\mathcal C}
=
\int_{\Sigma_{\mathcal C}}
\mathcal H_{\rm GDQ}(g_{\mathcal C},f_{\mathcal C},B_{\mathcal C})
\mathcal U_{\mathcal C}
\sqrt{\det g_{\mathcal C}}\,d\Sigma_{\mathcal C}.
\]

Então:

\[
\boxed{
M_{\mathcal C}c^2
=
E_0\mathcal I_{\mathcal C}.
}
\]

Com calibração eletrônica:

\[
E_0=M_ec^2,
\]

temos:

\[
\boxed{
\frac{M_{\mathcal C}}{M_e}
=
\mathcal I_{\mathcal C}.
}
\]

Portanto, a massa do próton em unidades do elétron exige:

\[
\boxed{
\mathcal I_p
=
\mathcal I_p^{\rm bulk}
+
\mathcal I_p^{\partial}.
}
\]

---

## 4. Decomposição por bulk e fronteira

O setor bariônico tem três estômatos. A variedade física efetiva é uma
variedade com núcleos removidos:

\[
\Sigma_B^\circ
=
\Sigma_B
\setminus
\bigcup_{a=1}^{3}D_a,
\]

onde \(D_a\) são pequenas vizinhanças tubulares dos estômatos.

Logo, mesmo que o espaço global não possua bordo, o domínio regularizado do
sóliton possui fronteiras internas:

\[
\partial\Sigma_B^\circ
=
\bigcup_{a=1}^{3}\partial D_a.
\]

Essa é a origem geométrica natural do termo de superfície.

A energia reduzida deve ter a forma:

\[
\mathcal I_B
=
\int_{\Sigma_B^\circ}
\mathcal H_{\rm bulk}\,d\mu_B
+
\int_{\partial\Sigma_B^\circ}
\mathcal H_{\partial}\,d\sigma_B.
\]

Ou:

\[
\boxed{
\mathcal I_B
=
\mathcal I_B^{\rm bulk}
+
\mathcal I_B^{\partial}.
}
\]

---

## 5. Por que o termo de volume pode dar \(6\pi^5\)

O termo de bulk é o custo inercial de preencher a célula bariônica compacta
com a densidade estacionária do vácuo deformado. Na normalização do elétron:

\[
\mathcal I_e=1.
\]

Para o bárion trimodal, o domínio interno efetivo é o toro trançado de
calibração:

\[
K_B\simeq T^5_{\rm trançado}.
\]

O capítulo 26 propõe:

\[
\operatorname{Vol}(T^5_{\rm trançado})
=
6\pi^5.
\]

A forma correta de transformar isso em massa é exigir que o integrando de
bulk, no ponto estacionário bariônico, seja normalizado pela unidade
eletrônica:

\[
\mathcal H_{\rm bulk}\mathcal U_B\sqrt{\det g_B}\,d\Sigma_B
\longrightarrow
d\mu_{T^5_{\rm trançado}}.
\]

Assim:

\[
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}
d\mu_{T^5_{\rm trançado}}
=
6\pi^5.
\]

Ou seja:

\[
\boxed{
6\pi^5
\text{ é massa apenas se for o volume de energia normalizado, não mero volume cinemático.}
}
\]

A lacuna que resta é calcular explicitamente:

\[
\mathcal H_{\rm bulk}\mathcal U_B\sqrt{\det g_B}
\]

a partir da ação oficial e mostrar que ela reduz à medida invariante acima.

---

## 6. Por que a torção aparece como termo de superfície

A torção de Bismut/Cartan é naturalmente um objeto de fronteira quando
avaliada em domínios perfurados por estômatos.

O motivo técnico é que as densidades topológicas associadas à torção aparecem
como termos de transgressão. Esquematicamente:

\[
d\,\operatorname{CS}_B
=
\operatorname{Tr}(R_B\wedge R_B)
-
\operatorname{Tr}(R_0\wedge R_0),
\]

ou, em linguagem de torção:

\[
d\,\mathcal T_{\rm NY}
=
\text{densidade de Nieh--Yan/Cartan}.
\]

Ao integrar sobre o domínio regularizado:

\[
\int_{\Sigma_B^\circ}
d\,\mathcal T_{\rm top}
=
\int_{\partial\Sigma_B^\circ}
\mathcal T_{\rm top}.
\]

Pelo teorema de Stokes:

\[
\boxed{
\text{densidade topológica de torção no bulk}
\quad\Longleftrightarrow\quad
\text{ação de superfície nos estômatos}.
}
\]

Portanto, é natural que a correção torsional de fronteira não apareça como
outro volume \(6\pi^5\), mas como:

\[
\mathcal I_p^{\partial}
=
\int_{\partial\Sigma_B^\circ}
\mathcal H_{\partial}(B,\omega,f)\,d\sigma.
\]

---

## 7. Identificação do termo de superfície do próton

O capítulo 26 propõe:

\[
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
\]

Essa expressão pode ser decomposta como:

\[
\mathcal I_p^{\partial}
=
\alpha
\left(
S_{\rm CS}^{(3)}
+
\lambda_{\rm throat}^{(3)}
\right),
\]

com:

\[
S_{\rm CS}^{(3)}
=
\frac{3\pi}{2},
\]

\[
\lambda_{\rm throat}^{(3)}
=
\frac{3}{4\pi^3}.
\]

Interpretação:

1. \(\frac{3\pi}{2}\) é a soma das três contribuições de fase/holonomia de
   contorno:

   \[
   3\times\frac{\pi}{2}.
   \]

2. \(\frac{3}{4\pi^3}\) é a contribuição espectral mínima das três gargantas,
   normalizada pelo volume \(2\pi^2\) de \(S^3\) e pelo ciclo angular
   \(2\pi\):

   \[
   \frac{3}{\operatorname{Vol}(S^3)\,2\pi}
   =
   \frac{3}{(2\pi^2)(2\pi)}
   =
   \frac{3}{4\pi^3}.
   \]

3. O fator \(\alpha\) é a admitância eletro-geométrica que converte a
   holonomia torsional de fronteira em energia inercial observável na unidade
   eletrônica.

Assim:

\[
\boxed{
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
}
\]

é interpretado como termo de superfície torsional, análogo ao termo de
superfície de Gamow, mas derivado de transgressão geométrica.

---

## 8. Relação com Gamow

A analogia com Gamow é estrutural:

\[
E_{\rm gota}
\sim
a_V A
-
a_S A^{2/3}
+
E_{\rm Coulomb}
\cdots
\]

Na GDQ bariônica:

\[
\frac{M_p}{M_e}
=
\underbrace{6\pi^5}_{\text{bulk/volume}}
+
\underbrace{
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
}_{\text{superfície torsional}}.
\]

A diferença é que, em Gamow, os coeficientes são fenomenológicos. Na GDQ, eles
devem ser invariantes geométricos:

1. \(6\pi^5\): volume inercial do domínio bariônico compacto;
2. \(\frac{3\pi}{2}\): holonomia/Chern--Simons dos três estômatos;
3. \(\frac{3}{4\pi^3}\): correção espectral de garganta;
4. \(\alpha\): admitância eletro-geométrica da fronteira.

Portanto, a analogia é útil para organizar a física, mas a prova deve ser
variacional.

---

## 9. Teorema condicional de massa do próton

Podemos formular o resultado como um teorema condicional.

**Teorema.** Seja \((g_p,f_p,B_p)\) uma solução estacionária da ação GDQ na
classe bariônica trimodal, com domínio regularizado
\(\Sigma_p^\circ\). Suponha que:

1. a energia estática reduzida se decomponha como:

   \[
   \mathcal I_p
   =
   \mathcal I_p^{\rm bulk}
   +
   \mathcal I_p^{\partial};
   \]

2. a normalização eletrônica satisfaça:

   \[
   \mathcal I_e=1;
   \]

3. a integral de bulk do domínio bariônico seja:

   \[
   \mathcal I_p^{\rm bulk}=6\pi^5;
   \]

4. a transgressão torsional de fronteira seja:

   \[
   \mathcal I_p^{\partial}
   =
   \alpha
   \left(
   \frac{3\pi}{2}
   +
   \frac{3}{4\pi^3}
   \right).
   \]

Então:

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

Essa formulação é importante porque separa o que já está organizado do que
ainda precisa ser provado diretamente da ação.

---

## 10. O que este adendo resolve

Este adendo resolve a interpretação conceitual:

\[
\boxed{
\text{volume = termo de massa de bulk;}
\qquad
\text{torção = termo de superfície por transgressão/Stokes.}
}
\]

Também transforma a semelhança com Gamow numa estrutura matemática:

\[
\boxed{
E_B
=
E_{\rm volume}
+
E_{\rm superfície}.
}
\]

Mas ainda não fecha completamente a Q40, porque falta executar a derivação
variacional explícita:

\[
\mathcal S_{\rm GDQ}
\longrightarrow
\mathcal H_{\rm bulk}
\quad\text{e}\quad
\mathcal H_{\partial}.
\]

---

## 11. Próximo passo

O próximo passo técnico deve ser provar:

\[
\boxed{
\mathcal I_p^{\rm bulk}
=
6\pi^5.
}
\]

Para isso é necessário especificar:

1. o domínio \(T^5_{\rm trançado}\);
2. a métrica reduzida \(g_{5D}\);
3. a medida de Perelman \(\mathcal U\sqrt{\det g}\);
4. a normalização eletrônica \(\mathcal I_e=1\);
5. o motivo pelo qual a densidade de energia estacionária reduz-se à medida
   invariante do domínio.

Depois disso, deve-se provar:

\[
\boxed{
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
}
\]

como termo de transgressão torsional nos três estômatos.
