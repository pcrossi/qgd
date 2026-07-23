# Q48 — Operador de campo próximo $\delta\mathcal D_{\rm near}$

## 1. Objetivo

Definir de forma operacional o termo que falta para a metrologia fina do
hidrogênio:

$$
\delta\mathcal D_{\rm near}.
$$

Esse termo não é um potencial adicionado manualmente. Ele é a resposta de
campo próximo do background protônico, extraída da Hessiana física da GDQ com
interface.

---

## 2. Decomposição da Hessiana

Considere uma vizinhança interna do próton:

$$
\mathcal N_p
$$

com fronteira:

$$
Y_p=\partial\mathcal N_p.
$$

O exterior atômico é:

$$
\Omega_p=\mathbb R^3\setminus\mathcal N_p.
$$

A Hessiana física da ação oficial, linearizada no background protônico
$\Phi_{p,*}$, é escrita em blocos:

$$
K_p
=
\begin{pmatrix}
K_{YY} & K_{YI}\\
K_{IY} & K_{II}
\end{pmatrix}.
$$

Aqui:

- $Y$ representa traços na interface;
- $I$ representa modos internos do próton;
- os modos de gauge e modos nulos já foram removidos pelo projetor físico.

O complemento de Schur fornece a impedância efetiva de superfície:

$$
\mathsf R_p
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}.
$$

Classificação:

$$
\boxed{
\text{definição variacional/DtN da resposta de campo próximo.}
}
$$

---

## 3. Comparação com o contorno pontual

No limite Coulomb pontual, o domínio é regular em $r=0$. A impedância efetiva
é substituída por uma condição de regularidade:

$$
\mathsf R_{\rm point}.
$$

O campo próximo físico é a diferença:

$$
\Delta\mathsf R_p
=
\mathsf R_p-\mathsf R_{\rm point}.
$$

Essa diferença contém:

1. raio do próton;
2. fator de forma;
3. torção de Bismut de superfície;
4. polarização geométrica de campo próximo;
5. resposta solitônica bidirecional.

---

## 4. Operador efetivo no subespaço espinorial

Se $P_{n\kappa}$ é o projetor no setor espinorial do nível atômico, o operador
de campo próximo é:

$$
\delta H_{\rm near}^{(n\kappa)}
=
P_{n\kappa}^\dagger
\Delta\mathsf R_p
P_{n\kappa}.
$$

Equivalentemente:

$$
\delta\mathcal D_{\rm near}
=
\Pi_{\rm spin}
\left(
\mathsf R_p-\mathsf R_{\rm point}
\right)
\Pi_{\rm spin}.
$$

onde $\Pi_{\rm spin}$ é a projeção da Hessiana GDQ no setor espinorial físico.

---

## 5. Lamb shift

O Lamb shift é:

$$
\Delta E_{\rm Lamb}
=
\langle 2s_{1/2}|
\delta H_{\rm near}
|2s_{1/2}\rangle
-
\langle 2p_{1/2}|
\delta H_{\rm near}
|2p_{1/2}\rangle.
$$

Como o estado $2s_{1/2}$ tem suporte no núcleo e o estado $2p_{1/2}$ tem
supressão centrífuga, a diferença de matriz é não nula quando
$\Delta\mathsf R_p\ne0$.

Isso responde estruturalmente por que a degenerescência Dirac é quebrada.

---

## 6. Relação com Heun/Hill do legado

O Capítulo 38 legado descreve o campo próximo por termos:

$$
\frac{\chi_3}{r^3},
\qquad
\frac{\chi_4}{r^4},
\ldots
$$

Na formulação atual, esses termos são a expansão radial local de
$\Delta\mathsf R_p$ ou, equivalentemente, de $\delta\mathcal D_{\rm near}$.

O determinante de Hill é a representação matricial do problema espectral:

$$
\det H_{\rm Hill}(E;\mathsf R_p)=0.
$$

Logo, o legado é preservado, mas reinterpretado:

$$
\boxed{
\text{Heun/Hill é a técnica radial; DtN/Schur é a origem GDQ do operador.}
}
$$

---

## 7. O que ainda precisa de número

Para obter previsão metrológica sem pós-ajuste, deve-se calcular:

$$
\mathsf R_p
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}
$$

diretamente no background protônico da Q40.

Portanto, a lacuna restante não é conceitual. É a avaliação do complemento de
Schur físico do próton.

Status:

$$
\boxed{
\text{operador formal fechado; valor numérico do Lamb shift condicional a }K_p.
}
$$

---

## 8. Escala requerida para o Lamb shift

O script:

$$
\texttt{avaliar\_recuo\_hessiana\_lamb\_q48.py}
$$

calculou a escala requerida para o operador de campo próximo. Usando a
referência metrológica do Lamb shift apenas como diagnóstico, temos:

$$
\Delta E_{\rm Lamb}^{\rm ref}
=
4.374891259184723\times10^{-6}\,{\rm eV}.
$$

O tamanho finito do próton já avaliado para $2s$ é:

$$
\Delta E_{\rm fs}^{H}(2s)
=
5.715065938836622\times10^{-10}\,{\rm eV}.
$$

Logo, a parte requerida de campo próximo é:

$$
\Delta E_{\rm near}^{\rm req}
=
4.374319752590839\times10^{-6}\,{\rm eV},
$$

ou:

$$
1.057705810320421\times10^9\,{\rm Hz}.
$$

Classificação:

$$
\boxed{
\text{diagnóstico de escala; previsão só após calcular }\Delta\mathsf R_p.
}
$$
