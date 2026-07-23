# Questão 55 — Buracos negros

## Status

$$
\boxed{
\text{fechada estruturalmente no mecanismo de regularização;}
\quad
\text{condicional para solução global, estabilidade e informação.}
}
$$

O capítulo legado mostrou corretamente a intuição física principal: a pressão
geométrica associada à densidade e ao potencial de Bohm cresce mais rápido
que o termo atrativo newtoniano quando a matéria colapsa. Porém, um balanço
newtoniano não resolve por si só singularidades da Relatividade Geral. A
resposta correta da GDQ deve ser covariante.

Esta Q55 reorganiza o problema usando a cadeia vigente:

$$
\mathcal S_{\rm GDQ}
\to
\text{equação métrica ponderada}
\to
T_{\mu\nu}^{\rm GDQ}
\to
\text{métrica efetiva regular}
\to
\text{horizontes e invariantes}
\to
\text{evaporação/informação condicional}.
$$

## 1. Perguntas obrigatórias

A questão exige responder:

1. solução covariante;
2. horizonte;
3. invariantes de curvatura;
4. extensão geodésica;
5. condições de energia;
6. estabilidade;
7. evaporação;
8. informação.

## 2. Correção do texto legado

O texto legado usa a energia efetiva

$$
E_{\rm total}(r_c)
=
-\frac{GM^2}{r_c}
+\frac{3\hbar^2M}{2m^2r_c^2}.
$$

Da condição

$$
\frac{dE_{\rm total}}{dr_c}=0
$$

obtém-se

$$
r_c
=
\frac{3\hbar^2}{GMm^2}.
$$

Esse cálculo é útil, mas tem status limitado:

$$
\boxed{
\text{é uma estimativa efetiva de escala de core, não uma solução covariante.}
}
$$

Ele mostra a tendência anti-singular, mas não fornece métrica, horizonte,
invariantes, extensão geodésica, condições de energia ou evaporação.

## 3. Fonte covariante da regularização na GDQ

Na Q54, a equação métrica macroscópica da GDQ foi escrita como

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}^{\rm GDQ}.
$$

Aqui

$$
T_{\mu\nu}^{\rm GDQ}
=
\left\langle
T_{\mu\nu}^{(\theta)}
+T_{\mu\nu}^{(\rho)}
+T_{\mu\nu}^{(H)}
+T_{\mu\nu}^{\partial}
\right\rangle_L.
$$

No colapso gravitacional, o termo essencial é o setor de densidade:

$$
f_R=-\ln\rho,
$$

com a identidade exata

$$
\nabla_\mu\nabla_\nu f_R
=
\nabla_\mu f_R\nabla_\nu f_R
-\frac1\rho\nabla_\mu\nabla_\nu\rho.
$$

Quando a densidade tenta concentrar em escala muito pequena, o termo

$$
-\frac1\rho\nabla_\mu\nabla_\nu\rho
$$

gera uma tensão geométrica crescente. Na redução Madelung, isso é o mesmo
conteúdo físico do potencial de Bohm:

$$
Q
=
-\frac{\hbar^2}{2m}
\frac{\Box\sqrt\rho}{\sqrt\rho}.
$$

Portanto, a regularização não é uma força externa adicionada. Ela vem da
própria dependência da ação oficial em $f$, $\rho$ e $\mathcal U$.

## 4. Solução covariante mínima

No setor esfericamente simétrico estático, a forma efetiva correta é

$$
ds^2
=
-e^{2\Phi(r)}A(r)c^2dt^2
+A(r)^{-1}dr^2
+r^2d\Omega^2,
$$

com

$$
A(r)
=
1-\frac{2Gm(r)}{c^2r}.
$$

A massa interna é determinada por

$$
m'(r)
=
\frac{4\pi r^2}{c^2}\epsilon_{\rm GDQ}(r).
$$

Para uma solução regular, a energia efetiva no centro deve satisfazer

$$
\epsilon_{\rm GDQ}(r)
=
\epsilon_0+O(r^2).
$$

Então

$$
m(r)
=
\frac{4\pi\epsilon_0}{3c^2}r^3+O(r^5),
$$

e

$$
A(r)
=
1-\frac{\Lambda_{\rm core}}{3}r^2+O(r^4),
$$

onde

$$
\Lambda_{\rm core}
=
\frac{8\pi G}{c^4}\epsilon_0.
$$

Logo, o centro não é Schwarzschild singular; ele é um core regular do tipo
de Sitter efetivo.

## 5. Horizonte

Horizontes são raízes de

$$
A(r_H)=0.
$$

Ou seja,

$$
r_H
=
\frac{2Gm(r_H)}{c^2}.
$$

Se a fonte GDQ se compacta em raio pequeno e

$$
m(r)\to M
$$

para $r$ grande, o horizonte externo aproxima o Schwarzschild clássico:

