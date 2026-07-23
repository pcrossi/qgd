# Q76 — protótipo parametrizado tipo NV/NESS

## 1. Por que usar um protótipo tipo NV

Um centro NV em diamante é um bom protótipo conceitual para a Q76 porque:

1. usa um grau de liberdade de spin localizado;
2. admite dois níveis operacionais como qubit;
3. pode operar longe do equilíbrio térmico;
4. exige separar gap energético, acoplamento ao banho, bombeamento e readout;
5. evita confundir “proteção topológica” com “Boltzmann vence tudo”.

Na linguagem GDQ, o qubit tipo NV não deve ser visto como dois níveis abstratos
inseridos manualmente. Ele deve ser lido como:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm NV,\ast}
\to
K_{\rm phys}^{\rm NV}
\to
P_Q^{\rm NV}
\to
\mathcal H_2.
$$

## 2. O ponto físico essencial

Em temperatura ambiente:

$$
\frac{k_BT}{h}
\simeq
6251\,{\rm GHz}
\qquad
(T=300\,{\rm K}).
$$

Um gap de poucos GHz satisfaz:

$$
\frac{hf_{\rm gap}}{k_BT}
\ll
1.
$$

Portanto, se o qubit estivesse em equilíbrio térmico simples, a polarização
seria praticamente destruída. A estabilidade prática só pode vir de:

1. acoplamento spin--rede fraco;
2. seleção por regras de transição;
3. bombeamento ótico ou preparação ativa;
4. readout não destrutivo ou quase não destrutivo;
5. desacoplamento dinâmico;
6. proteção geométrica/topológica efetiva, se a GDQ a derivar.

Assim, a condição correta não é apenas:

$$
hf_{\rm gap}
\gg
k_BT.
$$

A condição operacional mais realista é:

$$
\Gamma_{\rm th}t_{\rm op}
\ll
1,
$$

onde $\Gamma_{\rm th}$ é a taxa efetiva de relaxação induzida pelo banho.

## 3. Tradução GDQ

O banho térmico e o aparelho entram como fontes/contornos:

$$
J_{\rm bath},
\qquad
J_{\rm app},
\qquad
\mathsf R_{\rm app}.
$$

O acoplamento efetivo ao complemento é:

$$
J_{\rm th}^{\rm eff}
=
P_\perp
\delta K_{\rm bath}
P_Q.
$$

A taxa térmica reduzida deve ser calculada, no nível efetivo, como:

$$
\Gamma_{\rm th}
\sim
\|J_{\rm th}^{\rm eff}\|^2
S_{\rm bath}(\omega_Q),
$$

com:

$$
\omega_Q
=
2\pi f_{\rm gap}.
$$

Portanto, um qubit pode sobreviver mesmo com $hf_{\rm gap}\ll k_BT$ se:

$$
\|J_{\rm th}^{\rm eff}\|^2S_{\rm bath}(\omega_Q)
\text{ for pequeno.}
$$

Esta é a formulação GDQ correta da possível proteção: não basta o gap; é
preciso que a Hessiana e o contorno suprimam o canal de acoplamento térmico.

## 4. Estimador operacional

Para uma operação de duração $t_{\rm op}$, usamos:

$$
\epsilon_{T_1}
\simeq
1-e^{-t_{\rm op}/T_1},
$$

e:

$$
\epsilon_{T_2}
\simeq
1-e^{-t_{\rm op}/T_2}.
$$

O erro total reduzido fica:

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
\epsilon_{\rm read}.
$$

Este estimador usa tempos efetivos $T_1,T_2$ como dados de aparelho. Em uma
previsão GDQ completa, esses tempos devem ser calculados de:

$$
K_{\rm phys}^{\rm NV},
\qquad
\mathsf R_{\rm bath},
\qquad
\mathsf R_{\rm app}.
$$

## 5. Conclusão desta etapa

O protótipo tipo NV ensina a limitação física correta:

$$
\boxed{
\text{temperatura ambiente exige NESS/acoplamento térmico fraco; gap de GHz sozinho não basta.}
}
$$

Na GDQ, isso se transforma em um problema de Hessiana e contorno:

$$
\boxed{
\text{calcular }J_{\rm th}^{\rm eff},\ S_{\rm bath},\ T_1,\ T_2
\text{ a partir de }K_{\rm phys}\text{ e }\mathsf R_{\rm app}.
}
$$

