# Questão 44 — Dupla fenda

## 1. Enunciado

O enunciado exige responder:

1. qual equação GDQ é resolvida;
2. se a métrica é evoluída;
3. qual resultado difere da superposição padrão de gaussianas;
4. qual previsão experimental distingue a GDQ;
5. se o fator de decoerência é derivado.

O capítulo legado associado é:

- `pt-br/37 - Experimento da Dupla Fenda.md`.

O script legado associado é:

- `src/plot_dupla_fenda.py`.

## 2. Status curto

$$
\boxed{
\text{Q44 fechada condicionalmente no setor Madelung com detector linear reduzido.}
}
$$

O que está fechado:

1. a leitura geométrica da dupla fenda no setor de Madelung;
2. a recuperação do padrão usual de interferência no limite plano/paraxial;
3. a interpretação dos nodos como barreiras de pressão de Bohm;
4. a classificação dos scripts legados como visualização de modelo reduzido;
5. a substituição do fator fenomenológico de decoerência por uma impedância
   DtN/Schur para um detector linear reduzido.

O que não está fechado:

1. evolução da métrica pela ação oficial;
2. parâmetros microscópicos de um detector material real;
3. previsão metrológica para um experimento específico.

## 3. Qual equação GDQ é resolvida?

No estado atual, a equação efetivamente resolvida não é a variação completa:

$$
\delta \mathcal S_{\rm GDQ}=0
$$

para todos os campos $(g,J,H,f,\mathcal U)$.

O que o capítulo legado e o script usam é a redução Madelung da GDQ em fundo
fixo. Nessa redução:

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
$$

e a dinâmica efetiva no laboratório assume a forma:

$$
\partial_t\rho+\nabla\cdot\left(\rho\frac{\nabla S_R}{m}\right)=0,
$$

$$
\partial_tS_R+\frac{|\nabla S_R|^2}{2m}
+V_{\rm app}
-\frac{\hbar^2}{2m}\frac{\Delta\sqrt\rho}{\sqrt\rho}=0.
$$

Aqui $V_{\rm app}$ representa o vínculo clássico da barreira e das fendas. Ele
não é um novo termo fundamental da GDQ; é dado externo do aparelho/contorno.

Portanto, a Q44 resolve a dupla fenda no setor:

$$
\boxed{
\text{GDQ reduzida } \longrightarrow \text{Madelung em fundo estacionário com contorno de duas fendas.}
}
$$

## 4. Domínio e condições de contorno

O domínio efetivo é uma região plana pós-reconstrução:

$$
\Omega\subset\mathbb R^2_{x,y}
$$

ou a seção transversal de um domínio tridimensional onde a propagação principal
é ao longo de $y$.

A barreira fica em $y=0$ e contém duas aberturas centradas em:

$$
x=\pm\frac d2.
$$

No modelo reduzido, as condições são:

1. pacote incidente coerente antes da barreira;
2. transmissão apenas nas duas janelas;
3. corrente normal bloqueada na parte opaca da barreira;
4. fase coerente nas duas fontes secundárias quando não há detector de caminho;
5. leitura no anteparo em $y=L$.

Uma escrita mais fiel à GDQ é formular o contorno por fluxo:

$$
\int_{A_1}\rho v^n\,dA
+\int_{A_2}\rho v^n\,dA
=
\mathcal J_{\rm in},
$$

com simetria para fendas idênticas:

$$
\int_{A_1}\rho v^n\,dA
=
\int_{A_2}\rho v^n\,dA
=
\frac12\mathcal J_{\rm in}.
$$

## 5. A métrica é evoluída?

Não no tratamento legado nem no script atual.

A métrica usada é efetivamente:

$$
g_{ij}\simeq\delta_{ij}.
$$

Logo, as figuras atuais não devem ser chamadas de simulação completa de
Perelman--Bismut. Elas são visualizações de uma solução reduzida em fundo fixo.

Para evoluir a métrica seria necessário resolver uma cadeia mais forte:

$$
\mathcal S_{\rm GDQ}
\to
(g_*,J_*,H_*,f_*)
\to
\delta^2\mathcal S_{\rm GDQ}
\to
\text{domínio com fendas}
\to
\text{resposta acoplada}.
$$

Isso não foi feito no script de dupla fenda.

## 6. Densidade reduzida para duas gaussianas

O modelo legado assume duas fontes gaussianas paraxiais:

$$
\psi_{\rm tot}=\psi_1+\psi_2.
$$

Com largura efetiva $\sigma_t$, separação $d$ e comprimento de Rayleigh $y_R$,
obtém-se:

