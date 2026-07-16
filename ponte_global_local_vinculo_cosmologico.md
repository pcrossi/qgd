# Ponte global--local — vínculo cosmológico variacional

## 1. Objetivo

Construir o bloco cosmológico ausente sem acrescentar um termo fundamental à
ação da GDQ. Os dados externos são:

$$
L_{\rm cos},
\qquad
R_{\rm cos},
\qquad
E_H.
$$

Eles representam, respectivamente, o comprimento do ciclo causal compacto, o
raio efetivo da fibra cosmológica $S^3$ e a energia total fixada na fronteira
causal.

Esses números são condições do problema. Os funcionais que os medem devem ser
construídos a partir de $(g,J,f)$ e da ação oficial.

## 2. Estrutura geométrica prescrita

No setor cosmológico existe uma decomposição geométrica distinguida

$$
TM
=E_4\oplus E_1\oplus E_3,
$$

correspondente a

$$
T^4\times S^1\times S^3.
$$

Sejam $q_1$ e $q_3$ as métricas induzidas em $E_1$ e $E_3$. A decomposição é
parte do dado cosmológico global; ela não é inferida numa carta planar.

## 3. Vínculo do ciclo causal

> **Nota de compatibilidade.** A Questão 2 escolhe a forma-relógio em um
> círculo distinguido de $T^4$, enquanto a primeira versão deste documento
> chamou o quinto ciclo, parametrizado por $s$, de causal. Essas duas escolhas
> não são automaticamente equivalentes. A redução causal vigente em
> `ponte_global_local_exterior_causal.md` mantém $s$ como coordenada radial e
> escolhe $S^1_{\theta_0}\subset T^4$ como relógio. Assim, $\mathcal C_L$
> abaixo mede o quinto ciclo geométrico até que uma equivalência causal seja
> demonstrada.

Se $\Gamma_1$ é o gerador orientado do ciclo $S^1$, define-se

$$
\mathcal L_1[g]
=\int_{\Gamma_1}ds_g.
$$

O primeiro vínculo é

$$
\boxed{
\mathcal C_L[g]
=\log\frac{\mathcal L_1[g]}{L_{\rm cos}}=0.
}
$$

Para uma perturbação métrica $h=\delta g$, com tangente unitária $T$ ao ciclo,

$$
D\mathcal L_1[g]h
=\frac12\int_{\Gamma_1}h(T,T)\,ds_g.
$$

Logo,

$$
D\mathcal C_L[g]h
=\frac1{2\mathcal L_1}
\int_{\Gamma_1}h(T,T)\,ds_g.
$$

Para duas variações afins $h$ e $k$, mantendo a classe do ciclo fixa,

$$
D^2\mathcal L_1[g](h,k)
=-\frac14\int_{\Gamma_1}
h(T,T)k(T,T)\,ds_g.
$$

Equivalentemente, o Hessiano de $\log\mathcal L_1$ é

$$
D^2\mathcal C_L(h,k)
=\frac{D^2\mathcal L_1(h,k)}{\mathcal L_1}
-\frac{D\mathcal L_1(h)D\mathcal L_1(k)}{\mathcal L_1^2}.
$$

Se o ciclo é uma geodésica minimizante não degenerada, a variação de sua
posição acrescenta o termo padrão do índice de Jacobi. No setor homogêneo, a
curva é fixada pela simetria e esse termo desaparece.

## 4. Vínculo do raio da fibra cosmológica

Se $F_3$ é uma fibra $S^3$ e

$$
V_3[g]
=\int_{F_3}dV_{q_3},
$$

define-se o raio volumétrico

$$
\mathcal R_3[g]
=\left(\frac{V_3[g]}{2\pi^2}\right)^{1/3}.
$$

O vínculo é

$$
\boxed{
\mathcal C_R[g]
=\log\frac{\mathcal R_3[g]}{R_{\rm cos}}
=\frac13\log\frac{V_3[g]}{2\pi^2R_{\rm cos}^3}=0.
}
$$

Escrevendo

$$
\operatorname{tr}_3h=q_3^{ab}h_{ab},
$$

tem-se

$$
DV_3[g]h
=\frac12\int_{F_3}\operatorname{tr}_3h\,dV_{q_3},
$$

e

$$
D\mathcal C_R[g]h
=\frac1{6V_3}
\int_{F_3}\operatorname{tr}_3h\,dV_{q_3}.
$$

A segunda variação bilinear do volume é

$$
D^2V_3[g](h,k)
=\int_{F_3}
\left[
\frac14(\operatorname{tr}_3h)(\operatorname{tr}_3k)
-\frac12\operatorname{tr}_3(h^\sharp k^\sharp)
\right]dV_{q_3}.
$$

Portanto,

$$
\boxed{
D^2\mathcal C_R(h,k)
=\frac1{3V_3}D^2V_3(h,k)
-\frac1{3V_3^2}DV_3(h)DV_3(k).
}
$$

Essa Hessiana não é nula para deformações locais, mesmo quando o valor médio
do raio é fixado.

## 5. Vínculo de energia derivado da ação oficial

O parâmetro $\tau$ não é automaticamente o tempo físico. Seja $\xi$ o campo
vetorial que gera a translação do tempo físico reconstruído no contorno
causal. A densidade lagrangiana oficial será denotada por

