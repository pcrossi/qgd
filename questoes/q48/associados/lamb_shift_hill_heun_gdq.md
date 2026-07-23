# Q48 — Lamb shift como problema de campo próximo da Hessiana

## 1. Enunciado

O Lamb shift é:

$$
\Delta E_{\rm Lamb}
=
E(2s_{1/2})-E(2p_{1/2}).
$$

No problema Coulomb--Dirac puro:

$$
E(2s_{1/2})=E(2p_{1/2}).
$$

Logo, a Q48 precisa mostrar qual setor da GDQ quebra essa degenerescência.

---

## 2. O que o legado fornece

O Capítulo 38 sugere que o campo próximo produz termos:

$$
\frac{\chi_3}{r^3},
\qquad
\frac{\chi_4}{r^4},
\ldots
$$

e uma relação multi-termo tipo Hill/Heun. Isso é fisicamente útil, mas não
basta como prova metrológica.

Classificação:

$$
\boxed{
\text{estrutura radial efetiva e candidata ao operador de campo próximo.}
}
$$

---

## 3. Rota correta na GDQ

Deve-se escrever:

$$
\mathcal D^B_{p,e}
=
\mathcal D_{\rm Coul}
+
\delta\mathcal D_{\rm near}.
$$

O termo $\delta\mathcal D_{\rm near}$ deve vir de:

1. expansão do background protônico $\Phi_{p,*}$;
2. torção de Bismut $H_p$;
3. fator de forma de superfície;
4. operador DtN/Schur da região interna do próton;
5. domínio auto-adjunto.

Depois:

$$
\Delta E_a^{(1)}
=
\langle a|\delta H_{\rm near}|a\rangle.
$$

Logo:

$$
\Delta E_{\rm Lamb}^{(1)}
=
\langle 2s_{1/2}|\delta H_{\rm near}|2s_{1/2}\rangle
-
\langle 2p_{1/2}|\delta H_{\rm near}|2p_{1/2}\rangle.
$$

---

## 4. Forma por determinante de Hill

Se o campo próximo gera acoplamento multi-termo entre coeficientes radiais:

$$
A_ka_{k+1}+B_ka_k+C_ka_{k-1}+D_ka_{k-2}+\cdots=0,
$$

a condição espectral é:

$$
\det H_{\rm Hill}(E)=0.
$$

A degenerescência é quebrada porque os blocos $2s_{1/2}$ e $2p_{1/2}$ têm
domínios e acoplamentos de curto alcance diferentes:

$$
H_{\rm Hill}^{(2s_{1/2})}(E)
\ne
H_{\rm Hill}^{(2p_{1/2})}(E).
$$

---

## 5. Classificação honesta

Fechado estruturalmente:

$$
\boxed{
\text{Lamb shift é resposta de campo próximo/DtN da Hessiana GDQ.}
}
$$

Ainda condicional para previsão metrológica:

1. avaliar $\delta\mathcal D_{\rm near}$ diretamente no background protônico
   Q40;
2. fixar $\mathsf R_p$ sem usar o Lamb shift como alvo;
3. resolver o determinante ou o operador radial com convergência;
4. comparar com o valor experimental depois de congelar os parâmetros.

Portanto, neste ponto:

$$
\boxed{
\text{Q48 resolve a origem estrutural do Lamb shift, mas a previsão numérica
fica condicional à Hessiana de campo próximo.}
}
$$
