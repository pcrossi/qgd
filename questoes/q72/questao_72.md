# Questão 72 — Equação de transporte e escolha retardada de Wheeler

## 1. Enunciado

A Q72 recupera o tratamento legado:

- `pt-br/Apêndice 9 - A Equação de Transporte e a Escolha Retardada de Wheeler.md`.

O objetivo é decidir quais partes permanecem válidas na formulação vigente da
GDQ e quais devem ser reclassificadas como linguagem histórica, modelo reduzido
ou programa futuro.

O problema físico é o seguinte: em um experimento de escolha retardada, o
arranjo final do aparelho é decidido depois que o pacote já atravessou a região
das fendas ou braços interferométricos. A formulação não deve introduzir
colapso instantâneo, sinal para o passado ou uma substituição da ação oficial.

## 2. Status curto

$$
\boxed{
\text{Q72 fechada estruturalmente como problema de contorno/transporte no setor reduzido.}
}
$$

O fechamento é estrutural, não metrológico.

O que está fechado:

1. a escolha retardada é formulada como mudança de contorno do aparelho;
2. o efeito sobre as franjas é descrito pela resposta DtN/Schur do detector;
3. não há sinal físico para o passado;
4. a aparência retrocausal é substituída por solução global de valor de
   contorno compatível com a causalidade operacional;
5. o tratamento correto reaproveita a Q44 e a teoria de medida por interface.

O que não está fechado:

1. simulação completa de $(g,J,H,f,\mathcal U)$ pela ação oficial;
2. parâmetros materiais de um interferômetro real;
3. cálculo metrológico de uma montagem experimental específica.

Essas pendências não reabrem a questão conceitual. Elas pertencem à aplicação
experimental.

## 3. O que o apêndice legado acertou

O apêndice original contém uma ideia correta:

$$
\boxed{
\text{a escolha retardada deve ser tratada como alteração de contorno, não como decisão mística da partícula.}
}
$$

Na linguagem vigente da GDQ, o aparelho entra como dado clássico de fronteira
ou fonte externa:

$$
J_{\rm app}^{\rm clássico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm app}
\to
\text{resposta espectral}
\to
\text{registro}.
$$

Para a dupla fenda ou interferômetro, isso se reduz ao mecanismo já consolidado
na Q44:

$$
\mathsf R_{\rm det}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

A presença ou ausência do recombinador, divisor, detector de caminho ou tela
absorvente altera a impedância de interface. Isso muda o problema de valor de
contorno resolvido pelo setor hidrodinâmico reduzido.

## 4. O que precisa ser corrigido no apêndice legado

O texto original usa várias expressões fortes demais para a formulação atual.
Elas devem ser lidas assim:

| Expressão legada | Classificação correta |
|---|---|
| “propagador avançado envia restrição ao passado” | representação de Green de um problema de dois contornos; não é sinal físico |
| “ação funcional efetiva da malha” | redução Madelung em fundo fixo; não substitui a ação oficial |
| $\mathcal D_{\rm Total}=\square_K+\Delta_K$ | notação problemática; não é operador fundamental da GDQ |
| “condições de Israel na métrica de Kähler” | linguagem histórica; usar DtN/Schur/Robin de interface |
| $\sigma_{\rm det}\rho_{\rm det}$ | parâmetro fenomenológico de aparelho, substituível por $\mathsf R_{\rm det}$ |
| “colapso por solíton shrinking” | metáfora/redução; o correto é relaxação dissipativa do aparelho e seleção de registro |
| $\mathcal V_{\rm Bohm}\to0$ universal | válido apenas no limite incoerente suave do modelo reduzido |

O ponto mais importante é que a GDQ não precisa afirmar que uma influência
energética viaja para o passado. O que existe é uma solução estacionária ou
quase-estacionária que satisfaz simultaneamente os contornos efetivamente
impostos no domínio.

## 5. Formulação vigente do problema

No setor reduzido de laboratório, usamos:

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f).
$$

A dinâmica hidrodinâmica efetiva é:

$$
\partial_t\rho
+
\nabla\cdot\left(\rho\frac{\nabla S_R}{m}\right)
=0,
$$

$$
\partial_tS_R
+
\frac{|\nabla S_R|^2}{2m}
+
V_{\rm app}
-
\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}
=0.
$$

Aqui $V_{\rm app}$ não é termo novo da ação oficial. Ele representa o contorno
clássico da montagem.

Quando o aparelho final é alterado, não se muda a ação fundamental. Muda-se o
domínio variacional efetivo:

$$
(\Omega,\partial\Omega_{\rm old})
\longrightarrow
(\Omega,\partial\Omega_{\rm new}).
$$

