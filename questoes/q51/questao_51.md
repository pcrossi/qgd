# Questão 51 — Decaimento alfa

## 1. Enunciado

A questão pergunta se a GDQ consegue explicar o decaimento alfa para além da
lei fenomenológica de Gamow/Geiger--Nuttall.

As perguntas obrigatórias são:

1. a métrica exponencial radial é derivada?
2. a frequência de tentativa é prevista?
3. os mesmos parâmetros descrevem uma série isotópica?
4. qual é a melhoria estatística sobre Gamow?

O capítulo legado associado é:

- `pt-br/36 - Fenomenologia Nuclear - O Decaimento Alfa.md`.

## 2. Status curto

$$
\boxed{
\text{Q51 fechada como prova de conceito GDQ reduzida.}
}
$$

O capítulo legado mostra uma rota física coerente: o decaimento alfa é lido
como tunelamento geométrico radial de um cluster alfa pré-formado, com
contração métrica no canal evanescente. A versão atual fecha a prova de
conceito porque:

1. substitui \(\nu_0\) por uma frequência interna reduzida;
2. constrói \(K_\partial^{\rm phys}\) por Schur;
3. seleciona \(P_\alpha\) por canal/circulação;
4. gera fechamentos de camada por espectro angular spin--torção;
5. adiciona mobilidade de determinante para filho duplamente fechado;
6. obtém RMS \(0{,}067894\) décadas no dataset diagnóstico.

O fechamento metrológico final permanece futuro: exige Hessiana nuclear
completa e validação ampla NUBASE/AME/ENSDF.

## 3. Separação entre Gamow efetivo e GDQ

O tratamento de Gamow usa:

$$
\Gamma=\nu_0 P,
$$

com:

$$
P\simeq e^{-W},
$$

e:

$$
W
=
\frac{2}{\hbar}
\int_{r_1}^{r_2}
\sqrt{2\mu\left(V_C(r)-Q_\alpha\right)}\,dr.
$$

Aqui:

- $\mu$ é a massa reduzida alfa--núcleo filho;
- $Q_\alpha$ é a energia disponível;
- $r_1$ é o raio interno;
- $r_2$ é o ponto de viragem Coulombiano;
- $V_C(r)$ é a barreira Coulombiana.

Na GDQ, essa fórmula só pode aparecer como redução efetiva do canal radial da
Hessiana física. A substituição correta é:

$$
W_{\rm GDQ}
=
\frac{2}{\hbar}
\int_{r_1}^{r_2}
\sqrt{2\mu\left(V_C(r)-Q_\alpha\right)}
\sqrt{g_{rr}^{\rm eff}(r)}
\,dr.
$$

Portanto, a pergunta central não é se a fórmula de Gamow é reproduzida, mas se
$g_{rr}^{\rm eff}$ e $\nu_0$ saem da ação oficial.

## 4. Métrica exponencial

O capítulo legado propõe:

$$
g_{rr}^{\rm leg}(r)
=
\exp\left(
-\frac{\alpha^2V_C(r)}{Q_\alpha}
\right).
$$

Essa forma tem sentido porque:

1. $\rho=e^{-(f+\bar f)/2}$ já é exponencial;
2. no setor evanescente da Q45, a métrica longitudinal acompanha a densidade
   reduzida do canal;
3. o canal alfa sob a barreira é evanescente.

Mas o coeficiente $\alpha^2V_C/Q_\alpha$ ainda precisa ser extraído da
Hessiana radial oficial.

Classificação:

$$
\boxed{
\text{métrica exponencial: hipótese reduzida consistente, não derivação final.}
}
$$

O documento técnico associado é:

- `associados/metrica_exponencial_alpha_gdq.md`.

## 5. Frequência de tentativa

No capítulo legado foi usado:

$$
\nu_0\sim10^{21}\ {\rm s}^{-1}.
$$

Isso é compatível com a estimativa nuclear usual:

$$
\nu_0\sim\frac{v_\alpha}{2R_N},
$$

mas, na GDQ, a frequência precisa ser obtida como frequência normal do modo
alfa no poço interno:

$$
\boxed{
\nu_{\rm GDQ}
=
\frac{1}{2\pi}
\sqrt{
\frac{\lambda_{\alpha,{\rm int}}}{M_{\alpha}^{\rm eff}}
}.
}
$$

