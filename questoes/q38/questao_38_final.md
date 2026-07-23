# Relatório canônico da Questão 38 — derivação de \(G\) na GDQ

> **Documento único de referência.** Este relatório substitui, para fins de
> status e argumentação, os rascunhos `questoes/q38/historico/R38_2.md`, `questoes/q38/historico/r38_3.md`,
> `questoes/q38/historico/R_38_1t.md`, `questoes/q38/historico/RELATORIO_Q38_3.md` e os arquivos auxiliares em `questoes/q38/associados/`.
> Eles preservam o histórico dos cálculos, mas não devem ser citados como
> conclusões independentes. Em caso de divergência, vale este documento.

## 0. Pergunta, ação e geometrias oficiais

A pergunta é se a GDQ deriva a constante de Newton \(G\), incluindo a origem
da fórmula

\[
\Pi_G^{\rm GDQ}
=\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)},
\qquad
\Pi_G=\frac{GM_p^2}{\hbar c}.
\]

A ação fundamental considerada é

\[
\mathcal S_{\rm GDQ}=\int_\gamma\!\left[\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\left\{
\tau\left(\mathcal R+g^{\mu\bar\nu}\partial_\mu f
\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right\}\mathcal U\,dV_g\right]\frac{d\tau}{\tau},
\]

\[
n=4,
\qquad
\mathcal U=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^4},
\qquad
\int\mathcal U,dV_g=1.
\]

As representações geométricas adotadas pelo manuscrito são

\[
\boxed{\mathcal M_E=T^5\times S^3}
\]

para o espaço global/cosmológico de Einstein e

\[
\boxed{\mathcal M_P=T^4\times\mathbb R^4}
\]

para a leitura planar/local. Elas são backgrounds/regimes da mesma ação, não
uma compactificação convencional de Kaluza--Klein. Um mapa global explícito
entre as duas representações ainda não foi construído.

### 0.1 Níveis de fechamento usados neste relatório

- **Teorema:** consequência demonstrada das premissas declaradas.
- **Condição de contorno:** dado que define o problema físico particular.
- **Condicional:** consequência correta se uma identidade ainda não provada
  for assumida.
- **Fenomenológico:** fórmula numericamente eficaz, mas não completamente
  derivada.

## 1. Dados de contorno e grupo adimensional

O problema cosmológico é formulado com raio causal \(R_H\) e energia total
\(E_H\) dados na fronteira. Para um horizonte clássico,

\[
R_H=\frac{2GE_H}{c^4},
\qquad
\boxed{G=\frac{c^4R_H}{2E_H}}.
\]

Essa expressão é uma resposta de contorno, não uma previsão do tamanho ou da
energia particulares do universo. Ela só é não circular se \(E_H\) for dado
independentemente de \(G\).

Para a escala bariônica,

\[
\boxed{\Pi_G=\frac{GM_p^2}{\hbar c}},
\qquad
\boxed{G=\frac{\hbar c}{M_p^2}\Pi_G}.
\]

## 2. Regularidade térmica e remoção do \(7/2\)

A regularidade euclidiana do horizonte impõe

\[
\boxed{\beta_E=2\pi R_H}
\]

em unidades de comprimento. A medida de Perelman é normalizada,
\(\int\mathcal U dV=1\), portanto o termo constante

\[
\frac72=\frac{\binom82}{8}
\]

pertence ao background torsional médio e cancela no peso relativo

\[
\frac{\mathcal U_*}{\mathcal U_0}=e^{-(u_*-u_0)}.
\]

## 3. Fibrado axial

Da fase de Madelung \(e^{iv}\),

\[
v\sim v+2\pi,
\qquad f_v=1.
\]

O fibrado de sinal sobre \(\mathbb{RP}^2\) levanta para funções ímpares em
\(S^2_R\). O primeiro modo possui \(\ell=1\), logo

\[
\boxed{\lambda_{\rm ax}=\frac2{R^2}}.
\]

A ação axial relativa é

\[
\Delta u_v=\tau\pi^2\lambda_{\rm ax}
=\frac{2\pi^2\tau}{R^2}.
\]

## 4. Saddle térmico relativo

