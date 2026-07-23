# Q38 — Correção de rota: derivação exclusivamente pela ação GDQ

## 1. Princípio

A resposta oficial usa somente
\[
\mathcal S_{\rm GDQ}
=\int_\gamma\left[\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[\tau(\mathcal R+g^{\mu\bar\nu}\partial_\mu f
\partial_{\bar\nu}\bar f)+\frac{f+\bar f}{2}-n\right]
\mathcal U\sqrt{\det g}\,d^{2n}z\right]\frac{d\tau}{\tau}.
\]
Não se introduzem ação de Yang--Mills, campo BPST ou determinante instantônico
como substitutos dessa ação.

## 2. Origem GDQ do exponencial

Defina
\[
\sigma=\frac{f+\bar f}{2},\qquad
\mathcal U=\frac{e^{-\sigma}}{(4\pi z_\tau)^n}.
\]
Logo,
\[
\boxed{e^{-1/(2\alpha)}\Longleftrightarrow\sigma_*=\frac1{2\alpha}.}
\]
Essa igualdade deve vir da equação de Euler--Lagrange de \(f\).

No setor estacionário constante, com a restrição de normalização implementada
por um multiplicador \(\lambda\), a equação correta tem a forma
\[
\tau\mathcal R_*+\sigma_*-n-1=\lambda.
\]
Logo, a equação local não fixa \(\sigma_*\). Para medida constante, a
normalização global fornece
\[
\boxed{\sigma_*=\log[V_* /(4\pi z_\tau)^n].}
\]
O expoente proposto exige
\(V_* /(4\pi z_\tau)^n=e^{1/(2\alpha)}\), mas no modo totalmente normalizado
esse peso é cancelado pelo próprio volume. Ver questoes/q38/associados/fechamento_gdq_pura.md.

## 3. Coeficiente gravitacional direto

Para
\[
\mathcal M_{\mathbb C}\simeq N_4\times K,\qquad
ds^2=e^{2A}h_{\mu\nu}dx^\mu dx^\nu+q_{ab}dy^ady^b,
\]
a redução do termo de curvatura dá
\[
\boxed{
C_R^{\rm GDQ}
=\frac{\hbar}{\Lambda_C^2}\operatorname{Re}
\int_\gamma d\tau\int_K
\eta_R e^{2A}
\frac{e^{-\sigma_*}}{(4\pi z_\tau)^n}
\sqrt{\det q_*}\,d^{2n-4}y.
}
\]
Então
\[
\boxed{G_{\rm GDQ}=\frac{c^4}{16\pi C_R^{\rm GDQ}}.}
\]

## 4. Fatores geométricos

A combinação
\[
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
\]
só pode ser mantida se for a avaliação da integral interna:

1. \(\alpha^4\): jacobiano da forma de volume;
2. \(1+\alpha\): autovalor longitudinal do warp;
3. \(\chi_{\rm Fano}^{-1}\): projeção do modo gravitacional no contorno.

Ela não representa uma ação instantônica.

## 5. Reclassificação

Os adendos BPST, Pontryagin e determinantes não fazem parte da resposta
oficial de Q38. Podem ser preservados como exploração matemática, mas não
provam o fator exponencial da GDQ.

## 6. Pendências corretas

1. resolver conjuntamente as equações estacionárias métrica e dilatônica;
2. resolver o warp que satisfaz a equação métrica shrinking;
3. avaliar diretamente \(C_R^{\rm GDQ}\);
4. obter \(\alpha^4(1+\alpha)/\chi_{\rm Fano}\) da integral interna;
5. comparar com o valor observado somente ao final.

## 7. Status

\[
\boxed{\text{Q38 deve ser resolvida pela redução métrico--dilatônica da GDQ,}}
\]
\[
\boxed{\text{sem instantão de Yang--Mills e sem determinante BPST.}}
\]
