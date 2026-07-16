# Q42 — Derivação dos coeficientes físicos a partir da GDQ

## 1. Convenção do sistema reduzido

No subespaço dos dois projetores de Hopf, retire a energia comum e escreva

\[
 H_2(t)=\frac{\hbar}{2}
 \left[\omega_\parallel(t)\sigma_z+omega_\perp(t)\sigma_x\right].
\]

O acoplamento magnético já estabelecido no manuscrito é

\[
 H_Z=-\frac{g_{\rm geom}\mu_B}{2}\,\boldsymbol\sigma\cdot\boldsymbol B,
 \qquad \mu_B=\frac{e\hbar}{2m_e}.
\]

Após uma escolha de sinais/eixos que não altera probabilidades,

\[
 \omega_\parallel=\frac{g_{\rm geom}\mu_B}{\hbar}B_\parallel,
 \qquad
 \omega_\perp=\frac{g_{\rm geom}\mu_B}{\hbar}B_\perp.
\]

Comparando com o Hamiltoniano usado no teste de Landau--Zener,

\[
 H_2/\hbar=\frac12(vt\,\sigma_z+\Delta\,\sigma_x),
\]

obtém-se, sem ajuste,

\[
 \boxed{\Delta=\frac{|g_{\rm geom}|\mu_B}{\hbar}|B_\perp|}
 \quad[\mathrm{s}^{-1}],
\]

\[
 \boxed{v=\left|\frac{d\omega_\parallel}{dt}\right|
 =\frac{|g_{\rm geom}|\mu_B}{\hbar}
 \left|\partial_tB_\parallel+\boldsymbol u\cdot\nabla B_\parallel\right|}
 \quad[\mathrm{s}^{-2}].
\]

O campo e a velocidade são dados do aparelho, isto é, condições externas do
problema; não são parâmetros ajustáveis da GDQ. O valor de
\(g_{\rm geom}\) deve vir do setor estacionário de torção da partícula.

## 2. Background estacionário requerido

Se \(\Phi_*=(g_*,f_*,\bar f_*)\) é uma solução estacionária da ação oficial,
ela deve satisfazer as equações de Euler--Lagrange, a normalização de
\(\mathcal U_*\), regularidade exterior e a condição Robin no estômato. No
ansatz radial usado na Q42, isso significa fornecer efetivamente

\[
 \mathcal B_*=
 \{a(r),b(r),c(r),F(r),\Theta(r),r_c,\mathsf R,\mathcal U_*(r)\}.
\]

A Hessiana física, depois da remoção de difeomorfismos e modos zero, define

\[
 \mathbb H_R\Psi_\nu=\lambda_\nu\Psi_\nu,
 \qquad \lambda_\nu>0,
\]

e o coeficiente tangencial \(Z_\nu\) por

\[
 \mathbb H_R(k)\Psi_\nu=
 (\lambda_\nu+Z_\nu k^2+O(k^4))\Psi_\nu.
\]

Para a fonte geométrica do aparelho,

\[
 j_{\nu A}=\langle\Psi_\nu,J_{{\rm SG},A}\rangle_{\mathcal U_*},
\]

a rigidez é

\[
 \boxed{
 \kappa_H^{\rm SG}=
 \frac12(G_{\rm FS})^{AB}
 \sum_\nu\frac{Z_\nu}{\lambda_\nu^2}
 j_{\nu A}^*j_{\nu B}.}
\]

Esta expressão tem normalização física somente se a Hessiana, a medida e as
coordenadas tangenciais forem mantidas com as unidades da ação oficial.

## 3. Taxa de medição/decoerência

Se \(X_R\) é a flutuação da impedância física já projetada no setor axial,

\[
 C_R(t)=\langle X_R(t)X_R(0)\rangle_*
 =\sum_\nu C_\nu e^{-\gamma_\nu|t|},
\]

então

\[
 \boxed{\Gamma_{\rm SG}=
 \frac{\mu^2}{\hbar^2}\sum_\nu\frac{C_\nu}{\gamma_\nu}.}
\]

É essencial distinguir \(\gamma_\nu\), taxa de relaxação em
\(\mathrm{s}^{-1}\), do autovalor estático \(\lambda_\nu\) da Hessiana. A
identificação \(\gamma_\nu=\lambda_\nu\) só é válida depois que a métrica
cinética/mobilidade do fluxo causal for derivada. Os testes reduzidos
anteriores ocultavam essa conversão ao usar unidades adimensionais.

## 4. Resultado da auditoria do repositório

Os documentos atuais fornecem as fórmulas e o sinal positivo, mas não
fornecem os dados de \(\mathcal B_*\), os modos normalizados da Hessiana
oficial, a mobilidade causal nem os pesos térmicos \(C_\nu\). Logo:

- \(\Delta\) e \(v\) estão derivados em função de condições mensuráveis do
  aparelho e de \(g_{\rm geom}\);
- \(\kappa_H^{\rm SG}\) está derivado como momento espectral estático;
- \(\Gamma_{\rm SG}\) está derivado como momento do espectro dinâmico;
- valores numéricos GDQ para os dois últimos ainda não podem ser produzidos
  sem resolver e armazenar o background estacionário.

Preencher números arbitrários nesse ponto não substituiria o modelo de teste:
apenas o renomearia. O arquivo `background_q42.npz` descrito pelo novo
pipeline é o contrato numérico mínimo para completar a substituição.

