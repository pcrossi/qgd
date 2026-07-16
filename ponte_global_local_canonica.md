# Ponte global--local da GDQ — construção canônica

> [!important] Revisão de escopo
> Este documento permanece canônico para a interface estômato--bulk. A ponte
> entre $T^5\times S^3$ e $\mathbb R^4\times T^4$ é o limite apontado de
> `ponte_global_local_lemas_sem_colar.md`, não uma sela de colagem.

## 1. Finalidade e autoridade

Este documento passa a ser a referência canônica para a construção da ponte
global--local. Ele consolida os resultados válidos dos Lemas 1--6, da redução
do colar, da formulação DtN e das auditorias numéricas.

Os arquivos anteriores permanecem como demonstrações, cálculos e histórico.
Em caso de conflito de status, prevalece este documento, subordinado à ação
oficial e a `memory.md`.

## 2. Afirmação que se pretende demonstrar

Pretende-se construir uma família de backgrounds admissíveis $X_\varepsilon$
no setor cosmológico

$$
M_\varepsilon
=T^4\times S^1_{L_\varepsilon}\times S^3_{R_\varepsilon},
$$

contendo uma interface de estômato $Y_\varepsilon$, tal que:

1. $X_\varepsilon$ seja ponto crítico vinculado da ação oficial;
2. a vizinhança apontada do estômato convirja para o bulk local
   $\mathbb R^4\times T^4$;
3. a Hessiana física possua um cluster ligado separado por gap uniforme;
4. os projetores espectrais correspondentes convirjam;
5. os invariantes globais sejam transportados ao setor local sem serem
   recalculados em cada carta.

## 3. Ação e campos independentes

A única ação fundamental empregada é

$$
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
$$

Os campos independentes são

$$
X=(g,J,f),
$$

com

$$
H=d_J^c\omega_g,
\qquad
\mathcal R=R_{\rm LC}-\frac1{12}|H|^2.
$$

Logo, $H$ não é um campo variacional independente.

## 4. Decomposição geométrica correta

O problema é dividido em três regiões, sem identificá-las:

### 4.1 Interior local

Um colar de Berger termina numa interface finita $Y$:

$$
g_-
=N^2dr^2+a^2(\sigma_1^2+\sigma_2^2)+c^2\sigma_3^2.
$$

A torção dependente é

$$
H
=2c(a\dot a-c)\,\sigma_{123},
\qquad
\dot X=N^{-1}X'.
$$

A conservação strong-KT fixa

$$
h_0=2c(a\dot a-c).
$$

O colar é local e não deve ser prolongado artificialmente até um antipolo
cosmológico.

### 4.2 Interface

A interface transporta os traços dos campos e seus momentos canônicos. A
condição variacional livre é

$$
\Pi_-(X)=\Pi_+(X),
$$

modificada apenas pelos multiplicadores dos vínculos físicos explicitamente
declarados.

### 4.3 Exterior cosmológico

O exterior pertence ao problema multidimensional em
$T^4\times S^1\times S^3$. Sua ação on shell determina um operador
Dirichlet-to-Neumann matricial

$$
\Lambda_+.
$$

O exterior não pode ser substituído pelo mesmo ODE de Berger usado no colar.
O subsector isotrópico está em `ponte_global_local_exterior_warped.md` e foi
usado apenas para validar a álgebra. A redução física compatível com o DtN
interno é o exterior de dois raios em
`ponte_global_local_exterior_berger.md`. Ele mantém o modo anisotrópico que
deve ser testado pela Hessiana.
O adaptador canônico e o resíduo conjunto de duas interfaces estão definidos
em `ponte_global_local_colagem.md`.

## 5. Folha física de vínculos

Os vínculos já estabelecidos são reunidos em

$$
\mathcal C(X)
=\left(
N(X)-1,
Q(X)-q,
\mathcal F_Y(X),
\mathcal Q_{\rm Noether}(X)-q_{\rm N},
\mathcal C_{\rm cos}(X)
\right)=0.
$$

Aqui:

- $N(X)=1$ é a normalização de $\mathcal U$;
- $Q(X)=q$ fixa a carga relativa do estômato;
- $\mathcal F_Y=0$ impõe continuidade de fluxo e momento na interface;
- $\mathcal Q_{\rm Noether}=q_{\rm N}$ fixa as cargas conservadas;
- $\mathcal C_{\rm cos}$ representa os dados cosmológicos globais.

