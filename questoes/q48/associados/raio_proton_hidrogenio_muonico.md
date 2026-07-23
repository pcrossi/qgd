# Q48 — Raio do próton, fator de forma e hidrogênio muônico

## 1. Enunciado

O raio do próton entra no hidrogênio como propriedade do background bariônico,
não como constante livre da Q48.

Na GDQ:

$$
\Phi_{p,*}
\to
F_p(q^2),
\qquad
\Phi_{p,*}
\to
\mathsf R_p(r_p).
$$

O mesmo próton pode apresentar raio efetivo diferente para sondas diferentes
porque o acoplamento solitônico é bidirecional.

---

## 2. Fator de forma

No setor eletromagnético:

$$
F_p(q^2)
=
1-\frac{q^2 r_p^2}{6}+O(q^4).
$$

O potencial efetivo é:

$$
V_p(\mathbf q)
=
-\frac{4\pi Z\alpha\hbar c}{q^2}F_p(q^2).
$$

O primeiro termo de tamanho finito no espaço real é:

$$
\delta V_{\rm fs}(\mathbf r)
=
\frac{2\pi}{3}
Z\alpha\hbar c\,r_p^2\,
\delta^{(3)}(\mathbf r).
$$

---

## 3. Deslocamento de tamanho finito

Para estados $ns$:

$$
\Delta E_{\rm fs}(ns)
=
\frac{2\pi}{3}
Z\alpha\hbar c\,r_p^2
|\psi_{ns}(0)|^2.
$$

Como:

$$
|\psi_{ns}(0)|^2
=
\frac{(Z\alpha\mu c/\hbar)^3}{\pi n^3},
$$

temos:

$$
\Delta E_{\rm fs}(ns)
=
\frac{2}{3}
\frac{(Z\alpha)^4\mu^3c^4}{\hbar^2}
\frac{r_p^2}{n^3}.
$$

Classificação:

$$
\boxed{
\text{redução efetiva de fator de forma/contorno de superfície.}
}
$$

---

## 4. Hidrogênio muônico

A massa reduzida no hidrogênio muônico é muito maior:

$$
\mu_{\mu p}\gg\mu_{ep}.
$$

Como:

$$
\Delta E_{\rm fs}\propto\mu^3,
$$

o deslocamento de tamanho finito é amplificado por aproximadamente:

$$
\left(\frac{\mu_{\mu p}}{\mu_{ep}}\right)^3.
$$

Por isso o hidrogênio muônico é uma sonda de campo próximo e de raio/fator de
forma do próton.

---

## 5. Leitura GDQ do raio efetivo

O legado propõe que o múon deforma o background protônico por acoplamento
solitônico bidirecional. A leitura conservadora é:

$$
r_p^{\rm eff}(\text{sonda})
=
r_p^{(0)}
+
\delta r_p[\Phi_{\rm sonda}],
$$

com:

$$
\delta r_p[\Phi_{\rm sonda}]
=
-
\left(
H_p^{\rm surf}
\right)^{-1}
J_{p,\rm sonda}.
$$

Aqui:

- $H_p^{\rm surf}$ é a Hessiana física de superfície do próton;
- $J_{p,\rm sonda}$ é a fonte gerada pela sonda ligada;
- para o elétron, $J_{p,e}$ é pequeno;
- para o múon, $J_{p,\mu}$ é grande.

Para estados $s$ no mesmo nível principal, a razão das fontes de contato é
fixada sem conhecer o coeficiente absoluto da Hessiana:

$$
\frac{J_{p,e}}{J_{p,\mu}}
=
\frac{\delta r_p[e]}{\delta r_p[\mu]}
=
\left(
\frac{\mu_{ep}}{\mu_{\mu p}}
\right)^3.
$$

Usando as massas reduzidas físicas:

$$
\frac{\mu_{ep}}{\mu_{\mu p}}
=
5.378019759477932\times10^{-3},
$$

e portanto:

$$
\left(
\frac{\mu_{ep}}{\mu_{\mu p}}
\right)^3
=
1.555489846615637\times10^{-7}.
$$

Assim, a mesma retroação que pode ser relevante no hidrogênio muônico também
existe no hidrogênio eletrônico, mas é suprimida por aproximadamente sete
ordens de grandeza. Se a contração muônica estiver na escala de $10^{-2}$ fm,
a contração eletrônica esperada fica na escala de $10^{-9}$ fm.

O teste numérico de escala está em:

`estimar_retroacao_leptonica_raio_q48.py`

com saída em:

`saida_retroacao_leptonica_raio_q48.md`.

Classificação:

$$
\boxed{
\text{teorema condicional de resposta linear do raio efetivo.}
}
$$

---

## 6. O que fecha

Fechado estruturalmente:

1. raio entra por fator de forma/contorno;
2. estados $s$ são sensíveis ao raio;
3. hidrogênio muônico amplifica o efeito por $\mu^3$;
4. GDQ permite raio efetivo dependente da sonda por resposta do background.

Pendente para previsão cega:

1. calcular $H_p^{\rm surf}$ diretamente da Q40;
2. calcular $J_{p,\mu}$ sem usar o raio muônico como alvo;
3. resolver o problema ligado com esse raio efetivo congelado.