Após subtrair o setor térmico trivial \(m=0\), o primeiro winding do núcleo
8D é

\[
I_1(\tau)\propto\tau^{-4}e^{-\beta_E^2/(4\tau)}.
\]

Seu saddle é

\[
\boxed{\tau_*=\frac{\beta_E^2}{16}}.
\]

No saddle, o winding \(m=2\) é suprimido relativamente por
\(e^{-12}\simeq6.14\times10^{-6}\), e os seguintes ainda mais. Portanto, no
setor relativo, a aproximação de primeiro winding é estável ao nível de
\(10^{-5}\), antes das correções do potencial de Bismut.

Com \(\beta_E=2\pi R_H\),

\[
\tau_*=\frac{\pi^2R_H^2}{4}.
\]

Então

\[
\Delta u_v
=\frac{\pi^4}{2}\frac{R_H^2}{R^2}.
\]

## 5. Condição geométrica de compatibilidade

O expoente proposto é obtido se e somente se

\[
\frac{\pi^4}{2}\frac{R_H^2}{R^2}=\frac1{2\alpha},
\]

isto é,

\[
\boxed{
R=\pi^2\sqrt\alpha\,R_H
}
\]

ou

\[
\boxed{
\frac{R_H}{R}=\frac1{\pi^2\sqrt\alpha}=1.18608985.
}
\]

Tratada como condição de colagem dos dados de contorno cosmológicos com a
fibra \(S^3\), essa igualdade fornece

\[
\boxed{\Delta u_v=\frac1{2\alpha}},
\qquad
\boxed{\mathcal U_*/\mathcal U_0=e^{-1/(2\alpha)}}.
\]

Ela não é consequência da equação steady do bulk; deve ser explicitamente
declarada como condição geométrica de contorno ou derivada por um mapa de
colagem ainda não construído.

## 6. Prefator

A fórmula candidata é

\[
\Pi_G^{\rm GDQ}
=\mathcal A_{\rm spec}\,e^{-1/(2\alpha)},
\qquad
\mathcal A_{\rm spec}
\stackrel{\rm proposta}{=}
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}.
\]

### 6.1 \(\alpha^4\)

No canal Hermitiano complexo bidimensional, uma amplitude \(\alpha\) gera
resposta quadrática \(\alpha^2\) em cada direção e

\[
\det_{\mathbb C}(\alpha^2I_2)=\alpha^4.
\]

Esse resultado é válido se a transmissão reduzida for realmente
\(D_{\rm tr}=\alpha^2I_2\); essa identificação continua sendo uma lei
constitutiva do canal, não o determinante completo calculado.

### 6.2 \(1+\alpha\)

Uma classe de Chern integral não pode ser literalmente identificada com o
número real \(\alpha\): \(c_1(L)\in H^2(M,\mathbb Z)\). Portanto
\(1+\alpha\) não está derivado como classe de Chern. Ele permanece uma
correção efetiva de primeira ordem.

### 6.3 \(\chi_{\rm Fano}\)

\[
\chi_{\rm Fano}=\frac{3\sqrt2}{5}
\]

é uma contagem de canais. Sem os operadores de colagem e seus elementos de
matriz, não é um resultado espectral. Permanece conjectural.

Assim, o prefator completo continua fenomenológico, embora sua estrutura seja
geometricamente motivada.

## 7. Resultado numérico da fórmula candidata

Usando

\[
\Pi_G^{\rm GDQ}
=\frac{\alpha^4(1+\alpha)}{3\sqrt2/5}e^{-1/(2\alpha)},
\]

obtém-se

\[
\Pi_G^{\rm GDQ}=5.8906561\times10^{-39},
\]

\[
\boxed{
G_{\rm GDQ}=6.6567916\times10^{-11}
\ {\rm m^3\,kg^{-1}\,s^{-2}}.
}
\]

O desvio em relação a \(6.67430\times10^{-11}\) é

\[
\boxed{-0.262325\%.}
\]

Não se aplica correção eletromagnética posterior para apagar esse resíduo.

## 8. Veredito final

\[
\boxed{
\text{Buckingham, o limite newtoniano e a cadeia térmico-axial estão fechados
condicionalmente aos dados de contorno e à colagem }R=\pi^2\sqrt\alpha R_H.
}
\]

