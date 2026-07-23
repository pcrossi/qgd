# Q30 — Confinamento, Wilson loops e mass gap efetivo

Documentos canônicos:

- [questao_30.md](questao_30.md)
- [questao_30_yang_mills.md](questao_30_yang_mills.md)
- [avaliação reduzida do tubo Ricci--Bohm](associados/saida_tubo_ricci_bohm_gdq_q30.md)
- [integração direta do disco Ricci--Bohm](associados/saida_integracao_direta_tubo_ricci_bohm_q30.md)
- [derivação de C_GDQ no cap Ricci--Bohm](associados/derivacao_C_GDQ_tubo_ricci_bohm_q30.md)
- [fator de forma pelo raio efetivo legado](associados/saida_fator_forma_raio_efetivo_q30.md)
- [derivação do raio de superfície Q30/Q40](associados/derivacao_raio_efetivo_q30_q40.md)

Associados: [associados/](associados/)

Numéricos relacionados:

- `numerico/q30_confinamento/`

Status vigente: fechada estruturalmente na GDQ e fechada
metrologicamente de forma condicional ao raio efetivo de superfície/sonda; não
como solução Clay de Yang--Mills puro.

Resumo:

- Wilson loops, lei de área e gap geométrico são fechados como cadeia efetiva;
- Heaviside/YM é linguagem operacional externa, não ontologia fundamental;
- a integração direta do disco transversal Ricci--Bohm mostrou que, no cap
  primitivo, o fator $\pi$ vem de $\int_0^{r_\perp}2\pi s\,ds$, não de ajuste,
  e obteve
  $r_\perp=0{,}86\,\mathrm{fm}$,
  $\Delta_{\rm GDQ}=0{,}22945\,\mathrm{GeV}$ e
  $\sigma_{\rm GDQ}=0{,}83818\,\mathrm{GeV/fm}$;
- o coeficiente reduzido foi derivado geometricamente como
  $C_{\rm GDQ}=\frac14\int_{\rm cap}R_2dA=\pi$ no cap Ricci--Bohm primitivo;
- a cadeia Q39/Q40 deriva o raio canônico de superfície
  $r_p=0{,}840778765450\,\mathrm{fm}$, gerando
  $F_{\rm shape}=1{,}046245090518$ e
  $\sigma_{\rm GDQ}=0{,}876946044304\,\mathrm{GeV/fm}$, com desvio
  $-1{,}466737\%$;
- o raio legado comprimido $0{,}8354\,\mathrm{fm}$ melhora a tensão para
  $0{,}888274921594\,\mathrm{GeV/fm}$, mas deve ser tratado como cenário de
  compressão de sonda/probe, não como raio canônico de superfície;
- conclusão operacional: a lei linear, o gap positivo e a escala de tensão
  ficam fechados na GDQ; a distinção fina entre raio canônico
  $0{,}840778765450\,\mathrm{fm}$ e raio comprimido
  $0{,}8354\,\mathrm{fm}$ pertence ao contorno de sonda/aparelho;
- os arquivos associados registram os lemas e no-go necessários para preservar
  a coerência da rota.

Memória estruturada:

- `brain/conditional-results/q30-confinement-effective-su3/`
- `brain/open-problems/q30-explicit-confinement-numerics/`