Consequentemente, muda o operador de resposta:

$$
\mathsf R_{\rm old}
\longrightarrow
\mathsf R_{\rm new}.
$$

A densidade observada no anteparo pode ser escrita como:

$$
\rho_{\rm obs}
=
\rho_1+\rho_2
+
2\sqrt{\rho_1\rho_2}\,
\mathcal C_{\rm det}\,
\cos\left(\frac{S_1-S_2}{\hbar}\right),
$$

onde o coeficiente de coerência é:

$$
\mathcal C_{\rm det}
=
\exp(-\Gamma_{\rm det}).
$$

No modelo reduzido da Q44:

$$
\Gamma_{\rm det}
=
\frac12
\langle
\Delta\Phi_\partial,
\mathsf R_{\rm det}\Delta\Phi_\partial
\rangle.
$$

Assim:

1. detector desligado ou recombinação coerente:

   $$
   \Gamma_{\rm det}\simeq0,
   \qquad
   \mathcal C_{\rm det}\simeq1;
   $$

2. detector de caminho ou absorção forte:

   $$
   \Gamma_{\rm det}\gg1,
   \qquad
   \mathcal C_{\rm det}\simeq0.
   $$

## 6. Onde entra a escolha retardada

A escolha retardada não altera o passado físico. Ela altera qual problema de
contorno é efetivamente realizado antes do registro final.

O dado experimental é uma função de comutação do aparelho:

$$
\mathsf R_{\rm app}(t)
=
\mathsf R_{\rm off}
+
s(t-t_c)
\left(
\mathsf R_{\rm on}-\mathsf R_{\rm off}
\right),
$$

com $s$ suave, causal e suportada pelo tempo de resposta do aparelho.

O observável final depende do histórico de impedância visto pelo suporte
causal do pacote:

$$
\Gamma_{\rm det}[t_f]
=
\frac12
\int
\left\langle
\Delta\Phi_\partial(t),
\mathsf R_{\rm app}(t)\Delta\Phi_\partial(t)
\right\rangle
w(t_f,t)\,dt.
$$

O kernel $w(t_f,t)$ codifica o transporte causal efetivo entre a região do
aparelho e o registro. Ele não representa sinal superluminal; representa a
resposta do problema de contorno condicionado ao arranjo que efetivamente
existe quando o registro é produzido.

## 7. Por que não há paradoxo causal

O paradoxo surge quando se pergunta “por qual caminho a partícula passou?”
assumindo que a pergunta tem resposta independente do contorno final.

Na GDQ, o objeto físico relevante não é uma partícula pontual isolada com
história clássica pré-definida. O objeto é o conjunto:

$$
(\rho,S_R,\Omega,\partial\Omega,\mathsf R_{\rm app}).
$$

Mudar o aparelho muda a classe de soluções admissíveis. Isso não reescreve um
evento passado; apenas seleciona outro registro final compatível com outro
problema de contorno.

O conteúdo causal é:

1. energia, momento e informação operacional propagam-se causalmente;
2. a solução matemática pode depender de contornos globais;
3. dependência de contorno não é comunicação para o passado;
4. o registro só ocorre quando o aparelho macroscópico absorve e estabiliza uma
   resposta.

## 8. Relação com Q44

A Q72 não substitui a Q44. Ela é sua extensão temporal/operacional.

Q44 respondeu a dupla fenda com detector linear reduzido:

$$
\text{dupla fenda}
\to
\mathsf R_{\rm det}
\to
\Gamma_{\rm det}
\to
\rho_{\rm obs}.
$$

Q72 acrescenta:

$$
\mathsf R_{\rm det}
\longrightarrow
\mathsf R_{\rm det}(t)
$$

e interpreta a escolha retardada como variação temporal do contorno do
aparelho.

## 9. Cadeia de fechamento

A cadeia mínima vigente é:

$$
\mathcal S_{\rm GDQ}
\to
\text{redução Madelung em fundo estacionário}
\to
\text{domínio interferométrico}
\to
\text{contorno final do aparelho}
\to
\mathsf R_{\rm app}(t)
\to
\Gamma_{\rm det}
\to
\rho_{\rm obs}.
$$

Como a Hessiana completa do aparelho real não é calculada aqui, a classificação
correta é:

$$
\boxed{
\text{fechada estruturalmente no setor reduzido; metrologia de aparelho fica como aplicação.}
}
$$

## 10. Aplicação metrológica reduzida

Foi adicionada uma avaliação concreta para um interferômetro de Mach--Zehnder
eletro-óptico:

- `questoes/q72/associados/resposta_interferometro_real_q72.md`;
- `questoes/q72/associados/calcular_resposta_interferometro_q72.py`;
- `questoes/q72/associados/saida_resposta_interferometro_q72.md`.