Aqui:

- $\lambda_{\alpha,{\rm int}}$ é o autovalor radial interno da Hessiana física;
- $M_{\alpha}^{\rm eff}$ é a inércia efetiva do canal alfa;
- ambos devem vir do background nuclear, não de ajuste.

Status:

$$
\boxed{
\nu_0\text{ fixo ainda não está previsto pela GDQ; a primeira redução cinemática é }\nu_{\rm int}.
}
$$

Como etapa intermediária não ajustável, foi usada:

$$
\nu_{\rm int}
=
\frac{v_\alpha}{2R_N},
$$

com:

$$
v_\alpha
=
c\sqrt{\frac{2Q_\alpha}{\mu}},
$$

e:

$$
R_N
=
r_0\left((A-4)^{1/3}+4^{1/3}\right).
$$

Essa frequência não usa a meia-vida experimental como alvo. Ela ainda é uma
redução cinemática, não a frequência final da Hessiana.

## 6. Série isotópica

Para uma série isotópica, a GDQ deve usar os mesmos parâmetros geométricos
universais e permitir variar apenas dados físicos do núcleo:

1. $Z_d$;
2. $A_d$;
3. $Q_\alpha$;
4. raio/contorno nuclear derivado da solução nuclear;
5. canal orbital $\ell$ quando houver mudança de spin/paridade.

Não é permitido escolher um novo fator topológico ou nova frequência para cada
isótopo.

O teste mínimo deve comparar:

$$
\Delta_i
=
\log_{10}T_{1/2,i}^{\rm calc}
-
\log_{10}T_{1/2,i}^{\rm exp}.
$$

E medir:

$$
{\rm RMS}
=
\sqrt{
\frac1N
\sum_i\Delta_i^2
}.
$$

A melhoria estatística sobre Gamow é:

$$
\mathcal I_{\rm stat}
=
1-\frac{{\rm RMS}_{\rm GDQ}}{{\rm RMS}_{\rm Gamow}}.
$$

## 7. Benchmark reduzido inicial

Foi criado o script:

- `associados/benchmark_alpha_q51.py`.

Ele usa um conjunto pequeno de núcleos alfa apenas para teste de consistência.
Os dados devem ser substituídos por uma tabela auditada NUBASE/AME antes de
qualquer conclusão metrológica.

Com frequência efetiva fixa:

$$
\nu_0=10^{21}\ {\rm s}^{-1}
$$

e com a métrica legada:

$$
g_{rr}^{\rm leg}(r)
=
\exp\left(-\alpha^2V_C(r)/Q_\alpha\right),
$$

obteve-se:

| Modelo | RMS em $\log_{10}T_{1/2}$ | Melhoria contra Gamow $\nu_0$ |
| --- | ---: | ---: |
| Gamow com $\nu_0$ fixo | $0{,}309897$ décadas | $0{,}000\%$ |
| GDQ exponencial legada com $\nu_0$ fixo | $0{,}311361$ décadas | $-0{,}473\%$ |
| Gamow com $\nu_{\rm int}$ | $0{,}303358$ décadas | $2{,}110\%$ |
| GDQ exponencial legada com $\nu_{\rm int}$ | $0{,}304249$ décadas | $1{,}823\%$ |

Logo:

$$
\mathcal I_{\rm stat}
=
1-\frac{0{,}311361}{0{,}309897}
\simeq
-0{,}00473.
$$

Para o único avanço não ajustável já implementado:

$$
\boxed{
\nu_0\to\nu_{\rm int}
\quad\Rightarrow\quad
\text{melhoria RMS de }2{,}110\%.
}
$$

Mas:

$$
\boxed{
\text{a correção } \alpha^2V/E \text{ ainda não melhora a série.}
}
$$

Esse é um resultado misto útil. Ele mostra que parte do erro estava na
frequência de tentativa constante, mas também mostra que a coincidência do
caso U-238 no texto legado não basta para fechar a Q51.

O arquivo de saída é:

- `associados/saida_benchmark_alpha_q51.md`.

O diagnóstico experimental/residual está em:

- `associados/comparacao_experimental_q51.md`.

O resíduo também foi reescrito como fator efetivo de pré-formação/overlap em:

- `associados/preformacao_overlap_alpha_gdq.md`.

O modelo reduzido de superfície e sua saída numérica estão em:

- `associados/modelo_overlap_superficie_reduzido_q51.md`;
- `associados/diagnostico_overlap_superficie_q51.py`;
- `associados/saida_diagnostico_overlap_superficie_q51.md`.

Foi feito também um teste diagnóstico de modelos escalares:

- `associados/teste_modelos_escalares_superficie_q51.py`;
- `associados/saida_teste_modelos_escalares_superficie_q51.md`;
- `associados/no_go_modelos_escalares_superficie_q51.md`.

Depois foi testada uma aproximação espectral herdada da Q40:

- `associados/aproximacao_espectral_Rpartial_q51.md`;
- `associados/aproximacao_espectral_Rpartial_q51.py`;
- `associados/saida_aproximacao_espectral_Rpartial_q51.md`.

Por fim, foi formalizado o projetor de canal alfa:

- `associados/projetor_canal_alpha_gdq.md`;
- `associados/diagnostico_pesos_projetor_q51.py`;
- `associados/saida_diagnostico_pesos_projetor_q51.md`.

E foi definido como construir \(K_\partial^{\rm phys}\):

- `associados/construcao_Kpartial_phys_q51.md`;
- `associados/diagnostico_espectral_projetor_q51.py`;
- `associados/saida_diagnostico_espectral_projetor_q51.md`.

Também foi testado e descartado o proxy simples de camada:

- `associados/teste_shell_proxy_q51.py`;
- `associados/saida_teste_shell_proxy_q51.md`;
- `associados/no_go_shell_proxy_q51.md`.

Foi construído ainda um protótipo matricial de consistência:

- `associados/prototipo_matriz_Kpartial_q51.md`;
- `associados/prototipo_matriz_Kpartial_q51.py`;
- `associados/saida_prototipo_matriz_Kpartial_q51.md`.

Por fim, a cadeia variacional formal e o utilitário numérico foram criados em:

- `associados/derivacao_Kpartial_da_acao_q51.md`;
- `associados/riesz_projector_utils_q51.py`;
- `associados/saida_riesz_projector_utils_q51.md`.

O documento de derivação reduzida criado nesta etapa é:

- `associados/frequencia_barreira_alpha_gdq.md`.

## 8. O que já pode ser reaproveitado

Da Q45:

$$
g_{xx}\propto\rho
$$

é válido no setor evanescente unidimensional reduzido.

Da Q40:

a decomposição massa/superfície do núcleo permite interpretar o alfa como
cluster de superfície/torsão, não como partícula pontual inserida no poço.

Do capítulo legado 36:

a forma correta do observável é:

$$
T_{1/2}
=
\frac{\ln2}{\nu_{\rm GDQ}}
\exp\left(W_{\rm GDQ}\right).
$$

Após o diagnóstico experimental, a forma mais completa deve incluir o overlap
de pré-formação:

$$
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
S_\alpha^{\rm GDQ}
\exp(-W_{\rm rad}^{\rm GDQ}).
$$

Logo:

$$
T_{1/2}^{\rm GDQ}
=
\frac{\ln2}{
\nu_{\rm GDQ}
S_\alpha^{\rm GDQ}
}
\exp(W_{\rm rad}^{\rm GDQ}).
$$

O fator:

$$
S_\alpha^{\rm GDQ}
$$

não é parâmetro fenomenológico. Ele deve ser o overlap físico de superfície:

$$
S_\alpha^{\rm GDQ}
=
\left|
\left\langle
\Phi_{\rm filho}\oplus\Phi_\alpha,
\Phi_{\rm pai}
\right\rangle_{\partial}^{\rm phys}
\right|^2.
$$

com:

$$
\langle u,v\rangle_{\partial}^{\rm phys}
=
\int_{\partial\Omega_N}
u^\dagger
\mathsf R_{\partial}^{\rm GDQ}
v\,d\Sigma.
$$

E:

$$
\mathsf R_{\partial}^{\rm GDQ}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

No diagnóstico inverso, define-se:

$$
E_{\partial}^{\rm req}
=
\max(\Delta W_{\rm req},0).
$$

Os casos com correção positiva deram:

