# Q43 — Construção operacional de \(H_C,c,m_\perp\)

## 1. Objetivo

Este documento transforma a estrutura formal da Q43 em um objeto computável.

A cadeia correta é:

\[
\mathcal S_{\rm GDQ}
\to
\Phi_\ell
\to
H_{C,\ell}
\to
c_\ell
\to
m_{\perp,\ell}
\to
a_\ell.
\]

O cálculo abaixo não altera a ação oficial. Ele constrói uma redução
finito-dimensional controlada do setor de circulação de Noether para testar a
álgebra da resposta magnética.

## 2. Funcional vinculado

No background leptônico \(\Phi_\ell\), fixa-se a circulação:

\[
\mathcal C[\Phi]=C_\ell.
\]

Com campo magnético externo fraco \(B\), o funcional de teste é:

\[
\mathscr I[\Phi,\lambda;B]
=
\mathcal S_{\rm GDQ}[\Phi]
-B\,M[\Phi]
-\lambda\left(\mathcal C[\Phi]-C_\ell\right).
\]

O campo \(B\) é dado de aparelho. Ele não é campo fundamental novo.

Linearizando:

\[
\Phi=\Phi_\ell+\eta,
\]

\[
\mathcal C[\Phi]
=C_\ell+\langle c_\ell,\eta\rangle+O(\eta^2),
\]

\[
M[\Phi]
=M[\Phi_\ell]+\langle m_\ell,\eta\rangle+O(\eta^2).
\]

A Hessiana física vinculada é:

\[
H_{C,\ell}
=
P_C^\dagger
\left.\delta^2\mathcal S_{\rm GDQ}\right|_{\Phi_\ell}
P_C,
\]

onde \(P_C\) remove gauge, fase comum, modos nulos de Noether e variações que
mudam a circulação fixada.

## 3. Separação mínima e transversal

A fonte magnética se decompõe em:

\[
m_\ell
=
\gamma_{0,\ell}c_\ell+m_{\perp,\ell}.
\]

A parte mínima é protegida por Noether:

\[
\gamma_{0,\ell}=\frac{q_\ell}{m_\ell c}.
\]

Essa parte fornece:

\[
g_0=2.
\]

A parte transversal \(m_{\perp,\ell}\) contém a deformação interna do sóliton
que preserva a carga/circulação, mas altera o momento magnético.

O observável é:

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
\]

## 4. Bloco líder derivado pela projeção harmônica

No ciclo de fase \(S^1\), o modo físico é:

\[
h=\frac{d\vartheta}{2\pi},
\qquad
\oint h=1.
\]

Sua norma é:

\[
\langle h,h\rangle=\frac{1}{2\pi}.
\]

A intensidade eletrogeométrica elementar é \(\alpha\). Logo, o primeiro
vestido geométrico é:

\[
a^{(1)}
=
\alpha\langle h,h\rangle
=
\frac{\alpha}{2\pi}.
\]

Uma representação matricial mínima que implementa essa resposta é:

\[
H_{\rm lead}
=
\begin{pmatrix}
1 & -1\\
-1 & 2\pi/\alpha
\end{pmatrix},
\qquad
c=
\begin{pmatrix}
1\\0
\end{pmatrix},
\qquad
m_\perp=
\begin{pmatrix}
0\\1
\end{pmatrix}.
\]

Para esse bloco:

\[
\frac{\langle c,H_{\rm lead}^{-1}m_\perp\rangle}
{\langle c,H_{\rm lead}^{-1}c\rangle}
=
\frac{\alpha}{2\pi}.
\]

Esse bloco não usa \(g_e\), \(g_\mu\) ou \(g_\tau\). Ele usa somente a
normalização de \(\alpha\) e a norma harmônica.

## 5. Bloco superior diagnóstico

Para metrologia completa, adiciona-se um canal transversal superior:

\[
H_{\rm diag}
=
\begin{pmatrix}
1 & -1 & -J_2\\
-1 & K_1 & 0\\
-J_2 & 0 & K_{2,\ell}
\end{pmatrix},
\qquad
m_\perp=
\begin{pmatrix}
0\\1\\\mu_{2,\ell}
\end{pmatrix}.
\]

Aqui:

\[
K_1=\frac{2\pi}{\alpha}
\]

é o canal líder, enquanto \(K_{2,\ell}\), \(J_2\) e \(\mu_{2,\ell}\) pertencem
ao setor transversal superior.

No estado atual, \(K_{2,\ell}\), \(J_2\) e \(\mu_{2,\ell}\) ainda não foram
derivados da Hessiana oficial completa. Portanto, quando se escolhe
\(\mu_{2,\ell}\) para reproduzir o resíduo experimental, o resultado é
diagnóstico inverso, não previsão.

## 6. O que fica construído agora

Fica construído:

1. o funcional vinculado;
2. a definição operacional de \(H_C,c,m_\perp\);
3. o bloco líder sem uso de alvo experimental;
4. o avaliador numérico da contração;
5. o bloco diagnóstico para medir o tamanho do canal superior faltante.

Fica faltando para fechamento metrológico:

\[
\boxed{
\text{derivar }K_{2,\ell},J_{2,\ell},\mu_{2,\ell}
\text{ diretamente da Hessiana oficial em }\Phi_\ell.
}
\]

Esse é o elo físico que substitui qualquer tentativa de importar diagramas da
QED como ontologia.
