# Ponte global--local — Beltrami global da superfície de Hopf

## 1. Construção global

Considere a superfície de Hopf primária

$$
X_q=(\mathbb C^2\setminus\{0\})/
\langle z\mapsto qz\rangle,
\qquad 0<|q|<1.
$$

Como variedade diferenciável,

$$
X_q\simeq S^1\times S^3.
$$

Deforme a contração para

$$
Q_\varepsilon
=\operatorname{diag}(qe^{\varepsilon_1},qe^{\varepsilon_2}).
$$

Se os autovalores continuam dentro do disco unitário, o quociente permanece
uma superfície de Hopf complexa. A deformação é portanto integrável por
construção.

## 2. Representante de Beltrami

No recobrimento, defina

$$
t(z)=\frac{\log|z|^2}{2\log|q|},
\qquad t(qz)=t(z)+1.
$$

A conjugação diferenciável infinitesimal é gerada por

$$
V^{1,0}
=t(z)\sum_{i=1}^2\varepsilon_i z_i\partial_{z_i}.
$$

Embora $V$ não desça ao quociente, pois adquire o campo de Euler após uma
volta, sua derivada de Beltrami desce:

$$
\boxed{
\mu_{\rm Hopf}
=\bar\partial t\otimes
\sum_i\varepsilon_i z_i\partial_{z_i}.
}
$$

Em componentes,

$$
\boxed{
(\mu_{\rm Hopf})^i{}_{\bar j}
=\frac{\varepsilon_i z_i z_j}
{2\log|q|\,|z|^2}.
}
$$

Para $q$ complexo, os fatores de fase do deck devem ser incluídos no frame;
o caso real positivo já contém o módulo geométrico relevante.

## 3. Não é gauge global

Localmente,

$$
\mu_{\rm Hopf}=\bar\partial V^{1,0}.
$$

Globalmente, $V$ não é periódico. Portanto a deformação não pertence à imagem
de $\bar\partial$ agindo em campos vetoriais globais do quociente. Ela é um
modo de Kodaira--Spencer genuíno associado à variação dos autovalores de $Q$.

## 4. Maurer--Cartan

O representante linear é decomponível:

$$
\mu=\alpha\otimes E_\varepsilon,
\qquad \alpha=\bar\partial t.
$$

Tem-se

$$
\bar\partial\alpha=0,
\qquad \alpha\wedge\alpha=0.
$$

Ele satisfaz a equação linearizada

$$
\bar\partial\mu_1=0.
$$

Não se deve, porém, descartar automaticamente
$[\mu_1,\mu_1]$: a família finita contém correções de ordem superior. Uma
expressão exata é obtida da conjugação

$$
F_{\varepsilon,i}(z)=e^{\varepsilon_i t(z)}z_i.
$$

Defina

$$
A^i{}_j=\partial_{z_j}F_{\varepsilon,i},
\qquad
B^i{}_{\bar j}=\partial_{\bar z_j}F_{\varepsilon,i}.
$$

Então o coeficiente finito é

$$
\boxed{\mu_{\rm exact}=A^{-1}B.}
$$

Por ser pullback de uma estrutura complexa pela conjugação explícita,
$\mu_{\rm exact}$ satisfaz Maurer--Cartan em todas as ordens. Sua expansão é

$$
\mu_{\rm exact}=\mu_1+\mu_2+\cdots,
$$

com

$$
\bar\partial\mu_2=-\frac12[\mu_1,\mu_1].
$$

Logo, para a Hessiana basta $\mu_1$; para amplitudes finitas deve-se usar
$A^{-1}B$, não truncar a equação no representante linear.

## 5. Traço e anisotropia

Separe

$$
\varepsilon_+=\frac{\varepsilon_1+\varepsilon_2}{2},
\qquad
\varepsilon_-=\frac{\varepsilon_1-\varepsilon_2}{2}.
$$

O modo de traço $\varepsilon_+$ altera o módulo comum $q$ e, portanto, o ciclo
$S^1$. Ele pertence ao vínculo cosmológico de comprimento e não é um novo
parâmetro livre.

O modo