$$
\mathbf L_{\rm GDQ}(X).
$$

Sua primeira variação define a forma potencial simplética:

$$
\delta\mathbf L_{\rm GDQ}
=\mathbf E(X)\cdot\delta X
+d\boldsymbol\Theta_{\rm GDQ}(X;\delta X).
$$

A corrente de Noether associada a $\xi$ é

$$
\mathbf J_\xi
=\boldsymbol\Theta_{\rm GDQ}(X;\mathcal L_\xi X)
-\iota_\xi\mathbf L_{\rm GDQ}.
$$

On shell,

$$
d\mathbf J_\xi=0.
$$

O Hamiltoniano de Noether é definido por sua variação:

$$
\boxed{
\delta\mathcal H_\xi
=\int_{\partial\Sigma}
\left(
\delta\mathbf Q_\xi
-\iota_\xi\boldsymbol\Theta_{\rm GDQ}(X;\delta X)
\right),
}
$$

onde $\mathbf J_\xi=d\mathbf Q_\xi$ on shell. A integrabilidade exige que a
forma do lado direito seja exata no espaço de configurações admissíveis.

O vínculo energético correto é

$$
\boxed{
\mathcal C_E[X]
=\mathcal H_\xi[X]-E_H=0.
}
$$

Sua primeira variação é a expressão acima. Sua Hessiana é

$$
D^2\mathcal C_E(X)(\eta,\zeta)
=\delta_\zeta
\int_{\partial\Sigma}
\left(
\delta_\eta\mathbf Q_\xi
-\iota_\xi\boldsymbol\Theta_{\rm GDQ}(X;\eta)
\right).
$$

Essa definição usa somente a ação oficial. Não importa o Hamiltoniano de
Einstein--Hilbert nem identifica $\tau$ com tempo físico.

## 6. Vínculo cosmológico completo

O bloco ausente fica definido por

$$
\boxed{
\mathcal C_{\rm cos}[X]
=
\begin{pmatrix}
\mathcal C_L[g]\\
\mathcal C_R[g]\\
\mathcal C_E[X]
\end{pmatrix}=0.
}
$$

Os dados $L_{\rm cos}$, $R_{\rm cos}$ e $E_H$ não são ajustados durante a
solução. Eles definem a folha variacional.

## 7. Sela cosmológica vinculada

O funcional aumentado completo é

$$
\mathscr L
=\mathcal S_{\rm GDQ}
-\lambda_N\mathcal C_N
-\lambda_Q\mathcal C_Q
-\langle\lambda_Y,\mathcal C_Y\rangle
-\lambda_L\mathcal C_L
-\lambda_R\mathcal C_R
-\lambda_E\mathcal C_E.
$$

As equações são

$$
D_X\mathscr L(X_*,\lambda_*)=0,
$$

$$
\mathcal C(X_*)=0.
$$

No minisuperspaço homogêneo, com $x=\log L$ e $y=\log R$, os vínculos
reduzem-se a $x=x_{\rm cos}$ e $y=y_{\rm cos}$. Nesse setor,

$$
\lambda_L=1,
$$

$$
\lambda_R=3-\frac{8\tau}{R_{\rm cos}^2},
$$

antes da contribuição energética. Esses valores são reações dos vínculos,
não constantes fundamentais.

## 8. Hessiana cosmológica vinculada

A Hessiana exterior passa a ser um objeto definido:

$$
\boxed{
\mathbb H_+^{\rm cos}
=D^2\mathcal S_{\rm GDQ}
-\lambda_LD^2\mathcal C_L
-\lambda_RD^2\mathcal C_R
-\lambda_ED^2\mathcal C_E
-\sum_{a\ne L,R,E}\lambda_aD^2\mathcal C_a.
}
$$

O operador físico é

$$
K_+^{\rm phys}
=P^{{\rm phys}\dagger}
\mathbb H_+^{\rm cos}
P^{\rm phys}.
$$

## 9. O que foi efetivamente construído

Foram construídos sem alterar a ação:

1. o funcional de comprimento causal;
2. o funcional de raio volumétrico;
3. suas primeiras e segundas variações métricas;
4. o funcional energético como Hamiltoniano de Noether da ação oficial;
5. sua primeira e segunda variações em forma covariante;
6. o bloco $\mathcal C_{\rm cos}$;
7. a Hessiana cosmológica vinculada.

## 10. Próxima avaliação, agora bem definida

Foi calculada em `ponte_global_local_potencial_simpletico.md` a decomposição
explícita

$$
\boldsymbol\Theta_{\rm GDQ}
$$

em seus setores de curvatura, campo complexo e torção dependente. A
integrabilidade de $\mathcal H_\xi$ foi reduzida à anulação do fluxo
simplético na polarização de fronteira DtN. Resta expandir o concomitante de
Bismut no ansatz exterior e resolver o sistema elíptico vinculado.

## 11. Status

$$
\boxed{
\mathcal C_{\rm cos}
\text{ e }\boldsymbol\Theta_{\rm GDQ}\text{ construídos; avaliação da carga
no background warped ainda pendente.}
}
$$
