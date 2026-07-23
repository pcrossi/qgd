# Saída — Q76 toy tipo NV/NESS

Classificação: estimativa parametrizada / diagnóstico físico.

O ponto do cálculo é separar equilíbrio térmico de estabilidade
operacional fora do equilíbrio. Em temperatura ambiente, um gap de GHz
não polariza termicamente o qubit; a estabilidade exige acoplamento fraco
ao banho, preparação ativa e readout controlado.

## Cenários

| cenário | f_gap GHz | T K | beta=hf/kBT | polarização térmica tanh(beta/2) | t_op us | T1 ms | T2 us | leak | eps_T1 | eps_T2 | nonad | readout | erro op total | fidelidade op |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| NV_room_temp_fast_gate | 2.87 | 300 | 4.591276e-04 | 2.295638e-04 | 0.05 | 5 | 500 | 9.000e-06 | 1.000e-05 | 1.000e-04 | 1.000e-04 | 2.000e-02 | 2.022e-02 | 0.979781005 |
| NV_room_temp_improved_readout | 2.87 | 300 | 4.591276e-04 | 2.295638e-04 | 0.05 | 5 | 500 | 9.000e-06 | 1.000e-05 | 1.000e-04 | 1.000e-04 | 1.000e-03 | 1.219e-03 | 0.998781005 |
| NV_cryo_long_coherence | 2.87 | 4 | 3.443457e-02 | 1.721558e-02 | 0.05 | 1e+03 | 1e+04 | 1.000e-06 | 5.000e-08 | 5.000e-06 | 1.000e-05 | 1.000e-03 | 1.016e-03 | 0.998983950 |
| GDQ_hypothetical_topological_suppression | 2.87 | 300 | 4.591276e-04 | 2.295638e-04 | 0.05 | 1e+03 | 1e+05 | 1.000e-08 | 5.000e-08 | 5.000e-07 | 1.000e-06 | 1.000e-04 | 1.016e-04 | 0.999898440 |

## Interpretação

1. Para $f_{\rm gap}=2.87\,{\rm GHz}$ e $T=300\,{\rm K}$,
   $\beta=hf/k_BT\simeq4.59\times10^{-4}$, então a polarização térmica
   de equilíbrio é praticamente nula.
2. Se o qubit funciona nesse regime, ele não funciona porque
   $hf\gg k_BT$; ele funciona porque é preparado, controlado e lido fora
   do equilíbrio térmico simples.
3. A versão GDQ da melhora possível é reduzir $J_{\rm th}^{\rm eff}$ e
   aumentar $T_1,T_2$ por geometria/contorno, além de melhorar
   $\mathsf R_{\rm app}$ no readout.

$$
\boxed{
\text{limitação física: gap de GHz em 300 K não basta; é preciso NESS e acoplamento térmico efetivo fraco.}
}
$$
