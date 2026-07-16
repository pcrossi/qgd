# Relatório: Fatores de Forma de Superfície (Q40)

## 1. Regra geométrica

O espalhamento eletromagnético mede a coordenada projetada:

\[
r_{\rm obs}(\chi)=C_rR_B\chi.
\]

Com:

- \(C_r=0.125228042268\);
- \(R_B=579.238902\,\mathrm{fm}\);
- \(\epsilon_{\rm eff}=0.011591040463\);
- \(r_p=0.840778765\,\mathrm{fm}\).

## 2. Normalizações

\[
G_E^p(0)=1.000000000000,
\qquad
G_M^p(0)=2.792828941532.
\]

\[
G_E^n(0)=+0.000000000000e+00,
\qquad
G_M^n(0)=-1.912810907194.
\]

## 3. Inclinação elétrica do próton

\[
r_p^2=0.706908932402\,\mathrm{fm}^2.
\]

Pela derivada numérica:

\[
-6\left.\frac{dG_E^p}{dq^2}\right|_0
=0.706908932357\,\mathrm{fm}^2.
\]

Erro relativo:

\[
-6.236e-11.
\]

## 4. Nêutron

Foram avaliados dois níveis.

### 4.1 Fechamento líder mínimo

\[
G_E^n(q^2)
=
A_n[
j_0(qr_+)-j_0(qr_-)
],
\qquad
r_->r_+.
\]

Com:

\[
A_n=\alpha\delta_B=0.018468329045,
\quad
r_+=0.837711036\,\mathrm{fm},
\quad
r_-=0.843846495\,\mathrm{fm}.
\]

Isso garante:

\[
G_E^n(0)=0,
\qquad
\langle r_n^2\rangle=-1.905401041655e-04\,\mathrm{fm}^2.
\]

A forma fechada equivalente é:

\[
\langle r_n^2\rangle_{\rm líder}
=
-2\alpha^2\delta_B r_p^2
=
-1.905401041655e-04\,\mathrm{fm}^2.
\]

O valor acima não é uma comparação final com dados; ele apenas confirma a
estrutura de polarização com sinal negativo.

### 4.2 Fechamento estendido de cola dupla

A amplitude é a projeção torsional espacial já fixada pelo momento magnético:

\[
A_n^{(2)}=|\mu_n|=1.912810907194.
\]

O deslocamento relativo vem das duas interfaces antiparalelas:

\[
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2)
=
0.043530269017.
\]

Assim:

\[
r_+^{(2)}=0.822479103\,\mathrm{fm},
\qquad
r_-^{(2)}=0.859078428\,\mathrm{fm}.
\]

E:

\[
\langle r_n^2\rangle_{\rm ext}
=
-0.117721789624\,\mathrm{fm}^2.
\]

Pela derivada numérica:

\[
-6\left.\frac{dG_{E,\rm ext}^n}{dq^2}\right|_0
=
-0.117721789948\,\mathrm{fm}^2.
\]

Esse valor não foi usado como alvo. Ele sai de \(|\mu_n|\),
\(2\alpha\ln(2\pi^2)\) e \(r_p\).

### 4.3 Perfil suave de superfície

Para remover as deltas sem transformar a distribuição em densidade de bulk,
usa-se a coordenada local de superfície:

\[
\xi=r-r_p.
\]

A componente positiva fica no lado interno do estômato:

\[
\xi_+=-0.018299662921\,\mathrm{fm},
\]

e a componente negativa no lado externo:

\[
\xi_-=+0.018299662921\,\mathrm{fm}.
\]

A largura geométrica líder é:

\[
\sigma_r
=
\frac12r_p\alpha_{\rm tor}^{(2)}
=
0.018299662921\,\mathrm{fm}.
\]

O perfil suave é:

\[
\rho_E^n(\xi)
=
|\mu_n|[K_\sigma(\xi,\xi_+)-K_\sigma(\xi,\xi_-)].
\]

Resultado numérico:

\[
\int \rho_E^n d\xi
=
-6.101889826748e-16.
\]

\[
G_{E,\rm suave}^n(0)
=
-6.101889826748e-16.
\]

\[
-6\left.\frac{dG_{E,\rm suave}^n}{dq^2}\right|_0
=
-0.117721789721\,\mathrm{fm}^2.
\]

A diferença entre a inclinação suave e a inclinação de cascas é:

\[
-9.630e-11\,\mathrm{fm}^2.
\]

## 5. Status

\[
\boxed{
\text{fatores de forma fechados estruturalmente em normalização e baixa energia.}
}
\]

O perfil \(H_n(\chi)\) variacional é resolvido em
`solve_hn_variational_q40.py`. Este relatório mantém a checagem estrutural por
cascas e perfil suave, enquanto o relatório variacional fornece a curva
\(G_E^n(q^2)\) completa líder.
