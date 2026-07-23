# Q24 — Teorema assintótico de registros

## 1. Enunciado

Se o aparelho define um operador de medição GDQ auto-adjunto e setorialmente
gapped, então a dinâmica aberta reduzida suprime exponencialmente as coerências
entre registros e implementa fisicamente os projetores de Born da Q22.

---

## 2. Hipóteses

### H1 — Ação oficial preservada

A dinâmica fundamental continua sendo a ação oficial da GDQ. O aparelho entra
por fonte e contorno:

\[
J_{\rm app},\qquad \mathsf R_{\rm app}.
\]

### H2 — Background admissível

Existe um background estacionário durante a janela de medição:

\[
\Phi_*=(g_*,f_*,\bar f_*),
\]

com medida:

\[
\mathcal U_*=\frac{\rho_*}{(4\pi z_\tau)^n}.
\]

### H3 — Operador físico

O operador:

\[
\mathcal H_{\rm meas}
=
P^{\rm phys}
\operatorname{Hess}_{\Phi_*}
\mathcal S_{\rm GDQ}^{S+A+E}
P^{\rm phys}
\]

é auto-adjunto no domínio de aparelho.

### H4 — Setores de registro

Existem projetores setoriais:

\[
\Pi_i\Pi_j=\delta_{ij}\Pi_i,
\qquad
\sum_i\Pi_i=I_{\rm reg}.
\]

### H5 — Gap

\[
\Delta_{\rm meas}>0.
\]

### H6 — Born já vem da Q22

As probabilidades operacionais são:

\[
P(i)=\operatorname{Tr}(\rho_SP_i).
\]

---

## 3. Prova

Pela H3, o semigrupo:

\[
e^{-\tau\mathcal H_{\rm meas}}
\]

é bem definido no setor reduzido de densidade.

Pelas H4 e H5, cada registro possui cluster espectral separado. Portanto, para
\(i\ne j\):

\[
\|\Pi_i e^{-\tau\mathcal H_{\rm meas}}\Pi_j\|
\le
C_{ij}e^{-\Delta_{ij}\tau}.
\]

Logo, no estado correlacionado:

\[
|\Psi\rangle
=
\sum_i c_i|s_i\rangle|A_i\rangle|E_i\rangle,
\]

os fatores fora da diagonal satisfazem:

\[
|\Gamma_{ij}(\tau)|
\le
C_{ij}e^{-\Delta_{ij}\tau}.
\]

Assim:

\[
\rho_{SA}(\tau)
=
\sum_{ij}
c_ic_j^*\Gamma_{ij}(\tau)
|s_i,A_i\rangle\langle s_j,A_j|
\]

converge para:

\[
\boxed{
\rho_{SA}^{\rm diag}
=
\sum_i |c_i|^2
|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

Pela H6:

\[
|c_i|^2
=
\operatorname{Tr}(\rho_SP_i)
\]

no caso puro discreto, e a forma geral é:

\[
\boxed{
\rho_{SA}^{\rm diag}
=
\sum_i
\operatorname{Tr}(\rho_SP_i)
|s_i,A_i\rangle\langle s_i,A_i|.
}
\]

Se após o registro o estado é condicionado ao setor \(i\), então:

\[
\rho_{S|i}
=
\frac{P_i\rho_SP_i}{\operatorname{Tr}(\rho_SP_i)}.
\]

A repetição imediata da medição dá:

\[
\boxed{
\operatorname{Tr}(\rho_{S|i}P_i)=1.
}
\]

Isso prova repetibilidade.

---

## 4. Resultado único

A prova acima fecha:

1. seleção de base pelo aparelho;
2. decoerência assintótica;
3. estabilidade de registros;
4. Born operacional;
5. repetibilidade.

Ela não prova, sozinha, que só um ramo existe ontologicamente no sistema total
fechado. O adendo `resultado_unico_bacias_microgeometria.md` mostra como
elevar a antiga hipótese de bacia a um teorema condicional.

A condição adicional é que o espaço físico de microgeometrias \(A+E\) possua
um funcional de Lyapunov/Morse com bacias hiperbólicas:

\[
\boxed{
\mathcal C_{A+E}^{\rm reg}
=
\bigcup_i\mathcal B_i
\;\dot\cup\;
\mathcal N,
\qquad
\mu(\mathcal N)=0.
}
\]

Então, para quase toda condição inicial real:

\[
\boxed{
\Phi_0\in\mathcal B_i
\text{ para um único }i,
\qquad
\Phi(\tau;\Phi_0)\to R_i.
}
\]

A probabilidade do resultado é a medida da bacia:

\[
\boxed{
\mathbb P(R_i)
=
\mu_{\rm init}(\mathcal B_i)
=
\operatorname{Tr}(\rho_SP_i).
}
\]

Assim, o resultado único fica provado condicionalmente quando as hipóteses de
Morse/Lyapunov, hiperbolicidade, gap e regularidade da medida inicial são
verificadas para o aparelho.

---

## 5. Status da Q24 após o loop 1--6

\[
\boxed{
\text{Q24 fechada condicionalmente como teorema assintótico de registros e
bacias reais.}
}
\]

Condição:

\[
\boxed{
\mathcal H_{\rm meas}\text{ auto-adjunto, setores }R_i\text{ bem definidos e }
\Delta_{\rm meas}>0.
}
\]

Ressalva:

\[
\boxed{
\text{resultado único ontológico é teorema condicional de bacias reais,
dependente de verificar H1--H5 para o aparelho.}
}
\]

Essa ressalva não reabre a decoerência, Born operacional, repetibilidade ou
assintoticidade dos registros. Ela apenas separa o teorema geral de sua
verificação em aparelhos concretos.
