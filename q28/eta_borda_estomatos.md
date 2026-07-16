# Q28 — Bloco 6 — Operador tangencial e \(\eta\)-invariante dos estômatos

## 1. Objetivo

Este bloco explicita o operador tangencial de borda:

\[
\mathcal D_{\partial,B,A},
\]

e a forma da contribuição APS:

\[
\eta_{\partial}(0).
\]

A meta é mostrar como os três estômatos podem contribuir para a contagem
geracional e para a seleção quiral sem postular manualmente três famílias.

---

## 2. Geometria local da borda do estômato

Cada estômato é regularizado removendo uma pequena vizinhança tubular. A borda
local é uma 3-variedade compacta:

\[
\partial_a\simeq S^3/\Gamma_a
\]

ou, no caso sem quociente:

\[
\partial_a\simeq S^3.
\]

A métrica induzida é:

\[
h_a.
\]

A torção tangencial efetiva é:

\[
B_a=B|_{\partial_a}.
\]

A conexão interna restrita é:

\[
A_a=A|_{\partial_a}.
\]

---

## 3. Operador tangencial

O operador tangencial é:

\[
\boxed{
\mathcal D_a
=
\slashed D_{\partial_a}
+
\frac18B_{ijk}^{(a)}\gamma^{ijk}
-iA_i^{(a)}\gamma^i.
}
\]

Aqui:

1. \(\slashed D_{\partial_a}\) é o operador de Dirac da borda;
2. \(B_{ijk}^{(a)}\gamma^{ijk}/8\) é a torção de Bismut tangencial;
3. \(A_i^{(a)}\gamma^i\) é a conexão interna restrita ao estômato.

O espectro é:

\[
\mathcal D_a\varphi_{a,k}
=
\lambda_{a,k}\varphi_{a,k}.
\]

---

## 4. \(\eta\)-invariante local

Define-se:

\[
\boxed{
\eta_a(s)
=
\sum_{\lambda_{a,k}\ne0}
\operatorname{sign}(\lambda_{a,k})
|\lambda_{a,k}|^{-s}.
}
\]

Então:

\[
\eta_a(0)
\]

mede a assimetria espectral entre modos positivos e negativos.

A contribuição total é:

\[
\boxed{
\eta_{\partial}(0)
=
\sum_{a=1}^{3}\eta_a(0).
}
\]

---

## 5. Caso sem torção e sem conexão

Para \(S^3\) redondo sem torção e sem conexão, o espectro de Dirac é simétrico:

\[
\lambda_k^{+}=-\lambda_k^{-}.
\]

Logo:

\[
\boxed{
\eta_a(0)=0.
}
\]

Portanto, a contagem geracional não pode vir de uma borda \(S^3\) trivial. Ela
precisa da torção/holonomia de estômato:

\[
B_a\neq0
\quad\text{ou}\quad
A_a\neq0.
\]

Isso é bom: impede que a geração seja artefato de uma esfera comum.

---

## 6. Deslocamento espectral por holonomia

Com holonomia de estômato, o espectro tangencial sofre deslocamento:

\[
\lambda_{a,k}
\longrightarrow
\lambda_{a,k}+\theta_a.
\]

O parâmetro:

\[
\theta_a
\]

é determinado pela circulação/torção da cola:

\[
\theta_a
=
\frac{1}{2\pi}
\oint_{\gamma_a}
\left(
A+B_{\rm eff}
\right).
\]

A assimetria espectral local torna-se:

\[
\eta_a(0)
=
\eta(\theta_a).
\]

Para uma contribuição elementar normalizada de estômato, impõe-se:

\[
\boxed{
-\frac12\left(\eta_a(0)+h_a\right)=1
}
\]

no setor geracional líquido.

Com três estômatos:

\[
\boxed{
-\frac12
\sum_{a=1}^{3}
\left(\eta_a(0)+h_a\right)
=3.
}
\]

Essa é a condição APS que reproduz:

\[
N_{\rm ger}=3.
\]

---

## 7. Relação com monodromia fermiônica

A monodromia spinorial exige:

\[
\mathrm{Hol}_{\gamma_a}=-1.
\]

Isto é:

\[
\exp
\left(
i\oint_{\gamma_a}(A+B_{\rm eff})
\right)
=-1.
\]

Logo:

\[
\oint_{\gamma_a}(A+B_{\rm eff})
=
\pi
\pmod{2\pi}.
\]

Essa meia-holonomia é exatamente o tipo de deslocamento que quebra a simetria
do espectro tangencial e gera \(\eta_a\neq0\).

---

## 8. Forma operacional da contribuição de geração

Definimos o número geracional local por:

\[
\boxed{
n_a
=
-\frac12
\left(
\eta_a(0)+h_a
\right).
}
\]

Então:

\[
\boxed{
N_{\rm ger}
=
\sum_{a=1}^{3}n_a.
}
\]

No setor estável simétrico:

\[
n_a=1,
\qquad
a=1,2,3.
\]

Logo:

\[
\boxed{
N_{\rm ger}=3.
}
\]

---

## 9. Compatibilidade com \(h^{1,1}-h^{2,1}\)

A contagem por APS deve coincidir com a contagem topológica da Q39:

\[
N_{\rm ger}
=
|h^{1,1}-h^{2,1}|
=3.
\]

Assim:

\[
\boxed{
\sum_{a=1}^{3}n_a
=
|h^{1,1}-h^{2,1}|.
}
\]

Interpretação:

1. \(h^{1,1}-h^{2,1}\) dá a contagem topológica global;
2. \(\eta_{\partial}\) dá a realização espectral dessa contagem nas bordas dos
   estômatos.

---

## 10. Efeito da torção sobre a quiralidade

A torção tangencial atua como termo axial efetivo:

\[
\frac18B_{ijk}\gamma^{ijk}
\sim
\beta_a\Gamma_{\partial}.
\]

Assim, no operador tangencial:

\[
\mathcal D_a
\sim
\slashed D_{\partial_a}
+
\beta_a\Gamma_{\partial}
-iA_a.
\]

O sinal de \(\beta_a\) seleciona qual quiralidade possui modos estáveis de
baixa energia.

Condição GDQ:

\[
\boxed{
\beta_a<0
\quad\Longrightarrow\quad
P_L\text{ estável}.
}
\]

Isso fornece a implementação local da seleção:

\[
SU(2)\to SU(2)_L.
\]

---

## 11. O que este bloco fecha

Este bloco fecha estruturalmente:

1. a forma do operador tangencial;
2. a definição de \(\eta_a(0)\);
3. a necessidade de torção/holonomia para gerar assimetria;
4. a contribuição local \(n_a\) de cada estômato;
5. a compatibilidade entre APS e \(N_{\rm ger}=3\);
6. a ação da torção como seletor de quiralidade.

---

## 12. O que ainda falta

Ainda falta calcular explicitamente:

1. o espectro de \(\mathcal D_a\) para a métrica real de estômato;
2. a função \(\eta(\theta_a)\);
3. os valores de \(h_a\);
4. a prova de que o setor estável simétrico impõe \(n_a=1\);
5. a comparação entre \(\eta_{\partial}\) e as classes de Hodge do setor global.

Status:

\[
\boxed{
\text{\(\eta\)-invariante estruturado; cálculo espectral explícito ainda pendente.}
}