$$
r_+
\simeq
\frac{2GM}{c^2}.
$$

Mas a estrutura interna pode conter um horizonte interno $r_-$ e um estado
extremal quando

$$
A(r_*)=0,
\qquad
A'(r_*)=0.
$$

Esse ponto extremal é o candidato natural a remanescente regular de evaporação
na GDQ.

## 6. Invariantes de curvatura

No core regular:

$$
R(0)=4\Lambda_{\rm core},
$$

$$
R_{\mu\nu}R^{\mu\nu}(0)
=
4\Lambda_{\rm core}^2,
$$

$$
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}(0)
=
\frac83\Lambda_{\rm core}^2.
$$

Assim, se $\epsilon_0$ for finito, todos os invariantes escalares de curvatura
líderes são finitos. A singularidade de curvatura é evitada.

O que falta para uma prova completa é derivar $\epsilon_0$ e o perfil inteiro
$\epsilon_{\rm GDQ}(r)$ diretamente da sela de colapso da ação oficial, em vez
de escolher uma função de massa efetiva.

## 7. Extensão geodésica

Uma geodésica radial causal obedece, no caso $\Phi=0$ efetivo,

$$
\dot r^2
+A(r)\left(\varepsilon+\frac{L^2}{r^2}\right)
=
E^2,
$$

onde:

- $\varepsilon=1$ para geodésicas temporais;
- $\varepsilon=0$ para geodésicas nulas;
- $E$ é energia conservada;
- $L$ é momento angular.

No centro regular,

$$
A(r)=1-\frac{\Lambda_{\rm core}}{3}r^2+O(r^4).
$$

Logo o potencial efetivo é finito para $L=0$ e possui barreira angular usual
para $L\neq0$. Não há termo do tipo $1/r$ ou $1/r^6$ divergente no core.

Conclusão:

$$
\boxed{
\text{a extensão geodésica é plausível e estruturalmente indicada,
mas exige a solução global para ser demonstrada.}
}
$$

## 8. Condições de energia

Para fonte anisotrópica esférica,

$$
T^\mu{}_\nu
=
\operatorname{diag}
(-\epsilon,p_r,p_t,p_t).
$$

As condições usuais são:

$$
\text{WEC:}\quad
\epsilon\ge0,\quad
\epsilon+p_r\ge0,\quad
\epsilon+p_t\ge0.
$$

$$
\text{NEC:}\quad
\epsilon+p_r\ge0,\quad
\epsilon+p_t\ge0.
$$

$$
\text{SEC:}\quad
\epsilon+p_r+2p_t\ge0.
$$

Um core de Sitter efetivo possui

$$
p_r=p_t=-\epsilon.
$$

Então:

$$
\epsilon+p_r=0,
\qquad
\epsilon+p_t=0,
$$

mas

$$
\epsilon+p_r+2p_t
=
-2\epsilon<0.
$$

Portanto:

$$
\boxed{
\text{NEC/WEC podem ser saturadas no core; SEC é violada.}
}
$$

Essa violação da SEC é precisamente o que remove a hipótese dos teoremas de
singularidade clássicos. Na GDQ, ela vem da pressão geométrica de densidade,
não de matéria exótica adicionada.

## 9. Estabilidade

A estabilidade correta exige estudar a Hessiana física da ação oficial ao
redor do background regular:

$$
K_{\rm BH}^{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{(g,f,\bar f)}
\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

O critério mínimo é:

$$
\operatorname{spec}
\left(
K_{\rm BH}^{\rm phys}
\right)
\setminus
\{\text{modos de gauge, massa, translação, rotação}\}
\subset
[0,\infty).
$$

No nível estrutural, há três contribuições estabilizantes:

1. pressão de densidade/Bohm, que cresce no ultravioleta;
2. torção de Bismut, que penaliza compressão de circulação;
3. regularidade de contorno do core, que impede $m(r)\sim M$ até $r=0$.

Mas a estabilidade espectral completa ainda não está demonstrada.

## 10. Evaporação

No exterior, enquanto $r_+$ é aproximadamente Schwarzschild, a temperatura
líder é a de Hawking:

$$
T_H
\simeq
\frac{\hbar c^3}{8\pi G M k_B}.
$$

Na métrica regular, a expressão geral é

$$
T_H
=
\frac{\hbar c}{4\pi k_B}
e^{\Phi(r_H)}
|A'(r_H)|.
$$

Se a evaporação reduz $M$ até um ponto extremal:

$$
A(r_*)=0,
\qquad
A'(r_*)=0,
$$

então

$$
T_H\to0.
$$

Assim, a GDQ favorece uma evaporação que termina em remanescente regular ou
em transição de ricochete, não em singularidade final. A taxa completa,
entretanto, exige calcular os canais radiativos da Hessiana física e os
contornos assintóticos.

## 11. Informação

O paradoxo de informação clássico depende de duas hipóteses:

1. singularidade real que elimina linhas de evolução;
2. horizonte tratado como perda irreversível fundamental.

Na GDQ, se o core é regular e a evolução global no contorno causal $\gamma$
permanece bem posta, não há destruição ontológica da informação. A informação
fica codificada em:

1. deformações de densidade;
2. torção/Holonomia de Bismut;
3. modos de bordo do horizonte;
4. correlações avançado--retardadas permitidas pela causalidade complexa.

Mas isso ainda não é uma Page curve calculada. O status correto é:

$$
\boxed{
\text{a GDQ remove a causa geométrica da perda de informação,
mas a restituição quantitativa ainda é programa futuro.}
}
$$

## 12. Respostas diretas

| Exigência | Resposta GDQ | Status |
|---|---|---|
| Solução covariante | Ansatz regular estático com $m(r)$ derivado de $\epsilon_{\rm GDQ}$ | Estrutural; solução explícita pendente |
| Horizonte | Raízes de $A(r_H)=0$; exterior Schwarzschild no limite | Fechado estruturalmente |
| Invariantes | Finitos se $\epsilon_{\rm GDQ}(0)<\infty$; core de Sitter | Fechado condicionalmente |
| Extensão geodésica | Sem divergência central no core regular | Condicional à solução global |
| Condições de energia | SEC violada; NEC/WEC saturáveis no core | Fechado estruturalmente |
| Estabilidade | Exige espectro de $K_{\rm BH}^{\rm phys}$ | Aberta |
| Evaporação | Hawking externa; possível remanescente extremal $T_H\to0$ | Condicional |
| Informação | Sem singularidade, não há destruição geométrica; Page curve futura | Estrutural/condicional |

## 13. Veredito

A Q55 não deve ser fechada como “solução completa de buracos negros”. O que
está fechado é o mecanismo estrutural de regularização:

$$
\text{colapso}
\to
\nabla\nabla f_R\text{ e pressão de densidade}
\to
T_{\mu\nu}^{\rm GDQ}
\to
\text{core regular}
\to
\text{invariantes finitos}.
$$

O que falta para fechamento total:

1. resolver a sela covariante completa da ação oficial;
2. obter $\epsilon_{\rm GDQ}(r)$, $p_r(r)$, $p_t(r)$ e $\Phi(r)$ sem ansatz
   fenomenológico;
3. provar extensão geodésica global;
4. diagonalizar a Hessiana física;
5. calcular evaporação e correlações de saída.

Portanto o status operacional é:

$$
\boxed{
\text{Q55 parcialmente resolvida: mecanismo anti-singular fechado;
solução global e informação permanecem abertas.}
}
$$

O plano operacional para executar esse fechamento está em
`questoes/q55/associados/plano_fechamento_total_q55.md`.

## 14. Execução do plano

O plano foi executado em modo formal + numérico reduzido. O relatório está em
`questoes/q55/associados/execucao_plano_q55.md`.

Foram criados:

1. `questoes/q55/associados/derivacao_sred_bh_q55.md`;
2. `questoes/q55/associados/solver_sela_bh_q55.py`;
3. `questoes/q55/associados/saida_solver_sela_bh_q55.md`;
4. `questoes/q55/associados/hessiana_bh_q55.md`;
5. `questoes/q55/associados/hessiana_evaporacao_page_q55.py`;
6. `questoes/q55/associados/saida_hessiana_evaporacao_page_q55.md`.

Resultado do teste efetivo regular:

$$
r_-=
2{,}687007885126\times10^{-1},
\qquad
r_+=1{,}967716165985.
$$

No core:

$$
R(0)\simeq192,
\qquad
R_{\mu\nu}R^{\mu\nu}(0)\simeq9216,
\qquad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}(0)\simeq6144.
$$

Esses valores são finitos e coincidem com o core de Sitter efetivo para
\(\Lambda_{\rm core}=48\).

A Hessiana proxy exterior retornou:

$$
\lambda_{\min}^{\rm proxy}
=
1{,}353032114277\times10^{-2}>0.
$$

Interpretação:

$$
\boxed{
\text{o pipeline Q55 é consistente e executável, mas a sela covariante
completa ainda não foi derivada.}
}
$$

## 15. Sela reduzida densidade--Bohm--torção

Para reduzir a dependência do perfil fenomenológico

$$
m(r)=\frac{Mr^3}{r^3+\ell^3},
$$

foi construído um teste variacional radial mínimo para a amplitude

$$
u(r)=\sqrt{\rho(r)}.
$$

O sistema reduzido usado foi:

$$
u'=v,
$$

$$
v'
=
2\left(\phi+\lambda_Tu^2-\mu\right)u
-\frac{2}{r}v,
$$

$$
\phi'=\frac{M(r)}{r^2},
$$