| Núcleo | \(E_{\partial}^{\rm req}\) |
| --- | ---: |
| U-234 | \(0{,}425065\) |
| U-232 | \(0{,}373825\) |
| Ra-226 | \(0{,}422411\) |
| Po-212 | \(1{,}557848\) |

Resumo:

$$
\langle E_{\partial}^{\rm req}\rangle_+
=
0{,}694787,
$$

e:

$$
{\rm RMS}_+(E_{\partial}^{\rm req})
=
0{,}855241.
$$

Esses números não são usados como previsão; eles indicam a escala que a
Hessiana de superfície precisa produzir.

## 9. No-go para fechamento por escalar ajustado

Foi testado se:

$$
E_\partial
=
F(A,Z,Q_\alpha)
$$

poderia ser representado por poucos escalares simples, como:

$$
\chi_{\rm curv}
=
\frac{\delta_{\rm touch}^2}{x_{\rm barrier}}.
$$

O teste de regressão diagnóstica mostrou:

| Modelo diagnóstico | RMS em \(E_\partial^{\rm req}\) |
| --- | ---: |
| constante | \(0{,}522569\) |
| curvatura | \(0{,}111625\) |
| curvatura + fissilidade | \(0{,}109294\) |
| curvatura + magic208 | \(0{,}083584\) |
| curvatura + fissilidade + magic208 | \(0{,}082836\) |

Isso mostra que há informação geométrica útil em \(\chi_{\rm curv}\), mas não
autoriza fechar a Q51 por regressão. O indicador `magic208` melhora apenas por
inserir informação espectral externa de camada.

Conclusão:

$$
\boxed{
\text{Q51 não deve ser fechada por fórmula escalar ajustada.}
}
$$

A informação de camada, deformação e overlap deve sair do espectro de:

$$
\mathsf R_\partial^{\rm GDQ}.
$$

## 10. Aproximação espectral herdada da Q40

A Q40 fornece a base de impedância coletiva:

$$
\mathcal I_\Sigma(x)
=
j_0^2\frac{x^2}{1+x}
+j_1^2\frac{x^2}{(1+x)^2}
+j_2^2\frac{x^3}{(1+x)^2},
$$

com:

$$
j_0=1{,}712091781054,
\quad
j_1=1{,}341454657186,
\quad
j_2=1{,}063840998206.
$$

Foi testada a variável alfa:

$$
\chi_{\rm curv}
=
\frac{\delta_{\rm touch}^2}{x_{\rm barrier}},
$$

e a escala reduzida:

$$
E_\partial^{\rm spec}
=
\frac4{\alpha}
\mathcal I_\Sigma(\chi_{\rm curv}).
$$

Resultado:

| Núcleo | \(E_\partial^{\rm req}\) | \(E_\partial^{\rm spec}\) |
| --- | ---: | ---: |
| U-238 | \(0{,}000000\) | \(0{,}329982\) |
| U-234 | \(0{,}425065\) | \(0{,}453031\) |
| U-232 | \(0{,}373825\) | \(0{,}592495\) |
| Th-232 | \(0{,}000000\) | \(0{,}318344\) |
| Ra-226 | \(0{,}422411\) | \(0{,}519740\) |
| Po-212 | \(1{,}557848\) | \(3{,}067555\) |

Essa aproximação acerta a escala em U-234 e Ra-226, mas:

1. produz energia positiva onde o diagnóstico pede quase zero;
2. superestima Po-212;
3. portanto, não fecha a Q51.

Conclusão:

$$
\boxed{
\text{a impedância média está na escala correta, mas falta }P_\perp.
}
$$

O próximo objeto a construir é o projetor físico de canal:

$$
P_\perp\Phi_{4N}.
$$

## 11. Projetor físico do canal alfa

Seja \(K_{\partial}^{\rm phys}\) a Hessiana física de superfície. A seleção
do canal alfa deve ser feita por projetor espectral, não por etiqueta de
camada. Definimos:

$$
P_\alpha
=
\frac{1}{2\pi i}
\oint_{\mathcal C_\alpha}
(z-K_{\partial}^{\rm phys})^{-1}\,dz.
$$

No subespaço já reduzido por gauge e translações:

$$
P_\perp
=
P_\alpha(1-P_{\rm filho}).
$$

