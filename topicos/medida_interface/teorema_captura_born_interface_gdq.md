# Teorema condicional de captura e Born na interface GDQ

## 1. Objetivo

Este documento conclui a Rota A do modelo abstrato de aparelho. O objetivo é
determinar condições suficientes para que:

1. o objeto seja correlacionado a dois registros;
2. o sinal macroscópico permita inferir o canal;
3. a probabilidade condicionada seja um martingal;
4. a identificação do canal seja assintoticamente certa;
5. as frequências finais coincidam com o peso geométrico inicial.

O resultado não postula diretamente uma equação estocástica para a
probabilidade. Ela será obtida por filtragem causal do registro produzido pelo
aparelho.

---

## 2. Hipóteses do teorema

### H1 — Setor intrínseco de dois canais

O objeto possui dois setores ortogonais associados ao eixo clássico
\(\boldsymbol n_A\):

\[
P_++P_-=I,
\qquad
P_+P_-=0.
\]

Na GDQ, essa decomposição deve vir do módulo de Hopf e da circulação
semi-inteira, não ser criada pelo detector.

### H2 — Peso geométrico inicial

A medida positiva reconstruída da GDQ fornece pesos iniciais

\[
p_0=\mu_{\rm GDQ}(P_+),
\qquad
1-p_0=\mu_{\rm GDQ}(P_-),
\]

ou, na representação de Hilbert já reconstruída,

\[
p_0=\operatorname{Tr}(\rho_0P_+).
\]

Esta hipótese não deve ser confundida com o teorema de captura: a origem
geométrica de \(p_0\) pertence às Questões 20--24. O teorema abaixo demonstra
que a dinâmica de registro preserva esse peso e o converte em frequência de
resultados.

### H3 — Pré-medição não-demolidora

Durante a aquisição ideal, o canal medido é conservado:

\[
[H_{\rm eff},P_\pm]=0.
\]

Equivalentemente, não há transições \(+\leftrightarrow-\) na escala de tempo
da leitura. Essa é a condição QND/adiabática. Quando ela falha, o peso pode ter
drift físico e o martingal simples deixa de valer.

### H4 — Dois sinais distinguíveis

Depois da eliminação dos modos rápidos do aparelho, o registro normalizado
\(Y_t\) satisfaz, condicionado ao canal \(\kappa=\pm1\):

\[
\boxed{
dY_t=2\sqrt{\Gamma(t)}\,\kappa\,dt+dW_t,
}
\]

onde:

- \(W_t\) é a inovação do aparelho;
- \(\Gamma(t)\ge0\) é a taxa informacional derivada do kernel espectral;
- o ruído foi branqueado pela covariância física do detector.

Para ruído colorido, essa forma só é válida depois de ampliar o estado com as
variáveis de memória ou aplicar o filtro causal inverso apropriado.

### H5 — Informação acumulada ilimitada

Defina

\[
\mathcal I(t)=\int_0^t\Gamma(s)\,ds.
\]

Exige-se:

\[
\boxed{\mathcal I(t)\longrightarrow\infty.}
\]

Essa condição significa que o aparelho permanece ativo por tempo suficiente
e que os dois sinais não se tornam indistinguíveis.

### H6 — Registros macroscópicos estáveis

O modo ponteiro possui duas bacias \(\mathcal B_\pm\) com:

\[
\tau_{\rm escape}\gg\tau_{\rm leitura}\gg\tau_{\rm relax}.
\]

O mapa de leitura associa o sinal positivo/negativo persistente às bacias
\(\mathcal B_\pm\).

---

## 3. Filtragem causal do registro

Seja \(\mathcal F_t^Y\) a filtração gerada pelo registro até o instante \(t\):

\[
\mathcal F_t^Y=\sigma(Y_s:0\le s\le t).
\]

Defina a probabilidade condicionada

\[
\boxed{
p_t=\Pr(\kappa=+1\mid\mathcal F_t^Y).
}
\]

A média condicional do canal é

\[
\bar\kappa_t
=\mathbb E[\kappa\mid\mathcal F_t^Y]
=2p_t-1.
\]

O processo de inovação observado é

\[
\boxed{
d\widetilde W_t
=dY_t-2\sqrt{\Gamma(t)}(2p_t-1)dt.
}
\]

Sob as hipóteses usuais de filtragem, \(\widetilde W_t\) é um Wiener em
relação à filtração observada.

