# Q28 — Seleção local de três estômatos pelo equilíbrio torsional

## 1. Enunciado

Queremos determinar o número de canais de um defeito composto elementar sem
usar previamente $N=3$. A derivação usa:

1. a simetria de fase da ação oficial;
2. a distribuição horizontal da fibração de Hopf em $S^3$;
3. isotropia local do estômato estacionário;
4. estabilidade isolada da Hessiana, módulo a rotação global.

## 2. Corrente conservada da ação oficial

Escreva

$$
f=u+iv,
\qquad
S_R=\hbar v.
$$

A ação oficial depende de $v$ somente por suas derivadas, pois

$$
f+\bar f=2u
$$

e

$$
g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f
=|\nabla u|^2+|\nabla v|^2
$$

no setor real reduzido. Logo, ela é invariante sob

$$
v\longmapsto v+\varepsilon.
$$

A variação com $\varepsilon$ local fornece uma corrente proporcional a

$$
J_v^\mu
=2\frac{\hbar}{\Lambda_C^2}
\tau\mathcal U\sqrt{g}\,
g^{\mu\nu}\partial_\nu v,
$$

até a normalização comum da integral em $\tau$. On-shell,

$$
\boxed{
\nabla_\mu J_v^\mu=0.
}
$$

Integrando numa pequena região de junction,

$$
\boxed{
\sum_{a=1}^{N}\mathbf T_a=0,
}
$$

onde $\mathbf T_a$ é o fluxo vetorial tangencial transportado pelo canal
$a$. Esse fechamento mecânico não deve ser confundido com a soma das cargas
escalares orientadas, que pode ser não nula no próton.

## 3. Por que as tensões vivem num plano

Na fibração de Hopf,

$$
S^1\hookrightarrow S^3\longrightarrow S^2,
$$

a forma de contato $\eta_H$ separa a direção de circulação da distribuição
horizontal

$$
\mathcal H=\ker\eta_H.
$$

Como

$$
\operatorname{rank}_{\mathbb R}\mathcal H=2,
$$

as respostas de tensão que deslocam a posição relativa das gargantas
pertencem a um plano real. A componente vertical registra a circulação comum;
ela não equilibra as posições relativas.

## 4. Isotropia estacionária

Para canais equivalentes no background local isotrópico,

$$
|\mathbf T_a|=T.
$$

Escreva

$$
\mathbf T_a
=T(\cos\theta_a,\sin\theta_a).
$$

O funcional quadrático universal do modo de fechamento, obtido pelo pullback
da Hessiana positiva ao subespaço dos fluxos de fronteira, é

$$
\mathcal E_{\rm close}
=\frac{\kappa_H}{2}
\left|\sum_{a=1}^{N}\mathbf T_a\right|^2,
\qquad
\kappa_H>0.
$$

Sua condição estacionária mínima é precisamente a lei de Noether

$$
\sum_a\mathbf T_a=0.
$$

## 5. Análise por número de canais

### $N=1$

Para $T>0$,

$$
\mathbf T_1\ne0,
$$

logo não existe fechamento.

### $N=2$

O fechamento exige

$$
\mathbf T_2=-\mathbf T_1.
$$

Essa configuração ocupa somente uma reta:

$$
\operatorname{span}\{\mathbf T_1,\mathbf T_2\}
\ne\mathcal H.
$$

Ela é um tubo ou par estômato--antiestômato, não um junction bidimensional
não degenerado. Pode representar propagação ou aniquilação, mas não o núcleo
composto elementar procurado.

### $N=3$

O fechamento isotrópico fornece unicamente, módulo rotação e permutação,

$$
\theta_a
=\theta_0+\frac{2\pi(a-1)}3.
$$

Portanto,

$$
\mathbf T_1+\mathbf T_2+\mathbf T_3=0,
$$

com ângulos de $120^\circ$. As três tensões abrangem $\mathcal H$ e possuem
uma única relação linear, exatamente a conservação.

### $N>3$

No ponto regular,

$$
\theta_a
=\theta_0+\frac{2\pi(a-1)}N.
$$

Embora a soma também seja zero, existem deformações internas adicionais que
preservam o fechamento na ordem quadrática. Elas são modos de divisão ou
rearranjo do polígono, e impedem que a configuração seja um crítico isolado
do funcional universal.

## 6. Hessiana

No equilíbrio, uma variação angular produz

