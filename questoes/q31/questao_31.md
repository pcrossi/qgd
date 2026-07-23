# Questão 31 — Como o problema CP forte é resolvido?

## 1. Status

A Questão 31 pode ser formulada de modo consistente na GDQ depois da ponte
efetiva \(SU(3)_C\) construída nas Questões 28 e 30.

O ponto central da auditoria é correto:

\[
\boxed{
\text{escolher um potencial com mínimo em }\theta_{\rm efetivo}=0
\text{ apenas reproduz o mecanismo de áxion.}
}
\]

Para que a GDQ forneça uma resposta própria, é necessário mostrar que:

1. o campo que relaxa \(\theta\) não é uma nova partícula elementar livre;
2. ele é um modo torsional/geométrico já presente na estrutura da GDQ;
3. sua periodicidade é topológica;
4. seu potencial vem da suscetibilidade topológica do setor forte;
5. sua dinâmica de relaxação é imposta pelo fluxo geométrico;
6. o resíduo de EDM é calculável ou rigorosamente nulo sob hipóteses
   explicitadas.

Com a Q30 estruturada, a objeção conceitual principal fica resolvida: o modo que
relaxa \(\theta\) pode ser identificado como grau torsional geométrico acoplado
à densidade topológica do setor \(SU(3)_C\). Portanto:

\[
\boxed{
\text{a Questão 31 está fechada estruturalmente no setor efetivo GDQ--}SU(3)_C.
}
\]

O fechamento não significa cálculo numérico completo de \(\chi_{\rm top}\),
\(f_B\), EDM residual ou cosmologia. Esses itens passam para o bloco de
cálculo funcional, numérico e fenomenológico.

---

## 2. Formulação padrão do problema CP forte

No setor forte efetivo, a ação pode conter o termo topológico:

\[
S_\theta
=
i\theta
\int
\frac{g_s^2}{32\pi^2}
F_{\mu\nu}^a\tilde F^{a\mu\nu}\,d^4x.
\]

Definindo:

\[
Q
=
\int
\frac{g_s^2}{32\pi^2}
F_{\mu\nu}^a\tilde F^{a\mu\nu}\,d^4x
\in\mathbb Z,
\]

o peso euclidiano contém:

\[
e^{i\theta Q}.
\]

Como \(Q\in\mathbb Z\), a teoria é periódica:

\[
\boxed{
\theta\sim\theta+2\pi.
}
\]

O problema CP forte é que observáveis como o momento de dipolo elétrico do
nêutron exigem:

\[
|\theta_{\rm efetivo}|\lesssim 10^{-10}.
\]

Na QCD efetiva:

\[
\theta_{\rm efetivo}
=
\theta_{\rm QCD}
+
\arg\det M_q.
\]

A pergunta é por que esse parâmetro físico é tão pequeno.

---

## 3. O campo geométrico é equivalente a um áxion?

A resposta correta é:

\[
\boxed{
\text{ele é axion-like operacionalmente, mas não precisa ser uma nova partícula
elementar.}
}
\]

Na GDQ, o candidato é o modo pseudoscalar obtido da torção de Cartan/Bismut.
Se \(B\) é uma 3-forma torsional no espaço físico efetivo \(N^4\), então:

\[
*B
\]

é uma 1-forma axial. Um modo pseudoscalar pode ser definido, localmente, por:

\[
\boxed{
a(x)
\sim
f_B\,\vartheta_B(x),
}
\]

onde \(\vartheta_B\) é o ângulo torsional adimensional.

A combinação física que entra no termo CP é:

\[
\boxed{
\theta_{\rm efetivo}(x)
=
\theta_0
+
\frac{a(x)}{f_B}.
}
\]

Assim, do ponto de vista da ação efetiva, o modo torsional se comporta como um
áxion. A diferença ontológica proposta pela GDQ é:

\[
\boxed{
a(x)
\text{ não é postulado como nova partícula fundamental;}
\quad
\text{é um grau longitudinal/torsional da geometria.}
}
\]

Essa distinção só é defensável se \(a\) for realmente derivado da conexão
torsional da GDQ.

---

## 4. Qual é a periodicidade?

A periodicidade deve ser:

