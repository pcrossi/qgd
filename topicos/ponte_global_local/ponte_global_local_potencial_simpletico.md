# Ponte global--local — potencial simplético e energia cosmológica

## 1. Escopo

Este documento deriva a forma potencial simplética necessária para avaliar o
vínculo energético

$$
\mathcal C_E[X]=\mathcal H_\xi[X]-E_H.
$$

Não se importa uma energia de Einstein--Hilbert. A construção parte da ação
oficial e mantém

$$
H=d_J^c\omega.
$$

## 2. Forma real da densidade em uma fatia de $\gamma$

Escreva

$$
f=u+iv,
\qquad
w=\mathcal U
=\frac{e^{-u}}{(4\pi z_\tau)^4}.
$$

Na leitura hermitiana real da Questão 4, a densidade espacial é

$$
\mathbf L
=C_\tau w
\left[
\tau\left(
R_{\rm LC}-\frac1{12}|H|^2
+|\nabla u|^2+|\nabla v|^2
\right)
+u-4
\right]dV_g,
$$

onde

$$
C_\tau=\frac{\hbar}{\Lambda_C^2}
$$

e a integração externa $d\tau/\tau$ será restaurada no fim. O fator
$(4\pi z_\tau)^{-4}$ pode ser complexo ao longo de $\gamma$; a carga física é
obtida depois da prescrição real/causal já fixada na Questão 4.

## 3. Variações

Considere

$$
\eta=(h,\dot J,\varphi,\psi),
$$

com

$$
h=\delta g,
\qquad
\varphi=\delta u,
\qquad
\psi=\delta v.
$$

A variação da medida é

$$
\delta(wdV_g)
=w\left(\frac12\operatorname{tr}_gh-\varphi\right)dV_g.
$$

Esse termo não contém derivadas de $eta$ e, portanto, contribui às equações
de Euler--Lagrange, mas não ao potencial simplético.

## 4. Concomitante da curvatura

A identidade métrica

$$
\delta R_{\rm LC}
=-\langle\operatorname{Ric},h\rangle
+\nabla_a\left(
\nabla_bh^{ab}-\nabla^a\operatorname{tr}h
\right)
$$

fornece

$$
\boxed{
\Theta_R^a(X;h)
=C_\tau\tau w
\left(
\nabla_bh^{ab}-\nabla^a\operatorname{tr}h
\right).
}
$$

As derivadas de $w$ produzidas ao integrar por partes pertencem ao operador
de Euler--Lagrange ponderado. O fluxo de bordo é o vetor acima.

## 5. Concomitante do campo complexo

Dos termos cinéticos resulta

$$
\delta|\nabla u|^2
=-h^{ab}\nabla_au\nabla_bu
+2\nabla^au\nabla_a\varphi,
$$

e analogamente para $v$. Assim,

$$
\boxed{
\Theta_f^a(X;\varphi,\psi)
=2C_\tau\tau w
\left(
\nabla^au\,\varphi
+\nabla^av\,\psi
\right).
}
$$

## 6. Concomitante da torção dependente

Defina o operador linearizado

$$
\mathscr D_H\eta
:=D_{(g,J)}(d_J^c\omega_g)[h,\dot J].
$$

Ele é de primeira ordem em $(h,\dot J)$. Seu concomitante de Green
$\mathfrak B_H$ é definido invariantemente pela identidade

$$
\int_\Omega w
\langle H,\mathscr D_H\eta\rangle dV
=\int_\Omega
\langle\mathscr D_H^*(wH),\eta\rangle dV
+\int_{\partial\Omega}\mathfrak B_H(X;\eta).
$$

Essa equação fixa sinais e normalização sem tratar $H$ como campo
independente. A contribuição torsional é

$$
\boxed{
\boldsymbol\Theta_H(X;\eta)
=-\frac{C_\tau\tau}{6}\mathfrak B_H(X;\eta).
}
$$

No setor de $J$ fixo, a parte principal é

$$
\mathscr D_H(h,0)
=d_J^c(\delta\omega_h)
+\text{termos algébricos},
$$

e $\mathfrak B_H$ reduz ao concomitante de $d_J^c$ entre
$\delta\omega_h$ e $wH$. As variações de $J$ devem ser mantidas no cálculo
global; descartá-las mudaria a Hessiana física.

## 7. Potencial simplético oficial

Somando os três setores e restaurando o contorno causal,

