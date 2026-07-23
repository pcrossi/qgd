# Questão 43

## Status vigente

Q43 está fechada estrutural e operacionalmente no manuscrito autocontido,
mas permanece aberta metrologicamente para $g_e$ e $g_\mu-2$ completos.

Destino consolidado:

- [Capítulo 16 — Estrutura fina, Zeeman e g-2](../../manuscrito/16_fine_structure_zeeman_gminus2/index.md)

O capítulo preserva a cadeia GDQ:

$$
J_{\rm app}^{\rm clássico}
\to
\delta\Phi_{\rm app}
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\text{resposta magnética}
\to
\text{registro}.
$$

Também preserva a anomalia como contração Hessiana:

$$
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
$$

Resultados centrais:

- $g_0=2$ por Noether/circulação;
- $a^{(1)}=\alpha/(2\pi)$;
- a fonte superior direta uniforme é nula por Hodge,
  $\mu_{2,\ell}^{\rm direto}=0$;
- o canal superior plausível é Hessiano e mediado pela densidade,
  $\Delta H_{12}=\eta_\ell T_{123}$ com $T_{123}\simeq-2\pi$;
- a sela angular reduzida deu $\eta_\ell\simeq0$ e Hessiana negativa, logo não
  é a sela leptônica 8D física.

## Enunciado

- [43-0.md](43-0.md)

## Documento principal

- [questao_43.md](questao_43.md)
- [Fechamento da Q43](fechamento_q43.md)

## Arquivos relacionados