$$
M'(r)=r^2u^2.
$$

Aqui $\lambda_T>0$ é a rigidez repulsiva efetiva do setor de torção/densidade
na redução radial, e $\mu$ é determinado como autovalor pela normalização.
As condições impostas foram:

$$
u'(0)=0,
\qquad
M(0)=0,
\qquad
u(R)=0,
\qquad
M(R)=1,
\qquad
\phi(R)=-\frac1R.
$$

O script associado é:

`questoes/q55/associados/solve_sela_densidade_bohm_q55.py`.

A saída está em:

`questoes/q55/associados/saida_sela_densidade_bohm_q55.md`.

Resultado principal:

$$
\mu=
-1{,}067957044153\times10^{-1},
$$

e o ajuste central retornou:

$$
M(r)\sim r^{2{,}99999076}.
$$

Portanto, a própria redução densidade--Bohm--torção produz a condição
necessária para regularidade central:

$$
\boxed{
M(r)\sim r^3
\quad\Longrightarrow\quad
A(r)=1-O(r^2)
}
$$

sem escolher manualmente o perfil de massa.

Para compactness $\eta=1$, a solução é um lump regular subcrítico, sem
horizonte. A varredura efetiva encontrou:

$$
\eta_{\rm crit}\simeq5{,}188522012681.
$$

Acima desse valor, o mesmo perfil estacionário passa ao regime de horizonte.
Por exemplo:

| $\eta$ | $\min A$ | número de horizontes |
|---:|---:|---:|
| $5$ | $3{,}633443\times10^{-2}$ | $0$ |
| $8$ | $-5{,}418649\times10^{-1}$ | $2$ |
| $13$ | $-1{,}505530$ | $1$ |

Classificação:

$$
\boxed{
\text{teste de consistência de sela reduzida, não solução covariante
completa.}
}
$$

O ganho técnico é claro: a hipótese central de regularidade usada na Q55 não
depende mais apenas de um ansatz de massa; ela aparece como consequência de
uma equação estacionária radial com Bohm e rigidez torsional efetiva.

Naquele estágio, o elo ainda faltante era:

$$
\boxed{
\text{derivar }u(r),\phi(r),\lambda_T,\Phi(r),p_r(r),p_t(r)
\text{ da sela covariante completa da ação oficial.}
}
$$

## 16. Reconstrução covariante efetiva da sela reduzida

A etapa seguinte foi reconstruir uma métrica efetiva a partir da sela radial
reduzida, sem voltar ao perfil fenomenológico.

O script associado é:

`questoes/q55/associados/reconstrucao_covarante_sela_reduzida_q55.py`.

A saída está em:

`questoes/q55/associados/saida_reconstrucao_covarante_sela_reduzida_q55.md`.

Usou-se:

$$
A(r)=1-\frac{2\eta M(r)}{r},
$$

onde $M(r)$ vem da sela radial e $\eta$ é a compactness geométrica efetiva.
Para testar o regime de buraco negro regular, foi usado:

$$
\eta=8.
$$

O resultado foi:

$$
r_{H,1}
=
4{,}222352820613,
\qquad
r_{H,2}
=
15{,}95712272799.
$$

A regularidade central permaneceu:

$$
M(r)\sim r^{3{,}00002651}.
$$

No core, a leitura efetiva das pressões retornou:

$$
\epsilon_{\rm core}
=
9{,}934478711421\times10^{-3},
$$

$$
p_{r,\rm core}
=
-9{,}934478711373\times10^{-3},
$$

$$
p_{t,\rm core}
=
-9{,}934159730822\times10^{-3}.
$$

Logo:

$$
\epsilon+p_r
=
4{,}750637265869\times10^{-14},
$$

$$
\epsilon+p_t
=
3{,}189805987093\times10^{-7},
$$

e

$$
\epsilon+p_r+2p_t
=
-1{,}986831946160\times10^{-2}.
$$

Isto confirma a estrutura esperada:

$$
\boxed{
\text{NEC/WEC saturadas no core e SEC violada.}
}
$$

Os invariantes centrais ficaram finitos:

$$
R_{\rm core}
=
9{,}987066970693\times10^{-1},
$$

$$
R_{\mu\nu}R^{\mu\nu}_{\rm core}
=
2{,}493537672591\times10^{-1},
$$

$$
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}_{\rm core}
=
1{,}662358472304\times10^{-1}.
$$

A checagem de conservação anisotrópica foi:

$$
p_r'
+
(\epsilon+p_r)\frac{A'}{2A}
+
\frac{2(p_r-p_t)}{r}
=0.
$$

Usando derivadas analíticas de $A$ em termos de $M$, $M'$ e $M''$, o resíduo
RMS foi:

$$
{\rm RMS}_{\rm core}
=
3{,}283523548786\times10^{-10},
$$

e nos patches estáticos fora das vizinhanças dos horizontes:

$$
{\rm RMS}_{|A|>5\times10^{-2}}
=
4{,}232372694767\times10^{-10}.
$$

Portanto, a reconstrução efetiva é covariantemente consistente no nível
numérico testado.

Classificação:

$$
\boxed{
\text{reconstrução covariante efetiva a partir de sela reduzida.}
}
$$

Isto fortalece a Q55 em três pontos:

1. a condição $M(r)\sim r^3$ vem da sela radial;
2. horizontes aparecem quando a compactness ultrapassa $\eta_{\rm crit}$;
3. a fonte efetiva reconstruída satisfaz conservação covariante com erro
   numérico de ordem $10^{-10}$.

Naquele estágio, o que ainda impedia o fechamento total era:

$$
\boxed{
\text{falta derivar }\lambda_T,\eta,\Phi(r)\text{ e o setor tensorial completo
diretamente de }\operatorname{Hess}\mathcal S_{\rm GDQ}.
}
$$

## 17. Reconstrução efetiva de $\Phi(r)$ por TOV

Para não manter $\Phi(r)=0$ como escolha rígida, foi feito um teste adicional:
reconstruir o lapse pela conservação covariante efetiva.

O arquivo é:

`questoes/q55/associados/reconstrucao_lapse_tov_sela_q55.py`.

A saída é:

`questoes/q55/associados/saida_reconstrucao_lapse_tov_sela_q55.md`.

Escrevendo:

$$
g_{tt}=-A(r)e^{2\Phi(r)},
$$

define-se:

$$
\nu'(r)
=
\partial_r\log\sqrt{-g_{tt}}
=
\Phi'(r)+\frac{A'(r)}{2A(r)}.
$$

A equação efetiva de TOV fornece:

$$
\nu'
=
\frac{m+4\pi r^3p_r}{r^2A}.
$$

Portanto:

$$
\Phi'
=
\frac{m+4\pi r^3p_r}{r^2A}
-\frac{A'}{2A}.
$$

No teste, o setor radial reduzido fornece a equação de estado efetiva de core:

$$
p_r
=
-\epsilon+\frac{1}{8\pi}(u')^2.
$$

Então $p_t$ é reconstruído por conservação:

$$
p_t
=
p_r
\frac r2
\left[
p_r'
+
(\epsilon+p_r)
\left(
\Phi'+\frac{A'}{2A}
\right)
\right].
$$

Com $\eta=8$ e $\lambda_T=3$, os horizontes permanecem:

$$
r_{H,1}=4{,}222352820613,
\qquad
r_{H,2}=15{,}95712272799.
$$

O core preserva:

$$
M(r)\sim r^{3{,}00002651}.
$$

A reconstrução retornou:

$$
\epsilon_{\rm core}
=
9{,}934478711421\times10^{-3},
$$

$$
p_{r,\rm core}
=
-9{,}934477941512\times10^{-3},
$$

$$
p_{t,\rm core}
=
-9{,}934158191133\times10^{-3}.
$$

A igualdade entre o $p_r$ imposto pela equação de estado reduzida e o $p_r$
lido da métrica foi verificada por:

$$
\max_{\rm core}|p_r^{\rm metric}-p_r^{\rm input}|
=
2{,}506468990693\times10^{-12}.
$$

A conservação fechou com:

$$
{\rm RMS}_{\rm core}
=
2{,}104757829586\times10^{-16},
$$

e:

$$
{\rm RMS}_{|A|>5\times10^{-2}}
=
9{,}997320016076\times10^{-18}.
$$

O lapse é regular e pequeno nos patches estáticos:

$$
\langle\Phi\rangle_{\rm core}
=
-6{,}772283588559\times10^{-3},
$$

$$
\langle\Phi\rangle_{\rm exterior}
=
7{,}482240388239\times10^{-7}.
$$

Interpretação:

$$
\boxed{
\Phi(r)\text{ pode ser reconstruído por conservação efetiva da fonte radial.}
}
$$

Isso remove a escolha $\Phi=0$ como parte essencial do mecanismo. O que ainda
é condicional não é a forma de $\Phi(r)$ dentro dessa camada, mas a origem
variacional da equação de estado radial e dos coeficientes $\lambda_T$ e
$\eta$.

## 18. Virial e estabilidade coletiva da sela radial

Para auditar o papel de $\lambda_T$, foi testada a identidade de virial da
sela radial reduzida.

Os arquivos são:

`questoes/q55/associados/virial_lambda_t_sela_q55.py`;

`questoes/q55/associados/saida_virial_lambda_t_sela_q55.md`;

`questoes/q55/associados/estabilidade_escala_sela_q55.py`;

`questoes/q55/associados/saida_estabilidade_escala_sela_q55.md`.

Para o funcional reduzido:

$$
E[u]=K+U_T+W,
$$

com:

$$
K=\frac12\int|\nabla u|^2\,dV,
$$

$$
U_T=\frac{\lambda_T}{2}\int u^4\,dV,
$$

$$
W=\frac12\int\phi u^2\,dV,
$$

a variação de escala preservando massa:

$$
u_a(r)=a^{3/2}u(ar)
$$

implica, sem termos de bordo:

$$
2K+3U_T+W=0.
$$

A varredura mostrou que $\lambda_T$ parametriza uma família de selas
reduzidas. Portanto:

$$
\boxed{
\text{a identidade de virial audita }\lambda_T,
\text{ mas não fixa sozinha seu valor universal.}
}
$$

Para a escolha reduzida usada nos testes anteriores, $\lambda_T=3$, obteve-se:

$$
K=3{,}1675522712965487\times10^{-1},
$$

$$
U_T=9{,}808336775055311\times10^{-2},
$$

$$
W=-9{,}274781821673822\times10^{-1},
$$

e:

$$
2K+3U_T+W
=
2{,}8237534358688254\times10^{-4}.
$$

O resíduo relativo foi:

$$
1{,}5220431610642136\times10^{-4}.
$$

Esse resíduo é compatível com truncamento em $R$ e termos de bordo.

Em seguida foi testada a estabilidade coletiva na mesma direção:

$$
u_a(r)=a^{3/2}u(ar).
$$

O ajuste local de $E(a)$ em torno de $a=1$ deu:

$$
\frac{dE}{da}\bigg|_{a=1}
=
4{,}321493321954\times10^{-4},
$$

e:

$$
\frac{d^2E}{da^2}\bigg|_{a=1}
=
1{,}193971365853>0.
$$

Logo:

$$
\boxed{
\text{a sela reduzida é estável no modo coletivo radial de escala.}
}
$$

Classificação:

$$
\boxed{
\text{Hessiana reduzida de um único modo coletivo, não }K_{\rm BH}^{phys}.
}
$$

O resultado elimina uma instabilidade simples de colapso/expansão radial, mas
não substitui a diagonalização tensorial completa da Hessiana física da GDQ.

## 19. Primeiro bloco da Hessiana física: amplitude radial com Schur

O primeiro bloco espectral não-proxy da Hessiana reduzida foi construído em:

`questoes/q55/associados/hessiana_oficial_reduzida_bh_q55.md`.

O script numérico é:

`questoes/q55/associados/calcular_hessiana_radial_schur_q55.py`.

A saída está em:

`questoes/q55/associados/saida_hessiana_radial_schur_q55.md`.

O operador calculado foi:

$$
K_{uu}^{\rm Schur}
=
-\frac12\Delta
+
\phi-\mu
+
3\lambda_Tu^2
+
u\,\Delta^{-1}(2u\,\cdot).
$$

Esse operador é o bloco radial da amplitude com a retroação gravitacional
eliminada por complemento de Schur.

O modo de normalização foi removido por:

$$
P_N
=
1
-
\frac{|ru\rangle\langle ru|}
{\langle ru,ru\rangle}.
$$

Antes da projeção, o operador bruto contém:

$$
\lambda_{\rm raw,1}
=
-1{,}927437459951\times10^{-1}.
$$

Após a projeção física:

$$
\lambda_{\rm phys,1}
=
-5{,}982003087324\times10^{-13}
\simeq0,
$$

e:

$$
\lambda_{\rm phys,2}
=
3{,}651456961676\times10^{-2}>0.
$$

O resultado convergiu com a malha:

| $N$ | $\lambda_{\rm phys,2}$ |
|---:|---:|
| $300$ | $3{,}650859450588\times10^{-2}$ |
| $450$ | $3{,}651280931120\times10^{-2}$ |
| $650$ | $3{,}651456961676\times10^{-2}$ |
| $850$ | $3{,}651524343579\times10^{-2}$ |

Conclusão:

$$
\boxed{
\text{o bloco radial de amplitude é estável depois da projeção física.}
}
$$

Isso é mais forte que o teste de escala coletiva, porque inclui o operador
radial completo de amplitude e a retroação não-local do potencial por Schur.

Ainda assim, o status permanece parcial:

$$
\boxed{
\text{faltam os blocos métrico, torsional, fase e horizonte de }
K_{\rm BH}^{phys}.
}
$$

## 20. Modos escalares não homogêneos

O bloco de amplitude foi estendido para harmônicos:

$$
\delta u(r,\Omega)
=
\frac{y_\ell(r)}{r}Y_{\ell m}(\Omega).
$$

O arquivo é:

`questoes/q55/associados/calcular_hessiana_escalar_l_q55.py`.

A saída está em:

`questoes/q55/associados/saida_hessiana_escalar_l_q55.md`.

Para $0\le\ell\le8$, nenhum autovalor físico negativo foi encontrado.

O resumo dos menores autovalores físicos é:

| $\ell$ | $\lambda_{\min}^{phys}$ |
|---:|---:|
| $0$ | $3{,}651456961676\times10^{-2}$ |
| $1$ | $1{,}909625790263\times10^{-3}$ |
| $2$ | $5{,}421300837083\times10^{-2}$ |
| $3$ | $7{,}990922839410\times10^{-2}$ |
| $4$ | $1{,}000824073959\times10^{-1}$ |
| $5$ | $1{,}197517080975\times10^{-1}$ |
| $6$ | $1{,}402655798448\times10^{-1}$ |
| $7$ | $1{,}620974556422\times10^{-1}$ |
| $8$ | $1{,}854523830588\times10^{-1}$ |

O menor modo é:

$$
\lambda_{\ell=1}
=
1{,}909625790263\times10^{-3}>0.
$$

Portanto:

$$
\boxed{
\text{o setor escalar de amplitude é estável na redução testada.}
}
$$

Isso cobre os modos não homogêneos de densidade/amplitude. Ainda não cobre:

1. métrica tensorial;
2. torção independente;
3. fase/circulação;
4. modos de horizonte;
5. extensão global de Kruskal/Page curve.

## 21. Setor de fase/circulação

O setor de fase foi testado em:

`questoes/q55/associados/calcular_hessiana_fase_q55.py`.

A saída está em:

`questoes/q55/associados/saida_hessiana_fase_q55.md`.

A forma quadrática é:

$$
Q_\theta[\delta\theta]
=
\frac12\int\rho\,|\nabla\delta\theta|^2dV.
$$

O operador correspondente é:

$$
K_\theta
=
-\nabla\cdot(\rho\nabla).
$$

Para $0\le\ell\le8$, não apareceu autovalor físico negativo.

O setor $\ell=0$ possui um zero:

$$
\lambda_{\ell=0,1}
=
8{,}536256780627\times10^{-13}
\simeq0,
$$

que corresponde a:

$$
\delta\theta=\text{constante}.
$$

Esse é o modo de fase global protegido por Noether.

O primeiro autovalor físico não-zero em $\ell=0$ é:

$$
1{,}056785821936\times10^{-1}.
$$

O menor autovalor físico nos harmônicos testados ocorre em $\ell=1$:

$$
\lambda_{\ell=1}
=
6{,}572554660398\times10^{-2}>0.
$$

Conclusão:

$$
\boxed{
\text{o setor fase/circulação é estável na redução testada.}
}
$$

Com isso, os blocos reduzidos já testados são:

1. amplitude radial;
2. amplitude escalar não homogênea;
3. fase/circulação.

Permanecem:

1. torção independente;
2. métrica tensorial;
3. acoplamentos cruzados;
4. modos de horizonte;
5. Page curve física.

## 22. Blocos restantes reduzidos e modos de horizonte

Os blocos restantes foram avaliados em:

`questoes/q55/associados/calcular_blocos_restantes_hessiana_q55.py`.

A saída está em:

`questoes/q55/associados/saida_blocos_restantes_hessiana_q55.md`.

Classificação:

$$
\boxed{
\text{avaliação reduzida / diagnóstico espectral e de acoplamentos.}
}
$$

### 22.1 Setor torsional $K_{HH}^{red}$

O menor autovalor torsional independente reduzido foi:

$$
\lambda_{\min}(K_{HH}^{red})
=
1{,}485541777044\times10^{-1}>0.
$$

Para $0\le\ell\le8$, não apareceu modo negativo.

### 22.2 Setor métrico axial exterior $K_{gg}^{red}$

O menor autovalor métrico axial exterior foi:

$$
\lambda_{\min}(K_{gg}^{red})
=
1{,}493545907614\times10^{-1}>0.
$$

Para $2\le\ell\le8$, não apareceu modo negativo no patch exterior estático.

### 22.3 Acoplamentos cruzados

As normas reduzidas obtidas foram:

$$
\|K_{gf}^{red}\|
=
6{,}166879064740\times10^{-4},
$$

$$
\|K_{gH}^{red}\|
=
8{,}076881453156\times10^{-6}.
$$

As razões de Schur foram:

$$
\chi_{gf}
=
1{,}333410946325\times10^{-3},
$$

$$
\chi_{gH}
=
2{,}940248055209\times10^{-9}.
$$

Como ambas são muito menores que $1$, os acoplamentos cruzados reduzidos não
fecham o gap dos blocos diagonais testados.

### 22.4 Horizontes

Os horizontes da reconstrução efetiva são:

$$
r_{H,1}=4{,}222352820613,
\qquad
r_{H,2}=15{,}95712272799.
$$

As gravidades de superfície e temperaturas reduzidas foram:

$$
\kappa_1
=
1{,}465301433319\times10^{-1},
\qquad
T_1
=
2{,}332099662324\times10^{-2},
$$

$$
\kappa_2
=
3{,}044070699662\times10^{-2},
\qquad
T_2
=
4{,}844788989724\times10^{-3}.
$$

### 22.5 Page curve toy

Com canais espectrais positivos, foi calculada uma curva de Page toy:

$$
S_{\rm toy}(0)=0,
$$

$$
\max S_{\rm toy}
=
2{,}696953654801\times10^{-5},
$$

$$
S_{\rm toy}(1)=0.
$$

Esse resultado só mostra que a infraestrutura de canais positivos pode
produzir restituição unitária. Ainda não é a Page curve física da GDQ.

## 23. Status consolidado atual da Q55

Na camada reduzida, temos:

$$
\boxed{
\text{core regular + horizontes + conservação covariante efetiva +
estabilidade dos blocos testados.}
}
$$

## 23.1 Interpretação: sóliton geométrico com horizonte

Na GDQ, o objeto obtido deve ser interpretado como:

$$
\boxed{
\text{buraco negro regular GDQ}
=
\text{sóliton geométrico de densidade--torção--curvatura com horizonte.}
}
$$

Essa interpretação é natural porque a solução reduzida possui:

1. perfil localizado estacionário $u(r)=\sqrt\rho$;
2. massa acumulada regular, com $M(r)\sim r^3$ no core;
3. massa ADM finita no exterior;
4. pressão geométrica de densidade/Bohm contra colapso singular;
5. rigidez torsional efetiva $\lambda_T=3$;
6. horizontes causais dados por $A(r_H)=0$;
7. estabilidade espectral nos blocos reduzidos testados.

Portanto, o buraco negro não é tratado como singularidade pontual, mas como
um defeito geométrico compacto estabilizado por equilíbrio variacional, cuja
superfície causal aparece como horizonte.

Em forma curta:

$$
\boxed{
\text{um buraco negro GDQ é um sóliton gravitacional regular com horizonte.}
}
$$

Blocos reduzidos estáveis:

1. amplitude radial;
2. amplitude escalar não homogênea;
3. fase/circulação;
4. torção independente;
5. métrico axial exterior.

Acoplamentos cruzados reduzidos:

$$
\boxed{
\chi_{gf}\ll1,
\qquad
\chi_{gH}\ll1.
}
$$

Portanto, na redução executada, não apareceu canal de instabilidade.

O que ainda impede declarar a Q55 completamente fechada:

1. calcular o setor métrico polar completo;
2. tratar horizontes em coordenadas regulares atravessantes;
3. elevar a matriz acoplada reduzida para a Hessiana covariante 8D completa;
4. calcular a Page curve física por canais espectrais GDQ reais.

Assim, o status correto sobe para:

$$
\boxed{
\text{Q55 fechada na redução efetiva testada; pendente apenas para fechamento
covariante 8D completo.}
}
$$

## 24. Derivação dos faltantes principais a partir da ação oficial

Foi criado:

`questoes/q55/associados/derivacao_faltantes_acao_oficial_q55.md`.

O resultado principal é:

$$
\mathcal R^B
=
\mathcal R^{LC}
-
\frac1{12}|H|^2.
$$

No setor radial isotrópico:

$$
H_{abc}
=
q_T\rho\,\varepsilon_{abc}.
$$

Como:

$$
|H|^2=6q_T^2\rho^2,
$$

o termo torsional reduzido é:

$$
E_H
=
\frac{q_T^2}{2}\int\rho^2\,dV
=
\frac{q_T^2}{2}\int u^4\,dV.
$$

Logo:

$$
\boxed{
\lambda_T=q_T^2.
}
$$

Pela normalização isotrópica mínima dos três canais ortogonais de circulação
Cartan--Bismut:

$$
q_T^2=1+1+1=3,
$$

portanto:

$$
\boxed{
\lambda_T=3.
}
$$

O parâmetro $\eta$ foi reclassificado corretamente:

$$
\boxed{
\eta=\frac{GM_{\rm ADM}}{c^2R_0}.
}
$$

Ele é dado de contorno ADM/compactness da solução, não acoplamento livre da
ação.

Também foi removido o piso infravermelho artificial do setor torsional:

$$
K_{HH,\ell}^{red}
=
-\frac{d^2}{dr^2}
+
\frac{\ell(\ell+1)}{r^2}
+
2\lambda_T\rho(r).
$$

Mesmo sem piso artificial:

$$
\boxed{
\lambda_{\min}(K_{HH}^{red})
=
1{,}475541776890\times10^{-1}>0.
}
$$

Portanto, dentro da redução testada, os faltantes principais foram reduzidos a
dois programas covariantes:

1. setor métrico polar completo;
2. coordenadas regulares atravessando horizontes;
3. matriz acoplada covariante 8D completa;
4. Page curve física por canais espectrais reais.
