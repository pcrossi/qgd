---
title: "Fonte clássica, Hessiana, Schur e readout espectral"
status: "teorema estrutural condicional"
---

# Fonte clássica, Hessiana, Schur e readout espectral

## 1. Enunciado

Considere um background GDQ admissível $\Phi_*$ na presença de dados clássicos
de um aparelho. Depois de fixar vínculos, gauge, domínio e contorno, sejam

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}
$$

a Hessiana física e $J_{\rm app}$ a fonte linear produzida pelo aparelho.
Se $K_{\rm phys}$ é inversível no subespaço relevante, então

$$
\delta\Phi_{\rm app}
=
K_{\rm phys}^{-1}J_{\rm app}
$$

resolve exatamente

$$
K_{\rm phys}\delta\Phi_{\rm app}
=
J_{\rm app}.
$$

Quando graus internos são eliminados on shell, a resposta de fronteira é o
complemento de Schur. Se seus canais formam uma base ortonormal espectral e o
estado-resposta é normalizado, os pesos de registro são positivos e somam
um.

## 2. Fonte clássica

O aparelho não fornece um operador quântico fundamental. Ele fornece campos,
materiais, suportes e condições de contorno. Na aproximação linear, sua
contribuição aparece como um funcional de fonte:

$$
\delta S_{\rm app}
=
-\langle J_{\rm app},\delta\Phi\rangle.
$$

A equação variacional linearizada é

$$
K_{\rm phys}\delta\Phi
-J_{\rm app}
=0.
$$

Assim, $J_{\rm app}$ é um dado externo do problema experimental, enquanto
$K_{\rm phys}$ continua vindo da segunda variação da ação oficial no
background com aquele domínio físico.

## 3. Solução linear

Se existe um Green físico $G_{\rm phys}$ tal que

$$
K_{\rm phys}G_{\rm phys}=I,
$$

defina

$$
\delta\Phi_{\rm app}
=
G_{\rm phys}J_{\rm app}.
$$

Então

$$
K_{\rm phys}\delta\Phi_{\rm app}
=
K_{\rm phys}G_{\rm phys}J_{\rm app}
=
J_{\rm app}.
$$

Essa identidade não demonstra a existência do Green. A existência exige
domínio fechado, condições de contorno, remoção dos modos zero e controle do
espectro.

## 4. Eliminação do interior

Decomponha a perturbação em traço de fronteira e interior:

$$
\delta\Phi
=
\begin{pmatrix}
b\\
i
\end{pmatrix},
$$

e escreva

$$
K_{\rm phys}
=
\begin{pmatrix}
K_{bb}&K_{bi}\\
K_{ib}&K_{ii}
\end{pmatrix}.
$$

A equação interna homogênea é

$$
K_{ib}b+K_{ii}i=0.
$$

Se $K_{ii}^{-1}$ existe,

$$
i_*(b)
=
-K_{ii}^{-1}K_{ib}b.
$$

O resíduo de fronteira torna-se

$$
\begin{aligned}
r_b(b)
&=
K_{bb}b+K_{bi}i_*(b)
\\
&=
\left(
K_{bb}
-K_{bi}K_{ii}^{-1}K_{ib}
\right)b.
\end{aligned}
$$

Portanto,

$$
\boxed{
\mathsf R_{\rm app}
=
K_{bb}
-K_{bi}K_{ii}^{-1}K_{ib}.
}
$$

Esse operador é a impedância Schur/DtN efetiva. Nenhum coeficiente adicional
foi inserido para obtê-lo.

## 5. Canais de registro

Depois da reconstrução do Hilbert físico, suponha que a Hessiana complexificada
possua uma base ortonormal finita de canais:

$$
K_{\rm phys}\phi_i
=
E_i\phi_i.
$$

Se o estado-resposta normalizado é

$$
\psi_{\rm app}
=
G_{\rm phys}J_{\rm app},
\qquad
\|\psi_{\rm app}\|=1,
$$

o peso do canal $i$ é

$$
p_i
=
\left|
\langle\phi_i,\psi_{\rm app}\rangle
\right|^2.
$$

Parseval fornece

$$
\sum_i p_i
=
\|\psi_{\rm app}\|^2
=1,
$$

e Cauchy--Schwarz fornece

$$
0\leq p_i\leq1.
$$

Aqui os projetores não foram inseridos antes da dinâmica. Eles são a
representação espectral dos canais selecionados pela Hessiana e pelo contorno
do aparelho.

## 6. O que a camada espectral isolada não prova

A diagonalização e Born fornecem canais e frequências operacionais. Um evento
individual ainda exige uma dinâmica de captura. Se $\mathcal B_i$ é a bacia
microscópica do registro $i$, a condição de fechamento é

$$
\mu_{\rm micro}(\mathcal B_i)
=
p_i.
$$

Essa igualdade não segue apenas de Parseval ou do complemento de Schur. No
módulo geral `ApparatusBornReadout`, a realização por bacias permanece uma
estrutura com essa obrigação explicitamente visível.

No setor QND gaussiano, a obrigação é descarregada separadamente: a
normalização das verossimilhanças, a conservação da esperança dos pesos e a
absorção terminal implicam a igualdade Born--bacias. A prova humana está em
[[teorema_born_bacias_qnd_gaussiano|Teorema Born–bacias para aparelhos QND gaussianos]].

## 7. Certificação Lean

O módulo
[ClassicalApparatusResponse.lean](../../../formal/GDQ/ClassicalApparatusResponse.lean)
prova:

1. $K_{\rm phys}^{-1}J_{\rm app}$ resolve a equação linearizada;
2. a resposta interna resolve sua equação estacionária;
3. o resíduo de fronteira coincide exatamente com o complemento de Schur;
4. a inversão da resposta reduzida resolve a equação de interface.

O módulo
[ApparatusBornReadout.lean](../../../formal/GDQ/ApparatusBornReadout.lean)
prova:

1. o estado-resposta resolve a equação com fonte;
2. os pesos dos canais espectrais são não negativos;
3. os pesos somam exatamente um;
4. cada peso é menor ou igual a um;
5. bacias que realizam esses pesos também formam uma distribuição
   normalizada.

O módulo
[QNDBornBasins.lean](../../../formal/GDQ/QNDBornBasins.lean)
prova adicionalmente:

1. a condição QND é preservada pelo complemento de Schur;
2. os blocos fora da diagonal desaparecem entre projetores ortogonais;
3. as verossimilhanças normalizadas produzem posteriores positivos e
   normalizados;
4. a esperança física de cada posterior é exatamente seu peso inicial;
5. a covariância é de Gram, positiva e tangente ao simplex;
6. sob absorção terminal, a medida de cada bacia é exatamente o peso inicial.

## 8. Status

O resultado é estruturalmente fechado sob as hipóteses declaradas. Permanecem
condicionais por aparelho:

- derivação concreta de $J_{\rm app}$;
- background estacionário;
- Hessiana física e seu domínio;
- inversibilidade do bloco interno;
- base espectral estável;
- verificação QND e separação dos sinais no aparelho concreto;
- parâmetros materiais e ambientais.

Esses dados pertencem ao experimento e à aplicação da ação oficial; não são
novos axiomas da GDQ.