$$
\rho(x,y)
=
\frac{2}{\sqrt{2\pi\sigma_t^2}}
\exp\left[
-\frac{x^2+d^2/4}{2\sigma_t^2}
\right]
\left[
\cosh\left(\frac{xd}{2\sigma_t^2}\right)
+\cos\left(\frac{ydx}{2\sigma_t^2y_R}\right)
\right].
$$

Essa fórmula é correta como interferência de duas gaussianas coerentes. Em GDQ,
ela deve ser lida como solução reduzida para $\rho$ e $S_R$, não como solução
direta da métrica.

## 7. Pressão de Bohm e guiagem

O mecanismo físico GDQ aparece com mais clareza na pressão geométrica:

$$
Q[\rho]
=
-\frac{\hbar^2}{2m}
\frac{\Delta\sqrt\rho}{\sqrt\rho}.
$$

Nos mínimos de interferência, $\rho$ fica pequena. No limite nodal ideal:

$$
\rho\to0
\quad\Longrightarrow\quad
Q[\rho]\to+\infty
$$

em regiões onde a curvatura relativa de $\sqrt\rho$ diverge.

Fisicamente, isso significa:

1. a partícula-nó não precisa "passar por dois caminhos";
2. o fluido de densidade/fase sente ambos os contornos;
3. os nodos formam barreiras de pressão;
4. as franjas brilhantes são canais estáveis de fluxo.

Essa é uma explicação GDQ consistente, mas ainda no regime reduzido de
Madelung.

## 8. Qual resultado difere da superposição padrão de gaussianas?

No script atual, nenhum resultado metrológico difere de forma exclusiva da
superposição padrão de gaussianas.

O termo:

$$
\cosh\left(\frac{xd}{2\sigma_t^2}\right)
+\cos\left(\frac{ydx}{2\sigma_t^2y_R}\right)
$$

mostra mínimos não estritamente nulos fora do eixo para gaussianas finitas. Mas
isso já decorre da diferença local de amplitudes entre dois pacotes gaussianos
centrados em posições distintas. Portanto:

$$
\boxed{
\text{mínimos não nulos de gaussianas finitas não são assinatura exclusiva da GDQ.}
}
$$

A diferença real da GDQ é ontológica e dinâmica:

1. $\rho$ não é apenas regra de leitura; é densidade geométrica;
2. $S_R$ não é apenas fase abstrata; é fase de circulação;
3. $Q[\rho]$ é pressão geométrica do meio;
4. o detector deve entrar como contorno/fonte clássica que altera a impedância
   do problema.

## 9. Qual previsão distinguiria a GDQ?

O modelo gaussiano atual não fornece uma previsão experimental exclusiva.

O próximo nível distintivo é incluir o detector como interface física derivada
da GDQ:

$$
J_{\rm det}^{\rm clássico}
\to
\delta\Phi_{\rm det}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm det}
\to
\rho_{\rm anteparo}.
$$

Nesse caso, a assinatura experimental não seria a interferência em si, mas a
lei de perda de visibilidade em função da impedância geométrica do detector:

$$
\mathcal V_{\rm GDQ}
=
\mathcal V_0
\exp[-\Gamma_{\rm det}],
$$

com:

$$
\Gamma_{\rm det}
\quad\text{derivado de}\quad
\mathsf R_{\rm det}
$$

e não ajustado como parâmetro fenomenológico.

A previsão reduzida que será derivada abaixo é:

$$
\mathcal V
=
\mathcal V_0e^{-\Gamma_{\rm det}},
\qquad
\Gamma_{\rm det}
=
\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
$$

Para comparação metrológica com material real, deve-se medir ou calcular:

1. visibilidade das franjas;
2. distância do detector às fendas;
3. densidade e composição do substrato;
4. espessura efetiva;
5. energia/velocidade da partícula;
6. coerência da fonte.

Sem os parâmetros do material real, a Q44 fica fechada como teoria de
interface reduzida, não como previsão metrológica de um detector específico.

## 10. O fator de decoerência é derivado?

Não no capítulo legado.

O fator escrito como:

$$
\rho_{\rm total}
=
\rho_{\rm fluido}
\exp(-\sigma_{\rm det}\rho_{\rm det}L)
$$

é um ansatz fenomenológico de atenuação. Ele é fisicamente plausível, mas ainda
não é uma derivação da ação oficial.

Para virar derivação GDQ, é necessário obter:

$$
\sigma_{\rm det}\rho_{\rm det}L
=
\Gamma_{\rm det}
$$

a partir do operador de interface do aparelho:

$$
\mathsf R_{\rm det}
=
\operatorname{DtN}_{\rm det}
\quad
\text{ou}
\quad
\mathsf R_{\rm det}
=
\text{bloco de Schur da Hessiana GDQ+aparelho}.
$$