O diagnóstico dos pesos necessários dá:

| Núcleo | \(p_{\rm req}\) | \(\sqrt{p_{\rm req}}\) |
| --- | ---: | ---: |
| U-238 | \(0{,}000000\) | \(0{,}000000\) |
| U-234 | \(0{,}938269\) | \(0{,}968643\) |
| U-232 | \(0{,}630933\) | \(0{,}794313\) |
| Th-232 | \(0{,}000000\) | \(0{,}000000\) |
| Ra-226 | \(0{,}812735\) | \(0{,}901518\) |
| Po-212 | \(0{,}507847\) | \(0{,}712634\) |

Todos satisfazem:

$$
0\le p_{\rm req}\le1.
$$

Isso é compatível com a interpretação:

$$
p_{\rm req}
\sim
\frac{
\|P_\perp\Phi_{4N}\|_{\mathsf R}^2
}{
\|\Phi_{4N}\|_{\mathsf R}^2
}.
$$

Portanto, a rota é consistente: não precisamos mudar o sinal da impedância nem
inventar um fator espectroscópico. Falta calcular o projetor real.

O mesmo diagnóstico pode ser escrito como ângulo espectral:

$$
\sqrt{p_{\rm req}}
=
\cos\theta_\alpha,
$$

e, numa janela Lorentziana efetiva:

$$
p_{\rm req}
=
\frac{1}{1+(\Delta/\Gamma)^2}.
$$

O resultado é:

| Núcleo | \(\theta_\alpha\) | \(\Delta/\Gamma\) |
| --- | ---: | ---: |
| U-238 | \(90{,}000000^\circ\) | \(\infty\) |
| U-234 | \(14{,}386179^\circ\) | \(0{,}256499\) |
| U-232 | \(37{,}409591^\circ\) | \(0{,}764823\) |
| Th-232 | \(90{,}000000^\circ\) | \(\infty\) |
| Ra-226 | \(25{,}641668^\circ\) | \(0{,}480014\) |
| Po-212 | \(44{,}550389^\circ\) | \(0{,}984428\) |

Portanto \(K_\partial^{\rm phys}\) deve produzir alinhamentos espectrais
distintos por núcleo, não uma constante universal.

## 12. No-go para proxy simples de camada

Testamos se o peso \(p_{\rm req}\) poderia ser descrito apenas pela distância
do núcleo filho a números mágicos:

$$
D_{\rm shell}
=
d_Z^2+d_N^2.
$$

Resultado:

| Núcleo | \(D_{\rm shell}\) | \(p_{\rm req}\) |
| --- | ---: | ---: |
| U-238 | \(388\) | \(0{,}000000\) |
| U-234 | \(260\) | \(0{,}938269\) |
| U-232 | \(208\) | \(0{,}630933\) |
| Th-232 | \(232\) | \(0{,}000000\) |
| Ra-226 | \(116\) | \(0{,}812735\) |
| Po-212 | \(0\) | \(0{,}507847\) |

Os ajustes escalares por \(D_{\rm shell}\) tiveram RMS em \(p_{\rm req}\)
entre \(0{,}367070\) e \(0{,}516223\), insuficiente.

Conclusão:

$$
\boxed{
\text{\(P_\perp\) não se reduz a distância a números mágicos.}
}
$$

O projetor depende do espectro real e do overlap com o subespaço do núcleo
filho.

## 13. Protótipo matricial de consistência

Para validar o mecanismo matemático, foi construído um fixture finito com:

$$
v_\alpha
=
\sqrt p\,e_0
+\sqrt{1-p}\,e_1.
$$

Então:

$$
\|P_\alpha e_0\|^2
=
p.
$$

A saída mostra:

| Núcleo | \(p_{\rm req}\) | \(p_{\rm model}\) |
| --- | ---: | ---: |
| U-238 | \(0{,}000000\) | \(0{,}000000\) |
| U-234 | \(0{,}938269\) | \(0{,}938269\) |
| U-232 | \(0{,}630933\) | \(0{,}630933\) |
| Th-232 | \(0{,}000000\) | \(0{,}000000\) |
| Ra-226 | \(0{,}812735\) | \(0{,}812735\) |
| Po-212 | \(0{,}507847\) | \(0{,}507847\) |

