# Questão 76 — Qubits geométricos, estabilidade e computação quântica via GDQ

## 1. Enunciado

A Q76 pergunta se a GDQ pode formular qubits e computação quântica de modo mais
fundamental que a mecânica quântica operacional, tratando estabilidade,
decoerência, portas, readout e correção de erros como propriedades geométricas
de contorno, Hessiana e topologia.

A formulação deve obedecer à ação oficial da GDQ. Portanto, não se deve
postular um Hamiltoniano de qubit, um Lindblad, um código de correção de erros
ou uma porta lógica como ontologia primária. Essas estruturas podem aparecer
como reduções operacionais.

## 2. Status curto

$$
\boxed{
\text{Q76 iniciada como programa de avaliação: qubit = setor projetivo de uma geometria GDQ.}
}
$$

Status inicial:

- fechado conceitualmente: a MQ projetiva é setor operacional da GDQ;
- plausível estruturalmente: qubits podem ser subespaços bidimensionais
  isolados por projetores espectrais;
- aberto quantitativamente: estabilidade, taxas de erro, portas e readout
  exigem Hessiana física, contornos reais e fontes de aparelho;
- proibido por ora: afirmar fidelidade perfeita, ausência total de correção de
  erros, criogenia dispensável ou circuitos infinitos sem cálculo.

## 3. Cadeia GDQ correta

A cadeia mínima para construir um qubit geométrico é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ast
\to
K_{\rm phys}
\to
P_{\rm qubit}
\to
\mathcal H_2
\to
\text{qubit operacional}.
$$

Aqui:

- $\Phi_\ast=(g_\ast,J_\ast,H_\ast,f_\ast)$ é o background estacionário do
  dispositivo físico;
- $K_{\rm phys}$ é a Hessiana física projetada da ação oficial;
- $P_{\rm qubit}$ é um projetor espectral de Riesz que isola dois modos
  estáveis;
- $\mathcal H_2=P_{\rm qubit}\mathcal H_{\rm phys}$ é o subespaço operacional
  bidimensional;
- o qubit usual é a representação projetiva desse setor.

Portanto:

$$
\boxed{
\text{qubit operacional}
=
\text{projeção bidimensional de uma dinâmica GDQ mais ampla.}
}
$$

## 4. Definição provisória de qubit geométrico

Um qubit geométrico GDQ é um par de modos físicos $\psi_0,\psi_1$ tal que:

$$
K_{\rm phys}\psi_i
=
\lambda_i G_{\rm phys}\psi_i,
\qquad
i=0,1,
$$

com produto físico:

$$
\langle\psi_i,\psi_j\rangle_{\mathcal U}
=
\delta_{ij},
$$

e com isolamento espectral:

$$
\operatorname{dist}
\left(
\{\lambda_0,\lambda_1\},
\operatorname{spec}(K_{\rm phys})\setminus\{\lambda_0,\lambda_1\}
\right)
=
\Delta_{\rm gap}
>
0.
$$

O projetor do qubit é:

$$
P_{\rm qubit}
=
\frac{1}{2\pi i}
\oint_\Gamma
(z-K_{\rm phys})^{-1}\,dz,
$$

onde $\Gamma$ envolve apenas o par espectral $\lambda_0,\lambda_1$.

## 5. Estabilidade: o que a GDQ pode prometer

A estabilidade forte não deve ser declarada como erro zero. A declaração
correta é condicional:

$$
K_{\rm phys}
\ge
\Delta_{\rm gap}P_\perp,
\qquad
\Delta_{\rm gap}>0,
$$

no complemento $P_\perp=1-P_{\rm qubit}$.

Se uma perturbação local $\delta K$ satisfaz:

$$
\|\delta K\|
<
\frac{\Delta_{\rm gap}}{2},
$$

então a teoria de perturbações espectrais garante que o subespaço do qubit
permanece isolado. Assim, a GDQ transforma estabilidade de qubits em problema
de gap da Hessiana e estabilidade do domínio de contorno.

A formulação conservadora é:

$$
\boxed{
\text{a GDQ pode transformar correção de erro em problema de estabilidade geométrica calculável.}
}
$$

E não:

$$
\boxed{
\text{a GDQ elimina automaticamente todos os erros.}
}
$$

## 6. Proteção topológica

Perturbações locais pequenas não mudam invariantes topológicos se não cruzam
um ponto singular do espaço de configurações. Em termos GDQ, a proteção
esperada deve vir de:

1. classes de holonomia;
2. classes de Chern do fibrado efetivo;
3. cohomologia relativa da interface;
4. conservação de fluxo/circulação;
5. gap espectral que impede vazamento para modos não lógicos.

Uma porta, um ruído ou uma leitura só altera o dado lógico protegido se
conseguir mudar a classe topológica ou atravessar o gap. Portanto o slogan
correto é:

$$
\boxed{
\text{ruído local subcrítico deforma o representante, não necessariamente a classe lógica.}
}
$$

## 7. Portas lógicas

Portas lógicas devem ser tratadas como transporte controlado no espaço de
moduli do contorno, não como pulsos abstratos impostos externamente.

Se $\eta$ parametriza o controle clássico do aparelho, a porta ideal é:

$$
U_{\rm gate}
=
\operatorname{Pexp}
\left(
-
\int_{\eta_0}^{\eta_1}
\mathcal A_{\rm Berry}^{\rm GDQ}(\eta)\,d\eta
\right),
$$

onde:

$$
\mathcal A_{ij}^{\rm GDQ}(\eta)
=
\langle
\psi_i(\eta),
\partial_\eta\psi_j(\eta)
\rangle_{\mathcal U}.
$$

O erro de porta não é zero por definição. Ele deve ser calculado como:

$$
1-\mathcal F_{\rm gate}
=
\epsilon_{\rm leak}
+
\epsilon_{\rm therm}
+
\epsilon_{\rm app}
+
\epsilon_{\rm nonad}.
$$

Esses termos representam, respectivamente:

1. vazamento espectral para $P_\perp$;
2. excitações térmicas;
3. imperfeição do aparelho/contorno;
4. erro não adiabático do transporte.

## 8. Readout

O readout segue a mesma cadeia de teoria da medida já usada na GDQ:

$$
J_{\rm app}^{\rm clássico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm app}
\to
\text{bacias }B_0,B_1
\to
\text{registro}.
$$

Born fornece os pesos operacionais no Hilbert reconstruído:

$$
P(i)
=
\operatorname{Tr}(\varrho P_i),
\qquad
i=0,1.
$$

O evento individual depende da bacia dinâmica real do aparelho. Portanto a Q76
herda a distinção já estabelecida no manuscrito:

- Born operacional: fechada estruturalmente;
- resultado individual e taxa de erro: dependem da dinâmica de aparelho.

## 9. Comparação conservadora com computação quântica usual

Na computação quântica usual, a estabilidade é obtida combinando isolamento,
controle de ruído, correção de erros e redundância entre qubits físicos e
lógicos.

Na GDQ, a hipótese nova é que parte dessa estabilidade pode vir da própria
geometria:

$$
\text{estabilidade}
=
\text{gap Hessiano}
+
\text{proteção topológica}
+
\text{resposta dissipativa de contorno}.
$$

Isso poderia reduzir overhead de correção de erros, mas não prova
automaticamente que:

$$
\text{qubit físico}
=
\text{qubit lógico}.
$$

Essa igualdade só poderia ser declarada após calcular:

1. $\Delta_{\rm gap}$;
2. acoplamento térmico;
3. canais de vazamento;
4. fidelidade de portas;
5. erro de leitura;
6. estabilidade sob ruído real do material.

## 10. Plano de fechamento

Para fechar a Q76, os passos mínimos são:

1. escolher um protótipo físico de qubit: spin, fluxo, carga, íon, cavidade ou
   modo topológico abstrato;
2. escrever o background GDQ estacionário $\Phi_\ast$ desse protótipo;
3. construir a Hessiana física $K_{\rm phys}$ com projetor de gauge;
4. demonstrar a existência de dois modos isolados;
5. calcular o gap $\Delta_{\rm gap}$;
6. definir perturbações locais $\delta K_{\rm noise}$;
7. calcular estabilidade do projetor de Riesz;
8. construir uma porta como transporte de contorno;
9. calcular $\mathcal F_{\rm gate}$;
10. modelar readout com $\mathsf R_{\rm app}$;
11. comparar taxa de erro GDQ com taxa de erro de um qubit físico real.

## 11. Status final desta versão

$$
\boxed{
\text{Q76 aberta como programa promissor, com cadeia matemática definida.}
}
$$

O que já está claro:

1. a GDQ contém a MQ projetiva como caso particular operacional;
2. qubits podem ser definidos como setores projetivos bidimensionais;
3. estabilidade vira problema de Hessiana, gap e contorno;
4. readout vira problema de aparelho/fonte/bacia;
5. topologia pode proteger classes lógicas contra ruído local subcrítico.

O que ainda não está fechado:

1. qubit físico real;
2. Hessiana explícita do protótipo;
3. gap numérico;
4. fidelidade de portas;
5. taxa de erro;
6. comparação experimental.

Portanto, a Q76 não deve ser vendida como resolução da computação quântica, mas
como uma rota GDQ para transformar computação quântica em engenharia de
estabilidade geométrica.

## 12. Primeira construção formal

A primeira construção técnica foi registrada em:

- [associados/construcao_qubit_geometrico.md](associados/construcao_qubit_geometrico.md)

Ela fixa a definição operacional:

$$
\boxed{
\text{qubit GDQ}
=
\text{cluster espectral bidimensional isolado de }K_{\rm phys}.
}
$$

E explicita que a proteção é subcrítica:

$$
\|\delta K\|_G
<
\frac{\Delta_{\rm gap}}{2}
\quad
\Longrightarrow
\quad
\text{subespaço lógico permanece isolado.}
$$

Também foi criado um teste reduzido autocontido:

- [associados/testar_qubit_geometrico_gap.py](associados/testar_qubit_geometrico_gap.py)
- [associados/saida_testar_qubit_geometrico_gap.md](associados/saida_testar_qubit_geometrico_gap.md)

Esse teste não deriva a Hessiana de um hardware real. Ele apenas verifica a
álgebra mínima da Q76: projetor de Riesz, gap e estabilidade de subespaço sob
perturbação local.

## 13. Protótipo spin/circulação Hopf

O primeiro protótipo físico escolhido é o qubit de spin/circulação, pois ele
reaproveita Stern--Gerlach:

- [associados/qubit_spin_circulacao_hopf.md](associados/qubit_spin_circulacao_hopf.md)
- [associados/simular_qubit_spin_hopf.py](associados/simular_qubit_spin_hopf.py)
- [associados/saida_simular_qubit_spin_hopf.md](associados/saida_simular_qubit_spin_hopf.md)

A definição de eixo usa:

$$
P_{\mathbf n}^{\pm}
=
\frac12
\left(
I
\pm
\mathbf n\cdot\boldsymbol\sigma
\right).
$$

O estado preparado com vetor de Bloch $\mathbf a$ gera pesos:

$$
p_\pm
=
\frac12
\left(
1\pm\mathbf a\cdot\mathbf n
\right).
$$

Portas de um qubit são tratadas como transporte controlado do contorno:

$$
U(\theta,\mathbf n)
=
\exp
\left(
-\frac{i\theta}{2}\mathbf n\cdot\boldsymbol\sigma
\right),
$$

lido na GDQ como holonomia efetiva do subespaço lógico.

O erro de vazamento reduzido é estimado por:

$$
\epsilon_{\rm leak}
\sim
\frac{\|J\|^2}{\Delta_{\rm gap}^2}.
$$

Conclusão desta etapa:

$$
\boxed{
\text{qubit spin/Hopf fechado como redução operacional; hardware real permanece futuro.}
}
$$

## 14. Toy quase real de estabilidade

Para sair da discussão puramente formal, foi construído um toy parametrizado:

- [associados/toy_quase_real_estabilidade.md](associados/toy_quase_real_estabilidade.md)
- [associados/estimar_toy_quase_real.py](associados/estimar_toy_quase_real.py)
- [associados/saida_estimar_toy_quase_real.md](associados/saida_estimar_toy_quase_real.md)

O estimador separa:

$$
\epsilon_{\rm total}
\simeq
\epsilon_{\rm leak}
+
\epsilon_{\rm th}
+
\epsilon_{\rm nonad}
+
\epsilon_{\rm axis}
+
\epsilon_\phi
+
p_{\rm read}.
$$

Com:

$$
\epsilon_{\rm leak}
\simeq
\left(
\frac{\|J\|}{\Delta_{\rm gap}}
\right)^2,
\qquad
\epsilon_{\rm th}
\simeq
\exp
\left(
-
\frac{hf_{\rm gap}}{k_BT}
\right).
$$

O toy mostra a condição física essencial:

$$
\boxed{
\text{a rota GDQ só melhora qubits se aumentar }\Delta_{\rm gap}
\text{ e reduzir }J/\Delta_{\rm gap}.
}
$$

Para temperatura ambiente, a escala térmica é severa:

$$
\frac{k_BT}{h}
\simeq
6251\,{\rm GHz}
\quad
(T=300\,{\rm K}).
$$

Portanto operação em temperatura ambiente exigiria gap geométrico em escala
THz alta ou supressão topológica efetiva do acoplamento térmico. Isso permanece
uma hipótese de hardware, não resultado fechado.