$$
\boxed{
\boldsymbol\Theta_{\rm GDQ}(X;\eta)
=\int_\gamma
\left(
\boldsymbol\Theta_R
+\boldsymbol\Theta_f
+\boldsymbol\Theta_H
\right)\frac{d\tau}{\tau}.
}
$$

Termos sem derivadas das variações não aparecem nessa expressão.

## 8. Corrente simplética

Para duas perturbações $\eta_1$ e $\eta_2$, define-se

$$
\boldsymbol\omega_{\rm GDQ}
(X;\eta_1,\eta_2)
=\delta_{\eta_1}\boldsymbol\Theta_{\rm GDQ}(X;\eta_2)
-\delta_{\eta_2}\boldsymbol\Theta_{\rm GDQ}(X;\eta_1).
$$

Essa corrente é a quantidade que decide a integrabilidade da energia. Não é
suficiente que a corrente de Noether seja conservada.

## 9. Corrente e carga de Noether

Para o gerador de tempo físico reconstruído $\xi$,

$$
\mathbf J_\xi
=\boldsymbol\Theta_{\rm GDQ}(X;\mathcal L_\xi X)
-\iota_\xi\mathbf L_{\rm GDQ}.
$$

On shell,

$$
d\mathbf J_\xi=0.
$$

Localmente existe uma forma de carga $\mathbf Q_\xi$ tal que

$$
\mathbf J_\xi=d\mathbf Q_\xi.
$$

A variação hamiltoniana é

$$
\boxed{
\delta\mathcal H_\xi
=\int_{\partial\Sigma}
\left(
\delta\mathbf Q_\xi
-\iota_\xi\boldsymbol\Theta_{\rm GDQ}(X;\delta X)
\right).
}
$$

## 10. Condição de integrabilidade

Para existir uma função $\mathcal H_\xi[X]$ independente do caminho no espaço
de configurações, é necessário e, localmente, suficiente que

$$
\boxed{
\int_{\partial\Sigma}
\iota_\xi\boldsymbol\omega_{\rm GDQ}
(X;\eta_1,\eta_2)=0
}
$$

para todas as perturbações admissíveis.

Os dados escalares $L_{\rm cos}$, $R_{\rm cos}$ e $E_H$ não garantem sozinhos
essa condição. É necessário selecionar uma polarização de fronteira.

## 11. Polarização cosmológica admissível

A escolha mínima compatível com os dados do projeto é:

1. fixar a classe conforme da métrica induzida no contorno causal;
2. fixar $\mathcal L_1=L_{\rm cos}$ e $\mathcal R_3=R_{\rm cos}$;
3. fixar a carga relativa e os fluxos de Noether;
4. permitir somente variações conjugadas que obedeçam à colagem DtN.

Em notação de traços, se $q$ é o dado de configuração e $\pi$ seu momento,
o subespaço de fronteira deve ser lagrangiano:

$$
\int_{\partial\Sigma}
\left(
\delta_1\pi\,\delta_2q
-\delta_2\pi\,\delta_1q
\right)=0.
$$

Condições de Dirichlet, Neumann ou Robin auto-adjuntas são casos particulares.
A colagem física seleciona a condição Robin por

$$
\Lambda_-+\Lambda_+^{\rm eff}=0.
$$

Nessa polarização, o fluxo simplético pelo contorno se anula e
$\mathcal H_\xi$ é integrável localmente.

## 12. Resultado

Foram derivados:

1. o potencial simplético métrico ponderado;
2. o potencial dos campos $u$ e $v$;
3. o concomitante correto da torção dependente;
4. a corrente simplética;
5. a condição necessária e suficiente de integrabilidade;
6. a polarização de fronteira que torna $\mathcal H_\xi$ bem definido.

## 13. Pendência reduzida

A energia cosmológica deixou de ser um símbolo abstrato. Para sua avaliação
numérica ainda é necessário:

1. expandir $\mathfrak B_H$ no ansatz exterior escolhido;
2. resolver o background estacionário vinculado;
3. integrar $\delta\mathcal H_\xi$ a partir de um background de referência
   com a mesma topologia e polarização.

## 14. Status

$$
\boxed{
\boldsymbol\Theta_{\rm GDQ}
\text{ e o critério de integrabilidade estão construídos;}
\quad
\mathcal H_\xi
\text{ aguarda avaliação no exterior warped.}
}
$$
