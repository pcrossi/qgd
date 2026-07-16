# Corrente simplética da Hessiana oficial da GDQ

## 1. Objetivo e distinção

Derivar da ação oficial a corrente que normaliza os modos da cirurgia. No
setor densidade--fase, ela é a linearização da conservação da densidade. No
sistema completo, a corrente simplética contém também as variações métricas.

Portanto, as afirmações

$$
\nabla_AJ_\rho^A=0
$$

e

$$
\nabla_A\omega^A(\delta_1\Phi,\delta_2\Phi)=0
$$

são relacionadas, mas não idênticas: a primeira é uma corrente de Noether; a
segunda é a corrente bilinear da Hessiana.

## 2. Variáveis reais

Escreva

$$
f=\sigma+i\theta,
\qquad
\sigma=-\log\rho,
\qquad
\theta=\frac{S_R}{\hbar},
$$

e

$$
\mathcal U=\frac{e^{-\sigma}}{(4\pi z_\tau)^4}.
$$

Em um corte de $z_\tau$ fixo, a densidade hermitiana simetrizada nos campos é

$$
\mathcal L_z
=\frac{\hbar}{\Lambda_C^2}\sqrt g\,\mathcal U
\left[
\tau\left(\mathcal R+(\nabla\sigma)^2+(\nabla\theta)^2\right)
+\sigma-4
\right].
$$

O contorno causal será recolocado depois da derivação local.

## 3. Potencial pré-simplético

Para

$$
\delta\mathcal L_z
=\sqrt g\left[
\mathcal E_I\delta\Phi^I+\nabla_A\Theta_z^A(\Phi;\delta\Phi)
\right],
$$

adote $h^{AB}=\delta g^{AB}$ e $h=g_{AB}h^{AB}$. A contribuição do bloco de
curvatura ponderada é

$$
\boxed{
\begin{aligned}
\Theta_{g,z}^A
=\frac{\hbar\tau}{\Lambda_C^2}\big[
&\mathcal U(\nabla_Bh^{AB}-\nabla^Ah)\\
&-(\nabla_B\mathcal U)h^{AB}
+(\nabla^A\mathcal U)h
\big].
\end{aligned}
}
$$

A contribuição de densidade e fase é

$$
\boxed{
\Theta_{f,z}^A
=\frac{2\hbar\tau}{\Lambda_C^2}
\mathcal U
\left(\nabla^A\sigma\,\delta\sigma
+\nabla^A\theta\,\delta\theta\right).
}
$$

Termos sem derivadas das variações contribuem às equações de campo, mas não a
$\Theta^A$. A potencial pré-simplética total é

$$
\Theta_z^A=\Theta_{g,z}^A+\Theta_{f,z}^A.
$$

Como usual, $\Theta^A\mapsto\Theta^A+\nabla_BY^{AB}$ altera apenas termos de
canto; as condições APS/matching devem fixar essa escolha na cirurgia.

## 4. Corrente simplética

Para duas perturbações, defina

$$
\boxed{
\omega_z^A(\Phi;\delta_1\Phi,\delta_2\Phi)
=\delta_1\Theta_z^A(\Phi;\delta_2\Phi)
-\delta_2\Theta_z^A(\Phi;\delta_1\Phi).
}
$$

Antissimetrizando a segunda variação da ação,

$$
\nabla_A\omega_z^A
=\delta_1\mathcal E_I\,\delta_2\Phi^I
-\delta_2\mathcal E_I\,\delta_1\Phi^I.
$$

Se o background satisfaz as equações oficiais e $\delta_1\Phi,delta_2\Phi$
satisfazem a Hessiana linearizada, então

$$
\boxed{\nabla_A\omega_z^A=0.}
$$

Essa é a conservação simplética procurada.

Antes da normalização, devem ser removidas as direções degeneradas de
difeomorfismo e impostos o projetor de fluxo fixo $P_Q$ e as condições de
gauge. A forma resultante no quociente físico é não degenerada quando a
Hessiana física é Fredholm.

## 5. Redução à corrente de densidade

A simetria global

$$
\theta\mapsto\theta+\alpha
$$

fornece a corrente de Noether

$$
\boxed{
J_\theta^A
=\frac{2\hbar\tau}{\Lambda_C^2}
\mathcal U\nabla^A\theta
=\frac{2\tau}{\Lambda_C^2}
\mathcal U\nabla^AS_R.
}
$$

A equação da fase dá

$$
\nabla_AJ_\theta^A=0.
$$

Depois da reconstrução do tempo físico e da identificação da mobilidade, essa
equação assume a forma de continuidade

$$
\partial_t\mathcal U+\nabla_i(\mathcal Uv^i)=0.
$$

