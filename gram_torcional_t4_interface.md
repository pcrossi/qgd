# Matriz de Gram torsional de \(T^4\) e seleção do triplet de Hopf

## 1. Objetivo

Este documento calcula explicitamente as seis 2-formas harmônicas do toro
interno oficial, suas normas e sua decomposição quiral. O resultado fornece a
base necessária para determinar:

1. a normalização cinética do canal torsional;
2. a dependência da impedância nos raios internos;
3. a distinção entre base topológica e base canônica;
4. o triplet que pode acoplar ao vetor axial de Hopf;
5. a direção selecionada pelo campo do aparelho.

---

## 2. Toro retangular

Use coordenadas angulares

\[
0\le\theta^a<2\pi,
\qquad a=1,2,3,4,
\]

e métrica diagonal

\[
\boxed{
ds_{T^4}^2
=\sum_{a=1}^4R_a^2(d\theta^a)^2.
}
\]

O volume é

\[
\boxed{
V_{T^4}
=(2\pi)^4R_1R_2R_3R_4.
}

O coframe ortonormal é

\[
e^a=R_a,d\theta^a.
\]

---

## 3. Base topológica de fluxo unitário

Para cada par \(a<b\), defina

\[
\boxed{
\omega_{ab}
=\frac{d\theta^a\wedge d\theta^b}{(2\pi)^2}.
}

Então, no 2-ciclo coordenado \(C_{ab}\):

\[
\boxed{
\int_{C_{ab}}\omega_{cd}
=\delta_{ab,cd}.
}

Essa é a base apropriada para integralidade de períodos e cargas topológicas.

As seis formas são:

\[
\omega_{12},\ \omega_{13},\ \omega_{14},\
\omega_{23},\ \omega_{24},\ \omega_{34}.
\]

---

## 4. Produto interno não ponderado

Para a métrica diagonal:

\[
|d\theta^a\wedge d\theta^b|^2
=\frac1{R_a^2R_b^2}.
\]

Logo:

\[
\begin{aligned}
G^{\rm top}_{ab,cd}
&=\int_{T^4}
\langle\omega_{ab},\omega_{cd}\rangle,dV\\
&=\delta_{ab,cd}
\frac{R_1R_2R_3R_4}{R_a^2R_b^2}.
\end{aligned}
\]

Se \(\{c,d\}\) é o par complementar a \(\{a,b\}\):

\[
\boxed{
G^{\rm top}_{ab,ab}
=\frac{R_cR_d}{R_aR_b}.
}

Assim:

\[
\boxed{
G^{\rm top}
=\operatorname{diag}
\left(
\frac{R_3R_4}{R_1R_2},
\frac{R_2R_4}{R_1R_3},
\frac{R_2R_3}{R_1R_4},
\frac{R_1R_4}{R_2R_3},
\frac{R_1R_3}{R_2R_4},
\frac{R_1R_2}{R_3R_4}
\right)
}
\]

na ordem \((12,13,14,23,24,34)\).

Os elementos aparecem em pares recíprocos:

\[
G_{12}G_{34}
=G_{13}G_{24}
=G_{14}G_{23}=1.
\]

---

## 5. Produto ponderado da GDQ

A matriz física é

\[
\boxed{
G_{ab,cd}^{\rm GDQ}
=\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma
\left[
\int_{\Sigma_2\times T^4}
\mathcal U_*
\langle\omega_{ab},\omega_{cd}\rangle
dV_\perp
\right].
}

Se, na célula local, a medida se fatoriza e é aproximadamente constante no
toro:

\[
\mathcal U_*(z)
\simeq u_{\Sigma}(z_\Sigma)u_T,
\]

então:

\[
\boxed{
G^{\rm GDQ}
=\mathcal N_A G^{\rm top},
}

onde

\[
\mathcal N_A
=\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma
\left[
u_T\int_{\Sigma_2}u_\Sigma\,dV_{\Sigma_2}
\right].
\]

Toda a dependência anisotrópica nos raios fica em \(G^{\rm top}\); a escala
global fica em \(\mathcal N_A\).

---

## 6. Base canônica ortonormal

Defina

\[
\boxed{
\widehat\omega_{ab}
=\frac{\omega_{ab}}
{\sqrt{G^{\rm top}_{ab,ab}}}.
}

Então:

\[
\int_{T^4}
\langle\widehat\omega_{ab},
\widehat\omega_{cd}\rangle dV
=\delta_{ab,cd}.
\]

Equivalentemente:

\[
\widehat\omega_{ab}
=\frac{e^a\wedge e^b}{\sqrt{V_{T^4}}}
\]

até a convenção comum de \((2\pi)\) já absorvida pela base de período unitário.

Distinção essencial:

- \(\omega_{ab}\): período inteiro, normalização topológica;
- \(\widehat\omega_{ab}\): energia unitária, normalização cinética.

Não se pode usar simultaneamente período unitário e norma unitária sem carregar
a matriz de Gram.

---

## 7. Operador de Hodge

Fixe a orientação

\[
e^1\wedge e^2\wedge e^3\wedge e^4>0.
\]

No coframe ortonormal:

\[
*(e^1\wedge e^2)=e^3\wedge e^4,
\]

\[
*(e^1\wedge e^3)=-e^2\wedge e^4,
\]

\[
*(e^1\wedge e^4)=e^2\wedge e^3.
\]

Na base topológica:

\[
\boxed{
*\omega_{ab}
=s_{ab,cd}
\sqrt{\frac{G^{\rm top}_{ab,ab}}
{G^{\rm top}_{cd,cd}}}
\,\omega_{cd},
}

onde \(s_{ab,cd}=\pm1\) é o sinal da orientação e \(cd\) é o par
complementar.

Como os elementos complementares são recíprocos, isso equivale a

\[
*\omega_{ab}
=s_{ab,cd}G^{\rm top}_{ab,ab}\omega_{cd}.
\]

Em todos os casos:

\[
\boxed{*^2=1\quad\text{em }\Lambda^2(T^4).}
\]

---

## 8. Decomposição auto-dual e anti-auto-dual

Na base canônica, defina o triplet auto-dual:

\[
\boxed{
\begin{aligned}
\Sigma_1^+&=\frac1{\sqrt2}
(\widehat\omega_{12}+\widehat\omega_{34}),\\
\Sigma_2^+&=\frac1{\sqrt2}
(\widehat\omega_{13}-\widehat\omega_{24}),\\
\Sigma_3^+&=\frac1{\sqrt2}
(\widehat\omega_{14}+\widehat\omega_{23}).
\end{aligned}
}
\]

E o triplet anti-auto-dual:

\[
\boxed{
\begin{aligned}
\Sigma_1^-&=\frac1{\sqrt2}
(\widehat\omega_{12}-\widehat\omega_{34}),\\
\Sigma_2^-&=\frac1{\sqrt2}
(\widehat\omega_{13}+\widehat\omega_{24}),\\
\Sigma_3^-&=\frac1{\sqrt2}
(\widehat\omega_{14}-\widehat\omega_{23}).
\end{aligned}
}
\]

Eles satisfazem:

\[
*\Sigma_i^\pm=\pm\Sigma_i^\pm,
\]

\[
\langle\Sigma_i^\pm,\Sigma_j^\pm\rangle=\delta_{ij},
\qquad
\langle\Sigma_i^+,\Sigma_j^-\rangle=0.
\]

Portanto:

\[
\boxed{
\mathcal H^2(T^4)
=\mathcal H^2_+\oplus\mathcal H^2_-,
\qquad
\dim\mathcal H^2_+=\dim\mathcal H^2_-=3.
}

---

## 9. Relação com \(SU(2)_+\times SU(2)_-\)

Em quatro dimensões euclidianas:

\[
\operatorname{Spin}(4)
\simeq SU(2)_+\times SU(2)_-.
\]

As formas auto-duais e anti-auto-duais transformam, respectivamente, como

\[
(\mathbf3,\mathbf1),
\qquad
(\mathbf1,\mathbf3).
\]

O vetor de Hopf possui três componentes. Portanto, um acoplamento equivarante
linear entre o setor de Hopf e as formas internas deve selecionar um dos dois
tripletos:

\[
\boxed{
\omega_{\rm Hopf}(P)
=n^i(P)\Sigma_i^\chi,
\qquad
\chi=+\ \text{ou}\ -.
}

A escolha de \(\chi\) não pode ser feita apenas por conveniência. Ela deve vir
de:

1. orientação do estômato;
2. quiralidade da conexão de Bismut;
3. sinal da circulação;
4. condição de colagem com a folha física.

---

## 10. Norma do modo de Hopf

Como o triplet é ortonormal e \(|\boldsymbol n|=1\):

\[
\begin{aligned}
\|\omega_{\rm Hopf}(P)\|^2
&=n^in^j
\langle\Sigma_i^\chi,\Sigma_j^\chi\rangle\\
&=n^in_i=1.
\end{aligned}
\]

Logo, na base canônica:

\[
\boxed{
Z_x^{\rm Hopf}=\mathcal N_A
}
\]

independentemente da orientação \(P\), como exige a isotropia interna antes do
campo externo.

Os raios não desaparecem fisicamente: eles entram na conversão entre a base de
fluxo inteiro e a base canônica, portanto entram nos valores permitidos de
carga/período e no acoplamento \(g_X\).

---

## 11. Seleção pelo aparelho

Se a fonte clássica e o perfil do estômato produzem componentes \(j_i^\chi\),
o funcional de interface reduzido é

\[
S_{\rm int}^{\rm red}
\propto
n^i(P)j_i^\chi.
\]

Defina

\[
\boldsymbol j^\chi=(j_1^\chi,j_2^\chi,j_3^\chi).
\]

A direção selecionada é

\[
\boxed{
\boldsymbol n_A
=\frac{\boldsymbol j^\chi}{|\boldsymbol j^\chi|}.
}

O acoplamento é

\[
\boxed{
g_X
=g_0|\boldsymbol j^\chi|,
}

onde \(g_0\) contém o prefator de carga, a integral radial do estômato e a
normalização do modo coletivo.

Assim, o eixo de medida não é escolhido no espaço interno à mão: ele é a
direção do vetor de sobreposição produzido pelo campo clássico.

---

## 12. Efeito dos raios no acoplamento topológico

Escreva uma forma canônica em termos da base integral:

\[
\widehat\omega_{ab}
=\frac{\omega_{ab}}{\sqrt{G^{\rm top}_{ab,ab}}}.
\]

Logo uma componente de período inteiro \(m_{ab}\omega_{ab}\) possui amplitude
canônica

\[
q_{ab}^{\rm can}
=m_{ab}\sqrt{G^{\rm top}_{ab,ab}}.
\]

Portanto, para números topológicos fixos \(m_{ab}\), os raios controlam a
energia e a impedância efetiva:

\[
\boxed{
\|m_{ab}\omega_{ab}\|^2
=m_{ab}^2\frac{R_cR_d}{R_aR_b}.
}

Essa é a ponte correta entre:

- integralidade da carga;
- moduli geométricos do toro;
- normalização cinética;
- intensidade de acoplamento.

---

## 13. Caso isotrópico

Se

\[
R_1=R_2=R_3=R_4=R_T,
\]

então:

\[
\boxed{G^{\rm top}=I_6.}
\]

A base integral já é ortonormal no produto não ponderado. Os dois tripletos
possuem a mesma rigidez e a seleção quiral depende somente da conexão e da
colagem.

Nesse caso:

\[
Z_t^{\rm Hopf}
=\frac{\mathcal N_A}{c_{\rm phys}^2},
\qquad
Z_x^{\rm Hopf}=\mathcal N_A,
\]

\[
\boxed{
\gamma_A=\frac{\mathcal N_A}{c_{\rm phys}}.
}

---

## 14. Caso anisotrópico

Quando os raios são diferentes, a base integral não é canônica. Ainda assim,
a base auto-dual construída após normalização continua ortonormal.

A anisotropia aparece em:

1. períodos físicos das formas canônicas;
2. vetor de acoplamento \(j_i^\chi\);
3. energias de setores com números topológicos fixos;
4. possível mistura se a medida \(\mathcal U_*\) não fatorizar;
5. estabilização dos moduli \(R_a\).

Não se deve concluir que a impedância de uma orientação livre depende de
\(P\); isso quebraria a isotropia do módulo antes do aparelho. A dependência
angular só aparece quando a fonte ou o background já quebra a simetria.

---

## 15. Matriz geral para toro não diagonal

Se a métrica interna não for diagonal, a fórmula geral é

\[
\boxed{
G_{ab,cd}^{\rm top}
=\frac1{(2\pi)^4}
\int_{T^4}
\frac12
(\delta_a^m\delta_b^n-\delta_a^n\delta_b^m)
(\delta_c^p\delta_d^q-\delta_c^q\delta_d^p)
g_{mp}^{-1}g_{nq}^{-1}
\sqrt{\det g}\,d^4\theta.
}

Para métrica constante, essa expressão é algébrica. O background final pode
exigir diagonalizar essa matriz antes de construir os tripletos físicos.

---

## 16. O que foi fechado

1. seis formas harmônicas de período unitário;
2. matriz de Gram exata para raios arbitrários;
3. base canônica;
4. ação do Hodge e verificação \(*^2=1\);
5. decomposição \(3+3\) auto-dual/anti-auto-dual;
6. mapa equivarante do vetor de Hopf para um triplet;
7. norma isotrópica do modo de Hopf;
8. seleção do eixo pelo vetor de sobreposição;
9. dependência dos setores topológicos nos raios.

---

## 17. O que permanece

1. selecionar \(\chi=+\) ou \(-\) pela conexão concreta;
2. calcular \(\mathcal N_A\) pela projeção causal;
3. determinar os raios \(R_a\) pelo background de Ricci--Bismut;
4. calcular \(j_i^\chi\) com o perfil do campo clássico;
5. avaliar \(g_0\) e \(g_X\);
6. incluir mistura entre formas se \(g_*\) ou \(\mathcal U_*\) não forem
   diagonais/fatorizáveis.

## 18. Próximo passo

Construir um teste algébrico da matriz de Gram e do operador de Hodge para
raios arbitrários. Depois, usar a orientação do estômato e o sinal da torção de
Bismut para tentar selecionar o triplet \(\chi\).

O teste foi executado em `interface_medida/test_gram_t4.py`, com saída em
`interface_medida/saida_gram_t4.md`. A seleção geométrica foi desenvolvida em
`selecao_quiral_hopf_bismut.md`: na orientação complexa padrão de
\(\mathbb C^2\), o triplet hipercähler de Hopf é auto-dual.

## 19. Status

\[
\boxed{
\text{matriz de Gram e decomposição quiral de }T^4
\text{ calculadas exatamente;}
\quad
\text{seleção de quiralidade e escala causal permanecem abertas.}
}
\]
