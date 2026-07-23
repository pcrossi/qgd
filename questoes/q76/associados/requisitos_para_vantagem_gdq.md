# Q76 — requisitos para vantagem GDQ em qubits

## 1. Objetivo

Depois do toy tipo NV/NESS, o próximo passo é inverter a análise:

$$
\text{fidelidade alvo}
\to
\text{requisitos sobre }J,\Delta_{\rm gap},T_1,T_2,\mathsf R_{\rm app}.
$$

Isso evita linguagem vaga como “proteção topológica”. A pergunta física
correta é:

$$
\boxed{
\text{quão pequenos precisam ser os canais de erro para a GDQ superar um qubit convencional?}
}
$$

## 2. Orçamento de erro

Para uma porta, usamos:

$$
\epsilon_{\rm total}
\simeq
\epsilon_{\rm leak}
+
\epsilon_{T_1}
+
\epsilon_{T_2}
+
\epsilon_{\rm nonad}
+
\epsilon_{\rm axis}
+
\epsilon_{\rm read}.
$$

Se a fidelidade alvo é $\mathcal F_\ast$, então:

$$
\epsilon_\ast
=
1-\mathcal F_\ast.
$$

Distribuindo o orçamento em pesos $w_i$:

$$
\epsilon_i
\le
w_i\epsilon_\ast,
\qquad
\sum_iw_i=1.
$$

## 3. Requisitos invertidos

### 3.1 Vazamento

Como:

$$
\epsilon_{\rm leak}
\simeq
\left(
\frac{\|J\|}{\Delta_{\rm gap}}
\right)^2,
$$

o requisito é:

$$
\boxed{
\frac{\|J\|}{\Delta_{\rm gap}}
\le
\sqrt{w_{\rm leak}\epsilon_\ast}.
}
$$

### 3.2 Relaxação longitudinal

Para:

$$
\epsilon_{T_1}
\simeq
1-e^{-t_{\rm gate}/T_1}
\simeq
\frac{t_{\rm gate}}{T_1},
$$

exigimos:

$$
\boxed{
T_1
\ge
\frac{t_{\rm gate}}{w_{T_1}\epsilon_\ast}.
}
$$

### 3.3 De fase

Analogamente:

$$
\boxed{
T_2
\ge
\frac{t_{\rm gate}}{w_{T_2}\epsilon_\ast}.
}
$$

### 3.4 Não adiabaticidade

Com:

$$
\epsilon_{\rm nonad}
\simeq
\left(
\frac{1}{2\pi f_{\rm gap}t_{\rm gate}}
\right)^2,
$$

temos:

$$
\boxed{
f_{\rm gap}
\ge
\frac{1}
{2\pi t_{\rm gate}\sqrt{w_{\rm nonad}\epsilon_\ast}}.
}
$$

### 3.5 Erro angular

Com:

$$
\epsilon_{\rm axis}
\simeq
\frac{\delta\theta^2}{6},
$$

exigimos:

$$
\boxed{
\delta\theta
\le
\sqrt{6w_{\rm axis}\epsilon_\ast}.
}
$$

### 3.6 Readout

O readout exige simplesmente:

$$
\boxed{
p_{\rm read}
\le
w_{\rm read}\epsilon_\ast.
}
$$

Na GDQ, $p_{\rm read}$ deve sair de $\mathsf R_{\rm app}$ e das bacias reais do
aparelho, não de uma escolha manual.

## 4. Interpretação

Este bloco fornece o critério de engenharia:

$$
\boxed{
\text{vantagem GDQ}
\iff
\text{Hessiana/contorno reduzem }J/\Delta,\text{ aumentam }T_1,T_2
\text{ e melhoram readout.}
}
$$

Sem esses números, a Q76 permanece conceitual. Com esses números, ela se torna
comparável a tecnologias reais.