O termo $\partial_t\mathcal U$ não vem apenas da simetria global em um corte:
ele requer a reconstrução causal/fluxo conjugado. Essa distinção evita
confundir o parâmetro de fluxo $\tau$ com o tempo físico $t$.

Integrando numa região espacial,

$$
\frac{d}{dt}\int_\Sigma\mathcal U\,d\Sigma
=-\int_{\partial\Sigma}\mathcal Uv^in_i\,dA.
$$

Em uma seção fechada, $\int_\Sigma\mathcal U$ é constante. Na cirurgia, a
perda de densidade do ramo do nêutron é exatamente o fluxo total dos ramos de
saída. Isso fixa a normalização total, mas não a divisão dinâmica entre os
canais $S$ e $T$.

No background fixo, para duas perturbações puras de fase, a corrente
simplética reduz-se ao Wronskiano ponderado

$$
\boxed{
\omega_{\theta,z}^A
=\frac{2\hbar\tau}{\Lambda_C^2}\mathcal U
\left(
\delta_1\theta\nabla^A\delta_2\theta
-\delta_2\theta\nabla^A\delta_1\theta
\right).
}
$$

Assim, a conservação da densidade é o setor diagonal de Noether, enquanto a
normalização de dois modos usa sua polarização bilinear.

## 6. Forma de Green da Hessiana

Para um bloco físico da Hessiana escrito como

$$
L\psi
=-\mathcal U^{-1}\nabla_A
\left(\mathcal U A^{AB}\nabla_B\psi\right)+V\psi,
$$

a identidade de Green é

$$
\boxed{
\nabla_Aj^A(\psi_1,\psi_2)
=\mathcal U\left(\psi_2L\psi_1-\psi_1L\psi_2\right),
}
$$

com

$$
\boxed{
j^A(\psi_1,\psi_2)
=\mathcal U A^{AB}
\left(\psi_1\nabla_B\psi_2-\psi_2\nabla_B\psi_1\right).
}
$$

Para dois modos do kernel, $L\psi_1=L\psi_2=0$ e, portanto,
$\nabla_Aj^A=0$; a conservação independe da hipersuperfície usada para
calcular o fluxo.

## 7. Pullback pelo contorno causal

Como a derivação vale em cada corte, a corrente física de contorno é

$$
\boxed{
\omega_\gamma^A
=\oint_\gamma
\omega_z^A\frac{d\tau}{\tau}.
}
$$

Equivalentemente, parametrizando por $z$,

$$
\omega_\gamma^A
=\oint_\gamma
\frac{dz}{(4\pi z)^4}
\frac{d\tau}{dz}\frac1\tau
\widehat\omega^A(z).
$$

Logo, o mesmo princípio de Laurent seleciona o terceiro jato completo:

$$
\boxed{
\omega_\gamma^A
=\frac{2\pi i}{(4\pi)^4}[z^3]\widehat\omega^A(z)
}
$$

para orientação positiva, incluindo no chapéu o pullback e os pesos que não
foram exibidos.

## 8. Normalização dos quatro modos

Após reconstruir a seção lorentziana física, defina

$$
\boxed{
(\Psi_a,\Psi_b)_\Sigma
=i\int_\Sigma n_A
\omega_\gamma^A(\overline{\Psi_a},\Psi_b)d\Sigma
=s_a\delta_{ab},
}
$$

onde $s_a=+1$ para modos físicos de norma positiva. Na borda da cirurgia, a
orientação APS substitui $n_A$ pela normal de saída e fixa o sinal do fluxo.

As condições procuradas são

$$
(\Psi_n,\Psi_n)=
(\Psi_p,\Psi_p)=
(\Psi_e,\Psi_e)=
(\Psi_{\bar\nu},\Psi_{\bar\nu})=1.
$$

Isso remove a liberdade de reescalar separadamente as quatro pernas. Não
determina, porém, o Green transversal $K_\perp^{-1}$ nem o valor do vértice
entre modos já normalizados.

## 9. Resultado

> A corrente simplética da GDQ é a antissimetrização da variação do potencial
> de bordo da ação oficial. Ela é conservada para soluções da Hessiana. No
> setor fase--densidade, reduz-se ao Wronskiano ponderado pela densidade
> $\mathcal U$ e polariza a corrente de continuidade de Noether.

Portanto,

$$
\boxed{
\text{conservação da densidade}
\longrightarrow
\text{normalização simplética dos modos},
}
$$

mas a igualdade deve ser entendida como redução setorial, não como identidade
do bloco métrico completo.

## 10. Status

- potencial pré-simplético: derivado;
- corrente e lei de conservação: derivadas;
- redução densidade--fase: derivada;
- pullback causal/Laurent: estruturado;
- normalização APS unitária: definida;
- avaliação nos modos bariônicos: pendente das funções próprias de Q40;
- positividade: depende da reconstrução lorentziana e da orientação causal.
