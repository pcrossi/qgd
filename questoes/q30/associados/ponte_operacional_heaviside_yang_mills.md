# Q30 — Ponte operacional de Heaviside entre GDQ e Yang--Mills efetivo

## 1. Objetivo e símbolo de equivalência

Construir um representante local, em linguagem operacional de Heaviside, da
resposta coletiva confinante já derivada da sela tubular GDQ.

Usaremos

$$
\mathcal A\simeq_H\mathcal B
$$

para significar: os dois sistemas possuem a mesma função de transferência no
setor estático de fontes, depois da projeção e do limite distributivo
declarados. O símbolo não significa igualdade das ações fundamentais nem
identidade ontológica entre GDQ e Yang--Mills.

## 2. Entrada GDQ

A sela tubular fornece

$$
V_{m GDQ}(r)-V_{m GDQ}(0)=\sigma_{m GDQ}r,
\qquad
\sigma_{m GDQ}>0.
$$

Como

$$
\Delta^2r=-8\pi\delta^{(3)},
$$

a função de transferência é

$$
\widetilde V_{m GDQ}(k)
=-\frac{8\pi\sigma_{m GDQ}}{k^4}.
$$

## 3. Aproximação regular de Heaviside

Defina

$$
P_\mu:=-\Delta+\mu^2,
\qquad \mu>0.
$$

O operador regularizado é

$$
\boxed{
\mathcal L_{H,\mu}
:=-\frac1{8\pi\sigma_{m GDQ}}P_\mu^2.
}
$$

Seu inverso possui símbolo

$$
\boxed{
\widetilde{\mathcal L_{H,\mu}^{-1}}(k)
=-\frac{8\pi\sigma_{m GDQ}}{(k^2+\mu^2)^2}.
}
$$

## 4. Realização local em cascata

O operador de quarta ordem pode ser realizado por dois problemas locais de
segunda ordem:

$$
\boxed{
P_\mu\phi=\rho,
\qquad
P_\mu V=-8\pi\sigma_{m GDQ}\phi.
}
$$

Eliminando $\phi$,

$$
P_\mu^2V=-8\pi\sigma_{m GDQ}\rho.
$$

Para uma fonte pontual,

$$
\widetilde V_\mu(k)
=-\frac{8\pi\sigma_{m GDQ}}{(k^2+\mu^2)^2}.
$$

Essa cascata é a construção operacional procurada: cada estágio é elíptico,
local e de segunda ordem; o polo duplo aparece somente depois de eliminar o
modo intermediário coletivo.

## 5. Limite confinante

Em três dimensões,

$$
P_\mu^{-2}(r)=\frac{e^{-\mu r}}{8\pi\mu}.
$$

Logo,

$$
V_\mu(r)=-\frac{\sigma_{m GDQ}}\mu e^{-\mu r}
$$

e, após subtrair a constante não observável,

$$
\boxed{
V_\mu(r)-V_\mu(0)
=\frac{\sigma_{m GDQ}}\mu(1-e^{-\mu r})
\longrightarrow
\sigma_{m GDQ}r.
}
$$

Portanto,

$$
\boxed{
\mathsf R_{\rm tubo}^{\rm GDQ}
\simeq_H
-8\pi\sigma_{m GDQ}P_\mu^{-2}
\xrightarrow[\mu\to0^+]{}
-8\pi\sigma_{m GDQ}(-\Delta)^{-2}.
}
$$

## 6. Setor curto mais setor confinante

Se a resposta geométrica local contém também o bloco simples
$-4\pi\kappa_C/k^2$, a função de transferência completa é

$$
\boxed{
\widetilde V_{H,\mu}(k)
=-\frac{4\pi\kappa_C}{k^2+\mu^2}
-\frac{8\pi\sigma_{m GDQ}}{(k^2+\mu^2)^2}.
}
$$

No espaço real e no limite removido,

$$
V(r)=-\frac{\kappa_C}{r}+\sigma_{m GDQ}r+V_0.
$$

Essa é a forma operacional tipo Cornell. $\kappa_C$ não é identificado com
$4\alpha_s/3$ sem uma redução adicional.

## 7. Tradução para o observável tipo Yang--Mills

Para um contorno retangular $C_{R,T}$, a resposta estática satisfaz

$$
\langle\mathcal H(C_{R,T})\rangle
\sim
\exp\left[-\frac{T}{\hbar}V(R)\right].
$$

Como $V(R)=\sigma_{m GDQ}R+O(1)$,

$$
\boxed{
|\langle\mathcal H(C_{R,T})\rangle|
\sim e^{-\sigma_{m GDQ}RT/\hbar}
=e^{-\sigma_{m GDQ}A(C)/\hbar}.
}
$$

Logo, no setor de observáveis estáticos,

$$
\boxed{
\text{sela tubular GDQ}
\simeq_H
\text{resposta confinante efetiva tipo Yang--Mills}
}
$$

e ambas produzem a mesma lei de área e o mesmo potencial linear.

## 8. Gap

O modo intermediário $\phi$ é uma variável operacional eliminada, não um
estado assintótico. O espectro físico continua controlado pela Hessiana
transversal do tubo:

$$
\Delta_{m GDQ}=\frac{\hbar c}{r_\perp}>0.
$$

Assim, o polo estático duplo não introduz uma partícula livre sem massa.

## 9. Teorema operacional

> **Teorema.** Suponha que a ação oficial GDQ admita uma sela tubular
> homogênea com tensão $\sigma_{m GDQ}>0$ e Hessiana transversal com gap.
> Então sua resposta estática entre fontes possui uma realização local em
> cascata por dois operadores $P_\mu=-\Delta+\mu^2$. Depois da subtração da
> constante e do limite $\mu\to0^+$, essa realização converge
> distributivamente ao potencial linear e produz lei de área. O gap
> transversal permanece positivo.

## 10. Alcance para Clay

A construção resolve a tradução operacional

$$
\text{GDQ}\to(V,\widetilde V,\text{lei de área},\Delta>0)
\simeq_H\text{Yang--Mills confinante efetivo}.
$$

Ela não prova igualdade entre a medida GDQ e a medida quântica
Yang--Mills axiomática em quatro dimensões. Em particular, equivalência de
uma função de transferência estática não implica automaticamente os axiomas
de Osterwalder--Schrader, invariância de gauge não abeliana completa ou
existência da medida interagente contínua.

Portanto:

- problema operacional de Q30: fechado;
- confinamento e gap na GDQ: fechados estruturalmente no setor físico;
- equivalência estática com Yang--Mills: demonstrada como $\simeq_H$;
- problema Clay literal: não demonstrado por essa aproximação.

## 11. Classificação

- cascata e eliminação: identidades exatas;
- limite $\mu\to0$: convergência distributiva após subtração;
- lei de área: consequência do potencial linear;
- aproximação Yang--Mills: equivalência operacional;
- equivalência de teorias quânticas completas: aberta.