\[
\boxed{
\theta_{\rm efetivo}\sim\theta_{\rm efetivo}+2\pi.
}
\]

Logo:

\[
\boxed{
a\sim a+2\pi f_B.
}
\]

Na GDQ, essa periodicidade deve vir da holonomia torsional:

\[
\operatorname{Hol}_C(B)
=
\exp
\left(
i\oint_C \omega_B
\right),
\]

com:

\[
\oint_C\omega_B
\in
2\pi\mathbb Z.
\]

Equivalentemente, a integral topológica do setor forte/torsional deve ser
inteira:

\[
\boxed{
Q_B
=
\int_N
\mathcal P_B
\in
\mathbb Z,
}
\]

onde \(\mathcal P_B\) é a densidade de Pontryagin/Chern associada à conexão
efetiva.

Sem essa quantização, a solução perde a periodicidade correta e vira apenas um
campo escalar ajustável.

---

## 5. Qual é o potencial?

O potencial aceitável não deve ser escolhido arbitrariamente como quadrático.
Ele deve respeitar a periodicidade:

\[
\boxed{
V(\theta_{\rm efetivo})
=
\chi_{\rm top}
\left(
1-\cos\theta_{\rm efetivo}
\right)
+
O(\cos 2\theta_{\rm efetivo}).
}
\]

Para pequenos ângulos:

\[
V(\theta_{\rm efetivo})
=
\frac12
\chi_{\rm top}
\theta_{\rm efetivo}^2
+
O(\theta_{\rm efetivo}^4).
\]

Assim, a forma quadrática usada no texto original só é válida como expansão
local perto do mínimo. A forma global correta é periódica.

Na GDQ, a leitura geométrica é:

\[
\boxed{
V_{\rm GDQ}(\vartheta_B)
=
\chi_{\rm top}^{\rm GDQ}
\left[
1-\cos(\theta_0+\vartheta_B)
\right].
}
\]

O mínimo ocorre em:

\[
\boxed{
\theta_0+\vartheta_B=0\pmod{2\pi}.
}
\]

Esse mínimo não deve ser imposto; ele deve seguir da energia livre topológica
do setor forte.

---

## 6. Como a suscetibilidade topológica da QCD entra?

A suscetibilidade topológica é:

\[
\boxed{
\chi_{\rm top}
=
\left.
\frac{\partial^2 E_{\rm vac}(\theta)}
{\partial\theta^2}
\right|_{\theta=0}.
}
\]

Também:

\[
\boxed{
\chi_{\rm top}
=
\int d^4x\,
\langle q(x)q(0)\rangle,
}
\]

onde:

\[
q(x)
=
\frac{g_s^2}{32\pi^2}
F_{\mu\nu}^a\tilde F^{a\mu\nu}.
\]

Na GDQ, se \(F\) é substituído por uma curvatura efetiva/torsional
\(\mathcal R_B\), então a densidade correspondente é:

\[
\boxed{
q_B(x)
=
\frac{1}{32\pi^2}
\operatorname{Tr}
\left(
\mathcal R_B\wedge\mathcal R_B
\right)^\sim.
}
\]

E:

\[
\boxed{
\chi_{\rm top}^{\rm GDQ}
=
\int d^4x\,
\langle q_B(x)q_B(0)\rangle_{\rm GDQ}.
}
\]

Essa é uma peça obrigatória. Sem \(\chi_{\rm top}\), não há massa do modo, nem
potencial normalizado, nem previsão de relaxação.

---

## 7. Qual é a massa?

Se o campo geométrico \(a\) é canonicanamente normalizado, então:

\[
\boxed{
m_a^2 f_B^2
=
\chi_{\rm top}.
}
\]

Logo:

\[
\boxed{
m_a
=
\frac{\sqrt{\chi_{\rm top}}}{f_B}.
}
\]

Na GDQ:

\[
\boxed{
m_B
=
\frac{\sqrt{\chi_{\rm top}^{\rm GDQ}}}{f_B}.
}
\]

Se o modo torsional é puramente dissipativo e não aparece como partícula
assintótica, então \(m_B\) deve ser reinterpretado como escala de relaxação do
modo CP, não necessariamente como massa de uma partícula detectável.

