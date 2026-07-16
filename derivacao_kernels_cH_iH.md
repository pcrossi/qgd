# Derivação geométrica dos kernels de circulação e acoplamento magnético

> **Status após a auditoria de Noether:** este documento é um diagnóstico para
> o caso em que circulação e momento magnético sejam observáveis distintos.
> Para Stern--Gerlach, se o campo externo acopla ao mesmo fluxo de Noether que
> define a circulação, aplica-se `teorema_noether_zeeman_gdq.md`: a parte
> mínima tem \(Z_{\rm N}=1\), enquanto eventual excesso magnético vem da
> resposta transversal do próprio background. Kernels arbitrários continuam
> desnecessários.

## 1. Objetivo

O problema variacional do perfil torsional contém dois funcionais:

\[
\mathcal C_H[t]
\quad\text{e}\quad
\mathcal I_H[t].
\]

Este documento determina sua natureza geométrica e responde se eles devem ser
identificados.

O resultado é:

\[
\boxed{
\mathcal C_H\text{ é, em geral, funcional de holonomia/fluxo de traço;}
\qquad
\mathcal I_H\text{ é funcional volumétrico de resposta magnética.}
}
\]

Logo:

\[
\boxed{
\mathcal I_H=\mathcal C_H
}
\]

não é identidade automática. Ela exige uma lei constitutiva e uma identidade
de localização adicionais.

---

## 2. Conexão de fase e circulação

Na região sem nós, defina a 1-forma adimensional de fase

\[
\mathfrak a
=\frac1\hbar dS_R
\]

localmente. Em presença de defeito, \(\mathfrak a\) deve ser tratada como
conexão local de um fibrado, e sua curvatura é

\[
\mathfrak f=d\mathfrak a.
\]

Para um ciclo \(\gamma=\partial D\) que liga o defeito:

\[
\boxed{
\frac1\hbar\oint_\gamma dS_R
=\oint_\gamma\mathfrak a
=\int_D\mathfrak f.
}
\]

No setor semi-inteiro, a holonomia é

\[
\exp\left(i\oint_\gamma\mathfrak a\right)=-1,
\]

ou seja,

\[
\oint_\gamma\mathfrak a
=\pi\pmod{2\pi}.
\]

Essa é uma condição sobre a conexão de fase.

---

## 3. Torção de Bismut projetada

A 3-forma de torção é \(H\). Dada a velocidade ou normal temporal física
\(u\), sua projeção espacial é a 2-forma