$$
\boxed{(\varepsilon_1,\varepsilon_2)=(\epsilon,-\epsilon)}
$$

é anisotrópico, globalmente não-gauge e quebra a simetria ampliada do ponto
$Q=qI$ para o subgrupo diagonal, genericamente $U(1)\times U(1)$.

## 6. Norma

Use o métrico cilíndrico de Hopf

$$
g_H=|z|^{-2}\sum_i dz_i d\bar z_i.
$$

Com $L=|\log|q||$ e $\operatorname{Vol}(S^3)=2\pi^2$, a média angular fornece

$$
\boxed{
\|\mu_{\rm Hopf}\|_{L^2}^2
=\frac{\pi^2}{4L}
(|\varepsilon_1|^2+|\varepsilon_2|^2).
}
$$

Para o modo sem traço,

$$
\|\mu_-\|_{L^2}^2
=\frac{\pi^2}{2L}|\epsilon|^2.
$$

A normalização muda com a convenção métrica, mas finitude e não nulidade não.

## 7. Periodicidade e corte do colar

No domínio fundamental $0\le t\le1$, a condição correta não é Dirichlet
independente nas duas pontas. É a identificação torcida

$$
\boxed{
\mu(1,Qz)=Q_*\mu(0,z)Q_{ar *}^{-1}.
}
$$

Ao cortar a superfície para formar um colar local, o representante restringe
sem parâmetro radial arbitrário. Seu perfil é fixado pela construção global.
Na interface com outro domínio, permanecem as condições variacionais

$$
[\mu]_Y=0,
\qquad
[\Pi_J^{\rm aug}]_Y=0.
$$

## 8. Variação da torção

A conjugação é localmente gerada por $V$. Para preservar a compatibilidade
hermitiana, devem variar juntos

$$
h=\mathcal L_Vg,
\qquad
\delta J=\mathcal L_VJ.
$$

Como $H=d_J^c\omega$ é natural por difeomorfismos,

$$
\boxed{
\delta H=\mathcal L_VH.
}
$$

No setor strong-KT, $dH=0$, logo

$$
\delta H=d(\iota_VH).
$$

Localmente isso é uma direção de difeomorfismo; globalmente não é gauge porque
$V$ não desce. Essa fórmula fornece diretamente o vetor de Galerkin para o
bloco torsional da Hessiana, sem postular $\delta H$ independente.

## 9. Acoplamento ao background simétrico

No ponto $Q=qI$, o modo sem traço transforma como anisotropia não-singlet. Os
resíduos homogêneos $(r_a,r_c,r_u)$ são singlets. Portanto

$$
\boxed{B_{\mu_-}=0}
$$

na ordem linear. A deformação é real e global, mas não cura a deficiência de
posto da Jacobiana simétrica.

O primeiro efeito permitido é

$$
\mathscr L_{\rm on}
=\mathscr L_0+\kappa_H|\epsilon|^2+O(|\epsilon|^3),
$$

com

$$
\kappa_H
=\langle(h,\delta J),K^{\rm phys}(h,\delta J)\rangle.
$$

Se $\kappa_H$ mudar de sinal, pode surgir um ramo anisotrópico por bifurcação.
Isso requer a Hessiana oficial, não ajuste do residual.

## 10. Alimentação do Galerkin

O modo pode ser incluído intrinsecamente usando o vetor fixo

$$
\Phi_H=(\mathcal L_Vg,\mathcal L_VJ,0),
$$

normalizado pela fórmula acima. Não requer Robin externa nem fonte. Requer,
porém, que o fator global $S^1\times S^3$ seja efetivamente identificado com a
superfície de Hopf e que o mapa global--local transporte essa estrutura ao
colar oficial. Essa identificação ainda é uma hipótese geométrica da ponte,
não consequência já provada da ação.

## 11. Veredito

A contração diagonal produz o primeiro Beltrami global explícito,
integrável e não-gauge. Ele é admissível como modo de Galerkin condicional à
identificação Hopf global--local. No background simétrico, seu acoplamento
linear ao tripleto residual desaparece; sua relevância é quadrática e deve ser
decidida pela Hessiana/bifurcação.
