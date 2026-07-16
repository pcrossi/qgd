# Q28 — Hessiana espectral completa no background $C_3$ gaussiano

## 1. Background usado

Cada estômato possui fatia normal

$$
\mathbb C^2\simeq\mathbb R^4
$$

e preenchimento estacionário gaussiano

$$
g_*=\delta,
\qquad
f_*=\frac{|x|^2}{4\tau}+f_0.
$$

Os três preenchimentos são colados com a mesma orientação e relacionados pela
simetria $C_3$. O fechamento é imposto durante a variação:

$$
\sum_{a=1}^{3}\mathbf T_a=0.
$$

## 2. Operador espectral local

No shrinker gaussiano, o operador ponderado fundamental é

$$
L_f=-\Delta_f
=-\Delta+\frac{x}{2\tau}\cdot\nabla.
$$

Seu espectro no espaço gaussiano normalizado é

$$
\boxed{
\operatorname{spec}L_f
=\left\{\frac{m}{2\tau}:m=0,1,2,\ldots\right\}.
}
$$

Esse resultado vale componente a componente para os polinômios de Hermite.

## 3. Fase

A parte imaginária de $f$ aparece na ação por sua energia de Dirichlet. Sua
Hessiana normalizada é

$$
K_v=2L_f.
$$

O nível $m=0$ é o deslocamento constante de Noether e não é uma instabilidade.
No complemento físico,

$$
\operatorname{spec}K_v^{\rm phys}
=\left\{\frac{m}{\tau}:m\geq1\right\}>0.
$$

## 4. Dilatão e métrica

A variação de $f$ não é independente da métrica porque a medida satisfaz

$$
\int\mathcal U\,dV=1.
$$

Eliminando a resposta dilatônica pelo vínculo e impondo o gauge
Hermitiano--DeTurck ponderado, a segunda variação métrica de Perelman no fundo
gaussiano reduz ao Lichnerowicz com drift. Como

$$
\operatorname{Rm}(g_*)=0,
$$

o operador físico é, componente a componente,

$$
K_h=L_f
$$

depois de remover difeomorfismos, deformações paralelas do background e o modo
de escala fixado por $\tau$ e pela normalização.

Consequentemente,

$$
\boxed{
\operatorname{spec}K_h^{\rm phys}
\subseteq
\left\{\frac{m}{2\tau}:m\geq1\right\}>0.
}
$$

O Schur métrico--dilatônico já está incluído nessa redução: os termos mistos
não constituem um bloco $J$ adicional depois que a resposta de $f$ e o gauge
são resolvidos.

## 5. Setores coletivos de três centros

O cálculo vinculado anterior fornece

$$
H_{\rm rel}
=\frac32\kappa_{\rm rel}T^2I_2,
$$

$$
K_r^{(0)}=\frac{3}{2\tau}I_3,
$$

e, pela preservação da classe primitiva de fluxo,

$$
J_{\theta r}=0.
$$

As excitações não homogêneas pertencem ao operador $L_f$ e têm gap mínimo

$$
\lambda_{\rm nh}=\frac1{2\tau}.
$$

## 6. Hessiana física completa nesta classe de background

Depois de remover os modos de gauge e os vínculos, a Hessiana de três centros
é a soma ortogonal

$$
\boxed{
\mathbb H_{\rm phys}^{(3)}
=H_{\rm rel}
\oplus K_r^{(0)}
\oplus K_v^{\rm phys}
\oplus K_{(g,f)}^{\rm HD,phys}.
}
$$

Seu menor gap é

$$
\boxed{
\lambda_{\min}
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}>0.
}
$$

Na normalização primitiva usada pelo solver,

$$
\kappa_{\rm rel}T^2=1,
$$

e, para $\tau=1$,

$$
\boxed{\lambda_{\min}=\frac12.}
$$

## 7. Interpretação

O zero angular é a rotação comum; o zero da fase é a simetria global de
Noether; os zeros métricos são removidos pelo gauge, pela escolha de escala e
pela normalização. Nenhum deles é uma direção física negativa.

Assim, dentro do background estacionário $C_3$ formado pelos três
preenchimentos gaussianos primitivos, não restam modos físicos negativos:

$$
\boxed{
\mathbb H_{\rm phys}^{(3)}>0.
}
$$

Esse resultado não afirma estabilidade de todo background global arbitrário.
Ele demonstra a estabilidade integral da classe de background efetivamente
usada na cirurgia e na seleção numérica da Q28.