Essa distinção é importante:

\[
\boxed{
\text{se há polo propagante, há áxion efetivo;}
\quad
\text{se não há polo, há modo torsional relaxacional.}
}
\]

O texto da GDQ deve decidir qual leitura adota.

---

## 8. Qual é a constante de decaimento?

O texto propõe:

\[
f_B
=
M_P
\sqrt{
\frac{3}{\sqrt{6\pi^5}}
}.
\]

Numericamente:

\[
\boxed{
f_B
\approx
6{,}44\times10^{17}\ {\rm GeV}.
}
\]

Esse valor pode ser mantido como hipótese geométrica candidata, mas não deve ser
tratado como número sem origem. O capítulo original fornece uma tentativa
analítica explícita baseada na rigidez torsional e no volume de Kähler do
sóliton bariônico:

\[
\boxed{
V_K=6\pi^5\approx1836{,}118,
}
\]

\[
\boxed{
f_B
=
\sqrt{\frac{3}{\kappa^2\sqrt{V_K}}}
=
M_P\sqrt{\frac{3}{\sqrt{6\pi^5}}}
\approx6{,}44\times10^{17}\ {\rm GeV}.
}
\]

Portanto, a auditoria deve dizer:

\[
\boxed{
\text{\(f_B\) não é puramente ad hoc; há uma derivação geométrica proposta.}
}
\]

A ressalva é que essa derivação ainda precisa ser conectada tecnicamente à
normalização canônica do modo torsional no setor oficial da GDQ. Em particular,
faltam:

1. a normalização canônica do modo \(a\);
2. a origem do volume \(6\pi^5\) no setor oficial \(n=4\);
3. a conexão entre rigidez torsional e \(M_P\);
4. a ausência de inserção de escala externa calibrada;
5. a compatibilidade cosmológica.

Em forma correta:

\[
\boxed{
f_B^2
=
\left[
\text{coeficiente cinético do modo torsional }a
\right].
}
\]

Ou seja, \(f_B\) deve ser extraído do termo cinético efetivo:

\[
\boxed{
S_{\rm kin}[a]
=
\frac12
\int
(\partial a)^2\,d^4x.
}
\]

Se a expansão da ação GDQ gera:

\[
S_{\rm tor}
=
\frac12
\int
f_B^2
(\partial\vartheta_B)^2
d^4x,
\]

então:

\[
a=f_B\vartheta_B.
\]

Essa é a derivação que ainda precisa ser formalizada.

---

## 9. Dinâmica de relaxação

A rota geométrica da GDQ deve ser escrita como fluxo dissipativo:

\[
\boxed{
\frac{d\theta_{\rm efetivo}}{d\tau}
=
-
\kappa_{\rm CP}
\frac{\partial V}{\partial\theta_{\rm efetivo}},
\qquad
\kappa_{\rm CP}>0.
}
\]

Com:

\[
V(\theta_{\rm efetivo})
=
\chi_{\rm top}
(1-\cos\theta_{\rm efetivo}),
\]

temos:

\[
\boxed{
\frac{d\theta_{\rm efetivo}}{d\tau}
=
-
\kappa_{\rm CP}
\chi_{\rm top}
\sin\theta_{\rm efetivo}.
}
\]

Os pontos críticos são:

\[
\theta_{\rm efetivo}=n\pi.
\]

A estabilidade é dada por:

\[
\frac{\partial^2V}{\partial\theta_{\rm efetivo}^2}
=
\chi_{\rm top}\cos\theta_{\rm efetivo}.
\]

Logo:

1. \(\theta_{\rm efetivo}=0\pmod{2\pi}\) é mínimo estável;
2. \(\theta_{\rm efetivo}=\pi\pmod{2\pi}\) é máximo instável.

Então:

\[
\boxed{
\theta_{\rm efetivo}(\tau)
\longrightarrow
0
\pmod{2\pi}.
}
\]

Essa é a versão matematicamente limpa do relaxamento CP.

---

## 10. Qual EDM residual é previsto?

O EDM do nêutron é proporcional a \(\theta_{\rm efetivo}\) para ângulos pequenos:

\[
\boxed{
d_n
\approx
C_n\,\theta_{\rm efetivo}\, e\,{\rm cm}.
}
\]

