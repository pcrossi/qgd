# Q30 — Controle da Hessiana física no setor torsional

## 1. Espaço físico adotado

Segue-se a hipótese constitutiva do autor:

$$
\boxed{
\text{torções são admissíveis; elongações internas não pertencem ao setor
físico de cor.}
}
$$

Portanto, as variações Hermitianas simétricas $S$ do subfibrado $E_C$ são
excluídas do domínio de Q30. Permanecem:

1. flutuações torsionais/conexão $\alpha=\delta\mathcal A_C$;
2. flutuações fundamentais compatíveis $\varphi=\delta u$ e
   $\vartheta=\delta v$;
3. componentes Bismut induzidas por essas variações.

São removidos gauge, translação do tubo, fase constante e normalização da
medida.

## 2. Forma em blocos

Depois dessas projeções, escreva a Hessiana como

$$
\boxed{
\mathcal H_{\rm phys}
=
\begin{pmatrix}
L_{\mathcal A} & B^\dagger\\
B & L_f
\end{pmatrix},
}
$$

onde

$$
L_{\mathcal A}=D_{\mathcal A}^\dagger D_{\mathcal A}+V_{\mathcal A},
$$

$L_f$ reúne $\varphi,\vartheta$ e a resposta Bismut compatível, e $B$ é o
acoplamento misto determinado pela medida $e^{-u}$ e pela derivada horizontal.

## 3. Gap do bloco de conexão

Pelo teorema de holonomia irreducível,

$$
D_{\mathcal A}^\dagger D_{\mathcal A}
\ge\lambda_{1,\mathcal A}>0.
$$

Defina a cota efetiva, já incluindo o potencial do bloco,

$$
m_{\mathcal A}^2
:=\inf\operatorname{spec}L_{\mathcal A}.
$$

O teorema anterior garante a parte cinética positiva, mas
$m_{\mathcal A}^2>0$ ainda requer que $V_{\mathcal A}$ não a cancele.

## 4. Bloco fundamental

No complemento da fase constante e da normalização, o laplaciano ponderado em
seção compacta satisfaz uma desigualdade de Poincaré:

$$
\int_\Sigma e^{-u}|\nabla\psi|^2
\ge\lambda_{1,f}\int_\Sigma e^{-u}|\psi|^2,
\qquad
\lambda_{1,f}>0.
$$

Incluindo as parcelas locais da segunda variação, defina

$$
m_f^2:=\inf\operatorname{spec}L_f.
$$

Assim como no bloco de conexão, compacidade remove acumulação em zero, mas o
sinal final depende do background estacionário.

## 5. Complemento de Schur

Suponha

$$
L_{\mathcal A}\ge m_{\mathcal A}^2>0,
\qquad
L_f\ge m_f^2>0,
\qquad
\|B\|\le b.
$$

Para qualquer $(\alpha,\psi)$,

$$
\begin{aligned}
\langle(\alpha,\psi),\mathcal H_{\rm phys}(\alpha,\psi)\rangle
\ge{}&m_{\mathcal A}^2\|\alpha\|^2
+m_f^2\|\psi\|^2
-2b\|\alpha\|\|\psi\|.
\end{aligned}
$$

O menor autovalor da matriz de cotas é

$$
\boxed{
\lambda_-
=\frac12\left[
m_{\mathcal A}^2+m_f^2
-\sqrt{(m_{\mathcal A}^2-m_f^2)^2+4b^2}
\right].
}
$$

Logo,

$$
\boxed{
\mathcal H_{\rm phys}>0
\iff
b^2<m_{\mathcal A}^2m_f^2
}
$$

no nível dessas cotas. O gap completo satisfaz

$$
\boxed{
\Delta_{\rm GDQ}
\ge\Lambda_C\sqrt{\lambda_-}>0.
}
$$

## 6. Caso de minimizador não degenerado

Existe uma formulação equivalente que não exige separar os blocos. Se o tubo
$q_*$ é um ponto crítico não degenerado e estritamente estável da ação
restrita ao espaço físico torsional, então

$$
\ker\mathcal H_{\rm phys}=0
$$

depois de remover as simetrias. Como o domínio transversal é compacto e a
Hessiana é elíptica auto-adjunta, seu resolvente é compacto. Portanto,

$$
\boxed{
q_*\text{ estável e não degenerado}
\Longrightarrow
\lambda_1(\mathcal H_{\rm phys})>0.
}
$$

Não basta dizer apenas “mínimo”: um mínimo degenerado pode possuir direção
quadrática nula estabilizada apenas em ordem superior.

## 7. Auditoria dos dados disponíveis

O corpus atual fornece:

1. positividade condicional do bloco cinético de conexão por holonomia
   irreducível;
2. compacidade e desigualdade ponderada no bloco escalar, uma vez fixado o
   background;
3. exclusão dos modos de elongação segundo a hipótese do autor.

Antes da análise de representações, não estavam fixados:

$$
\boxed{
m_{\mathcal A}^2,\qquad m_f^2,\qquad b.
}
$$

Consequentemente, naquele estágio não era lícito afirmar que os demais blocos
estavam controlados. O critério exato de fechamento era:

$$
\boxed{b^2<m_{\mathcal A}^2m_f^2.}
$$

## 8. Conclusão

O mass gap do bloco torsional não abeliano está provado condicionalmente. O
mass gap da Hessiana GDQ completa no setor físico torsional fica reduzido a um
único teste de estabilidade de blocos, sem qualquer referência a QCD:

$$
\boxed{
\text{calcular }m_{\mathcal A}^2\text{ no minimizador torsional irreducível.}
}
$$

Esse cálculo não pode ser substituído pelos valores escolhidos do solver
histórico.

O bloco misto foi posteriormente calculado por representação em
`q30/desacoplamento_singlet_adjunto.md`: como $f$ é singlet e
$\delta\mathcal A_C$ é adjunto, não existe bilinear $SU(3)$-invariante
$\mathbf1\otimes\mathbf8$, logo $b=0$. Para o mass gap de cor resta provar
que o minimizador irreducível é isolado e estável no bloco de conexão.

## 9. Classificação

- decomposição e complemento de Schur: derivação exata;
- gap do bloco de conexão: teorema condicional já provado;
- gap completo: condicionado à desigualdade explícita;
- bloco misto: $b=0$ por simetria no background equivariante;
- estabilidade/isolamento do bloco de conexão: ainda não demonstrados.