- [Expansão da anomalia pela Hessiana](associados/expansao_hessiana_g2.md)
- [Script do cálculo líder](associados/calcular_g2_lider_q43.py)
- [Saída do cálculo líder](associados/saida_g2_lider_q43.md)
- [Script de resíduos superiores](associados/calcular_residuos_superiores_q43.py)
- [Saída de resíduos superiores](associados/saida_residuos_superiores_q43.md)
- [Avaliador de Hessiana](associados/avaliar_hessiana_q43.py)
- [Saída de fixture do avaliador](associados/saida_fixture_hessiana_q43.md)
- [Modelo reduzido Q39→Q43](associados/modelo_reduzido_q39_q43.py)
- [Saída do modelo reduzido Q39→Q43](associados/saida_modelo_reduzido_q39_q43.md)
- [Construção operacional de H_C, c e m_perp](associados/hessiana_operacional_q43.md)
- [Construtor de blocos de Hessiana](associados/construir_blocos_hessiana_q43.py)
- [Saída dos blocos de Hessiana](associados/saida_blocos_hessiana_q43.md)
- [Canal superior formal e obstrução metrológica](associados/canal_superior_formal_q43.md)
- [Sete passos da Hessiana oficial reduzida](associados/sete_passos_hessiana_oficial_q43.md)
- [Script da Hessiana oficial Galerkin](associados/hessiana_oficial_galerkin_q43.py)
- [Saída da Hessiana oficial Galerkin](associados/saida_hessiana_oficial_galerkin_q43.md)
- [NPZ Galerkin sem fonte magnética](associados/hessiana_oficial_galerkin_nua_q43.npz)
- [Extração Galerkin sem fonte magnética](associados/saida_extracao_hessiana_oficial_galerkin_nua_q43.md)
- [NPZ Galerkin com fonte líder](associados/hessiana_oficial_galerkin_lider_q43.npz)
- [Extração Galerkin com fonte líder](associados/saida_extracao_hessiana_oficial_galerkin_lider_q43.md)
- [Construtor de background leptônico e fonte magnética](associados/construir_background_fonte_q43.py)
- [Saída do background leptônico e fonte magnética](associados/saida_background_fonte_q43.md)
- [Derivação do canal superior físico](associados/derivar_canal_superior_fisico_q43.py)
- [Saída do canal superior físico](associados/saida_canal_superior_fisico_q43.md)
- [Derivação reduzida de H1 por mistura harmônica](associados/derivar_h1_mistura_q43.py)
- [Saída de H1 por mistura harmônica](associados/saida_h1_mistura_q43.md)
- [Variações superiores da ação GDQ reduzida](associados/calcular_variacoes_superiores_gdq_q43.py)
- [Saída das variações superiores da ação GDQ reduzida](associados/saida_variacoes_superiores_gdq_q43.md)
- [Contração do canal mediado pela densidade](associados/contrair_canal_densidade_q43.py)
- [Saída da contração do canal mediado pela densidade](associados/saida_contracao_canal_densidade_q43.md)
- [Cálculo de eta pela sela normalizada](associados/calcular_eta_pela_sela_q43.py)
- [Saída de eta pela sela normalizada](associados/saida_eta_pela_sela_q43.md)
- [Background efetivo estável do elétron](associados/background_leptonico_estavel_e_q43.npz)
- [Extração do background efetivo do elétron](associados/saida_extracao_background_estavel_e_q43.md)
- [Background efetivo estável do múon](associados/background_leptonico_estavel_mu_q43.npz)
- [Extração do background efetivo do múon](associados/saida_extracao_background_estavel_mu_q43.md)
- [Background efetivo estável do tau](associados/background_leptonico_estavel_tau_q43.npz)
- [Extração do background efetivo do tau](associados/saida_extracao_background_estavel_tau_q43.md)
- [Background com seleção física do elétron](associados/background_leptonico_selecao_e_q43.npz)
- [Extração da seleção física do elétron](associados/saida_extracao_selecao_e_q43.md)
- [Background com seleção física do múon](associados/background_leptonico_selecao_mu_q43.npz)
- [Extração da seleção física do múon](associados/saida_extracao_selecao_mu_q43.md)
- [Background com seleção física do tau](associados/background_leptonico_selecao_tau_q43.npz)
- [Extração da seleção física do tau](associados/saida_extracao_selecao_tau_q43.md)
- [Background H1-mistura do elétron](associados/background_leptonico_h1mix_e_q43.npz)
- [Extração H1-mistura do elétron](associados/saida_extracao_h1mix_e_q43.md)
- [Background H1-mistura do múon](associados/background_leptonico_h1mix_mu_q43.npz)
- [Extração H1-mistura do múon](associados/saida_extracao_h1mix_mu_q43.md)
- [Background H1-mistura do tau](associados/background_leptonico_h1mix_tau_q43.npz)
- [Extração H1-mistura do tau](associados/saida_extracao_h1mix_tau_q43.md)
- [Extrator de canais superiores](associados/extrair_canal_superior_q43.py)
- [Extração no bloco líder](associados/saida_extracao_canais_lider_q43.md)
- [Extração no bloco required do elétron](associados/saida_extracao_canais_required_e_q43.md)
- [Extração no bloco required do múon](associados/saida_extracao_canais_required_mu_q43.md)
- [Auditoria de não-unicidade do canal superior](associados/auditar_nao_unicidade_canal_superior_q43.py)
- [Saída da auditoria de não-unicidade](associados/saida_nao_unicidade_canal_superior_q43.md)
- [Bloco líder H_C](associados/hessiana_lider_q43.npz)
- [Avaliação do bloco líder](associados/saida_avaliacao_hessiana_lider_q43.md)
- [Bloco required do elétron](associados/hessiana_required_e_q43.npz)
- [Avaliação required do elétron](associados/saida_avaliacao_hessiana_required_e_q43.md)
- [Bloco required do múon](associados/hessiana_required_mu_q43.npz)
- [Avaliação required do múon](associados/saida_avaliacao_hessiana_required_mu_q43.md)
- [Referências experimentais externas](associados/referencias_experimentais_g2.md)
- [Background físico experimental](associados/background_fisico_experimental_g2.md)
- [Teorema de Noether--Zeeman](../../topicos/medida_interface/teorema_noether_zeeman_gdq.md)
- [Projeção da Hessiana oficial no ciclo de Noether](../../topicos/geometria_torcao_hopf/projecao_hessiana_noether_g2.md)
- [Questão 42 — Stern--Gerlach](../q42/questao_42.md)
- [Nota futura sobre \(g-2\) e mésons](../../brain/future/muon-g2-meson-anomalies/index.md)
