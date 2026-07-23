# Holonomia Aharonov--Bohm na GDQ

## 1. Domínio

Considere o exterior de um solenoide ideal:

$$
M_{\rm ext}
=
\mathbb R^3\setminus\mathcal S,
$$

onde $\mathcal S$ é o núcleo excluído do solenoide. Fora do solenoide:

$$
F=dA=0.
$$

Mas o domínio não é simplesmente conexo:

$$
\pi_1(M_{\rm ext})\simeq\mathbb Z.
$$

Logo, pode existir uma 1-forma fechada e não exata:

$$
dA=0,
\qquad
A\ne d\chi
\quad
\text{globalmente}.
$$

## 2. Representante harmônico

No exterior cilíndrico ideal, o representante harmônico da classe de
cohomologia é:

$$
A_{\rm harm}
=
\frac{\Phi}{2\pi}\,d\theta.
$$

Em coordenadas vetoriais usuais:

$$
\boldsymbol A_{\rm harm}
=
\frac{\Phi}{2\pi r}\,\boldsymbol e_\theta.
$$

Ele satisfaz:

$$
dA_{\rm harm}=0
\quad
\text{em }M_{\rm ext},
$$

mas:

$$
\oint_\gamma A_{\rm harm}=\Phi
$$

para qualquer curva $\gamma$ que enlace o solenoide uma vez.

## 3. Holonomia

O observável físico é a holonomia:

$$
\operatorname{Hol}_\gamma(A)
=
\exp\left[
\frac{iq}{\hbar c}\oint_\gamma A
\right].
$$

Para o solenoide:

$$
\operatorname{Hol}_\gamma(A)
=
\exp\left[
\frac{iq\Phi}{\hbar c}
\right].
$$

Assim, o deslocamento relativo de fase é:

$$
\Delta\varphi
=
\frac{q\Phi}{\hbar c}.
$$

Para o elétron, usando $q=-e$:

$$
\Delta\varphi
=
-\frac{e\Phi}{\hbar c}
$$

com sinal dependente da orientação escolhida para $\gamma$.

## 4. Leitura GDQ

Na GDQ, o potencial $A$ não precisa ser interpretado como entidade fundamental
independente. Ele é a conexão efetiva do setor de calibre emergente, isto é, a
forma que registra cisalhamento/holonomia da geometria no canal externo.

O núcleo do solenoide fornece um contorno excluído. A solução exterior é
plana em curvatura local:

$$
F=0,
$$

mas carrega memória topológica global:

$$
[A]\in H^1(M_{\rm ext}).
$$

Portanto, a fase AB é uma consequência de:

$$
\text{ação oficial}
\to
\text{setor efetivo de conexão}
\to
\text{domínio perfurado}
\to
\text{classe }[A]
\to
\text{holonomia}.
$$

## 5. Mayer--Vietoris

Cubra o exterior por dois abertos:

$$
M_{\rm ext}=U_N\cup U_S.
$$

Em cada patch:

$$
A_N=d\chi_N,
\qquad
A_S=d\chi_S.
$$

Na interseção:

$$
A_N-A_S=d(\chi_N-\chi_S).
$$

A função de transição:

$$
g_{NS}
=
\exp\left[
\frac{iq}{\hbar c}(\chi_N-\chi_S)
\right]
$$

carrega o cociclo. A integral de contorno mede precisamente essa falha de
trivialização global:

$$
\frac{q}{\hbar c}\oint_\gamma A
=
\frac{q\Phi}{\hbar c}.
$$

Esse é o papel correto de Mayer--Vietoris na Q46: ele organiza a colagem dos
potenciais locais e mostra por que $A$ pode ser localmente puro calibre, mas
globalmente observável.

## 6. Invariância de calibre

Sob:

$$
A\mapsto A+d\chi,
$$

temos:

$$
\oint_\gamma A
\mapsto
\oint_\gamma A+\oint_\gamma d\chi.
$$

Para $\chi$ globalmente bem definida:

$$
\oint_\gamma d\chi=0.
$$

Logo:

$$
\operatorname{Hol}_\gamma(A+d\chi)
=
\operatorname{Hol}_\gamma(A).
$$

Se $\chi$ é multivalorada, a mudança admissível preserva a holonomia física
quando:

$$
\frac{q}{\hbar c}\oint_\gamma d\chi
\in
2\pi\mathbb Z.
$$

Portanto, a invariância de calibre é preservada.

## 7. Mecanismo local adicional

O elemento adicional da GDQ não é uma nova fase AB. A fase ideal já é a
holonomia.

O mecanismo adicional é a resposta local de interface: o solenoide, como
contorno material, impõe uma impedância geométrica ao setor de conexão. Em
linguagem reduzida:

$$
\mathsf R_{\rm sol}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

No limite ideal blindado, essa resposta só fixa a classe harmônica $[A]$ e
recupera a eletrodinâmica convencional.

Para solenoides reais, a mesma resposta pode produzir correções de envelope,
visibilidade ou atraso de fase por:

$$
A_{\rm eff}
=
A_{\rm harm}
+\delta A_{\rm surf},
$$

com:

$$
\delta A_{\rm surf}
\sim
\mathsf R_{\rm sol}J_{\rm beam}.
$$

Sem calcular $\mathsf R_{\rm sol}$ da Hessiana oficial para um aparato real,
essas correções permanecem programa futuro.