---

## 4. Derivação da equação de (p_t)

Para os dois valores do sinal,

\[
h_+(t)=+2\sqrt{\Gamma(t)},
\qquad
h_-(t)=-2\sqrt{\Gamma(t)}.
\]

A equação de Kushner--Stratonovich para uma variável estática discreta fornece

\[
dp_t
=p_t\left[h_+(t)-\bar h_t\right]d\widetilde W_t,
\]

onde

\[
\bar h_t
=p_th_+(t)+(1-p_t)h_-(t)
=2\sqrt{\Gamma(t)}(2p_t-1).
\]

Logo:

\[
h_+-\bar h_t
=4\sqrt{\Gamma(t)}(1-p_t),
\]

e finalmente

\[
\boxed{
dp_t
=4\sqrt{\Gamma(t)}\,p_t(1-p_t)d\widetilde W_t.
}
\]

Essa é precisamente a equação usada nos testes da Q42, agora obtida do sinal
causal do aparelho.

Não há termo de drift porque o canal é conservado e a atualização apenas
condiciona informação já presente no registro.

---

## 5. Propriedade de martingal

Como \(0\le p_t\le1\) e o incremento possui apenas termo de inovação:

\[
\mathbb E[dp_t\mid\mathcal F_t^Y]=0.
\]

Portanto:

\[
\boxed{\mathbb E[p_t]=p_0.}
\]

Além disso, \(p_t\) é um martingal limitado. Pelo teorema de convergência de
martingais, existe uma variável \(p_\infty\) tal que

\[
p_t\longrightarrow p_\infty
\]

quase certamente e em \(L^1\).

---

## 6. Identificação assintótica do canal

### 6.1 Razão de verossimilhança

Defina

\[
L_t=\log\frac{p_t}{1-p_t}.
\]

Para taxa constante \(\Gamma\), a razão de verossimilhança do registro é

\[
\boxed{
L_t=L_0+4\sqrt\Gamma\,Y_t.
}
\]

Condicionado a \(\kappa=+1\):

\[
L_t
=L_0+8\Gamma t+4\sqrt\Gamma W_t,
\]

e, condicionado a \(\kappa=-1\):

\[
L_t
=L_0-8\Gamma t+4\sqrt\Gamma W_t.
\]

Como \(W_t/t\to0\) quase certamente:

\[
\kappa=+1\Rightarrow L_t\to+\infty,
\]

\[
\kappa=-1\Rightarrow L_t\to-\infty.
\]

Consequentemente:

\[
\boxed{
p_\infty=\mathbf1_{\{\kappa=+1\}}
\quad\text{quase certamente.}
}
\]

Para \(\Gamma(t)\) variável, a mesma conclusão vale se
\(\mathcal I(t)\to\infty\).

### 6.2 Natureza assintótica

Na difusão ideal, se \(0<p_0<1\), os valores exatos \(p=0\) e \(p=1\) não são
atingidos em tempo finito. A “captura” matemática é assintótica.

Um aparelho real registra em tempo finito porque possui resolução finita. Para
\(0<\varepsilon\ll1\), define-se

\[
\tau_\varepsilon
=\inf\{t:p_t\le\varepsilon
\text{ ou }p_t\ge1-\varepsilon\}.
\]

O resultado físico é declarado quando \(t=\tau_\varepsilon\) e o ponteiro
entra na bacia correspondente.

---

## 7. Regra de Born como probabilidade de registro

Da identificação assintótica:

\[
p_\infty\in\{0,1\}.
\]

Pela conservação da esperança do martingal:

\[
\mathbb E[p_\infty]=p_0.
\]

Mas

\[
\mathbb E[p_\infty]
=\Pr(p_\infty=1).
\]

Portanto:

\[
\boxed{
\Pr(\text{registro }+)
=p_0,
\qquad
\Pr(\text{registro }-)
=1-p_0.
}
\]

Se a geometria inicial fornece

\[
p_0=\operatorname{Tr}(\rho_0P_+),
\]

então a frequência de registros satisfaz a regra de Born.

O teorema demonstra a transmissão sem viés do peso inicial para o registro.
Ele não deve ser usado para esconder a obrigação independente de derivar a
medida inicial da GDQ.

---

## 8. Erro de leitura em tempo finito

Para prioris iguais, taxa constante e decisão pelo sinal de \(Y_t\), sob o
canal \(+\):