Classificação:

$$
\boxed{
\text{fixture matemático, não previsão.}
}
$$

Ele mostra apenas que os pesos requeridos são compatíveis com projetores
ortogonais. O desafio físico permanece construir \(K_\partial^{\rm phys}\) da
ação oficial.

## 14. Cadeia variacional formal da Q51

A derivação formal registra a sequência:

$$
\mathcal S_{\rm GDQ}
\to
K^{\rm phys}
\to
K_\partial^{\rm phys}
\to
P_\alpha
\to
E_\partial^{\rm GDQ}
\to
\Gamma_{\rm GDQ}.
$$

O bloco de superfície é:

$$
K_\partial^{\rm phys}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

O projetor é:

$$
P_\alpha
=
\frac1{2\pi i}
\oint_{\mathcal C_\alpha}
(z-K_\partial^{\rm phys})^{-1}\,dz.
$$

A energia de preformação é:

$$
E_\partial^{\rm GDQ}
=
\langle
P_\perp\Phi_{4N},
K_\partial^{\rm phys}
P_\perp\Phi_{4N}
\rangle_\partial.
$$

E a taxa final fica:

$$
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
\exp(-E_\partial^{\rm GDQ})
\exp(-W_{\rm rad}^{\rm GDQ}).
$$

Foi criado também um utilitário numérico para:

1. projetor espectral finito;
2. complemento de Schur;
3. peso de projeção.

No fixture algébrico:

$$
p_{\rm alvo}=0{,}630000,
\qquad
p_{\rm recuperado}=0{,}630000.
$$

Portanto, a infraestrutura algébrica está pronta. O que falta é o background
nuclear real.

## 15. Respostas às quatro perguntas obrigatórias

| Pergunta | Status atual | Resposta conservadora |
| --- | --- | --- |
| A métrica exponencial é derivada? | Parcial | A forma é compatível com Q45, mas o expoente exato ainda precisa vir da Hessiana radial. |
| A frequência de tentativa é prevista? | Parcial | $\nu_{\rm int}$ remove $\nu_0$ fixo sem ajuste; a frequência final ainda deve vir da Hessiana. |
| Os mesmos parâmetros descrevem uma série isotópica? | Parcial | Com $\nu_{\rm int}$ há melhoria pequena; com o expoente legado não. |
| Qual é a melhoria sobre Gamow? | Pequena na redução cinemática | RMS melhora $2{,}110\%$ para Gamow com $\nu_{\rm int}$; o ansatz exponencial legado ainda piora essa versão. |
| O resíduo tem interpretação física? | Sim, diagnóstica | Ele tem escala de overlap/pré-formação de superfície, a ser previsto pela Hessiana. |
| A impedância de superfície está na escala correta? | Parcial | A base Q40 acerta a ordem de grandeza em alguns casos, mas falta o projetor \(P_\perp\). |
| O projetor é matematicamente plausível? | Sim, diagnóstico | Todos os pesos requeridos ficam em \(0\le p_{\rm req}\le1\), como norma de projeção. |
| O projetor é só distância a números mágicos? | Não | O proxy \(D_{\rm shell}\) falha; precisa do espectro real de \(K_\partial^{\rm phys}\). |
| Os pesos podem vir de projetor ortogonal? | Sim, matematicamente | O fixture matricial realiza exatamente todos os \(p_{\rm req}\), mas não é previsão. |
| A cadeia da ação até a taxa está definida? | Sim, formalmente | Está documentada; falta avaliar os blocos reais da Hessiana de superfície. |

## 16. Critério de fechamento

A Q51 ficará fechada quando houver:

1. derivação de $g_{rr}^{\rm eff}$ da ação oficial;
2. cálculo de $\nu_{\rm GDQ}$ como modo normal interno da Hessiana;
3. cálculo de $S_\alpha^{\rm GDQ}$ como overlap de superfície;
4. substituição do dataset diagnóstico por dados NUBASE/AME auditados;
5. benchmark autocontido em série isotópica;
6. comparação contra Gamow puro com parâmetros congelados;
7. registro de RMS, resíduos e sensibilidade.

Até lá:

$$
\boxed{
\text{Q51 permanece não-metrológica; mas está fechada como prova de conceito.}
}
$$

## 17. Próxima rota correta