\[
\boxed{
\mathcal T=\iota_uH.
}

No setor de Hopf:

\[
\mathcal T(r,P)
=t(r)n^i(P)\Sigma_i^+.
\]

Para transformar a holonomia de fase numa restrição sobre \(t\), é necessária
uma relação constitutiva entre as duas curvaturas:

\[
\boxed{
\mathfrak f
=\lambda_T\,\mathcal P_D(\mathcal T)
+d\beta.
}

Aqui:

- \(\lambda_T\) é a soldagem fase--torção;
- \(\mathcal P_D\) é o pullback/projeção para a superfície de ligação;
- \(d\beta\) representa mudança local de gauge sem alterar o período fechado.

O manuscrito afirma que a vorticidade atua como fonte da torção, mas ainda não
deriva globalmente essa igualdade com coeficiente normalizado.

---

## 4. Kernel de circulação

Usando Stokes e a relação constitutiva:

\[
\mathcal C_H[t]
=\lambda_T\int_D\mathcal P_D(\mathcal T).
\]

Para ansatz radial fatorizado:

\[
\mathcal P_D(\mathcal T)
=t(r_D)\,omega_D,
\]

onde \(r_D\) indica a localização da superfície de ligação. Então:

\[
\boxed{
\mathcal C_H[t]
=\lambda_TA_Dt(r_D),
}

com

\[
A_D=\int_D\omega_D.
\]

No espaço funcional radial, isso corresponde a um kernel de distribuição:

\[
\boxed{
c_H(r)
=\lambda_TA_D\delta(r-r_D).
}

Se a superfície possuir espessura física, a delta é substituída por um perfil
localizado determinado pela colagem.

Portanto, a circulação é naturalmente um funcional de traço/fluxo, não uma
integral uniforme de todo o volume radial.

---

## 5. Distinção entre circulação e número de Chern

Há dois invariantes diferentes:

1. holonomia da conexão de fase ao redor de um ciclo físico;
2. número de Chern da fibração de Hopf:

   \[
   c_1
   =\frac1{2\pi}\int_{S^2}F_H\in\mathbb Z.
   \]

A Q42 já identificou que a fibra \(S^1\) é contrátil no espaço total \(S^3\)
e não pode ser usada diretamente como gerador de \(\pi_1(S^3)\).

Assim, o valor semi-inteiro de spin, a holonomia \(-1\) e \(c_1=\pm1\) são
estruturas relacionadas, mas não são a mesma integral.

O kernel \(c_H\) só fica completamente determinado depois de especificada a
superfície de ligação correta no espaço perfurado.

---

## 6. Kernel de acoplamento magnético

O acoplamento externo é

\[
S_{\rm int}
=\frac q c\int
\langle\mathcal T,F_{\rm app}\rangle d\mu.
\]

Para campo lentamente variável e levantamento equivarante:

\[
F_{\rm app}
=\ell_BB^i\Sigma_i^+.
\]

Como

\[
\langle\Sigma_i^+,\Sigma_j^+\rangle=\delta_{ij},
\]

segue:

\[
S_{\rm int}^{\rm red}
=\frac{q\ell_B}{c}
n^iB_i
\int_{r_c}^{\infty}
w_H(r)t(r)dr.
\]

Portanto:

\[
\boxed{
\mathcal I_H[t]
=\int_{r_c}^{\infty}w_H(r)t(r)dr,
}

e

\[
\boxed{i_H(r)=w_H(r).}
\]

Para campo não uniforme:

\[
i_H(r;X)
=w_H(r)B_i(X+r)/B_i(X),
\]

com a expansão multipolar já derivada.

O kernel magnético é, portanto, volumétrico e ponderado pela medida oficial.

---

## 6.1 Teste espectral do caso de traço no bordo

O problema reduzido foi avaliado também com o operador axial da Q42,

\[
K_Hu=-\frac1w(wu')'+2u,
\qquad w(x)=e^{-x^2/4},
\]

e uma fonte unitária fraca em \(x=0\). A circulação-resposta é o traço
\(C_{\rm resp}=u(0)\). Para cada kernel magnético define-se

\[
Z_H=\frac{\mathcal I_H[u]}{u(0)}.
\]

O cálculo convergente fornece

\[
Z_{\rm uniforme}\longrightarrow0.375000,
\qquad
Z_{\rm local}(\ell=0.4)\longrightarrow0.701977.
\]

Robin altera fortemente \(u(0)\), mas não esses fatores normalizados dentro da
precisão numérica. Isso é consistente com a linearidade: o dado Robin controla
a amplitude da resposta, enquanto a divisão pelo traço deixa a forma
normalizada da extensão para o bulk. Já a troca do kernel magnético altera
\(Z_H\), confirmando que circulação e momento integrado são observáveis
distintos.

Os dados e o status científico estão em
`interface_medida/saida_boundary_kernels_IH.md`.

---

## 7. Por que os kernels não coincidem genericamente

As formas naturais são:

\[
c_H(r)
\sim\delta(r-r_D),
\]

\[
i_H(r)
\sim w_H(r).
\]

Logo:

\[
\boxed{
c_H\ne i_H
}
\]

em geral.

A circulação fixa o fluxo em uma seção ligada ao defeito; o momento magnético
mede a resposta integrada de toda a distribuição de corrente/torção.

Essa diferença é análoga à distinção entre carga total e momento de uma
distribuição: a carga pode ser topológica, enquanto o momento depende do
perfil espacial.

---

## 8. Identidade necessária para localização

Para que a integral volumétrica seja reduzida ao fluxo topológico, seria
necessária uma identidade on-shell:

\[
\boxed{
\int_{\Omega_perp}w_Ht\,dr
=Z_{\rm loc}
\int_D\mathcal P_D(\mathcal T).
}

Em linguagem de funcionais:

\[
\boxed{
\mathcal I_H[t_*]
=Z_{\rm loc}\mathcal C_H[t_*].
}

O fator \(Z_{\rm loc}\) poderia surgir de:

1. equação de movimento de primeira ordem;
2. conservação radial que torne o fluxo constante;
3. localização do integrando numa classe de cohomologia;
4. identidade de transgressão;
5. saturação de uma cota tipo BPS;
6. termo de bordo da solução completa.

Nenhuma dessas identidades foi ainda demonstrada para o background torsional
da Q42.

---

## 9. Integração por partes e momento magnético

O Capítulo 19 usa

\[
j^\mu=\nabla_\alpha\mathcal T^{\alpha\mu}.
\]

O acoplamento de corrente

\[
\frac q c\int A_\mu j^\mu dV
\]

é integrado por partes para produzir

\[
\frac q{2c}
\int\mathcal T^{\mu\nu}F_{\mu\nu}dV
\]

mais o termo de bordo.

Essa identidade demonstra gauge-invariância e relaciona corrente a torção,
mas não transforma a integral volumétrica de \(\mathcal T\) em holonomia de
fase. Para isso ainda é necessária a relação
\(\mathfrak f=\lambda_T\mathcal T\) e uma localização on-shell.

---

## 10. Kernels radiais propostos pela geometria

Para o primeiro problema radial honesto, usar:

### Circulação

\[
\boxed{
\mathcal C_H[t]
=\lambda_TA_Dt(r_c)
}

se a superfície de ligação está no estômato.

### Magnetismo uniforme

\[
\boxed{
\mathcal I_H[t]
=\int_{r_c}^{\infty}
w_H(r)t(r)dr.
}

### Magnetismo não uniforme

\[
\boxed{
\mathcal I_H^i[t;X]
=\int w_H(r)t(r)B^i(X+r)dr.
}

Esses kernels substituem os gaussianos arbitrários do teste anterior por
objetos com interpretação geométrica precisa.

---

## 11. Solução variacional com circulação de bordo

Se o vínculo é

\[
t(r_c)=t_c,
\qquad
t_c=\frac{C_{1/2}}{\lambda_TA_D},
\]

o problema de energia mínima torna-se um problema de Dirichlet no estômato,
ou Robin se a colagem possuir impedância finita.

Para o operador \(K_H\), a solução de norma mínima é a extensão harmônica
ponderada do dado de bordo:

\[
\boxed{
K_Ht_*=0,
\qquad
t_*(r_c)=t_c,
\qquad
t_*(\infty)=0.
}

No operador axial cilíndrico da Q42, essa é precisamente a estrutura da função
\(\eta\) usada no cálculo DtN:

\[
t_*(x)=t_c\eta(x),
\qquad
\eta(0)=1,
\qquad
\eta(\infty)=0.
\]

Essa observação fornece uma ponte melhor que tratar a circulação como fonte
volumétrica.

---

## 12. Fórmula específica usando a solução da Q42

Para

\[
\eta(x)
=\frac{U(2,1/2,x^2/4)}{U(2,1/2,0)},
\]

o perfil torsional diagnóstico seria

\[
t_*(x)
=\frac{C_{1/2}}{\lambda_TA_D}\eta(x).
\]

O momento torna-se

\[
\boxed{
I_H
=\frac{C_{1/2}}{\lambda_TA_D}
\int_0^\infty w_H(x)\eta(x)dx.
}

Logo:

\[
\boxed{
Z_{\rm loc}
=\frac1{\lambda_TA_D}
\int_0^\infty w_H(x)\eta(x)dx.
}

Agora a pergunta “a integral \(1/2\) passa para o momento?” torna-se:

\[
\boxed{Z_{\rm loc}=1?}
\]

Isso depende de \(w_H\), \(\lambda_T\), \(A_D\) e da identificação do
operador axial com o torsional.

---

## 13. Relação com a condição Robin

Se a colagem do estômato impõe

\[
(\partial_r+R_H)t|_{r_c}=J_c,
\]

a circulação pode aparecer como fonte de bordo \(J_c\), não como valor
Dirichlet fixo.

Nesse caso:

\[
t_*=C_{1/2}K_{H,R}^{-1}\delta_{r_c}
\]

após a normalização apropriada. Essa é a versão distribucional testada
numericamente no próximo artefato.

---

## 14. Resultado para o valor \(1/2\)

Se a teoria já demonstrou

\[
C_{1/2}=\frac12
\]

na convenção adimensional relevante, então:

\[
\boxed{
I_H
=\frac12Z_{\rm loc}.
}

Somente uma das seguintes condições permite concluir \(I_H=1/2\):

1. \(Z_{\rm loc}=1\) por identidade on-shell;
2. a definição física de \(I_H\) coincide com a de \(C_H\);
3. a normalização de soldagem fixa
   \(\lambda_TA_D=\int w_H\eta\).

A terceira possibilidade é uma escolha de normalização; para ser preditiva,
ela deve vir da ação ou da quantização de carga, não do resultado desejado.

---

## 15. O que foi derivado

1. \(c_H\) como kernel de fluxo/traço;
2. \(i_H\) como kernel volumétrico ponderado;
3. necessidade da soldagem fase--torção \(\lambda_T\);
4. distinção entre holonomia e Chern;
5. condição de localização on-shell;
6. interpretação do perfil \(\eta\) da Q42 como extensão de dado de bordo;
7. fórmula \(I_H=C_{1/2}Z_{\rm loc}\);
8. condições exatas para transmitir o valor \(1/2\).

---

## 16. O que permanece

1. derivar \(\lambda_T\) da equação constitutiva GDQ;
2. fixar a superfície \(D\) e \(A_D\);
3. demonstrar que \(K_H=L_H\) para a 3-forma torsional;
4. calcular o peso magnético \(w_H\);
5. avaliar \(Z_{\rm loc}\);
6. decidir se a identidade de localização é teorema ou normalização.

## 17. Próximo passo

Calcular numericamente a resposta do operador \(L_H\) a uma fonte de bordo e
comparar:

\[
\mathcal C_H[t]=t(0),
\qquad
\mathcal I_H[t]=\int e^{-x^2/4}t(x)dx.
\]

Isso fornece o primeiro valor diagnóstico de \(Z_{\rm loc}\) para o
background cilíndrico, ainda com \(\lambda_TA_D=1\).

## 18. Status

\[
\boxed{
\text{kernels derivados por sua natureza geométrica;}
\quad
\mathcal C_H\ne\mathcal I_H\text{ genericamente;}
\quad
I_H=\tfrac12Z_{\rm loc}.
}
\]
