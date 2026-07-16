# Q30 — Minimizador irreducível enquadrado das três câmaras

## 1. Domínio e dados de fonte

A Q28 identifica o setor de cor com automorfismos unitários das três câmaras e
o grupo geométrico efetivo $PSU(3)=SU(3)/\mathbb Z_3$.

Para o tubo entre fontes topológicas, tome como seção transversal uma
superfície compacta de três bordos $\Sigma_{0,3}$. Os bordos representam as
três câmaras. Suas holonomias enquadradas são dados de contorno das fontes,
permitidos pelo problema variacional; não são termos novos na ação.

A representação fundamental é

$$
\pi_1(\Sigma_{0,3})
=\langle x,y,z\mid xyz=1\rangle.
$$

## 2. Par clock--shift em $SU(3)$

Defina

$$
\omega=e^{2\pi i/3},
$$

$$
P=\begin{pmatrix}
1&0&0\\0&\omega&0\\0&0&\omega^2
\end{pmatrix},
\qquad
Q=\begin{pmatrix}
0&1&0\\0&0&1\\1&0&0
\end{pmatrix}.
$$

Ambas pertencem a $SU(3)$ e satisfazem, conforme a convenção de shift,

$$
PQ=\omega^2QP.
$$

O comutador é central. Portanto, no quociente $PSU(3)$, as holonomias
comutam projetivamente, exatamente como esperado para o cociclo $\mathbb Z_3$
das três câmaras.

Fixe

$$
\rho(x)=P,
\qquad
\rho(y)=Q,
\qquad
\rho(z)=(PQ)^{-1}.
$$

Então $\rho(x)\rho(y)\rho(z)=1$, definindo uma representação de
$\pi_1(\Sigma_{0,3})$.

## 3. Irredutibilidade

Se uma matriz $X$ comuta com $P$, como os autovalores de $P$ são distintos,
$X$ é diagonal. Se também comuta com o shift $Q$, seus três elementos
diagonais são iguais. Logo,

$$
\operatorname{Comm}(P,Q)=\mathbb C\,I.
$$

Intersectando com $\mathfrak{su}(3)$,

$$
\boxed{
\operatorname{Comm}(P,Q)\cap\mathfrak{su}(3)=\{0\}.
}
$$

Portanto, a conexão plana associada a $\rho$ é irreducível no adjunto.

## 4. Existência do minimizador

Todo homomorfismo $\rho:\pi_1(\Sigma)\to SU(3)$ define, por suspensão, um
fibrado plano

$$
E_\rho
=\widetilde\Sigma\times_\rho\mathbb C^3
$$

com conexão plana $\mathcal A_\rho$. Assim,

$$
\mathcal F_{\mathcal A_\rho}=0
$$

no interior; a informação torsional reside na holonomia global e nas
transições de patch.

Para a forma quadrática de curvatura do bloco de conexão,

$$
\int_\Sigma|\mathcal F_{\mathcal A}|^2\,d\mu\ge0,
$$

$\mathcal A_\rho$ atinge o mínimo absoluto zero entre conexões com os mesmos
dados enquadrados.

Isso não afirma que a tensão total do tubo seja zero: a ação GDQ contém a
circulação de $f$, a medida ponderada, bordos e colagem. Afirma apenas que o
background de conexão irreducível existe sem exigir elongação local.

## 5. Isolamento no problema enquadrado

Os valores de $\rho(x)$ e $\rho(y)$ são fixados como matrizes nos frames das
câmaras, não apenas por suas classes de conjugação. Uma representação do grupo
livre em $x,y$ fica então completamente determinada. Transformações de gauge
admissíveis são identidade nos bordos.

Consequentemente, não há deformação plana enquadrada que altere $P,Q$:

$$
\boxed{
H^1_{\rm par}
(\Sigma_{0,3};\operatorname{ad}\rho)=0
}
$$

para esse problema de bordo totalmente enquadrado. O minimizador é isolado
módulo gauge baseado.

Se apenas as classes de conjugação fossem fixadas, poderia existir um espaço
de módulos. O enquadramento das três câmaras é, portanto, parte essencial dos
dados das fontes.

## 6. Gap

Como a conexão é irreducível,

$$
\ker D_{\mathcal A_\rho}^\dagger D_{\mathcal A_\rho}=0.
$$

Como $\Sigma_{0,3}$ é compacta e as condições enquadradas fornecem um domínio
elíptico auto-adjunto,

$$
\boxed{
\lambda_{1,\rm cor}>0.
}
$$

O desacoplamento singlet--adjunto já provou que o bloco $f$ não cancela esse
gap. Portanto,

$$
\boxed{
\Delta_{\rm cor}
=\Lambda_C\sqrt{\lambda_{1,\rm cor}}>0
}
$$

em unidades de Cartan.

## 7. O que foi resolvido

Foi construída explicitamente uma conexão:

1. compatível com as três câmaras e o cociclo projetivo $\mathbb Z_3$ da Q28;
2. sem elongação dos módulos internos;
3. torsional por holonomia/transição de patch;
4. irreducível;
5. minimizante no bloco de curvatura com bordos enquadrados;
6. isolada no problema enquadrado;
7. portadora de gap adjunto positivo.

## 8. Limitações

1. O valor numérico de $\lambda_{1,\rm cor}$ depende da métrica e dos
   comprimentos da seção transversal.
2. A tensão $\sigma$ ainda requer avaliar a ação GDQ completa, incluindo
   circulação, medida e bordos.
3. O enquadramento deve ser mantido explicitamente como dado das fontes; sem
   ele, isolamento não está demonstrado.

## 9. Status

$$
\boxed{
\text{existência, irreducibilidade e isolamento do minimizador de conexão
resolvidos para o tubo de três câmaras com bordos enquadrados.}
}
$$

O mass gap de cor está fechado condicionalmente a essa realização topológica
da seção transversal. A próxima pendência quantitativa da Q30 é $\sigma$, não
mais a existência abstrata do gap.

A auditoria posterior `q30/no_go_sigma_holonomia_plana.md` mostrou que a
conexão plana minimizante tem densidade local de curvatura nula. Ela prova o
gap por holonomia, mas não produz por si só tensão positiva. $\sigma$ exige o
background métrico--dilatônico e os termos de colagem da ação oficial.
