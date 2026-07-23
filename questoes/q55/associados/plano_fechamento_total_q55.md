# Q55 — Plano de fechamento total

## Objetivo

Fechar a Questão 55 além do mecanismo anti-singular estrutural, chegando a
uma solução covariante GDQ para buracos negros regulares com horizonte,
invariantes finitos, extensão geodésica, estabilidade, evaporação e
informação.

O alvo não é ajustar um modelo regular conhecido. O alvo é derivar tudo da
ação oficial:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*^{\rm BH}
\to
T_{\mu\nu}^{\rm GDQ}
\to
g_{\mu\nu}^{\rm eff}
\to
K_{\rm BH}^{\rm phys}
\to
\Gamma_{\rm evap}
\to
\mathcal I_{\rm out}.
$$

## Fase 1 — Formulação variacional covariante

### 1.1 Enunciado variacional

Definir o setor de colapso esfericamente simétrico como redução admissível da
ação oficial, com campos:

$$
X(r)
=
\{\Phi(r),A(r),f_R(r),S_R(r),H(r),\mathcal U(r)\}.
$$

Usar a métrica efetiva:

$$
ds^2
=
-e^{2\Phi(r)}A(r)c^2dt^2
+A(r)^{-1}dr^2
+r^2d\Omega^2.
$$

com:

$$
A(r)=1-\frac{2Gm(r)}{c^2r}.
$$

### 1.2 Redução da ação oficial

Reduzir a ação oficial para um funcional radial:

$$
S_{\rm red}^{\rm BH}
=
\int dr\,
\mathcal L_{\rm red}
\left(
\Phi,A,f_R,S_R,H;
\Phi',A',f_R',S_R',H'
\right).
$$

Exigência:

- não inserir Einstein--Hilbert como ação fundamental;
- usar a equação métrica ponderada da GDQ;
- usar Einstein apenas como forma efetiva macroscópica já justificada na Q54;
- manter $\rho=e^{-f_R}$ e $\mathcal U$ constitutiva.

### 1.3 Equações de Euler--Lagrange

Derivar:

$$
\frac{\delta S_{\rm red}^{\rm BH}}{\delta\Phi}=0,
\qquad
\frac{\delta S_{\rm red}^{\rm BH}}{\delta A}=0,
\qquad
\frac{\delta S_{\rm red}^{\rm BH}}{\delta f_R}=0,
\qquad
\frac{\delta S_{\rm red}^{\rm BH}}{\delta H}=0.
$$

Resultado esperado da fase:

$$
\mathcal E_A=0,
\quad
\mathcal E_\Phi=0,
\quad
\mathcal E_f=0,
\quad
\mathcal E_H=0.
$$

## Fase 2 — Fonte física sem ansatz fenomenológico

### 2.1 Extração de $\epsilon$, $p_r$, $p_t$

Definir o tensor efetivo por variação métrica:

$$
T_{\mu\nu}^{\rm GDQ}
=
-\frac{2}{\sqrt{-g}}
\frac{\delta S_{\rm eff}^{\rm mat}}{\delta g^{\mu\nu}}.
$$

Na simetria esférica:

$$
T^\mu{}_\nu
=
\operatorname{diag}
(-\epsilon,p_r,p_t,p_t).
$$

Então:

$$
\epsilon(r)
=
-T^t{}_t,
\qquad
p_r(r)
=
T^r{}_r,
\qquad
p_t(r)
=
T^\theta{}_\theta.
$$

### 2.2 Relações geométricas úteis

Com

$$
A(r)=1-\frac{2Gm(r)}{c^2r},
$$

as equações efetivas fornecem:

$$
m'(r)
=
\frac{4\pi r^2}{c^2}\epsilon(r),
$$

e

$$
\Phi'(r)
=
\frac{Gm(r)/c^2+4\pi Gr^3p_r(r)/c^4}
{r^2A(r)}.
$$

Essas fórmulas devem ser usadas como leitura geométrica da solução GDQ, não
como entrada independente.

### 2.3 Condições de contorno

No centro:

$$
m(0)=0,
\qquad
\epsilon(r)=\epsilon_0+O(r^2),
\qquad
\Phi'(0)=0.
$$

No infinito:

$$
m(r)\to M,
\qquad
\Phi(r)\to0,
\qquad
f_R(r)\to f_\infty.
$$

No horizonte:

$$
A(r_H)=0
$$

com regularidade em coordenadas de Eddington--Finkelstein ou Kruskal
generalizadas.

## Fase 3 — Existência e extensão geodésica

### 3.1 Prova local no centro

Provar que as EDOs admitem expansão regular:

$$
m(r)=m_3r^3+m_5r^5+\cdots,
$$

$$
\Phi(r)=\Phi_0+\Phi_2r^2+\Phi_4r^4+\cdots,
$$

$$
f_R(r)=f_0+f_2r^2+f_4r^4+\cdots.
$$

Critério:

$$
|R|,
\quad
R_{\mu\nu}R^{\mu\nu},
\quad
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}
<\infty.
$$

### 3.2 Continuação até o exterior

Resolver o problema de valor de contorno:

$$
X(0)=X_{\rm core},
\qquad
X(\infty)=X_{\rm Schw}(M).
$$

Mostrar que a solução cruza horizontes usando coordenadas regulares, não a
carta Schwarzschild singular.

### 3.3 Extensão geodésica

Demonstrar que para todo geodésico causal:

$$
\lambda_{\rm aff}
\to
\pm\infty
$$

ou que qualquer ponto de retorno/continuação é regular. O teste prático é
integrar:

$$
\dot r^2
+A(r)\left(\varepsilon+\frac{L^2}{r^2}\right)
=
E^2
$$

em carta regular.

## Fase 4 — Hessiana física e estabilidade

### 4.1 Segunda variação

Construir:

$$
K_{\rm BH}
=
\operatorname{Hess}_{X_*}
S_{\rm red}^{\rm BH}.
$$

### 4.2 Remoção de gauge

Definir o projetor físico:

$$
P_{\rm phys}
=
1-P_{\rm gauge}-P_{\rm zero}.
$$

com modos zero:

- massa total $M$;
- translação;
- rotação;
- reparametrização radial;
- normalização de fase/medida.

### 4.3 Operador físico

Definir:

$$
K_{\rm BH}^{\rm phys}
=
P_{\rm phys}K_{\rm BH}P_{\rm phys}.
$$

Critério de estabilidade:

$$
\operatorname{spec}
\left(
K_{\rm BH}^{\rm phys}
\right)
\subset
[0,\infty)
$$

fora de modos zero controlados.

### 4.4 Validação numérica

Construir solver Sturm--Liouville matricial para os setores:

1. radial escalar;
2. métrico polar;
3. métrico axial;
4. torcional;
5. dilatônico;
6. misto métrico--dilatônico--torcional.

## Fase 5 — Evaporação

### 5.1 Temperatura

Calcular:

$$
T_H
=
\frac{\hbar c}{4\pi k_B}
e^{\Phi(r_H)}
|A'(r_H)|.
$$

### 5.2 Canais radiativos

A taxa deve vir dos autovalores da Hessiana física:

$$
\Gamma_{\rm evap}
=
\sum_j
\Gamma_j
\left[
\lambda_j(K_{\rm BH}^{\rm phys}),
r_H,
T_H
\right].
$$

Não inserir espectro de partículas do Modelo Padrão como ontologia. Se usado,
classificar como comparação efetiva externa.

### 5.3 Remanescente

Identificar se existe ponto extremal:

$$
A(r_*)=0,
\qquad
A'(r_*)=0.
$$

Se existir:

$$
T_H\to0.
$$

## Fase 6 — Informação e Page curve

### 6.1 Observável de informação

Definir entropia de entrelaçamento efetiva para modos de saída:

$$
S_{\rm out}(u)
=
-\operatorname{Tr}
\rho_{\rm out}(u)\ln\rho_{\rm out}(u).
$$

### 6.2 Canal GDQ

Construir o mapa:

$$
\mathcal C_{\rm BH}:
\mathcal I_{\rm in}
\to
\mathcal I_{\rm core}
\to
\mathcal I_{\rm out}.
$$

Na GDQ, a hipótese forte é que o core regular e o contorno causal $\gamma$
preservam a informação global:

$$
\mathcal C_{\rm BH}^\dagger\mathcal C_{\rm BH}=1.
$$

Isso deve ser provado por conservação de medida, fluxo e holonomia, não apenas
afirmado.

### 6.3 Page curve

Calcular numericamente:

$$
S_{\rm out}(u)
$$

e verificar se:

1. cresce no regime térmico inicial;
2. atinge máximo;
3. decresce quando correlações de core/horizonte retornam;
4. termina finita ou nula no remanescente/transição.

## Entregáveis

1. `derivacao_sred_bh_q55.md` — redução radial da ação oficial.
2. `solver_sela_bh_q55.py` — solução covariante do background.
3. `saida_solver_sela_bh_q55.md` — perfis $A,\Phi,\epsilon,p_r,p_t$.
4. `invariantes_geodesicas_q55.py` — invariantes e geodésicas.
5. `saida_invariantes_geodesicas_q55.md`.
6. `hessiana_bh_q55.md` — operador físico e projetores.
7. `solver_hessiana_bh_q55.py`.
8. `saida_hessiana_bh_q55.md`.
9. `evaporacao_page_curve_q55.py`.
10. `saida_evaporacao_page_curve_q55.md`.
11. atualização final de `questoes/q55/questao_55.md`.

## Critério de fechamento

A Q55 só poderá ser declarada fechada totalmente se:

1. a solução covariante for obtida da ação oficial;
2. os invariantes forem finitos;
3. geodésicas causais forem extensíveis;
4. a Hessiana física não tiver modo instável não-gauge;
5. evaporação for computada a partir dos modos físicos;
6. a curva de informação for calculada ou houver teorema claro de unitariedade
   do canal.

Antes disso, o status correto permanece:

$$
\boxed{
\text{mecanismo anti-singular fechado estruturalmente;
fechamento global de buracos negros aberto.}
}
$$

