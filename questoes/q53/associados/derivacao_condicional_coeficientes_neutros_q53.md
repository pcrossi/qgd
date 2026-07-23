# Q53 — Derivação condicional dos coeficientes neutros

## 1. Objetivo

Explicar, em terminologia GDQ, de onde podem vir os três números usados na
execução reduzida das escalas inerciais neutras:

$$
S_\nu=\alpha^7Q_\beta^2,
\qquad
\lambda_2=\frac{\chi_\nu^2}{2},
\qquad
\lambda_3=\frac{6\pi}{5}.
$$

Status:

$$
\boxed{
\text{derivação reduzida condicional; ainda não é Hessiana neutra 8D completa.}
}
$$

---

## 2. Escala neutra beta

O canal neutro local já vem do nêutron:

$$
\psi_{\bar\nu}\in\ker D_{0,-3/2}^{(0)}.
$$

A energia disponível para esse canal é a escala cinemática beta:

$$
Q_\beta=M_n-M_p-m_e.
$$

Como a oscilação neutra mede diferenças quadráticas de escala inercial, a
escala dimensional mínima é:

$$
Q_\beta^2.
$$

O modo neutro, porém, não possui estômato localizado. Ele só acopla ao setor
local através de vazamento torsional. Na redução GDQ, esse vazamento atravessa
sete filtros de fluxo:

1. três direções espaciais reais do suporte de tensão;
2. três canais de folha/leptônicos;
3. uma seleção causal do canal neutro pela borda APS.

Cada filtro carrega uma supressão de complacência eletrogeométrica $\alpha$.
Logo, a escala neutra reduzida é:

$$
\boxed{
S_\nu=\alpha^7Q_\beta^2.
}
$$

Esta é uma leitura reduzida de fluxo. Para virar teorema forte, deve ser
obtida como elemento de matriz da corrente simplética ponderada do canal
neutro.

---

## 3. Primeiro autovalor não nulo

O primeiro acoplamento entre folhas é bicanal: folha eletrônica e primeira
folha transportada. Na GDQ, a impedância neutra reduzida é tomada como produto
dos dois componentes primitivos de um triângulo $3$--$4$--$5$:

$$
\chi_0
=
\frac35\frac45
=
\frac{12}{25}
=
0.48.
$$

Interpretação:

- $3/5$ mede a projeção axial/torsional;
- $4/5$ mede a projeção transversal propagante;
- o produto mede o canal neutro misto, sem estômato localizado.

A correção fina de contorno causal é:

$$
\chi_\nu
=
\chi_0e^{-\alpha/4}.
$$

O fator $1/2$ vem da diagonalização do subespaço de duas folhas
normalizadas. Para o par simétrico/antissimétrico:

$$
K_2
\sim
\chi_\nu^2
\begin{pmatrix}
1 & -1\\
-1 & 1
\end{pmatrix},
\qquad
G_2\sim 2I,
$$

e o modo relativo recebe:

$$
\boxed{
\lambda_2=\frac{\chi_\nu^2}{2}.
}
$$

Este passo é razoável como redução de interface. Para ser final, o bloco
$K_2$ deve ser calculado diretamente por:

$$
K_{\alpha\beta}^{\nu}
=
\langle
\Psi_\alpha^{\rm folha},
K_{\rm neutro}^{\rm phys}
\Psi_\beta^{\rm folha}
\rangle_{\mathcal U}.
$$

---

## 4. Autovalor superior

O terceiro modo neutro envolve a circulação fechada entre as três folhas
leptônicas. Esse modo não é local; ele pertence ao transporte global de folha.

No espaço cosmológico de Einstein, a fibra axial relevante para o transporte
neutro possui cinco ciclos toroidais. A fase elementar média por ciclo axial é:

$$
\varphi_5=\frac{2\pi}{5}.
$$

Como o modo superior fecha o ciclo nas três folhas:

$$
\lambda_3
=
3\varphi_5
=
3\frac{2\pi}{5}.
$$

Logo:

$$
\boxed{
\lambda_3=\frac{6\pi}{5}.
}
$$

Leitura física: o modo superior é a primeira circulação neutra que usa as três
folhas. O fator $5$ não vem do bulk local $\mathbb R^4\times T^4$; ele vem da
normalização global do espaço cosmológico de Einstein usado para transporte
de fase. Portanto, esta etapa depende explicitamente da ponte global--local.

Para fechar fortemente, é preciso mostrar que o operador de transporte
global--local reduz, no setor neutro, a:

$$
\mathcal T_{\rm folhas}^{(3)}
\leadsto
\frac{6\pi}{5}.
$$

---

## 5. Espectro reduzido

Com os três ingredientes:

$$
\boxed{
\lambda
=
\left(
0,
\frac{1}{2}
\left[
\frac{12}{25}e^{-\alpha/4}
\right]^2,
\frac{6\pi}{5}
\right).
}
$$

E:

$$
\boxed{
\Delta m_{ij}^2
=
\alpha^7Q_\beta^2(\lambda_i-\lambda_j).
}
$$

---

## 6. Limitações explícitas

Esta derivação não deve ser chamada de fechamento metrológico final porque:

1. a potência $\alpha^7$ ainda precisa sair da corrente simplética neutra;
2. o triângulo $3$--$4$--$5$ precisa ser identificado como autovetor real da
   Hessiana de interface, não apenas como decomposição geométrica plausível;
3. o fator $2\pi/5$ precisa vir do operador de transporte global--local;
4. o bloco completo $G^\nu,K^\nu$ ainda não foi integrado no background 8D.

Classificação final:

$$
\boxed{
\text{candidato reduzido forte para Q53; pendente de derivação variacional direta.}
}
$$
