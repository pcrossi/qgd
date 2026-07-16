# Q42 — Background estacionário mínimo da ação oficial

## 1. Redução na fatia normal

A fatia normal necessária ao elo de Hopf é
\(\mathbb C^2\simeq\mathbb R^4\). Considere o ansatz

\[
 ds_\perp^2=dr^2+a(r)^2d\Omega_3^2,
 \qquad f=F(r)\in\mathbb R.
\]

No ponto estacionário do funcional de Perelman, a equação métrica é

\[
 \operatorname{Ric}+\nabla^2F=\frac1{2\tau}g.
\]

Para o ansatz acima, suas duas equações independentes são

\[
 -3\frac{a''}{a}+F''=\frac1{2\tau},
\]

\[
 \frac{2(1-a'^2)-aa''}{a^2}
 +\frac{F'a'}a=\frac1{2\tau}.
\]

## 2. Solução exata no bulk

A solução regular plana é

\[
 \boxed{a_*(r)=r},
 \qquad
 \boxed{F_*(r)=\frac{r^2}{4\tau}+F_0}.
\]

Ela dá \(\operatorname{Ric}=0\) e
\(\nabla^2F_*=g/(2\tau)\), portanto resolve exatamente ambas as equações.
Esta não é uma aproximação numérica nem um potencial escolhido para ajustar
o espectro: é o shrinker gaussiano da ação na fatia \(\mathbb C^2\).

Em todo \(\mathbb R^4\), a medida normalizada é

\[
 d\mu_*=(4\pi\tau)^{-2}e^{-r^2/(4\tau)}d^4x.
\]

Se o núcleo \(r<r_c\) for excisado, a massa gaussiana exterior é

\[
 Q_2(x_c)=e^{-x_c}(1+x_c),
 \qquad x_c=\frac{r_c^2}{4\tau}.
\]

Assim, a normalização exterior exige

\[
 \boxed{F_0=\log Q_2(x_c)}.
\]

## 3. O que a excisão muda

No bordo interior, a normal exterior ao domínio \(r\ge r_c\) é
\(n=-\partial_r\). Logo,

\[
 n\cdot\nabla F_*=-\frac{r_c}{2\tau}\ne0.
\]

Consequentemente, integrações por partes da primeira e segunda variações
produzem termos em \(r=r_c\). A ação oficial de bulk, tal como congelada no
manuscrito, não especifica um funcional de bordo nem fixa quais combinações
de \(\delta g\), \(\delta f\) são mantidas. Portanto, ela não seleciona uma
matriz Robin única \(\mathsf R_0\).

Isto gera uma alternativa matemática precisa:

1. **Dirichlet geométrico:** fixar a métrica induzida e \(f\) no estômato;
2. **Robin externo:** declarar a impedância como dado físico do objeto/aparelho;
3. **ação de bordo derivada:** fornecer o termo de contorno GDQ cuja variação
   produz \(\mathsf R_0\).

Sem escolher uma dessas classes, o operador da Hessiana não possui domínio
auto-adjunto determinado. Portanto seus autovalores físicos não estão
definidos unicamente.

## 4. Consequência para os quatro coeficientes

O background de bulk permite fixar a escala geométrica e o peso radial. Para
um aparelho especificado,

\[
 \Delta=\frac{|g_{\rm geom}|\mu_B}{\hbar}|B_\perp|,
 \qquad
 v=\frac{|g_{\rm geom}|\mu_B}{\hbar}
 |\partial_tB_\parallel+\boldsymbol u\cdot\nabla B_\parallel|.
\]

Mas \(\kappa_H^{\rm SG}\) requer o domínio Robin da Hessiana e
\(\Gamma_{\rm SG}\) requer, adicionalmente, a lei causal de mobilidade e a
covariância térmica da impedância. Esses objetos não são determinados pelo
background estático de bulk.

## 5. Status

Foi construído um background estacionário exato da ação oficial na fatia
normal correta. Não foi construída uma solução de **estômato com bordo
dinâmico**, porque a ação oficial atual não contém o dado variacional que
seleciona esse bordo. Esta é agora a pendência mínima, localizada e testável;
não é legítimo escondê-la por meio de um potencial radial fenomenológico.