\[
Y_t\sim\mathcal N(2\sqrt\Gamma t,t).
\]

A probabilidade de erro é

\[
\boxed{
P_{\rm erro}(t)
=\Phi\left(-2\sqrt{\Gamma t}\right),
}

onde \(\Phi\) é a distribuição normal acumulada.

Para taxa variável, substitui-se \(\Gamma t\) pela informação acumulada
\(\mathcal I(t)\):

\[
\boxed{
P_{\rm erro}(t)
=\Phi\left(-2\sqrt{\mathcal I(t)}\right)
}

no protocolo normalizado correspondente.

Assim, um alvo de erro \(\epsilon\) determina o tempo mínimo de leitura por

\[
\mathcal I(t_{\rm leitura})
\ge\frac14[\Phi^{-1}(\epsilon)]^2.
\]

---

## 9. Acoplamento ao ponteiro bistável

O filtro \(p_t\) descreve a informação no registro contínuo. O ponteiro
macroscópico deve converter essa informação numa bacia estável.

Fisicamente, em cada solução correlacionada, o ponteiro responde ao canal
\(\kappa\) e ao ruído microscópico:

\[
dX_t
=-\mathcal M_X
\partial_XU(X_t;\kappa)dt
+\sqrt{2D_X}\,dV_t,
\]

com

\[
U(X;\kappa)
=-\frac A2X^2+\frac B4X^4-g_X\kappa X.
\]

Na descrição condicionada apenas aos dados observados, substitui-se a força
não conhecida por sua esperança condicional. Então aparece a equação de
filtro

\[
dX_t
=-\mathcal M_X
\partial_XU(X_t;p_t)dt
+\sqrt{2D_X}\,dV_t,
\]

com

\[
U(X;p)
=-\frac A2X^2+\frac B4X^4
-g_X(2p-1)X.
\]

Portanto, \(p_t\) não é um campo físico adicional que atua sobre o aparelho.
Ele resume a informação disponível em \(\mathcal F_t^Y\). A dinâmica
microscópica continua sendo determinada pela interface torsional e pelos graus
de liberdade do aparelho.

Condições suficientes de registro:

1. \(A>0\), \(B>0\);
2. \(g_X\) forte o bastante para separar as taxas de captura;
3. \(\tau_{\rm relax}\ll\tau_\varepsilon\);
4. \(\tau_{\rm escape}\gg\tau_{\rm leitura}\);
5. ruídos \(W_t\) e \(V_t\) derivados da mesma matriz de covariância do
   aparelho, sem dupla contagem.

No regime de amplificação forte, a bacia final acompanha o sinal de
\(2p_t-1\).

---

## 10. Condição de não-demolição e suas violações

Se o Hamiltoniano efetivo contém um termo que não comuta com o canal:

\[
[H_{\rm eff},P_+]\ne0,
\]

então \(p_t\) recebe drift dinâmico. Em notação operacional:

\[
dp_t
=-\frac{i}{\hbar}
\operatorname{Tr}([P_+,H_{\rm eff}]\rho_t)dt
+4\sqrt{\Gamma}p_t(1-p_t)d\widetilde W_t
+\cdots.
\]

Nesse regime:

- \(p_t\) não é martingal em geral;
- Landau--Zener pode transferir peso entre canais;
- a estatística final deve ser calculada pela dinâmica completa;
- a fórmula de Born continua aplicável ao estado imediatamente antes da
  leitura, mas esse estado foi alterado pela evolução.

Esse resultado coincide com os testes não adiabáticos da Q42.

---

## 11. Medições sequenciais

Após um registro ideal no eixo \(\boldsymbol n\), o estado geométrico de saída
fica condicionado à bacia observada. Um segundo aparelho com eixo
\(\boldsymbol m\) constrói nova decomposição:

\[
P_{\boldsymbol m}^{\pm}.
\]

O novo peso inicial é determinado pela sobreposição geométrica de Hopf:

\[
p_0^{(2)}
=\operatorname{Tr}
(P_{\boldsymbol n}^{\kappa}P_{\boldsymbol m}^{+})
=\frac{1+\kappa\boldsymbol n\cdot\boldsymbol m}{2}.
\]

O mesmo teorema de filtragem converte esse peso em frequência do segundo
registro. Assim, sequências \(z\to z\) e \(z\to x\to z\) usam a mesma dinâmica
de interface com condições iniciais atualizadas.

---

## 12. Estatuto ontológico de \(\kappa\)

Na derivação clássica de filtragem, \(\kappa\) é uma variável discreta estática
oculta. Na aplicação GDQ, essa notação deve ser interpretada com cuidado.

Ela pode representar:

1. o setor topológico já preparado antes do aparelho; ou
2. o índice de uma das duas soluções correlacionadas da pré-medição.

Não se deve concluir que toda medição revela um valor local preexistente para
todo eixo possível. Essa leitura produziria uma teoria de variáveis ocultas
locais incompatível com Bell.

Para um eixo escolhido pelo aparelho, \(\kappa\) indexa o canal condicionado
na decomposição efetiva. A extensão multipartida exige um filtro conjunto e
será tratada separadamente.

---

## 13. Relação de \(\Gamma\) com o aparelho GDQ

A taxa informacional da hipótese H4 deve vir do espectro do aparelho. Se o
observável de saída é \(O_A\) e sua susceptibilidade aos dois canais é
\(\Delta O_A\), uma forma de baixa frequência é

\[
\Gamma
\sim
\frac{(\Delta O_A)^2}{4S_O(0)},
\]

onde \(S_O(0)\) é a densidade espectral de ruído referida à saída. Os fatores
exatos dependem da normalização de \(Y_t\).

Na redução modal do documento anterior:

\[
\Delta O_A
\propto g_X\operatorname{Re}G_X^{\rm ret}(0),
\]

e

\[
S_O(\omega)
\propto
|G_X^{\rm ret}(\omega)|^2S_\xi(\omega).
\]

Logo, \(\Gamma\) é calculável depois de conhecidos:

- \(g_X\);
- kernel retardado;
- espectro de ruído;
- transdução entre \(X\) e o sinal lido.

---

## 14. Teorema condicional

### Teorema — Captura informacional e Born

Suponha H1--H6. Então:

1. a probabilidade condicionada satisfaz

   \[
   dp_t
   =4\sqrt{\Gamma(t)}p_t(1-p_t)d\widetilde W_t;
   \]

2. \(p_t\) é martingal limitado;
3. se \(\mathcal I(t)\to\infty\), então

   \[
   p_t\to p_\infty\in\{0,1\}
   \quad\text{quase certamente};
   \]

4. as probabilidades dos registros são

   \[
   \Pr(+)=p_0,
   \qquad
   \Pr(-)=1-p_0;
   \]

5. com limiar finito \(\varepsilon\), o erro de leitura decai
   exponencialmente com a informação acumulada.

### Alcance

O teorema fecha a transmissão dinâmica do peso geométrico inicial para um
registro clássico. Ele permanece condicional à derivação de H2--H6 a partir de
um background GDQ concreto.

---

## 15. O que foi fechado e o que falta

### Fechado estruturalmente

1. origem do processo estocástico de \(p_t\) por filtragem;
2. martingal sem postulado adicional;
3. convergência assintótica sob informação ilimitada;
4. Born como probabilidade de registro;
5. erro e tempo de leitura finitos;
6. acoplamento ao ponteiro bistável;
7. condição QND e diagnóstico não adiabático;
8. extensão para medidas sequenciais.

### Ainda falta para fechamento intrínseco

1. derivar \(g_X\), \(G_X^{\rm ret}\) e \(S_O\) da Hessiana de um aparelho;
2. calcular \(\Gamma\) sem normalização escolhida;
3. demonstrar H6 num detector físico;
4. conectar a medida inicial H2 diretamente ao fluxo GDQ no protocolo;
5. formular o caso multipartido e Bell;
6. distinguir experimentalmente a GDQ da teoria operacional padrão.

## 16. Próximo passo

A Rota A está fechada como teorema condicional. O próximo passo é a Rota B:
especificar um aparelho físico mínimo e calcular a taxa informacional.

Para evitar complexidade material prematura, recomenda-se começar por um
detector idealizado com:

1. modo coletivo harmônico ou bistável;
2. banho ôhmico com corte geométrico;
3. transdução linear conhecida;
4. campo de Stern--Gerlach prescrito;
5. parâmetros separados entre dados experimentais e coeficientes GDQ.

## 17. Status

\[
\boxed{
\text{Rota A fechada como teorema condicional de interface;}
\quad
\text{Rota B quantitativa permanece aberta.}
}
\]