Com dados externos congelados de uma chave EO-MZI em $1550\,\mathrm{nm}$:

$$
V_\pi=2{,}445\,\mathrm V,
\qquad
\tau_{\rm sw}=18{,}1\,\mathrm{ps},
\qquad
\text{crosstalk}=-30\,\mathrm{dB},
$$

obteve-se:

$$
\mathsf R_{\rm on}=3{,}453877639491,
\qquad
\Gamma_\infty=3{,}453877639491,
\qquad
\mathcal C_\infty=3{,}162277660168\times10^{-2}.
$$

O resultado significa que, para esse aparelho reduzido, a escolha ativa elimina
aproximadamente $96{,}84\%$ da coerência de amplitude, deixando uma coerência
residual compatível com o crosstalk de $-30\,\mathrm{dB}$.

Classificação:

$$
\boxed{
\text{avaliação direta de modelo reduzido com dados externos de aparelho.}
}
$$

## 11. Comparação com o limite experimental do aparelho

A comparação relevante neste estágio não é com uma curva completa de franjas,
mas com o limite físico imposto pelo próprio aparelho.

O dado externo congelado foi o crosstalk de potência:

$$
p_{\rm leak}=10^{-3}
$$

correspondente a $-30\,\mathrm{dB}$.

Se o vazamento é de potência, a coerência residual de amplitude esperada é:

$$
\mathcal C_{\rm exp}^{\rm app}
=
\sqrt{p_{\rm leak}}
=
3{,}162277660168\times10^{-2}.
$$

O cálculo reduzido da GDQ forneceu:

$$
\mathcal C_{\rm GDQ}
=
e^{-\Gamma_\infty}
=
3{,}162277660168\times10^{-2}.
$$

Portanto:

$$
\boxed{
\mathcal C_{\rm GDQ}
=
\mathcal C_{\rm exp}^{\rm app}
}
$$

dentro da precisão numérica do cálculo.

Isso mostra que a cadeia:

$$
\mathsf R_{\rm app}(t)
\to
\Gamma_{\rm det}
\to
\mathcal C_{\rm det}
$$

reproduz exatamente o limite de coerência imposto pelo aparelho quando a
impedância é fixada pelo crosstalk medido.

Classificação honesta:

$$
\boxed{
\text{comparação positiva do modelo reduzido com dado externo de aparelho.}
}
$$

Não é ainda uma previsão de primeiros princípios, porque o crosstalk foi usado
como entrada experimental. Para elevar o resultado, é necessário derivar
$\mathsf R_{\rm app}$ diretamente de $K_{\rm app}$.

## 12. Nova seção — rumo à Hessiana material do aparelho

O próximo passo natural é substituir:

$$
p_{\rm leak}
\quad\text{e}\quad
\tau_{\rm sw}
$$

por grandezas calculadas da própria resposta material do interferômetro.

A cadeia desejada é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm app}^{*}
\to
K_{\rm app}^{\rm phys}
\to
\mathsf R_{\rm app}(\omega)
\to
\mathsf R_{\rm app}(t)
\to
\Gamma_{\rm det}.
$$

Nesta nova seção, o alvo não é recalibrar $\Gamma_{\rm det}$ pelo crosstalk
observado, mas derivar o crosstalk como consequência de:

1. comprimento do acoplador;
2. contraste de índice;
3. resposta eletro-óptica;
4. perdas materiais;
5. impedância de saída;
6. tempo finito de comutação.

No nível reduzido de engenharia, isso equivale a calcular o operador material:

$$
K_{\rm app}
=
-\partial_s^2
+
\lambda_{\rm app}^2
+
V_{\rm EO}(s,t)
+
V_{\rm loss}(s),
$$

com condições de interface nos braços do Mach--Zehnder. O complemento de Schur
então define:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Esse será o ponto de continuação da Q72.

## 13. Hessiana material reduzida do EO-MZI

A continuação foi executada em:

- `questoes/q72/associados/hessiana_material_mzi_q72.md`;
- `questoes/q72/associados/calcular_hessiana_material_mzi_q72.py`;
- `questoes/q72/associados/saida_hessiana_material_mzi_q72.md`.

No modelo reduzido de braços do Mach--Zehnder:

$$
T_{\rm MZI}
=
C(\theta_2)P(\phi,\eta)C(\theta_1),
$$

com:

$$
C(\theta)
=
\begin{pmatrix}
\cos\theta & i\sin\theta \\
i\sin\theta & \cos\theta
\end{pmatrix},
\qquad
P(\phi,\eta)
=
\begin{pmatrix}
e^{i\phi/2} & 0 \\
0 & \eta e^{-i\phi/2}
\end{pmatrix}.
$$