Na literatura efetiva, \(C_n\) é da ordem de \(10^{-16}\). Para a GDQ, não é
necessário fixar esse número no texto estrutural; basta manter:

\[
\boxed{
d_n\propto\theta_{\rm residual}.
}
\]

Se o fluxo geométrico trava exatamente:

\[
\theta_{\rm residual}=0,
\]

então:

\[
\boxed{
d_n=0.
}
\]

Mas essa é a previsão forte. Ela só é legítima se a teoria provar ausência de:

1. desalinhamento de quarks;
2. efeitos de fronteira;
3. instantons residuais;
4. correções de volume finito;
5. ruído estocástico estacionário.

Caso contrário, a previsão segura é:

\[
\boxed{
|d_n|
\le
C_n|\theta_{\rm residual}|.
}
\]

com:

\[
\boxed{
|\theta_{\rm residual}|
\sim
e^{-\kappa_{\rm CP}\chi_{\rm top}\tau_{\rm conf}}
|\theta_{\rm inicial}|.
}
\]

Assim, a GDQ deve escolher entre duas teses:

1. tese forte: \(d_n=0\) exatamente;
2. tese conservadora: \(d_n\) é exponencialmente suprimido.

A tese conservadora é mais defensável enquanto a dinâmica estocástica completa
não for calculada.

---

## 11. A cosmologia do campo é viável?

Se \(a\) for um áxion propagante com:

\[
f_B\sim10^{17}\ {\rm GeV},
\]

então há risco de superprodução cosmológica por desalinhamento inicial.

A GDQ tenta evitar isso dizendo que o modo é viscoso/dissipativo, não um campo
livre subamortecido. A equação correta deve ter a forma:

\[
\boxed{
\ddot a
+
(3H+\Gamma_{\rm GDQ})\dot a
+
\frac{\partial V}{\partial a}
=0.
}
\]

Para evitar oscilações cosmológicas perigosas, é necessário:

\[
\boxed{
\Gamma_{\rm GDQ}\gg m_a
}
\]

no regime inicial relevante, ou ao menos amortecimento suficiente para impedir
densidade relicta excessiva.

Em termos de \(\theta\):

\[
\ddot\theta
+
(3H+\Gamma_{\rm GDQ})\dot\theta
+
m_a^2\sin\theta
=0.
\]

Se o regime é superamortecido:

\[
3H+\Gamma_{\rm GDQ}>2m_a,
\]

então o campo relaxa sem oscilações relevantes.

Portanto, a viabilidade cosmológica exige provar:

1. valor ou cota inferior de \(\Gamma_{\rm GDQ}\);
2. ausência de superprodução;
3. ausência de isocurvatura incompatível;
4. compatibilidade com nucleossíntese, CMB e estrutura;
5. se o modo tem ou não partícula assintótica observável.

Sem isso, a cosmologia ainda é uma pendência.

---

## 12. Respostas diretas às perguntas obrigatórias

### 1. O campo geométrico é equivalente a um áxion?

Operacionalmente sim:

\[
\theta_{\rm efetivo}
=
\theta_0+\frac{a}{f_B}.
\]

Mas na GDQ ele deve ser um modo torsional geométrico, não uma nova partícula
fundamental postulada.

### 2. Qual é sua periodicidade?

\[
\boxed{
a\sim a+2\pi f_B.
}
\]

Equivalentemente:

\[
\theta_{\rm efetivo}\sim\theta_{\rm efetivo}+2\pi.
\]

### 3. Qual é seu potencial?

Globalmente:

\[
\boxed{
V(a)
=
\chi_{\rm top}
\left[
1-\cos\left(\theta_0+\frac{a}{f_B}\right)
\right].
}
\]

Localmente:

\[
V(a)
\approx
\frac12
\chi_{\rm top}
\left(
\theta_0+\frac{a}{f_B}
\right)^2.
\]

### 4. Qual é sua massa?

\[
\boxed{
m_a^2
=
\frac{\chi_{\rm top}}{f_B^2}.
}
\]

Se não houver polo propagante, essa quantidade deve ser interpretada como
escala de relaxação, não massa de partícula.

### 5. Qual é sua constante de decaimento?

