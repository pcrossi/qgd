# Q30 — Desacoplamento quadrático entre singletos GDQ e o adjunto de cor

## 1. Representações

No setor da Q28,

$$
\delta\mathcal A_C\in\mathbf 8
$$

transforma no adjunto de $SU(3)$, enquanto

$$
\delta u,\delta v\in\mathbf 1
$$

são singletos. A ação oficial e a medida são escalares sob mudanças de frame
interno.

## 2. Ausência do bloco misto

Um termo misto da Hessiana teria localmente a forma

$$
\delta^2\mathcal S_{\rm mix}
=\int_\Sigma \delta u\,B^A\delta\mathcal A_C^A
+\delta v\,\widetilde B^A\delta\mathcal A_C^A.
$$

Para ser invariante, $B^A$ e $\widetilde B^A$ teriam de ser vetores
invariantes no adjunto. Mas

$$
(\mathbf8)^{SU(3)}=\{0\},
\qquad
\operatorname{Hom}_{SU(3)}(\mathbf1,\mathbf8)=0.
$$

Equivalentemente, qualquer termo linear em uma flutuação adjunta e
multiplicado somente por escalares contém $\operatorname{tr}(T_A)=0$.
Portanto,

$$
\boxed{B=0.}
$$

## 3. Hipótese sobre o background

O desacoplamento vale quando o background é $SU(3)$-equivariante e não contém
um vetor adjunto externo. A holonomia pode ser irreducível: observáveis do
background dependem de sua classe de conjugação, não de uma orientação de cor
externamente escolhida.

Uma fonte clássica de cor orientada invalidaria o argumento localmente. O tubo
físico combinado em singlet de cor não fornece esse dado no bulk.

## 4. Consequência espectral

No bulk físico,

$$
\boxed{
\mathcal H_{\rm phys}=L_{\mathcal A}\oplus L_f.
}
$$

O mass gap de cor é

$$
\boxed{
\lambda_{\rm cor}^+
=\inf\operatorname{spec}L_{\mathcal A}>0,
}
$$

independentemente de o setor singlet possuir uma excitação mais leve. Uma
instabilidade singlet seria um problema do background completo, não um modo de
cor sem massa.

No critério de Schur, $b=0$ e

$$
\lambda_-=min(m_{\mathcal A}^2,m_f^2).
$$

Para a pergunta específica da Q30, basta $m_{\mathcal A}^2>0$.

## 5. Elo remanescente

Irredutibilidade prova o gap de
$D_{\mathcal A}^\dagger D_{\mathcal A}$. Para o operador completo de conexão,
é necessário que o minimizador torsional seja estável e isolado:

$$
\delta_{\mathcal A}^2\mathcal S_{\rm GDQ}\ge0,
\qquad
\ker L_{\mathcal A}=0
$$

depois de remover gauge. Irredutibilidade não exclui, sozinha, módulos de
Jacobi da família de conexões.

## 6. Veredito

$$
\boxed{
b=0\text{ exatamente por }SU(3),
\quad
\Delta_{\rm cor}>0
\text{ para um minimizador torsional irreducível e isolado.}
}
$$

O problema de três coeficientes foi reduzido a uma única questão geométrica:
construir ou provar a existência do minimizador irreducível isolado da ação
oficial.

Uma realização explícita com dados de fonte enquadrados foi construída em
`q30/minimizador_irredutivel_tres_camaras.md` pelo par clock--shift associado
às três câmaras.

## 7. Classificação

- $B=0$: teorema de representação no background equivariante;
- separação dos espectros: exata;
- gap do Laplaciano covariante: teorema condicional anterior;
- isolamento/estabilidade do minimizador: ainda não demonstrado.