Para:

$$
\theta_1=\theta_2=\frac{\pi}{4},
\qquad
\eta=1,
\qquad
\phi=\pi\frac{V}{V_\pi},
$$

e $V=V_\pi$, o cálculo dá:

$$
p_{\rm dark}^{\rm ideal}
=
3{,}749399456655\times10^{-33},
\qquad
p_{\rm bright}^{\rm ideal}
=
1.
$$

Ou seja, o crosstalk ideal é nulo no limite numérico.

Para produzir $-30\,\mathrm{dB}$ por imperfeições materiais isoladas, os
equivalentes calculados são:

$$
\delta\phi
=
6{,}322448399238\times10^{-2}\,\mathrm{rad},
$$

$$
\delta V
=
4{,}920557195241\times10^{-2}\,\mathrm V,
$$

$$
\eta
=
0{,}938693139937,
$$

ou:

$$
\delta\theta
=
3{,}161224199619\times10^{-2}\,\mathrm{rad}
$$

em um acoplador, correspondente a split de potência:

$$
0{,}531591185416.
$$

Conclusão desta camada:

$$
\boxed{
\text{o crosstalk finito pertence a } \delta K_{\rm app},
\text{ não à ação fundamental.}
}
$$

Assim, a GDQ fixa a forma variacional da resposta de interface. O valor
estacionário de um aparelho real exige a Hessiana material concreta do
dispositivo.

## 14. Fechamento final da Q72

A Q72 está fechada no nível correto.

O tratamento legado do Apêndice 9 foi recuperado sem manter as formulações que
misturavam GDQ com linguagem excessiva de retrocausalidade física. O resultado
vigente é:

$$
\boxed{
\text{escolha retardada = mudança de contorno/aparelho + transporte causal da resposta.}
}
$$

A cadeia fechada é:

$$
\mathcal S_{\rm GDQ}
\to
\text{setor Madelung reduzido}
\to
\text{interferômetro}
\to
\mathsf R_{\rm app}(t)
\to
\Gamma_{\rm det}
\to
\mathcal C_{\rm det}
\to
\rho_{\rm obs}.
$$

Para o aparelho EO-MZI reduzido, a comparação com o limite de crosstalk
$-30\,\mathrm{dB}$ deu:

$$
\mathcal C_{\rm GDQ}
=
e^{-\Gamma_\infty}
=
3{,}162277660168\times10^{-2}
=
\sqrt{10^{-3}}.
$$

A camada material reduzida mostrou ainda que, no Mach--Zehnder ideal:

$$
p_{\rm dark}\simeq3{,}75\times10^{-33},
$$

isto é, a extinção é ideal. O crosstalk real aparece quando:

$$
K_{\rm app}
=
K_{\rm ideal}
+
\delta K_{\rm app}.
$$

Assim:

$$
\boxed{
\text{o crosstalk real pertence ao aparelho, não à ação fundamental.}
}
$$

Isso é exatamente o comportamento esperado para uma teoria de contorno: a ação
fornece a lei geral, enquanto o aparelho fornece o background, a fonte, as
perdas e as imperfeições materiais.

## 15. Limitação que não reabre a questão

O fechamento da Q72 não afirma que já calculamos a microestrutura completa do
dispositivo real. Para isso seria necessário conhecer ou modelar:

1. geometria dos guias;
2. perfil de índice;
3. perdas diferenciais;
4. resposta eletro-óptica espacial;
5. acopladores reais;
6. temperatura e dispersão.

Esses dados determinam $\delta K_{\rm app}$. Portanto, eles pertencem à
metrologia do aparelho, não ao fundamento da escolha retardada.

Classificação final:

$$
\boxed{
\text{Q72 fechada estruturalmente e validada em modelo material reduzido.}
}
$$

Refinamento futuro:

$$
\boxed{
\delta K_{\rm app}
\text{ direto para um dispositivo experimental específico.}
}
$$

## 16. Conclusão textual para reescrita do apêndice

O Apêndice 9 deve ser reaproveitado, mas reescrito.

A ideia central permanece válida: a escolha retardada não exige colapso
instantâneo nem retrocausalidade física. Na GDQ, ela é um problema de
transporte com contorno final variável.

A linguagem correta é:

$$
\boxed{
\text{não há sinal para o passado; há dependência global de contorno no problema variacional efetivo.}
}
$$

Portanto, a Q72 fica respondida como extensão estrutural da Q44 e da teoria de
medida. O tratamento legado não deve ser usado literalmente, mas fornece uma
rota clara para o manuscrito reescrito.