\[
\boxed{
\text{o valor completo de }G\text{ ainda não é ab initio porque a condição de
colagem e o prefator espectral não foram derivados do bulk.}
}
\]

Este é o fechamento máximo permitido pelos documentos atuais. Chamar a fórmula
de previsão exata exigiria transformar \(R=\pi^2\sqrt\alpha R_H\),
\(1+\alpha\) e \(3\sqrt2/5\) em resultados independentes, não condições
escolhidas pela concordância numérica.

## 9. Rotas examinadas e descartadas

### 9.1 Polo meromorfo do warp

Um warp dependente apenas do parâmetro de fluxo não pode gerar curvatura
espacial externa: as equações impõem \(A'(z_\tau)=0\) no background homogêneo.
Além disso, uma potência fracionária
\((z_\tau-z_*)^{5/6}\) possui ponto de ramificação, mas resíduo de Laurent
nulo. Essa rota não deriva \(G\).

### 9.2 Localização instantônica direta

O escalar de curvatura de Bismut é linear na curvatura contraída, enquanto
\(\operatorname{Tr}(\mathcal F_B\wedge\mathcal F_B)\) é quadrático. Não existe
identidade universal que transforme um no outro. Portanto, a ação
\(S_{\rm inst}/\hbar=Q/\alpha\) não decorre por mera integração por partes da
ação oficial.

### 9.3 Condensado NJL/BCS

Eliminar o campo auxiliar \(B\) na Lagrangiana completa fornece

\[
\mathcal L_{\rm eff}=-\frac{3\hbar^2}{64}
(\bar\psi\gamma^{(3)}\psi)^2.
\]

O contato de quatro férmions é derivado, mas seu canal atrativo depende das
convenções de assinatura e dualização. Em \(3+1\) dimensões e densidade zero,
um NJL possui acoplamento crítico e não produz automaticamente uma
singularidade BCS \(e^{-c/\alpha}\). Essa rota não demonstrou o expoente.

### 9.4 Autovalor \(1/8\)

Para o Dirac round em \(S^3\), com
\(m=n+3/2\), a expansão correta é

\[
\frac{\deg(n)}{\lambda_n}
=R\left(m-\frac1{4m}\right).
\]

O antigo coeficiente positivo \(1/8\) era erro aritmético e dimensional; sua
coincidência com o \(1/8\) do acoplamento de Bismut foi descartada.

### 9.5 Minimização da temperatura

Para \(Z=\operatorname{Tr}e^{-\beta H}\) e \(\Gamma=-\log Z\),

\[
\partial_\beta\Gamma=\langle H\rangle,
\qquad
\partial_\beta^2\Gamma=-\operatorname{Var}(H)\le0.
\]

O determinante térmico isolado não seleciona um mínimo finito em \(\beta\).
Nesta Q38, \(\beta_E\) é corretamente fixado pela regularidade de horizonte e
pelos dados de contorno, não por minimização canônica.

## 10. Status item a item

| Item | Resultado | Status |
|---|---|---|
| Grupo \(GM_p^2/(\hbar c)\) | Único no conjunto \(\{G,M_p,\hbar,c\}\) | Teorema |
| \(G=c^4R_H/(2E_H)\) | Resposta do horizonte aos dados \(R_H,E_H\) | Condição de contorno |
| \(\beta_E=2\pi R_H\) | Regularidade euclidiana | Teorema condicional à existência do horizonte |
| Cancelamento do \(7/2\) | Zero-mode comum removido pela medida normalizada | Teorema |
| \(f_v=1\) | Periodicidade da fase \(e^{iv}\) | Teorema |
| \(\lambda_{\rm ax}=2/R^2\) | Primeiro modo ímpar do fibrado de sinal | Teorema no operador canônico |
| \(\tau_*=\beta_E^2/16\) | Saddle do primeiro winding térmico relativo 8D | Aproximação controlada |
| \(R=\pi^2\sqrt\alpha R_H\) | Colagem necessária para o expoente | Condição de contorno, não derivada do bulk |
| \(e^{-1/(2\alpha)}\) | Segue da cadeia anterior | Condicional à colagem |
| \(\alpha^4\) | Determinante proposto do canal Hermitiano | Condicional |
| \(1+\alpha\) | Correção efetiva; não é literalmente classe de Chern integral | Fenomenológico |
| \(3\sqrt2/5\) | Contagem de canais, sem matriz de transmissão calculada | Conjectural |
| Correção EM posterior | Remove o resíduo após a comparação | Fit; não utilizar |

## 11. Respostas diretas às sete perguntas originais

1. **Por que Buckingham tem essa forma?** Porque
   \(GM_p^2/(\hbar c)\) é o único grupo do conjunto dimensional escolhido.
2. **Por que \(\alpha^4\)?** Há uma derivação condicional pelo determinante
   complexo bidimensional; o determinante completo ainda não foi calculado.
3. **Por que \(e^{-1/(2\alpha)}\)?** Ele resulta do modo axial térmico se a
   colagem de contorno satisfizer
   \(R=\pi^2\sqrt\alpha R_H\).
4. **Existe meio-instantão explícito?** Não foi construída uma solução de
   instanton de Pontryagin. A descrição correta atual é saddle axial relativo.
5. **Por que Fano?** O valor é motivado por três canais de Hopf, cinco ciclos
   toroidais e dois ramos conjugados, mas não foi derivado de uma matriz de
   transmissão.
6. **A massa do próton é entrada?** Na avaliação numérica atual, sim. Ela pode
   servir como calibração metrológica; sua derivação independente pertence ao
   setor de massas.
7. **A correção eletromagnética foi prevista?** Não. A correção usada para
   eliminar \(-0.26\%\) foi posterior e deve ser removida.

## 12. Conclusão executiva

A Q38 possui duas respostas válidas, que não devem ser confundidas:

### Resposta como problema de contorno

Dados \(R_H\), \(E_H\) e a colagem

\[
R=\pi^2\sqrt\alpha R_H,
\]

a cadeia térmico-axial produz \(e^{-1/(2\alpha)}\), e a fórmula GDQ fornece o
valor numérico de \(G\) com desvio de \(-0.262325\%\).

### Resposta como previsão ab initio

Uma previsão do valor global a partir do bulk local não é um requisito
fisicamente adequado para esta questão. Falta ao setor local informação sobre
a organização cosmológica e os dados de contorno que definem $G$. A relação

\[
R=\pi^2\sqrt\alpha R_H,
\]

permanece uma condição global de colagem. O prefator espectral, atualmente
representado por

\[
\frac{\alpha^4(1+\alpha)}{3\sqrt2/5}.
\]

continua fenomenológico. Essa limitação classifica a força preditiva da
fórmula, mas não reabre a Q38 como problema global.

## 13. Trabalhos locais posteriores

Pode-se investigar, sem usar \(G_{\rm CODATA}\), como a condição global de
colagem

\[
\boxed{
R=\pi^2\sqrt\alpha\,R_H.
}
\]

Para isso deve-se construir o mapa geométrico entre

\[
T^5\times S^3
\longrightarrow
T^4\times\mathbb R^4,
\]

acompanhando a métrica, a medida de Perelman, o ciclo térmico, a fase axial e
os raios \(R\) e \(R_H\). O objetivo é verificar se a continuidade da ação, da
medida ou do fluxo normal na interface impõe

\[
\frac{R}{R_H}=\pi^2\sqrt\alpha.
\]

Depois disso, deve-se calcular um único prefator espectral

\[
\mathcal A_{\rm spec}
\stackrel{?}{=}
\frac{\alpha^4(1+\alpha)}{3\sqrt2/5},
\]

em vez de justificar separadamente \(\alpha^4\), \(1+\alpha\) e
\(\chi_{\rm Fano}\). Esse cálculo permitirá decidir se o resíduo de
\(0.262325\%\) é uma correção geométrica prevista ou apenas a incerteza da
fórmula fenomenológica.

A Q38 fica encerrada como solução global no espaço cosmológico de Einstein.
Esses cálculos posteriores testam a projeção local e a força fenomenológica da
fórmula; não se deve exigir que um infinitésimo da fibra reconstrua o valor
global de \(G\).
