# Q38 — Fano como impedância gravitacional de contorno

## 1. Objetivo

Este documento organiza o papel de:

\[
\chi_{\rm Fano}
\]

na avaliação de:

\[
\mathcal V_{\rm eff}^{(G)}.
\]

O problema imediato é que aparecem dois valores:

\[
\chi_{\rm Fano}^{(1)}
=
\frac{3\sqrt2}{5}
\approx0.848528,
\]

e, no solver V2:

\[
\chi_{\rm Fano}^{(2)}
\approx0.4791.
\]

Esses dois números não devem ser tratados como constantes independentes.

---

## 2. Identificação do conflito

Calculando:

\[
\frac{3\sqrt2/5}{\sqrt{\pi}}
=
0.4787307\ldots
\]

Logo:

\[
\boxed{
0.4791
\approx
\frac{\chi_{\rm Fano}}{\sqrt{\pi}}
}
\]

com:

\[
\chi_{\rm Fano}
=
\frac{3\sqrt2}{5}.
\]

Portanto, o valor usado no script V2 parece ser um Fano já planificado:

\[
\chi_{\rm Fano}^{\rm flat}
=
\frac{\chi_{\rm Fano}^{\rm bulk}}{J_{\rm flat}},
\qquad
J_{\rm flat}\approx\sqrt{\pi}.
\]

---

## 3. Consequência para o solver V2

O script usa:

\[
\Pi_{1,\rm bulk}
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm script}}
V_{\rm eff},
\]

com:

\[
\chi_{\rm Fano}^{\rm script}
\approx
\frac{\chi_{\rm Fano}^{\rm bulk}}{\sqrt{\pi}}.
\]

Depois aplica:

\[
\Pi_{1,\rm obs}
=
\frac{\Pi_{1,\rm bulk}}{\sqrt{\pi}}.
\]

Substituindo:

\[
\Pi_{1,\rm obs}
=
\frac{
\alpha^4(1+\alpha)
V_{\rm eff}
}{
(\chi_{\rm Fano}^{\rm bulk}/\sqrt{\pi})
}
\frac1{\sqrt{\pi}},
\]

logo:

\[
\boxed{
\Pi_{1,\rm obs}
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}}
V_{\rm eff}.
}
\]

Ou seja: no solver V2, a planificação por \(\sqrt{\pi}\) cancela o uso de um
Fano já dividido por \(\sqrt{\pi}\).

Conclusão:

\[
\boxed{
\text{o erro de }0,34\%\text{ do V2 não prova independentemente a planificação;}
}
\]

ele testa uma combinação já misturada de Fano e planificação.

---

## 4. Interpretação física correta

O fator de Fano deve representar uma impedância/admitância de contorno entre:

1. canal solitônico discreto;
2. canal geométrico contínuo;
3. modo gravitacional que escapa para o observador local.

Na linguagem de operadores, a forma correta é:

\[
Z_{\rm eff}
=
Z_0
-
J^\dagger K^{-1}J.
\]

Aqui:

1. \(K\) é a Hessiana do setor interno/contorno;
2. \(J\) é o acoplamento entre o modo gravitacional externo e o canal interno;
3. \(Z_{\rm eff}\) é a impedância efetiva vista pelo modo \(R[h]\).

Então o fator de Fano deve ser definido por uma dessas formas:

\[
\chi_{\rm Fano}
=
Z_{\rm eff}^{-1},
\]

ou:

\[
\chi_{\rm Fano}
=
\frac{\Gamma_{\rm trans}}
{\Gamma_{\rm trans}+\Gamma_{\rm refl}},
\]

dependendo da convenção de transmissão/reflexão.

O ponto obrigatório:

\[
\boxed{
\chi_{\rm Fano}\text{ deve sair do operador de contorno, não de ajuste numérico.}
}
\]

---

## 5. Separação limpa dos fatores

Para evitar dupla contagem, a expressão deve ser escrita como:

\[
\Pi_{1,\rm obs}
=
\mathcal P_{\rm flat}
\left[
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}}
V_{\rm eff}^{\rm bulk}
\right].
\]

Se a projeção plana for escalar:

\[
\mathcal P_{\rm flat}[X]
=
\frac{X}{J_{\rm flat}},
\]

então:

\[
\Pi_{1,\rm obs}
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}J_{\rm flat}}
V_{\rm eff}^{\rm bulk}.
\]

Alternativamente, se o Fano usado já for planificado:

\[
\chi_{\rm Fano}^{\rm flat}
=
\chi_{\rm Fano}^{\rm bulk}J_{\rm flat},
\]

então não se deve aplicar outro fator de planificação depois.

No caso do solver V2, ocorreu a forma inversa:

\[
\chi_{\rm Fano}^{\rm script}
\approx
\frac{\chi_{\rm Fano}^{\rm bulk}}{\sqrt{\pi}},
\]

e depois houve divisão por \(\sqrt{\pi}\). Isso cancela a planificação em vez
de aplicá-la como fator físico independente.

---

## 6. Valor recomendado de trabalho

Para a derivação estrutural, manter:

\[
\boxed{
\chi_{\rm Fano}^{\rm bulk}
=
\frac{3\sqrt2}{5}.
}
\]

E manter separado:

\[
\boxed{
J_{\rm flat}
\quad\text{ou}\quad
\mathcal P_{\rm flat}.
}
\]

Assim:

\[
\Pi_{1,\rm obs}
=
\frac{1}{J_{\rm flat}}
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}}
V_{\rm eff}^{\rm bulk}.
\]

Se posteriormente for provado que:

\[
J_{\rm flat}=\sqrt{\pi},
\]

então:

\[
\Pi_{1,\rm obs}
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}\sqrt{\pi}}
V_{\rm eff}^{\rm bulk}.
\]

Essa é a forma sem mistura.

---

## 7. O que deve ser corrigido no solver

Criar uma versão auditada do solver Q38 com variáveis separadas:

\[
\chi_{\rm Fano}^{\rm bulk}
=
\frac{3\sqrt2}{5},
\]

\[
J_{\rm flat}
=
\sqrt{\pi}
\quad
\text{apenas se usado como hipótese explícita,}
\]

e:

\[
\Pi_{1,\rm obs}
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}}
V_{\rm eff}
\times
\frac1{J_{\rm flat}}.
\]

Também testar:

1. \(J_{\rm flat}=1\);
2. \(J_{\rm flat}=\sqrt{\pi}\);
3. \(J_{\rm flat}\) calculado por média ponderada;
4. \(J_{\rm flat}\) calculado pela norma do modo gravitacional.

---

## 8. Veredito

\[
\boxed{
\chi_{\rm Fano}\text{ não está perdido; a inconsistência é de mistura de normalizações.}
}
\]

O valor:

\[
0.4791
\]

deve ser reclassificado como fator efetivo misturado, aproximadamente:

\[
\frac{3\sqrt2/5}{\sqrt{\pi}}.
\]

Para fechar Q38, precisamos manter separados:

1. Fano bulk;
2. planificação;
3. normalização radial;
4. volume térmico efetivo.

---

## 9. Próximo passo

O próximo documento deve formular o solver auditado:

\[
\boxed{
\texttt{questoes/q38/associados/solver\_auditado\_q38.md}
}
\]

Objetivo:

1. separar \(\chi_{\rm Fano}\) e \(J_{\rm flat}\);
2. corrigir Dirichlet/Neumann/Robin;
3. testar sensibilidade do resultado;
4. indicar qual cálculo ainda falta para transformar o teste em previsão.

Continuação criada:

\[
\boxed{
\texttt{questoes/q38/associados/solver\_auditado\_q38.md}
}
\]

Ele especifica a forma correta de separar \(\chi_{\rm Fano}^{\rm bulk}\),
\(J_{\rm flat}\), \(S_{\rm inst}\), volume efetivo e condições de contorno.

Implementação executada:

\[
\boxed{
\texttt{numerico/q38\_gravidade/solve\_gravity\_q38\_auditado.py}
}
\]

Resultado:

\[
\boxed{
\text{a boa concordância atual usa }\chi_{\rm Fano}^{\rm bulk}=3\sqrt2/5
\text{ sem }J_{\rm flat}\text{ independente.}
}
\]

Aplicar \(J_{\rm flat}=\sqrt\pi\) separadamente desloca o resultado para erro
de aproximadamente \(43.7\%\). Portanto, a planificação deve ser tratada como
pendência derivacional, não como fator externo validado.
