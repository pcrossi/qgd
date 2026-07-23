# Q29 — Papel da $\eta$-forma no determinante eletromagnético

## 1. Determinante de uma família de Dirac--Bismut

Para um operador autoadjunto $D_Q$ acoplado à conexão eletromagnética, o
determinante regularizado separa-se em

$$
\boxed{
\log\det D_Q
=-\frac12\zeta'_{D_Q^2}(0)
-\frac{i\pi}{2}\eta_{D_Q}(0).
}
$$

A primeira parcela controla o módulo:

$$
\log|\det D_Q|
=-\frac12\zeta'_{D_Q^2}(0).
$$

A segunda controla a fase:

$$
\arg\det D_Q
=-\frac\pi2\eta_{D_Q}(0).
$$

## 2. Paridade dos termos efetivos

A variação da parte real produz operadores pares, incluindo

$$
\int F_Q\wedge *_4F_Q,
$$

e, portanto, a rigidez $K_Q=1/e^2$.

A $\eta$-forma/Chern--Simons produz o setor ímpar,

$$
\int A_Q\wedge dA_Q
$$

na fronteira ou

$$
\int F_Q\wedge F_Q
$$

no preenchimento. Ela altera a fase do funcional, não o módulo gaussiano.

Consequentemente,

$$
\boxed{
\delta^2\eta
\not\equiv
\delta^2\zeta',
}
$$

e o valor $3\pi/2$ da fase não pode ser convertido diretamente em uma correção
positiva de $1/e^2$.

## 3. Contorno causal

Uma mistura seria possível se o contorno complexo $\gamma$ demonstrasse uma
identidade do tipo

$$
\operatorname{Re}
\oint_\gamma i\,\eta_Q(z_\tau)dz_\tau
\ne0.
$$

Mas isso exige polo, corte ou monodromia não holomorfa. A Q38 já mostrou que,
para uma família suave e normalizada,

$$
\operatorname{Re}
\oint_\gamma i\,\eta_Q(z_\tau)dz_\tau=0.
$$

Portanto, usar o contorno para transformar automaticamente a fase em rigidez
repetiria a lacuna causal da Q38.

## 4. Objeto correto para a normalização de $\alpha$

A correção par deve vir da parte real do determinante:

$$
\Delta K_Q
=-\frac12
\left.
\frac{\delta^2}{\delta A_Q^2}
\zeta'_{D_Q^2}(0)
\right|_{A_Q=0}.
$$

Equivalentemente, por traço de calor,

$$
\Delta K_Q
=\frac12\int_0^\infty\frac{dt}{t}
\,\delta_A^2
\operatorname{Tr}(e^{-tD_Q^2}),
$$

com subtrações geométricas definidas pelo operador físico, não por
contratermos fundamentais importados.

Para avaliar isso são necessários:

1. o espectro carregado completo, não apenas $\gamma/W/Z$;
2. os vértices geométricos $\delta_AD_Q$;
3. a condição Robin da conexão;
4. uma prescrição finita fixada por comparação de backgrounds.

## 5. Veredito

$$
\boxed{
\text{a $\eta$-forma explica a fase topológica,
mas não veste a rigidez par }1/e^2.
}
$$

Assim, o fator $3\pi/2$ não fecha $\alpha^{-1}=132{,}457669$. A rota correta
é a parte $\zeta'$ do determinante espectral.
