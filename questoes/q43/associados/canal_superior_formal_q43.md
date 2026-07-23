# Q43 — Canal superior de \(g-2\): derivação formal e obstrução metrológica

## 1. Objetivo

Este documento responde diretamente ao pedido de substituir os parâmetros
diagnósticos

\[
\mu_{2,\ell}^{\rm required}
\]

por quantidades derivadas da ação oficial.

A conclusão é:

\[
\boxed{
\text{o canal superior é formalmente derivável da ação oficial,}
}
\]

mas:

\[
\boxed{
\text{os números metrológicos ainda não são determináveis com os dados atuais.}
}
\]

O motivo não é conceitual. É falta de três objetos físicos do background
leptônico:

\[
e_{2,\ell},
\qquad
K_{2,\ell},
\qquad
\mu_{2,\ell}.
\]

## 2. Definição variacional exata do canal superior

No setor com circulação fixada:

\[
\mathcal C[\Phi]=C_\ell,
\]

o funcional aumentado é:

\[
\mathscr I[\Phi,\lambda;B]
=
\mathcal S_{\rm GDQ}[\Phi]
-B\,M[\Phi]
-\lambda\left(\mathcal C[\Phi]-C_\ell\right).
\]

No background estacionário \(\Phi_\ell\), defina a Hessiana física:

\[
H_{C,\ell}
=
P_C^\dagger
\left.\delta^2\mathcal S_{\rm GDQ}\right|_{\Phi_\ell}
P_C.
\]

Escolha uma base física ortogonal:

\[
\{e_{0,\ell},e_{1,\ell},e_{2,\ell},\ldots\},
\]

com:

1. \(e_{0,\ell}\): direção do vínculo de circulação;
2. \(e_{1,\ell}\): canal harmônico líder que produz \(\alpha/(2\pi)\);
3. \(e_{2,\ell}\): primeiro canal transversal superior.

Então os coeficientes superiores não são livres. Eles são:

\[
K_{2,\ell}
=
\langle e_{2,\ell},H_{C,\ell}e_{2,\ell}\rangle,
\]

\[
J_{2,\ell}
=
-\langle e_{0,\ell},H_{C,\ell}e_{2,\ell}\rangle,
\]

\[
\mu_{2,\ell}
=
\langle e_{2,\ell},m_{\perp,\ell}\rangle,
\]

onde:

\[
m_{\perp,\ell}
=
\left.
\frac{\delta M}{\delta\Phi}
\right|_{\Phi_\ell}
-\gamma_{0,\ell}
\left.
\frac{\delta\mathcal C}{\delta\Phi}
\right|_{\Phi_\ell}.
\]

Essas fórmulas são a substituição correta para
\(\mu_{2,\ell}^{\rm required}\).

## 3. O que a ação oficial já fixa

A ação oficial fixa:

1. \(H_{C,\ell}\), uma vez dado o background \(\Phi_\ell\);
2. \(c_\ell=\delta\mathcal C/\delta\Phi\);
3. a parte mínima \(\gamma_{0,\ell}c_\ell\);
4. o canal harmônico líder, pela norma:

\[
\left\langle\frac{d\vartheta}{2\pi},
\frac{d\vartheta}{2\pi}\right\rangle
=
\frac{1}{2\pi}.
\]

Por isso:

\[
a^{(1)}=\frac{\alpha}{2\pi}
\]

está fechado.

## 4. O que a ação oficial ainda não fornece nos arquivos atuais

Para fechar a metrologia superior, falta construir o próprio modo
\(e_{2,\ell}\) no background físico.

Isso exige:

1. definir o domínio físico completo de \(H_{C,\ell}\);
2. projetar gauge, fase comum, modos de Noether e variações de carga;
3. diagonalizar o setor transversal;
4. identificar o primeiro modo que acopla ao momento magnético, mas não à
   carga;
5. calcular \(K_{2,\ell}\), \(J_{2,\ell}\) e \(\mu_{2,\ell}\) pelas integrais
   acima.

Sem essa etapa, qualquer número para \(\mu_{2,\ell}\) é escolha de modelo ou
engenharia inversa.

## 5. Prova de não-unicidade

No bloco operacional:

\[
H_{\rm req}
=
\begin{pmatrix}
1 & -1 & -J_2\\
-1 & K_1 & 0\\
-J_2 & 0 & K_2
\end{pmatrix},
\qquad
m_\perp=
\begin{pmatrix}
0\\1\\\mu_2
\end{pmatrix},
\]

o observável é:

\[
a
=
\frac{\langle c,H_{\rm req}^{-1}m_\perp\rangle}
{\langle c,H_{\rm req}^{-1}c\rangle}.
\]

Fixado um alvo \(a_{\rm obs}\), para muitos pares \((J_2,K_2)\) existe um
\(\mu_2\) distinto que reproduz o mesmo valor. Logo:

\[
\boxed{
a_{\rm obs}\text{ não determina }(J_2,K_2,\mu_2).
}
\]