Candidata do texto:

\[
\boxed{
f_B
\approx
6{,}44\times10^{17}\ {\rm GeV}.
}
\]

Mas ainda falta derivá-la por normalização canônica do modo torsional.

### 6. Como a suscetibilidade topológica da QCD entra?

Ela fixa a curvatura do potencial e a massa:

\[
\chi_{\rm top}
=
\left.
\frac{\partial^2E_{\rm vac}}{\partial\theta^2}
\right|_{\theta=0},
\qquad
m_a^2f_B^2=\chi_{\rm top}.
\]

### 7. Qual EDM residual é previsto?

Se o relaxamento for exato:

\[
\boxed{
d_n=0.
}
\]

Se houver resíduo:

\[
\boxed{
d_n\propto\theta_{\rm residual}.
}
\]

A tese conservadora é prever supressão exponencial, não zero absoluto, enquanto
a dinâmica completa não for demonstrada.

### 8. A cosmologia do campo é viável?

Só se o modo for superamortecido ou não propagante:

\[
\Gamma_{\rm GDQ}\gg m_a
\]

ou condição equivalente. Isso ainda precisa ser demonstrado.

---

## 13. O que pode ser aproveitado do texto original

Pode ser aproveitado:

1. a ideia de \(\theta\) como deformação torsional;
2. a identificação de um modo pseudoscalar geométrico;
3. a relaxação por fluxo de Perelman como mecanismo dissipativo;
4. a proposta de \(f_B\) como rigidez torsional;
5. a leitura de que o modo não precisa ser uma partícula elementar nova.

Não deve ser aproveitado como prova final:

1. potencial quadrático global sem periodicidade;
2. afirmação de \(\theta_{\rm efetivo}=0\) por escolha de mínimo;
3. \(d_n=0\) exato sem cálculo de resíduos;
4. \(f_B\) numérico sem normalização canônica;
5. cosmologia resolvida sem equação de amortecimento e densidade relicta.

---

## 14. Fechamento

A Questão 31 fica com o seguinte status:

\[
\boxed{
\text{resolução geométrica tipo áxion/torsão: fechada estruturalmente;}
}
\]

\[
\boxed{
\text{periodicidade, potencial periódico e atrator CP: especificados;}
}
\]

\[
\boxed{
\text{suscetibilidade, massa/escala, EDM e cosmologia: cálculo posterior.}
}
\]

Logo:

\[
\boxed{
\text{Questão 31 está fechada estruturalmente no setor efetivo GDQ--}SU(3)_C.
}
\]

---

## 15. Adendo — Teorema de Lyapunov para o relaxamento de \(\theta\)

Embora a avaliação numérica de \(\chi_{\rm top}\) e a normalização canônica
completa de \(f_B\) ainda sejam trabalho posterior, a parte dinâmica do
relaxamento fica fechada agora.

Defina:

\[
\theta
\equiv
\theta_{\rm efetivo}
=
\theta_0+\frac{a}{f_B}.
\]

O potencial periódico mínimo compatível com a topologia é:

\[
\boxed{
V(\theta)
=
\chi_{\rm top}(1-\cos\theta),
\qquad
\chi_{\rm top}>0.
}
\]

A dinâmica geométrica dissipativa proposta pela GDQ é o fluxo de gradiente:

\[
\boxed{
\frac{d\theta}{d\tau}
=
-
\kappa_{\rm CP}
\frac{\partial V}{\partial\theta},
\qquad
\kappa_{\rm CP}>0.
}
\]

Como:

\[
\frac{\partial V}{\partial\theta}
=
\chi_{\rm top}\sin\theta,
\]

temos:

\[
\boxed{
\frac{d\theta}{d\tau}
=
-
\kappa_{\rm CP}\chi_{\rm top}\sin\theta.
}
\]

Agora calcule a variação do potencial ao longo do fluxo:

\[
\frac{dV}{d\tau}
=
\frac{\partial V}{\partial\theta}
\frac{d\theta}{d\tau}.
\]

Substituindo a equação de evolução:

\[
\frac{dV}{d\tau}
=
-
\kappa_{\rm CP}
\left(
\frac{\partial V}{\partial\theta}
\right)^2.
\]

