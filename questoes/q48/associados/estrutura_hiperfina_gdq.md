# Q48 — Estrutura hiperfina na leitura GDQ

## 1. Enunciado

A estrutura hiperfina do hidrogênio depende do acoplamento entre:

1. circulação/spin do elétron;
2. circulação/spin do próton;
3. momento magnético mínimo protegido por Noether;
4. resposta interna/anômala dos sólitons;
5. fator de forma e contorno do próton.

Na GDQ, o Hamiltoniano hiperfino não é postulado como termo fundamental. Ele é
a redução efetiva da resposta magnética de dois backgrounds com circulação.

---

## 2. Canal magnético mínimo

Da Q43:

$$
\boldsymbol\mu_\ell
=
g_\ell\frac{q_\ell}{2m_\ell c}\boldsymbol S_\ell.
$$

A parte mínima do elétron é:

$$
g_e^{(0)}=2.
$$

A correção geométrica é:

$$
g_e
=
2(1+a_e),
\qquad
a_e
=
\frac{\Delta\gamma_e}{\gamma_{0,e}}.
$$

Para o próton, o momento magnético vem do setor bariônico Q40/Q43:

$$
\boldsymbol\mu_p
=
g_p\frac{e}{2m_pc}\boldsymbol I.
$$

Se $g_p$ for usado como dado experimental, a comparação é fenomenológica. Se
vier da Q40/Q43, a comparação é previsão condicional.

---

## 3. Forma efetiva

A interação spin--spin reduzida tem a estrutura:

$$
H_{\rm hfs}
=
\frac{8\pi}{3}
\boldsymbol\mu_e\cdot\boldsymbol\mu_p\,
\delta^{(3)}(\mathbf r)
+
H_{\rm dip}
+
H_{\rm recoil}
+
H_{\rm ff}.
$$

Na GDQ, essa forma aparece como limite pontual da impedância magnética:

$$
\mathsf R_{\rm mag}^{p,e}
=
\mathsf R_{\rm contact}
+
\mathsf R_{\rm dip}
+
\mathsf R_{\rm ff}
+
\mathsf R_{\rm recoil}.
$$

Para estados $ns$, a parte de contato domina:

$$
\Delta E_{\rm hfs}(ns)
\propto
\boldsymbol\mu_e\cdot\boldsymbol\mu_p\,|\psi_{ns}(0)|^2.
$$

Como:

$$
|\psi_{ns}(0)|^2
=
\frac{(Z\alpha\mu c/\hbar)^3}{\pi n^3},
$$

a escala da hiperfina é:

$$
\Delta E_{\rm hfs}(ns)
\propto
\alpha^4
\frac{\mu^3}{m_em_p}
\frac{g_eg_p}{n^3}.
$$

---

## 4. Fórmula operacional em SI

Para o estado $1s$, usando momento magnético do próton $\mu_p$ e magneton de
Bohr $\mu_B$, a frequência de Fermi pode ser escrita na forma operacional:

$$
\nu_F
=
\frac{16}{3}
Z^3\alpha^2 cR_\infty
\left(\frac{\mu}{m_e}\right)^3
\frac{\mu_p}{\mu_B}.
$$

Essa expressão é útil para comparação, mas sua classificação depende da
origem de $\mu_p$:

$$
\boxed{
\mu_p\text{ experimental}\Rightarrow\text{comparação fenomenológica.}
}
$$

$$
\boxed{
\mu_p\text{ derivado pela Q40/Q43}\Rightarrow\text{previsão condicional.}
}
$$

---

## 5. O que fecha e o que permanece condicional

Fechado estruturalmente:

1. a origem do acoplamento hiperfino como resposta de circulação;
2. a necessidade de $g=2$ mínimo;
3. a dependência em $|\psi(0)|^2$ para estados $s$;
4. a separação entre contato, dipolo, recuo e fator de forma.

Condicional:

1. valor metrológico de $\mu_p$ se não for herdado da Q40;
2. correções radiativas/geométricas superiores de $g_e$ e $g_p$;
3. correções de estrutura interna do próton.

---

## 6. Como obter os termos finais por $\mathsf R_p$

A fórmula líder de Fermi usa o próton como momento magnético pontual. Os
termos finais aparecem quando substituímos esse ponto por uma interface
protônica dinâmica.

O dado geométrico é a Hessiana física de superfície:

$$
K_p
=
\begin{pmatrix}
K_{YY} & K_{YI}\\
K_{IY} & K_{II}
\end{pmatrix},
$$

e sua impedância efetiva:

$$
\mathsf R_p
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}.
$$

O acoplamento hiperfino completo é obtido projetando $\mathsf R_p$ no canal
magnético/spinorial do par elétron--próton:

$$
\Delta H_{\rm hfs}^{p}
=
P_{\rm hfs}^\dagger
\left(
\mathsf R_p-\mathsf R_{\rm point}
\right)
P_{\rm hfs}.
$$

Aqui $P_{\rm hfs}$ contém:

1. o traço espinorial do elétron no núcleo;
2. a orientação de circulação do próton;
3. o canal de magnetização superficial;
4. a projeção de fator de forma.

Então:

$$
\Delta\nu_{\rm hfs}^{p}
=
\frac1h
\langle 1s,F|
\Delta H_{\rm hfs}^{p}
|1s,F\rangle_{\Delta F=1}.
$$

Mais explicitamente:

$$
\nu_{\rm hfs}
=
\nu_F
+
\Delta\nu_{\rm recoil}
+
\Delta\nu_{\rm surf}
+
\Delta\nu_{\rm geom}.
$$

Cada termo é obtido por uma projeção diferente da mesma impedância:

$$
\Delta\nu_{\rm recoil}
=
\frac1h
\langle 1s|
P_{\rm recoil}^\dagger
\Delta\mathsf R_p
P_{\rm recoil}
|1s\rangle,
$$

$$
\Delta\nu_{\rm surf}
=
\frac1h
\langle 1s|
P_{\rm surf}^\dagger
\Delta\mathsf R_p
P_{\rm surf}
|1s\rangle,
$$

$$
\Delta\nu_{\rm geom}
=
\frac1h
\langle 1s|
P_{\rm mag}^\dagger
\Delta\mathsf R_p
P_{\rm mag}
|1s\rangle.
$$

onde:

$$
\Delta\mathsf R_p=\mathsf R_p-\mathsf R_{\rm point}.
$$

Interpretação:

- $P_{\rm recoil}$ mede a resposta de centro de massa/massa reduzida;
- $P_{\rm surf}$ mede a extensão finita da distribuição de magnetização;
- $P_{\rm mag}$ mede a deformação geométrica/anômala do canal magnético
  protônico.

---

## 7. Algoritmo de cálculo

1. Tomar o background protônico $\Phi_{p,*}$ da Q40.
2. Linearizar a ação oficial na camada de superfície $Y_p$.
3. Separar os modos físicos:

   $$
   \eta_Y=(\eta_{\rm normal},\eta_{\rm shear},\eta_{\rm mag},\eta_{\rm tor}).
   $$

4. Montar os blocos $K_{YY}$, $K_{YI}$, $K_{II}$.
5. Remover modos nulos e gauge pelo projetor físico $P_{\rm phys}$.
6. Calcular:

   $$
   \mathsf R_p^{\rm phys}
   =
   P_{\rm phys}
   \left(
   K_{YY}-K_{YI}K_{II}^{-1}K_{IY}
   \right)
   P_{\rm phys}.
   $$

7. Subtrair o limite pontual:

   $$
   \Delta\mathsf R_p
   =
   \mathsf R_p^{\rm phys}-\mathsf R_{\rm point}.
   $$

8. Projetar nos canais hiperfinos:

   $$
   P_{\rm recoil},\quad
   P_{\rm surf},\quad
   P_{\rm mag}.
   $$

9. Calcular os elementos de matriz no estado $1s$.
10. Somar:

    $$
    \nu_{\rm hfs}
    =
    \nu_F
    +
    \Delta\nu_{\rm recoil}
    +
    \Delta\nu_{\rm surf}
    +
    \Delta\nu_{\rm geom}.
    $$

Esse procedimento é direto, mas exige a Hessiana de superfície do próton.

Classificação:

$$
\boxed{
\text{programa metrológico derivado; não é novo axioma e não é ajuste.}
}
$$

---

## 8. Efeito adicionado numericamente

O primeiro efeito adicional já calculável é o canal magnético líder da Q43:

$$
a_e^{(1)}=\frac{\alpha}{2\pi}.
$$

Ele modifica:

$$
\nu_F\mapsto\nu_F(1+a_e^{(1)}).
$$

Numericamente:

$$
\nu_F=1.418840090665555\times10^9\,{\rm Hz},
$$

e:

$$
\nu_F(1+a_e^{(1)})
=
1.420487945355137\times10^9\,{\rm Hz}.
$$

O erro relativo contra a linha de 21 cm passa de:

$$
-1.102263\times10^{-3}
$$

para:

$$
5.786627\times10^{-5}.
$$

A avaliação reduzida da impedância coletiva de superfície da Q40 na escala
atômica fornece correção desprezível:

$$
\mathcal I_\Sigma(1/a_B^*)\simeq-2.09\times10^{-21}.
$$

Portanto:

$$
\boxed{
\text{o próximo termo relevante não é a impedância coletiva }q^4,\text{ mas
recuo/Zemach/Hessiana magnética superior.}
}
$$

O efeito de Zemach de casca superficial foi então adicionado. Para duas cascas
finas elétrica e magnética no raio $r_p$:

$$
r_Z^{\rm shell}=\frac43r_p.
$$

Com $r_p=0.84077876545\,{\rm fm}$:

$$
r_Z^{\rm shell}=1.121038353933\,{\rm fm}.
$$

A correção:

$$
\delta_Z=-2\alpha\frac{\mu c}{\hbar}r_Z
$$

fornece:

$$
\delta_Z=-4.234604693327742\times10^{-5}.
$$

Assim:

$$
\nu_F(1+a_e^{(1)})(1+\delta_Z)
=
1.420427793305934\times10^9\,{\rm Hz}.
$$

O erro relativo cai para:

$$
1.551778\times10^{-5}.
$$

O resíduo remanescente fica concentrado em:

$$
\boxed{
\text{recuo relativístico + Hessiana magnética superior.}
}
$$