## 15. Protótipo tipo NV/NESS

Para separar estabilidade térmica de estabilidade operacional, foi adicionado
um protótipo parametrizado tipo centro NV:

- [associados/prototipo_nv_ness_parametrico.md](associados/prototipo_nv_ness_parametrico.md)
- [associados/estimar_nv_ness_parametrico.py](associados/estimar_nv_ness_parametrico.py)
- [associados/saida_estimar_nv_ness_parametrico.md](associados/saida_estimar_nv_ness_parametrico.md)

O ponto físico é:

$$
\frac{hf_{\rm gap}}{k_BT}
\ll
1
\quad
\text{para gaps de GHz em }300\,{\rm K}.
$$

Logo, operação em temperatura ambiente não pode ser justificada por equilíbrio
térmico simples. A condição correta é operacional:

$$
\Gamma_{\rm th}t_{\rm op}
\ll
1.
$$

Na GDQ:

$$
\Gamma_{\rm th}
\sim
\|J_{\rm th}^{\rm eff}\|^2
S_{\rm bath}(\omega_Q).
$$

Portanto, para um qubit tipo NV, a melhoria GDQ deveria vir de:

1. redução de $J_{\rm th}^{\rm eff}$ pela geometria/contorno;
2. aumento de $T_1$ e $T_2$ efetivos;
3. readout mais estável via $\mathsf R_{\rm app}$;
4. preparação ativa/NESS, não equilíbrio térmico passivo.

Conclusão desta etapa:

$$
\boxed{
\text{gap de GHz em temperatura ambiente não basta; a Q76 precisa de NESS e acoplamento térmico efetivo fraco.}
}
$$

## 16. Requisitos para vantagem GDQ

Foi adicionada a inversão do problema:

- [associados/requisitos_para_vantagem_gdq.md](associados/requisitos_para_vantagem_gdq.md)
- [associados/calcular_requisitos_vantagem.py](associados/calcular_requisitos_vantagem.py)
- [associados/saida_calcular_requisitos_vantagem.md](associados/saida_calcular_requisitos_vantagem.md)

A pergunta deixa de ser “a GDQ protege qubits?” e passa a ser:

$$
\boxed{
\text{quais valores de }J/\Delta,\ T_1,\ T_2,\ f_{\rm gap}
\text{ e readout a Hessiana GDQ precisa produzir?}
}
$$

Para fidelidade alvo $\mathcal F_\ast$:

$$
\epsilon_\ast
=
1-\mathcal F_\ast.
$$

O requisito de vazamento é:

$$
\frac{\|J\|}{\Delta_{\rm gap}}
\le
\sqrt{w_{\rm leak}\epsilon_\ast}.
$$

O requisito de coerência é:

$$
T_1
\ge
\frac{t_{\rm gate}}{w_{T_1}\epsilon_\ast},
\qquad
T_2
\ge
\frac{t_{\rm gate}}{w_{T_2}\epsilon_\ast}.
$$

Portanto, a próxima prova física da Q76 não é verbal. Ela é calcular, de
$K_{\rm phys}$ e $\mathsf R_{\rm app}$, se esses requisitos podem ser
atingidos por um protótipo real.

## 17. Protocolo de fechamento experimental

Foi adicionado um protocolo de fechamento para transformar a Q76 em teste
comparável a um dispositivo real:

- [associados/protocolo_fechamento_experimental.md](associados/protocolo_fechamento_experimental.md)
- [associados/avaliar_prototipo_qubit.py](associados/avaliar_prototipo_qubit.py)
- [associados/saida_avaliar_prototipo_qubit.md](associados/saida_avaliar_prototipo_qubit.md)

A cadeia de fechamento é:

$$
\Phi_\ast
\to
K_{\rm phys}
\to
\Delta_{\rm gap},J_{\rm leak}
\to
\mathsf R_{\rm app}
\to
T_1,T_2,p_{\rm read}
\to
\mathcal F_{\rm gate}.
$$

O ponto conceitual é que os parâmetros do qubit não devem ser inseridos como
Hamiltoniano efetivo. Eles devem ser lidos do background estacionário, da
Hessiana física e do contorno do aparelho. Quando valores experimentais forem
usados, eles entram como dados do material/aparelho, não como novos termos da
ação oficial.

Status desta etapa:

$$
\boxed{
\text{Q76 possui agora critério operacional, toy reduzido, requisitos quantitativos e protocolo de fechamento.}
}
$$