Os quatro primeiros blocos estão formulados. O último foi construído em
`ponte_global_local_vinculo_cosmologico.md` como o conjunto formado pelo
comprimento do ciclo causal, pelo raio volumétrico da fibra $S^3$ e pelo
Hamiltoniano de Noether da ação oficial. Sua avaliação no background warped
ainda requer a forma potencial simplética explícita da GDQ.

## 6. Problema de sela

O funcional aumentado é

$$
\mathscr L(X,\lambda)
=\mathcal S_{\rm GDQ}(X)
-\langle\lambda,\mathcal C(X)\rangle.
$$

A sela física deve satisfazer simultaneamente

$$
D_X\mathscr L(X_*,\lambda_*)=0,
$$

$$
\mathcal C(X_*)=0.
$$

Esse sistema, e não um background importado de outra questão, define
$X_*$.

## 7. Projetor físico

No background obtido, defina

$$
A_*
=\begin{pmatrix}
D\mathcal C(X_*)\\
R_*^\dagger\mathbb G_*
\end{pmatrix},
$$

onde $R_*$ gera as redundâncias de gauge e difeomorfismo. O projetor conjunto
é

$$
P^{\rm phys}
=I-\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+A_*.
$$

Essa fórmula está demonstrada. Sua avaliação numérica depende de $X_*$.

## 8. Hessiana física e colagem

A Hessiana correta é

$$
\mathbb H_*
=D^2\mathcal S_{\rm GDQ}(X_*)
-\lambda_*^aD^2\mathcal C_a(X_*).
$$

Depois da projeção,

$$
K_*^{\rm phys}
=P^{{\rm phys}\dagger}\mathbb H_*P^{\rm phys}.
$$

Separando interior e exterior, o operador efetivo de interface é obtido pela
colagem dos DtN:

$$
\Lambda_{\rm tot}^{\rm phys}
=P_Y^\dagger
\left(\Lambda_-+\Lambda_+^{\rm eff}\right)P_Y.
$$

Para a compensação global antipodal,

$$
\Lambda_+^{\rm eff}
=D-OD^+O.
$$

## 9. Critério de estabilidade e transporte

Depois de remover os zeros exatos de Noether, define-se

$$
\Delta_\varepsilon
=\inf\operatorname{spec}K_{*,\varepsilon}^{\rm phys}.
$$

A ponte espectral requer

$$
\inf_{0<\varepsilon<\varepsilon_0}\Delta_\varepsilon>0.
$$

Sob esse gap, valem a localização de Agmon, a convergência de formas, a
convergência forte de resolventes e o transporte dos projetores de Riesz já
demonstrados nos Lemas 3--5.

## 10. Resultados já válidos

1. A família geométrica homogênea e seu limite apontado foram construídos.
2. A identificação dos espaços ponderados foi formulada em regularidade
   Hölder local.
3. A redução correta do colar com $H=d_J^c\omega$ foi derivada.
4. O sistema DAE local e sua linearização foram implementados e refinados.
5. A restrição foi preservada numericamente até aproximadamente $10^{-14}$.
6. O DtN interno foi construído.
7. A forma do DtN exterior com compensação antipodal foi derivada.
8. O projetor físico abstrato foi obtido.
9. O modelo espectral de referência foi refinado em malha, raio e corte
   harmônico.
10. Foi demonstrado que a compactificação, sozinha, não produz gap uniforme.

## 11. Resultados excluídos

Não pertencem à cadeia canônica:

1. tratar $H=h\sigma_{123}$ como variável independente;
2. prolongar o ODE local de Berger até o antipolo global;
3. usar o produto homogêneo como sela com $L$ livre;
4. importar o background warped da Q29 como prova da sela da ponte;
5. interpretar o operador de referência como Hessiana física completa;
6. inferir $\mu_*>0$ apenas de compactificação ou corte harmônico;
7. inserir uma tensão cosmológica sem definir seu funcional variacional.

## 12. Única pendência de avaliação

Toda a cadeia reduz-se agora a um único bloco:

$$
\boxed{
\text{avaliar }\mathcal H_\xi
\text{ e resolver o exterior warped vinculado.}
}
$$

Esse bloco deve fornecer:

1. a carga hamiltoniana integrável $\mathcal H_\xi$ no ansatz exterior;
2. a solução $(X_*,\lambda_*)$;
3. o DtN exterior matricial no background obtido;
4. o valor de $\Delta_\varepsilon$.

## 13. Status

$$
\boxed{
\text{ponte fechada estruturalmente e aberta em uma única aplicação global.}
}
$$

Nenhuma outra pendência independente deve ser criada antes de resolver esse
bloco.
