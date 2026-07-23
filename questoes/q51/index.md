# Questão 51 — Decaimento alfa

Documento principal:

- `questao_51.md`

Arquivos associados:

- `associados/benchmark_alpha_q51.py` — script-base para comparar Gamow, frequência interna e correção geométrica reduzida.
- `associados/saida_benchmark_alpha_q51.md` — saída auditada do script.
- `associados/metrica_exponencial_alpha_gdq.md` — auditoria da métrica exponencial usada no capítulo legado.
- `associados/frequencia_barreira_alpha_gdq.md` — derivação reduzida da frequência interna e da barreira efetiva.
- `associados/comparacao_experimental_q51.md` — comparação experimental reduzida e diagnóstico de \(\Delta W_{\rm req}\).
- `associados/preformacao_overlap_alpha_gdq.md` — interpretação do resíduo como overlap/pré-formação de superfície.
- `associados/modelo_overlap_superficie_reduzido_q51.md` — modelo reduzido do overlap como forma quadrática de superfície.
- `associados/diagnostico_overlap_superficie_q51.py` — script de diagnóstico inverso de \(E_\partial^{\rm req}\).
- `associados/saida_diagnostico_overlap_superficie_q51.md` — saída auditada do diagnóstico de overlap.
- `associados/teste_modelos_escalares_superficie_q51.py` — teste diagnóstico de fórmulas escalares para \(E_\partial\).
- `associados/saida_teste_modelos_escalares_superficie_q51.md` — saída do teste de modelos escalares.
- `associados/no_go_modelos_escalares_superficie_q51.md` — conclusão: não fechar Q51 com fórmula escalar ajustada.
- `associados/aproximacao_espectral_Rpartial_q51.md` — teste da base espectral de superfície herdada da Q40.
- `associados/aproximacao_espectral_Rpartial_q51.py` — script da aproximação espectral.
- `associados/saida_aproximacao_espectral_Rpartial_q51.md` — saída da aproximação espectral.
- `associados/projetor_canal_alpha_gdq.md` — definição variacional do projetor físico alfa por Riesz.
- `associados/diagnostico_pesos_projetor_q51.py` — diagnóstico dos pesos requeridos do projetor.
- `associados/saida_diagnostico_pesos_projetor_q51.md` — saída dos pesos \(p_{\rm req}\).
- `associados/construcao_Kpartial_phys_q51.md` — plano construtivo de \(K_\partial^{\rm phys}\).
- `associados/diagnostico_espectral_projetor_q51.py` — conversão de pesos em ângulos/gaps espectrais.
- `associados/saida_diagnostico_espectral_projetor_q51.md` — saída do diagnóstico espectral.
- `associados/teste_shell_proxy_q51.py` — teste de proxy de camada por números mágicos.
- `associados/saida_teste_shell_proxy_q51.md` — saída do teste de proxy de camada.
- `associados/no_go_shell_proxy_q51.md` — conclusão: \(P_\perp\) não reduz a distância a números mágicos.
- `associados/prototipo_matriz_Kpartial_q51.md` — fixture matricial demonstrando pesos como normas de projetores.
- `associados/prototipo_matriz_Kpartial_q51.py` — script do protótipo matricial.
- `associados/saida_prototipo_matriz_Kpartial_q51.md` — saída do protótipo matricial.
- `associados/derivacao_Kpartial_da_acao_q51.md` — cadeia variacional formal da ação oficial até \(\Gamma_{\rm GDQ}\).
- `associados/riesz_projector_utils_q51.py` — infraestrutura numérica para Schur e projetores espectrais.
- `associados/saida_riesz_projector_utils_q51.md` — validação algébrica do utilitário.

Status vigente após benchmark inicial:

$$
\boxed{
\text{Q51 parcialmente resolvida; }\nu_{\rm int}\text{ melhora pouco, ansatz exponencial legado não.}
}
$$

O próximo fechamento deve vir da frequência normal interna, da impedância
radial/superficial e do overlap de pré-formação \(S_\alpha^{\rm GDQ}\)
derivados da Hessiana GDQ. O teste espectral inicial mostra que a impedância
média está na escala correta, mas falta o projetor físico de canal
\(P_\perp\). Os pesos requeridos estão todos em \(0\le p_{\rm req}\le1\),
compatíveis com norma quadrática de projeção.

A cadeia formal da ação oficial até a taxa alfa já está documentada. Falta
avaliação dos blocos reais da Hessiana de superfície nuclear.