Formalmente, o caminho correto é:

$$
\Gamma_{\rm det}
=
\int_{\Omega_{\rm det}}
J_{\rm det}\,
K_{\rm det}^{-1}\,
J_{\rm det}\,
d\mu,
$$

onde:

1. $J_{\rm det}$ é a fonte clássica efetiva do detector;
2. $K_{\rm det}$ é a Hessiana física do setor do detector;
3. $d\mu$ é a medida induzida pela GDQ no domínio de acoplamento.

Essa cadeia é calculada no modelo linear reduzido nas seções seguintes.

## 11. Detector linear reduzido por DtN/Schur

O detector pode ser tratado, no primeiro fechamento controlado, como um canal
material linear no intervalo:

$$
s\in[0,L].
$$

A Hessiana efetiva mínima do canal é:

$$
K_{\rm det}
=
-\partial_s^2+\lambda_{\rm det}^2.
$$

O funcional quadrático correspondente é:

$$
S_{\rm det}^{(2)}[\varphi]
=
\frac12
\int_0^L
\left[
(\partial_s\varphi)^2+\lambda_{\rm det}^2\varphi^2
\right]ds.
$$

Com condição de interface $\varphi(0)=\varphi_0$ e condição absorvente
macroscópica $\varphi(L)=0$, a solução estacionária é:

$$
\varphi(s)
=
\varphi_0
\frac{\sinh[\lambda_{\rm det}(L-s)]}
{\sinh(\lambda_{\rm det}L)}.
$$

Portanto:

$$
-\partial_s\varphi(0)
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L)\varphi_0.
$$

A impedância do detector é:

$$
\boxed{
\mathsf R_{\rm det}
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
}
$$

Essa mesma expressão é obtida pela eliminação dos graus internos do detector:

$$
\boxed{
\mathsf R_{\rm det}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
}
$$

Esse é o ponto essencial: o detector não é inserido como operador quântico
manual. Ele entra como impedância de contorno, derivada da Hessiana efetiva do
aparelho.

## 12. Fator de decoerência derivado

Se o detector distingue as duas fendas, a diferença de campo no contorno é:

$$
\Delta\Phi_\partial
=
\Phi_\partial^{(1)}-\Phi_\partial^{(2)}
=
\zeta_{\rm det}(w_1-w_2).
$$

Com:

$$
\int_{\partial\Omega}(w_1-w_2)^2d\Sigma=C_{\rm path},
$$

o custo quadrático de distinguir caminhos é:

$$
\Gamma_{\rm det}
=
\frac12
\int_{\partial\Omega}
\Delta\Phi_\partial
\mathsf R_{\rm det}
\Delta\Phi_\partial
d\Sigma.
$$

Logo:

$$
\boxed{
\Gamma_{\rm det}
=
\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
}
$$

Para marcador primitivo normalizado:

$$
C_{\rm path}=1.
$$

A densidade no anteparo torna-se:

$$
\boxed{
\rho_{\rm det}
=
I_1+I_2
+2e^{-\Gamma_{\rm det}}\sqrt{I_1I_2}\cos\Delta\phi.
}
$$

Os limites são corretos:

$$
\Gamma_{\rm det}=0
\Longrightarrow
\rho_{\rm det}=I_1+I_2+2\sqrt{I_1I_2}\cos\Delta\phi,
$$

e:

$$
\Gamma_{\rm det}\to\infty
\Longrightarrow
\rho_{\rm det}=I_1+I_2.
$$

Portanto, o fator de decoerência deixa de ser:

$$
\exp(-\sigma_{\rm det}\rho_{\rm det}L)
$$

postulado fenomenologicamente, e passa a ser:

$$
\boxed{
\exp(-\Gamma_{\rm det})
}
$$

derivado da impedância do detector.

## 13. Validação numérica

O script:

- `questoes/q44/associados/resolver_dupla_fenda_detector_q44.py`

avalia o modelo reduzido com:

$$
\lambda_{\rm det}=1{,}1,
\qquad
L=1,
\qquad
C_{\rm path}=1.
$$

Assim:

$$
\mathsf R_{\rm det}
=
\lambda_{\rm det}\coth(\lambda_{\rm det}L)
=
1{,}37414284103.
$$

Para $N=8000$, a saída auditada foi:

| $\zeta_{\rm det}$ | $\Gamma_{\rm det}$ | $e^{-\Gamma_{\rm det}}$ | visibilidade bruta central |
|---:|---:|---:|---:|
| 0 | 0 | 1 | 0,987400675 |
| 0,5 | 0,171767855 | 0,842174657 | 0,893408543 |
| 1,25 | 1,073549095 | 0,341793305 | 0,547559863 |
| 2,5 | 4,294196378 | 0,013647535 | 0,270891364 |

O observável de coerência é o coeficiente do termo cruzado:

$$
e^{-\Gamma_{\rm det}}.
$$

A visibilidade bruta central não precisa tender exatamente a zero no detector
forte porque ainda contém variação do envelope incoerente $I_1+I_2$.

O estudo de malha mostra estabilidade de $N=1000$ a $N=8000$. A saída completa
está em:

- `questoes/q44/associados/saida_solver_detector_q44.md`.

O enquadramento metodológico reutilizável da Q44 está registrado em:

- `metodologia/aplicacoes/q44_dupla_fenda_detector.md`.

A comparação gráfica entre a predição GDQ reduzida e os limites padrão
coerente/incoerente está em:

- `questoes/q44/associados/comparacao_gdq_padrao_q44.md`;
- `questoes/q44/associados/comparacao_gdq_padrao_q44.png`;
- `questoes/q44/associados/comparar_gdq_padrao_q44.py`.

## 14. Relação com escolha retardada

A GDQ permite formular a escolha retardada como problema de contorno:

$$
\text{fonte}
\quad+\quad
\text{barreira}
\quad+\quad
\text{detector final}
\quad\Longrightarrow\quad
\text{solução estacionária admissível}.
$$

Isso é conceitualmente forte porque evita dizer que a partícula muda
retroativamente sua história. O que muda é o problema de contorno global
resolvido pelo fluxo físico.

Mas, para a Q44, a afirmação deve ser conservadora:

$$
\boxed{
\text{a escolha retardada é estruturalmente compatível com GDQ como problema de contorno,}
}
$$

não:

$$
\boxed{
\text{o script atual prova quantitativamente a escolha retardada.}
}
$$

## 15. Respostas diretas às perguntas obrigatórias

### 15.1 Qual equação GDQ é resolvida?

A redução efetiva Madelung da GDQ em fundo fixo:

$$
\partial_t\rho+\nabla\cdot(\rho\nabla S_R/m)=0,
$$

$$
\partial_tS_R+\frac{|\nabla S_R|^2}{2m}
+V_{\rm app}
-\frac{\hbar^2}{2m}\frac{\Delta\sqrt\rho}{\sqrt\rho}=0.
$$

Não a variação completa da ação oficial.

### 15.2 A métrica é evoluída?

Não. A métrica é fixa/plana no modelo atual.

### 15.3 Qual resultado difere da superposição padrão de gaussianas?

No script atual, nenhum resultado exclusivo. A fórmula usada é justamente a
superposição coerente de duas gaussianas. A leitura GDQ difere na ontologia e
na interpretação de $Q[\rho]$ como pressão geométrica.

### 15.4 Qual previsão experimental distingue a GDQ?

A previsão distintiva, no fechamento reduzido, é a lei de
decoerência/visibilidade derivada da impedância do detector:

$$
\mathcal V_{\rm GDQ}
=
\mathcal V_0 e^{-\Gamma_{\rm det}},
\qquad
\Gamma_{\rm det}
=
\Gamma[\mathsf R_{\rm det}].
$$

Para previsão metrológica em material real, ainda é necessário calcular
$\lambda_{\rm det}$ e $\zeta_{\rm det}$ a partir do detector concreto.

### 15.5 O fator de decoerência é derivado?

Sim, condicionalmente, para o detector linear reduzido:

$$
\Gamma_{\rm det}
=
\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
$$

Não, ainda, para um material real específico sem calcular seus parâmetros
microscópicos.

## 16. Veredito

$$
\boxed{
\text{Q44 está fechada condicionalmente no setor Madelung com detector linear reduzido.}
}
$$

A dupla fenda sem detector segue da redução Madelung já obtida na GDQ. Com
detector, a perda de coerência foi derivada como custo de impedância de
interface. Isso fecha a estrutura matemática mínima da questão.

Limitação que não reabre a estrutura:

$$
\boxed{
\text{material real exige calcular } \lambda_{\rm det},L,\zeta_{\rm det}
\text{ a partir da microgeometria do aparelho.}
}
$$

## 17. Próximo passo mínimo

$$
\text{detector material real}
\to
(\lambda_{\rm det},\zeta_{\rm det},L)
\to
\Gamma_{\rm det}^{\rm real}
\to
\mathcal V_{\rm exp}.
$$

Esse passo é fenomenologia/aplicação de aparelho, não lacuna estrutural da
Q44.