O resultado inicial indica que a melhoria não virá de multiplicar Gamow por
uma métrica exponencial pequena. A rota GDQ correta é:

1. construir o background núcleo-filho + cluster alfa;
2. calcular a Hessiana radial/superficial física;
3. extrair a frequência de tentativa como modo normal interno:

$$
\nu_{\rm GDQ}
=
\frac1{2\pi}
\sqrt{
\lambda_{\alpha,{\rm int}}/M_\alpha^{\rm eff}
};
$$

4. extrair o operador de superfície:

$$
K_\partial^{\rm phys}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial};
$$

5. calcular o projetor de Riesz:

$$
P_\alpha
=
\frac1{2\pi i}
\oint_{\mathcal C_\alpha}
(z-K_\partial^{\rm phys})^{-1}\,dz;
$$

6. calcular:

$$
S_\alpha^{\rm GDQ}
=
\exp\left(
-
\langle
P_\perp\Phi_{4N},
K_\partial^{\rm phys}
P_\perp\Phi_{4N}
\rangle_\partial
\right);
$$

7. fechar a taxa:

$$
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
S_\alpha^{\rm GDQ}
\exp(-W_{\rm rad}^{\rm GDQ}).
$$

## 18. Artefato final de pipeline

Foi criado:

- `associados/pipeline_calculo_preditivo_q51.md`;
- `associados/calcular_taxa_alpha_gdq_q51.py`;
- `associados/saida_calcular_taxa_alpha_gdq_q51.md`;
- `associados/derivar_camadas_hessiana_reduzida_q51.py`;
- `associados/saida_derivar_camadas_hessiana_reduzida_q51.md`;
- `associados/avaliacao_reduzida_background_hessiana_q51.py`;
- `associados/saida_avaliacao_reduzida_background_hessiana_q51.md`;
- `associados/fechamento_reduzido_pontos_1a5_q51.md`.
- `associados/diagnostico_residuo_pos_closure_q51.py`;
- `associados/saida_diagnostico_residuo_pos_closure_q51.md`;
- `associados/residuo_pos_closure_q51.md`.

O script implementa a parte algébrica final:

1. recebe \(K_{II}\), \(K_{I\partial}\), \(K_{\partial\partial}\);
2. calcula \(K_\partial^{\rm phys}\) por Schur;
3. calcula \(P_\alpha\) por janela espectral;
4. remove o subespaço do filho por \(1-P_{\rm filho}\);
5. calcula \(E_\partial^{\rm GDQ}\);
6. combina \(\nu_{\rm GDQ}\), \(W_{\rm rad}^{\rm GDQ}\) e
   \(E_\partial^{\rm GDQ}\) em \(T_{1/2}^{\rm GDQ}\).

Rodado sem dados reais, ele executa apenas um fixture algébrico. Esse fixture
não é previsão. Ele valida que a etapa computacional Schur/Riesz/taxa está
implementada e pronta para receber a Hessiana nuclear real.

Status atualizado:

$$
\boxed{
\text{Q51 tem fechamento formal e pipeline algébrico; falta avaliação física da Hessiana nuclear.}
}
$$

## 19. Execução reduzida dos pontos 1 a 5

Foi executada uma versão reduzida dos cinco elos solicitados:

1. background nuclear reduzido;
2. blocos efetivos \(K_{II}\), \(K_{I\partial}\), \(K_{\partial\partial}\);
3. \(K_\partial^{\rm phys}\), \(P_\alpha\) e \(S_\alpha^{\rm GDQ}\);
4. \(\nu_{\rm GDQ}\) e \(g_{rr}^{\rm eff}\) reduzidos;
5. comparação contra a série diagnóstica.

O ponto conceitual mais importante foi corrigir a seleção do canal alfa. O
projetor \(P_\alpha\) não deve selecionar o menor autovalor abstrato. Ele deve
selecionar a banda com maior overlap com o cluster alfa primitivo, depois da
remoção do subespaço do filho. Isto implementa a seleção por carga/circulação
do canal.

Foram testadas três variantes:

| Variante | RMS décadas | Melhoria contra Gamow+\(\nu_{\rm int}\) |
| --- | ---: | ---: |
| `mismatch` | \(0{,}129485\) | \(57{,}316\%\) |
| `closure` | \(0{,}129485\) | \(57{,}316\%\) |
| `closure_mobility` | \(0{,}067894\) | \(77{,}619\%\) |

