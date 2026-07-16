# Q42 — Simulações de Stern–Gerlach

Esta pasta reúne os testes numéricos da formulação de contorno e medição
condicionada desenvolvida em questão_42.md.

## Ordem de trabalho

1. simulate_measurement_q42.py
   - simula o martingal
     \[
     dp_t=4\sqrt{\Gamma}\,p_t(1-p_t)dW_t;
     \]
   - implementa captura nos limiares \(\varepsilon\) e \(1-\varepsilon\);
   - compara Monte Carlo, primeiro alcance analítico e Born;
   - executa convergência em \(dt\).

2. solve_robin_channels_q42.py
   - construir \(\mathbb H_R^\pm\);
   - obter \(\lambda_\nu^\pm\), autofunções e gap;
   - calcular \(\Gamma_{\rm SG}\) e \(\kappa_H^{\rm SG}\).

3. simulate_beam_q42.py
   - propagar os canais sob
     \(\mathbf F_\pm=\pm\mu\nabla|\mathbf B|\);
   - formar as duas manchas no detector;
   - testar sequências \(z\to x\to z\).

4. simulate_sequences_q42.py
   - verifica repetibilidade \(z\to z\);
   - verifica incompatibilidade \(z\to x\to z\);
   - usa a SDE de captura em cada estágio.

5. simulate_nonadiabatic_q42.py
   - integra uma passagem de Landau–Zener;
   - compara a transição numérica com a fórmula assintótica;
   - exibe o termo de deriva que destrói o martingal quando
     \([H,P_{\boldsymbol n}]\ne0\).

6. test_physical_zeeman_q42.py
   - calcula \(\Delta\) e \(v\) em SI a partir do campo, gradiente,
     velocidade e \(g_{\rm geom}\);
   - mantém os dados do aparelho explícitos, sem embuti-los como constantes.

7. evaluate_gdq_background_q42.py
   - lê o espectro de um background estacionário realmente resolvido;
   - calcula \(\kappa_H^{\rm SG}\) e \(\Gamma_{\rm SG}\);
   - recusa executar se os modos da Hessiana, taxas e pesos estiverem
     ausentes. O formato está descrito em derivacao_coeficientes_fisicos_q42.md.

8. test_background_pipeline_q42.py
   - valida exatamente as contrações espectrais com um fixture sintético;
   - o fixture testa o código, não representa uma solução da GDQ.

9. build_stationary_background_q42.py
   - constrói o shrinker gaussiano exato na fatia normal \(\mathbb C^2\);
   - verifica as duas equações estacionárias e a normalização exterior;
   - mede o fluxo no estômato, evidenciando a necessidade do dado variacional
     de bordo antes de calcular o espectro físico.

10. verify_variational_boundary_q42.py
   - verifica a completação Gibbons--Hawking ponderada;
   - testa \(K-nF=0\) e a seleção \(r_c=\sqrt{6\tau}\);
   - separa a condição geométrica comum da resposta axial do aparelho.

11. solve_gaussian_robin_q42.py
   - usa o peso do background gaussiano variacional, não o antigo poço teste;
   - recebe um autovalor Robin diagnóstico \(\beta_B=\sqrt\tau r_B\);
   - compara os espectros alinhado e antiparalelo com \(V_H=0\).

12. test_zh_gaussian_q42.py
   - calcula uma sequência minimizante da energia axial;
   - demonstra que o shrinker gaussiano puro possui \(Z_H=0\);
   - identifica a necessidade de um potencial/conexão axial localizado.

13. solve_cylindrical_hopf_q42.py
   - usa o shrinker estacionário \(\mathbb R_+\times S^3_{2\sqrt\tau}\);
   - deriva \(V_H\tau=2\) do harmônico \(l=2\) do mapa de Hopf;
   - calcula o coeficiente universal Dirichlet--to--Neumann \(z_H\).

14. compare_stationary_actions_q42.py
   - inclui o termo de bordo ponderado na ação on-shell;
   - compara o exterior gaussiano livre com o cilindro de Hopf;
   - não substitui a análise da Hessiana completa de estabilidade.

15. check_cylinder_radius_stability_q42.py
   - restringe a ação GDQ à família cilíndrica normalizada;
   - calcula a Hessiana do raio em \(a=2\sqrt\tau\);
   - testa o resultado analítico por diferenças finitas.

16. auditoria_fechamento_intrinseco_q42.md
   - localiza o material de Hopf, Hessiana e torção já existente;
   - distingue resultados reaproveitáveis de lacunas ainda reais;
   - impede repetir a mesma busca sob notações diferentes.

17. verify_hopf_atlas_q42.py
   - constrói as duas cartas do fibrado de Hopf;
   - verifica a colagem, a invariância do projetor e a métrica
     Fubini--Study;
   - acompanha a conclusão analítica \(Z_{\rm bulk}=0\) para rotação global.

## Regra metodológica

O primeiro teste usa unidades adimensionais e não prevê uma taxa física.
\(\Gamma\) apenas redefine a unidade de tempo; as probabilidades de captura
não dependem de seu valor. Um valor físico de \(\Gamma_{\rm SG}\) só será
calculado após obter o espectro Robin do background GDQ.