Portanto, ajustar \(\mu_2\) não é derivar o canal superior.

## 6. Critério de fechamento metrológico

Q43 só vira previsão metrológica completa quando for possível escrever:

\[
\mu_{2,\ell}^{\rm GDQ}
=
\left\langle e_{2,\ell},
\left.
\frac{\delta M}{\delta\Phi}
\right|_{\Phi_\ell}
-\gamma_{0,\ell}
\left.
\frac{\delta\mathcal C}{\delta\Phi}
\right|_{\Phi_\ell}
\right\rangle
\]

e:

\[
K_{2,\ell}^{\rm GDQ}
=
\langle e_{2,\ell},H_{C,\ell}e_{2,\ell}\rangle,
\]

\[
J_{2,\ell}^{\rm GDQ}
=
-\langle e_{0,\ell},H_{C,\ell}e_{2,\ell}\rangle,
\]

com todos os termos avaliados no mesmo background \(\Phi_\ell\).

## 7. Veredito

\[
\boxed{
\text{não há ainda previsão metrológica completa de }g-2.
}
\]

O que existe agora é mais forte do que antes:

1. o termo líder está derivado e computado;
2. a estrutura \(H_C,c,m_\perp\) está operacional;
3. os resíduos experimentais foram isolados;
4. a não-unicidade dos blocos superiores foi explicitada;
5. o contrato exato para substituir \(\mu_{2,\ell}^{\rm required}\) foi
   definido.

Esse resultado impede fechar Q43 por ajuste e define exatamente o próximo
cálculo físico necessário.

## 8. Extração computacional dos coeficientes

Foi criado o script:

\[
\texttt{extrair\_canal\_superior\_q43.py}.
\]

Ele recebe um arquivo `.npz` com:

1. \(H\);
2. \(c\);
3. \(m_\perp\);
4. \(\gamma_0\).

O algoritmo faz:

1. normaliza:

\[
e_0=\frac{c}{\|c\|};
\]

2. constrói o complemento ortogonal \(Q\) de \(e_0\);
3. projeta a Hessiana:

\[
H_T=Q^\dagger H Q;
\]

4. diagonaliza:

\[
H_Tv_i=K_i v_i;
\]

5. levanta:

\[
e_i=Qv_i;
\]

6. calcula:

\[
K_i=\langle e_i,He_i\rangle,
\qquad
J_i=-\langle e_0,He_i\rangle,
\qquad
\mu_i=\langle e_i,m_\perp\rangle.
\]

Portanto, se a entrada for a Hessiana oficial projetada, o script executa
exatamente a derivação numérica dos coeficientes superiores.

## 9. Resultados nos blocos disponíveis

### 9.1 Bloco líder

Entrada:

\[
\texttt{hessiana\_lider\_q43.npz}.
\]

Resultado:

| canal | \(K_i\) | \(J_i\) | \(\mu_i\) |
|---:|---:|---:|---:|
| 1 | \(8.6102257658\times10^2\) | \(1\) | \(1\) |

Esse é o canal harmônico líder e reproduz:

\[
a^{(1)}=\frac{\alpha}{2\pi}.
\]

### 9.2 Bloco `required` do elétron

Entrada:

\[
\texttt{hessiana\_required\_e\_q43.npz}.
\]

Resultado:

| canal | \(K_i\) | \(J_i\) | \(\mu_i\) |
|---:|---:|---:|---:|
| 1 | \(8.6102257658\times10^2\) | \(1\) | \(1\) |
| 2 | \(8.6102257658\times10^2\) | \(1\) | \(-1.5132915275\times10^{-3}\) |

Como \(K_2=K_1\) nesse bloco diagnóstico, há degenerescência. Assim, a escolha
do segundo canal não é única. Isso confirma que o bloco não é uma derivação
física.

### 9.3 Bloco `required` do múon

Entrada:

\[
\texttt{hessiana\_required\_mu\_q43.npz}.
\]

Resultado:

| canal | \(K_i\) | \(J_i\) | \(\mu_i\) |
|---:|---:|---:|---:|
| 1 | \(8.6102257658\times10^2\) | \(1\) | \(1\) |
| 2 | \(1.7803179361\times10^5\) | \(1\) | \(8.0307612309\times10^{-1}\) |

Esse resultado recupera a engenharia inversa já embutida no bloco. Ele mostra
como extrair os coeficientes, mas não prova que esses são os coeficientes da
GDQ oficial.

## 10. Conclusão operacional

O pedido “derivar \(K_2,J_2,\mu_2\)” foi reduzido a um procedimento explícito:

\[
\boxed{
H_{C,\ell}\ \text{oficial}
\quad\Longrightarrow\quad
e_{2,\ell},K_{2,\ell},J_{2,\ell},\mu_{2,\ell}.
}
\]

O script já executa essa seta. O que ainda falta para a previsão metrológica
não é álgebra, mas a entrada física:

\[
\boxed{
H_{C,\ell}\text{ oficial no background leptônico }\Phi_\ell.
}
\]