$$
\delta^2\mathcal E_{\rm close}
=\kappa_HT^2
\left|
\sum_aJ\widehat{\mathbf T}_a\,\delta\theta_a
\right|^2,
$$

onde $J$ é a rotação de $90^\circ$ em $\mathcal H$. A Hessiana é

$$
H_{ab}
=\kappa_HT^2
\widehat{\mathbf T}_a\cdot\widehat{\mathbf T}_b.
$$

Como os vetores vivem em dimensão dois,

$$
\operatorname{rank}H\le2.
$$

Para $N=3$, o espectro é

$$
\boxed{
\operatorname{spec}H
=\kappa_HT^2
\left\{0,\frac32,\frac32\right\}.
}
$$

O único modo zero é a rotação comum $\delta\theta_1=\delta\theta_2=
\delta\theta_3$. Após quocientar essa isometria, a Hessiana é positiva.

Para $N>3$, a nulidade satisfaz

$$
\dim\ker H\ge N-2>1.
$$

Depois de remover a rotação global, restam pelo menos $N-3$ modos zero
internos. Portanto, o junction não é isolado pela Hessiana universal.

## 7. Teorema de seleção local

> **Teorema.** Considere um junction GDQ isotrópico cujos canais carregam
> fluxos não nulos equivalentes na distribuição horizontal de Hopf. Se o
> junction for não colinear, elementar e tiver Hessiana positiva depois de
> quocientada a rotação global, então ele possui exatamente três canais.

A prova combina:

$$
N\ge3
$$

pela não colinearidade e

$$
N-3=0
$$

pela ausência de modos zero internos. Logo,

$$
\boxed{N=3.}
$$

## 8. Próton e nêutron

É necessário separar direção mecânica e carga orientada. No próton, os três
canais têm direções espaciais a $120^\circ$, enquanto suas circulações
escalares possuem a mesma orientação. Assim, a força fecha, mas a carga
topológica soma.

No nêutron, a conservação escalar adicional pode assumir a solução inteira
mínima

$$
(q_1,q_2,q_3)=(1,1,-2),
$$

de modo que

$$
q_1+q_2+q_3=0.
$$

O fator dois pertence à compensação do fluxo orientado; ele não altera o
teorema vetorial que seleciona os três canais geométricos.

## 9. Consequência para Q28

Com três componentes primitivas coorientadas no setor carregado, a cirurgia
APS já demonstrada fornece

$$
\operatorname{Ind}_{\rm total}=1+1+1=3.
$$

Pela colagem $\mathbb Z_6$,

$$
A=6\operatorname{Ind}_{\rm total}=18,
$$

e

$$
\boxed{N_G=3.}
$$

A cadeia obtida é

$$
\text{simetria de fase da ação oficial}
\to
\text{Noether}
\to
\text{fechamento horizontal}
\to
N=3
\to
\text{aditividade APS}
\to
A=18.
$$

## 10. Limitação precisa

A seleção é um teorema dentro do ansatz de junction **elementar, isotrópico e
horizontal de Hopf**. Ainda deve ser verificado, na Hessiana completa da ação
oficial, que:

1. não existem modos radiais/tensoriais negativos omitidos;
2. termos de ordem superior levantam ou desestabilizam os modos zero de
   $N>3$ em vez de criar novos mínimos isolados;
3. o complemento da cirurgia tem índice zero;
4. os três canais locais são transportados independentemente ao fibrado
   geracional global.

Portanto, a derivação remove a escolha arbitrária de três no modelo reduzido,
mas seu levantamento ao teorema completo da GDQ permanece condicionado à
estabilidade da Hessiana não reduzida.

## 11. Auditoria da Hessiana completa

A Q42 demonstra que a orientação global homogênea de Hopf é isometria e tem
$\kappa_H^{\rm global}=0$. Logo, a rigidez positiva deste documento deve ser
entendida como $\kappa_{\rm rel}$ da textura multicítrica.

Decompondo a Hessiana completa em modos relativos e transversais, a
estabilidade integral equivale a

$$
H_{\rm rel}-JK_\perp^{-1}J^\dagger>0.
$$

O modo radial homogêneo já possui gap $3/(2\tau)>0$, mas
$\kappa_{\rm rel}$, o gap completo de $K_\perp$ e o acoplamento $J$ ainda não
foram avaliados no background de três centros. A derivação e o critério exato
estão em `questoes/q28/associados/estabilidade_completa_junction_torcional.md`.
