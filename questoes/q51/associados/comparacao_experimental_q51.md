# Q51 — Comparação experimental e diagnóstico do termo faltante

## 1. Classificação

Esta comparação é:

$$
\boxed{
\text{teste de consistência e comparação fenomenológica, não previsão cega.}
}
$$

Motivo: os dados do dataset atual são diagnósticos e a frequência final
\(\nu_{\rm GDQ}\) ainda não foi obtida da Hessiana física.

## 2. Observável comparado

O observável é:

$$
\log_{10}T_{1/2}.
$$

O modelo reduzido usa:

$$
T_{1/2}
=
\frac{\ln2}{\nu}
\exp(W),
$$

com:

$$
W
=
\frac2{\hbar}
\int_{r_1}^{r_2}
\sqrt{2\mu(V_C-Q_\alpha)}\,dr.
$$

## 3. Frequência interna reduzida

A primeira substituição não ajustável foi:

$$
\nu_0
\longrightarrow
\nu_{\rm int}
=
\frac{c}{2R_N}
\sqrt{\frac{2Q_\alpha}{\mu}}.
$$

Ela usa apenas \(Q_\alpha\), massa reduzida e raio geométrico de contato.

## 4. Resultado contra experimento

| Modelo | RMS em \(\log_{10}T_{1/2}\) | Melhoria |
| --- | ---: | ---: |
| Gamow com \(\nu_0=10^{21}\,\mathrm{s}^{-1}\) | \(0{,}309897\) | \(0{,}000\%\) |
| GDQ exponencial legada com \(\nu_0\) | \(0{,}311361\) | \(-0{,}473\%\) |
| Gamow com \(\nu_{\rm int}\) | \(0{,}303358\) | \(2{,}110\%\) |
| GDQ exponencial legada com \(\nu_{\rm int}\) | \(0{,}304249\) | \(1{,}823\%\) |

Portanto, a troca de frequência ajuda pouco, mas objetivamente. Já a métrica
exponencial legada não melhora o benchmark.

## 5. Correção de ação requerida

Defina:

$$
W_{\rm req}
=
\ln\left(
\frac{T_{1/2}^{\rm exp}\nu_{\rm int}}{\ln2}
\right).
$$

Então:

$$
\Delta W_{\rm req}
=
W_{\rm req}-W_{\rm Gamow}.
$$

No dataset diagnóstico:

| Núcleo | \(\Delta W_{\rm req}\) |
| --- | ---: |
| U-238 | \(-0{,}039094\) |
| U-234 | \(0{,}425065\) |
| U-232 | \(0{,}373825\) |
| Th-232 | \(-0{,}014190\) |
| Ra-226 | \(0{,}422411\) |
| Po-212 | \(1{,}557848\) |

## 6. Interpretação GDQ

O termo faltante não parece ser uma constante universal simples. A diferença
de padrão entre U-238/Th-232 e Po-212 indica que a correção deve depender da
estrutura do contorno nuclear:

1. deformação da superfície;
2. canal orbital \(\ell\);
3. impedância alfa--núcleo;
4. mistura dos modos internos eliminados.

Na linguagem GDQ, isso deve entrar por:

$$
V_{\rm Schur}
=
-K_{rI}K_{II}^{-1}K_{Ir}.
$$

## 7. Conclusão

O benchmark experimental atual mostra:

$$
\boxed{
\text{a Q51 melhora com }\nu_{\rm int},\text{ mas não fecha sem }V_{\rm Schur}.
}
$$

O próximo cálculo deve construir a Hessiana radial/superficial alfa--núcleo e
extrair \(V_{\rm Schur}\) diretamente, sem usar \(\Delta W_{\rm req}\) como
ajuste.

