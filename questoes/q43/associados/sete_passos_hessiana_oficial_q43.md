# Q43 — Execução dos 7 passos para a Hessiana oficial

## 1. Objetivo

Executar, em forma reprodutível, os sete passos necessários para construir a
Hessiana oficial da GDQ no problema de Zeeman/\(g-2\).

O resultado é um pipeline funcional:

\[
\mathcal S_{\rm GDQ}
\to
H
\to
c
\to
H_C
\to
K_i,J_i,\mu_i.
\]

A execução foi feita em uma truncagem Galerkin reduzida. Ela testa a cadeia
matemática, mas ainda não é a Hessiana física metrológica do lépton.

## 2. Passo 1 — Background leptônico

Foi usado um background reduzido:

\[
x_*=(1,0,0,0,0),
\]

onde:

| índice | modo |
|---:|---|
| 0 | circulação/fase linear no ciclo |
| 1 | modo harmônico líder \(\sin\theta\) |
| 2 | modo fase superior \(\sin2\theta\) |
| 3 | modo de densidade \(\cos\theta\) em \(\operatorname{Re}f\) |
| 4 | modo métrico conformal \(\cos\theta\) |

Esse background não é declarado como o background leptônico físico final. Ele
é uma fatia Galerkin para testar a segunda variação.

## 3. Passo 2 — Flutuações

As flutuações foram parametrizadas por:

\[
f=F+iP,
\]

com:

\[
F=x_3\cos\theta,
\]

\[
P=\frac{x_0\theta}{2\pi}
+x_1\sin\theta
+x_2\sin2\theta,
\]

e métrica conformal:

\[
g=e^{2\sigma},
\qquad
\sigma=x_4\cos\theta.
\]

## 4. Passo 3 — Ação oficial reduzida

Foi avaliada a estrutura do integrando oficial:

\[
\left[
\tau\left(
\mathcal R
+g^{-1}\partial f\,\partial\bar f
\right)
+\frac{f+\bar f}{2}
-n
\right]
\mathcal U\sqrt g.
\]

Com:

\[
\mathcal U=e^{-(f+\bar f)/2},
\]

e a aproximação conformal bidimensional:

\[
\mathcal R=-2e^{-2\sigma}\Delta\sigma.
\]

Essa redução preserva a dependência correta em \(g,f,\bar f\) e na medida
\(\mathcal U\sqrt g\), mas não substitui o bulk oficial completo.

## 5. Passo 4 — Hessiana bruta

A Hessiana foi calculada por diferenças finitas:

\[
H_{ij}
=
\left.
\frac{\partial^2\mathcal S_{\rm GDQ}^{\rm red}}
\partial x_i\partial x_j
\right|_{x_*}.
\]

Autovalores obtidos:

| \(i\) | \(\lambda_i\) |
|---:|---:|
| 0 | \(-1.0620081191\times10^2\) |
| 1 | \(-4.3479167158\times10^1\) |
| 2 | \(6.2767127651\) |
| 3 | \(2.5079724492\times10^1\) |
| 4 | \(5.7527344657\times10^2\) |

O resultado possui modos negativos. Portanto, essa truncagem não é ainda uma
sela física estável. Ela é uma auditoria da cadeia.

## 6. Passo 5 — Circulação

A circulação reduzida é:

\[
\mathcal C(x)=x_0.
\]

Logo:

\[
c=\frac{\partial\mathcal C}{\partial x}
=(1,0,0,0,0).
\]

## 7. Passo 6 — Fonte magnética

A ação oficial nua não contém o campo externo \(B\) nem o funcional magnético
\(M[\Phi;B]\). Portanto:

\[
m_\perp^{\rm naked}=0.
\]

Consequência:

\[
a_{\rm geom}^{\rm naked}=0.
\]

Isso não contradiz o efeito Zeeman. Significa apenas que o campo magnético é
fonte/aparelho/contorno externo e deve ser especificado por:

\[
\mathscr I[\Phi,\lambda;B]
=
\mathcal S_{\rm GDQ}[\Phi]
-B\,M[\Phi]
-\lambda(\mathcal C[\Phi]-C).
\]

Sem o mapa \(M[\Phi]\), a ação oficial determina \(H\) e \(c\), mas não
\(m_\perp\).

## 8. Passo 7 — Extração dos canais

O script `extrair_canal_superior_q43.py` foi aplicado aos arquivos:

1. `hessiana_oficial_galerkin_nua_q43.npz`;
2. `hessiana_oficial_galerkin_lider_q43.npz`.

### 8.1 Setor nu

Como:

\[
m_\perp^{\rm naked}=0,
\]

todos os \(\mu_i\) extraídos são zero.

### 8.2 Setor com fonte líder de contorno

Usando uma fonte líder representada pelo modo 1:

\[
m_\perp=(0,1,0,0,0),
\]

o extrator encontrou:

| canal | \(K_i\) | \(J_i\) | \(\mu_i\) |
|---:|---:|---:|---:|
| 1 | \(-5.3372177576\times10^1\) | \(3.9878590801\times10^1\) | \(-2.0563710146\times10^{-3}\) |
| 2 | \(6.2766830908\) | \(-1.0395156988\times10^{-1}\) | \(9.9997387755\times10^{-1}\) |
| 3 | \(2.5012672968\times10^1\) | \(5.7400657812\) | \(1.5977145081\times10^{-3}\) |
| 4 | \(1.5340171328\times10^2\) | \(3.2283834497\times10^2\) | \(6.7426156054\times10^{-3}\) |

Como o primeiro canal tem \(K_1<0\), a truncagem ainda não é fisicamente
admissível para metrologia. O procedimento de extração, porém, está validado.

## 9. Arquivos produzidos

1. `hessiana_oficial_galerkin_q43.py`;
2. `hessiana_oficial_galerkin_nua_q43.npz`;
3. `hessiana_oficial_galerkin_lider_q43.npz`;
4. `saida_hessiana_oficial_galerkin_q43.md`;
5. `saida_extracao_hessiana_oficial_galerkin_nua_q43.md`;
6. `saida_extracao_hessiana_oficial_galerkin_lider_q43.md`.

## 10. Veredito

Os sete passos foram executados em uma redução Galerkin da ação oficial.

O que ficou demonstrado:

1. a segunda variação da ação oficial fornece uma Hessiana \(H\);
2. a circulação fornece \(c\);
3. o extrator calcula \(K_i,J_i,\mu_i\) quando recebe \(H,c,m_\perp\);
4. sem fonte magnética externa, \(m_\perp=0\);
5. a fonte magnética é dado de aparelho/contorno, não termo oculto da ação nua;
6. a truncagem Galerkin testada não é uma sela física, pois possui modos
   negativos.

O próximo passo real para previsão metrológica é construir um background
leptônico estável \(\Phi_\ell\) e o mapa físico \(M[\Phi;B]\). Só então os
coeficientes extraídos serão os coeficientes oficiais de \(g-2\).
