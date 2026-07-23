# Associados da Q76

Arquivos:

- `construcao_qubit_geometrico.md`: construção formal inicial do qubit como
  cluster espectral bidimensional da Hessiana física.
- `testar_qubit_geometrico_gap.py`: teste reduzido autocontido de projetor,
  gap e estabilidade sob perturbações locais.
- `saida_testar_qubit_geometrico_gap.md`: saída gerada pelo script.
- `qubit_spin_circulacao_hopf.md`: protótipo de qubit por spin/circulação.
- `simular_qubit_spin_hopf.py`: teste reduzido de projetores, porta e
  vazamento do protótipo spin/Hopf.
- `saida_simular_qubit_spin_hopf.md`: saída gerada pelo script spin/Hopf.
- `toy_quase_real_estabilidade.md`: fórmulas do toy quase real parametrizado.
- `estimar_toy_quase_real.py`: estima vazamento, erro térmico, erro
  não adiabático, erro de eixo, decoerência de porta e readout.
- `saida_estimar_toy_quase_real.md`: saída gerada pelo toy quase real.
- `prototipo_nv_ness_parametrico.md`: protótipo tipo NV/NESS e limitação
  física de operação fora do equilíbrio.
- `estimar_nv_ness_parametrico.py`: toy parametrizado com gap de GHz,
  temperatura, $T_1$, $T_2$, vazamento e readout.
- `saida_estimar_nv_ness_parametrico.md`: saída gerada pelo toy NV/NESS.
- `requisitos_para_vantagem_gdq.md`: inversão do problema, de fidelidade alvo
  para requisitos sobre Hessiana/contorno.
- `calcular_requisitos_vantagem.py`: calcula requisitos quantitativos de
  $J/\Delta$, $T_1$, $T_2$, $f_{\rm gap}$, erro angular e readout.
- `saida_calcular_requisitos_vantagem.md`: saída gerada pelo cálculo de
  requisitos.
- `protocolo_fechamento_experimental.md`: protocolo para comparar um protótipo
  real sem trocar a GDQ por Hamiltoniano postulado de qubit.
- `avaliar_prototipo_qubit.py`: avaliador autocontido de cenários fixos.
- `saida_avaliar_prototipo_qubit.md`: saída gerada pelo avaliador.

Comando:

```bash
python3 questoes/q76/associados/testar_qubit_geometrico_gap.py
python3 questoes/q76/associados/simular_qubit_spin_hopf.py
python3 questoes/q76/associados/estimar_toy_quase_real.py
python3 questoes/q76/associados/estimar_nv_ness_parametrico.py
python3 questoes/q76/associados/calcular_requisitos_vantagem.py
python3 questoes/q76/associados/avaliar_prototipo_qubit.py
```