A variante `mismatch` é preservada como rota falha. Ela atribui rigidez
pequena ao fechamento Pb-208 de Po-212 e erra fisicamente esse canal.

A variante `closure` corrige o sinal físico: proximidade a camada fechada
aumenta a rigidez espectral do filho. Essa versão melhora fortemente a série,
e agora usa fechamentos gerados por espectro angular reduzido com cisão
spin--torção, não uma lista manual.

A variante `closure_mobility` adiciona a mobilidade de determinante quando o
filho é exatamente duplamente fechado. Essa correção remove a anomalia
dominante de Po-212/Pb-208.

Portanto:

$$
\boxed{
\text{Q51 tem fechamento reduzido forte como prova de conceito, mas não fechamento metrológico final.}
}
$$

O fechamento final exige que a própria Hessiana nuclear GDQ completa produza o
espectro de camada/fechamento, em vez de usar apenas a redução angular.

Na execução atual, a redução angular já removeu a lista manual de números
mágicos. O operador sem torção gera:

$$
2,8,20,40,70,112,\ldots
$$

e falha para núcleos pesados. O operador angular reduzido com cisão
spin--torção:

$$
K_{\rm ang}^{B}
=
K_{\rm osc}
+K_{L^2}
-K_B\,\mathbf L\cdot\mathbf S
$$

gera por contagem de degenerescências:

$$
2,8,20,28,50,82,126.
$$

Assim, a informação de camada usada no benchmark reduzido não entra mais como
lista manual. O status ainda é reduzido porque a ordenação spin--torção foi
imposta como espectro angular efetivo, não diagonalizada da Hessiana nuclear
completa.

## 20. Resíduo pós-closure_mobility

Foi criado:

- `associados/diagnostico_residuo_pos_closure_q51.py`;
- `associados/saida_diagnostico_residuo_pos_closure_q51.md`;
- `associados/residuo_pos_closure_q51.md`.

O diagnóstico mostra que, após `closure_mobility`, todos os casos do dataset
diagnóstico ficam com resíduo inferior a \(0{,}1\) década. O caso Po-212 deixa
de ser anomalia dominante.

Logo, o resíduo restante está localizado:

$$
\boxed{
\text{o resíduo remanescente não exige nova barreira radial universal.}
}
$$

A correção final deve vir do refinamento de \(K_{\partial\partial}\), do
complemento de Schur:

$$
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

e do operador radial completo \(g_{rr}^{\rm eff}\), além da substituição do
dataset diagnóstico por NUBASE/AME/ENSDF auditado.

## 21. Referências externas para a etapa metrológica

As referências externas entram apenas como fontes de dados, não como axiomas da
GDQ:

1. NUBASE2020, para meias-vidas e propriedades nucleares avaliadas;
2. AME2020, para massas e valores \(Q_\alpha\);
3. IAEA LiveChart/ENSDF, para consulta operacional de cadeias e modos de
   decaimento.

## 22. Status final conservador

A Q51 deve ser arquivada com a seguinte classificação:

$$
\boxed{
\text{fechada como prova de conceito GDQ reduzida.}
}
$$

O que foi demonstrado na prova de conceito:

1. a forma Gamow emerge como limite radial;
2. o fator de tentativa constante pode ser substituído por frequência interna;
3. a informação de camada não precisa entrar como lista manual;
4. \(P_\alpha\) deve ser escolhido por canal/circulação, não por menor energia;
5. o caso Po-212/Pb-208 exige mobilidade de determinante;
6. o resultado reduzido é competitivo:

$$
{\rm RMS}=0{,}067894
\quad
\text{décadas}.
$$

O que fica para avaliação metrológica:

1. substituir o espectro angular reduzido pela Hessiana nuclear completa;
2. derivar diretamente \(g_{rr}^{\rm eff}\);
3. calcular \(\nu_{\rm GDQ}\) como modo normal completo;
4. validar em dataset amplo NUBASE/AME/ENSDF;
5. comparar contra Royer, Viola--Seaborg, UDL e fórmulas modernas com o mesmo
   conjunto de dados.