Logo:

\[
\boxed{
\frac{dV}{d\tau}
=
-
\kappa_{\rm CP}
\chi_{\rm top}^2
\sin^2\theta
\le
0.
}
\]

Portanto, \(V\) é uma função de Lyapunov para o fluxo CP.

Os pontos estacionários satisfazem:

\[
\sin\theta=0
\quad\Longrightarrow\quad
\theta=n\pi.
\]

A segunda variação é:

\[
\frac{d^2V}{d\theta^2}
=
\chi_{\rm top}\cos\theta.
\]

Então:

1. \(\theta=0\pmod{2\pi}\) é mínimo estável;
2. \(\theta=\pi\pmod{2\pi}\) é máximo instável.

Assim, para dados iniciais fora do conjunto instável de medida nula:

\[
\boxed{
\theta(\tau)
\longrightarrow
0
\pmod{2\pi}.
}
\]

Isso demonstra que, uma vez aceitos \(\chi_{\rm top}>0\), periodicidade
topológica e fluxo dissipativo da GDQ, o relaxamento de CP não é uma escolha de
mínimo colocada à mão. Ele é consequência da monotonicidade:

\[
\boxed{
\frac{dV}{d\tau}\le0.
}
\]

---

## 16. Supressão residual do EDM

No regime próximo ao mínimo:

\[
\sin\theta\simeq\theta.
\]

Então:

\[
\frac{d\theta}{d\tau}
\simeq
-
\kappa_{\rm CP}\chi_{\rm top}\theta.
\]

A solução é:

\[
\boxed{
\theta(\tau)
=
\theta(0)
\exp(-\kappa_{\rm CP}\chi_{\rm top}\tau).
}
\]

Se o confinamento fornece um tempo efetivo de relaxamento
\(\tau_{\rm conf}\), então:

\[
\boxed{
|\theta_{\rm residual}|
\le
|\theta_{\rm inicial}|
\exp(-\kappa_{\rm CP}\chi_{\rm top}\tau_{\rm conf}).
}
\]

Como:

\[
d_n\propto\theta_{\rm residual},
\]

segue:

\[
\boxed{
|d_n|
\le
C_n
|\theta_{\rm inicial}|
\exp(-\kappa_{\rm CP}\chi_{\rm top}\tau_{\rm conf}).
}
\]

Portanto, a previsão conservadora da GDQ é:

\[
\boxed{
\text{o EDM é exponencialmente suprimido.}
}
\]

A previsão mais forte:

\[
\boxed{
d_n=0
}
\]

exige a condição adicional:

\[
\boxed{
\tau_{\rm conf}\to\infty
\quad
\text{ou}
\quad
\text{projeção exata no atrator } \theta=0.
}
\]

Assim, a tese segura é supressão exponencial; o zero exato fica como caso
limite.

---

## 17. Fechamento atualizado

Com o adendo de Lyapunov e com a ponte \(SU(3)_C\) da Questão 30, a dinâmica de
relaxamento fica fechada em nível estrutural:

\[
\boxed{
V(\theta)=\chi_{\rm top}(1-\cos\theta),
\quad
\dot\theta=-\kappa_{\rm CP}\partial_\theta V
\quad
\Longrightarrow
\quad
\dot V\le0.
}
\]

O que permanece pendente não é a arquitetura do mecanismo de relaxamento, mas os
dados físicos que entram nele:

1. derivar \(\chi_{\rm top}\);
2. formalizar a derivação de \(f_B\) por volume de Kähler/rigidez torsional como
   normalização canônica do modo;
3. determinar se o modo torsional é propagante ou puramente relaxacional;
4. calcular \(\kappa_{\rm CP}\tau_{\rm conf}\);
5. avaliar a cosmologia.

O adendo técnico de referência é:

\[
\boxed{
\texttt{questoes/q31/associados/cp\_forte\_torcao\_su3.md}
}
\]

Portanto, o status atualizado é:

\[
\boxed{
\text{Q31 fechada estruturalmente no setor efetivo GDQ--}SU(3)_C;
}
\]

\[
\boxed{
\text{normalização, suscetibilidade, EDM numérico e cosmologia: cálculo
posterior.}
}
\]
