---
title: "Auditoria numérica de Stern-Gerlach"
---

# Auditoria numérica de Stern--Gerlach

Esta nota registra os scripts finais preservados no manuscrito. Eles são
autocontidos e não dependem de arquivos externos ao capítulo.

## 1. Captura condicionada e Born

O script `simular_captura_sg.py` integra:

$$
dp_t=4\sqrt{\Gamma}\,p_t(1-p_t)\,dW_t.
$$

Com limiares $\varepsilon$ e $1-\varepsilon$, a probabilidade analítica de
primeiro alcance do limiar superior é:

$$
P_\varepsilon(+)
=
\frac{p_0-\varepsilon}{1-2\varepsilon}.
$$

O script `validar_limiar_born_sg.py` verifica que:

$$
\lim_{\varepsilon\to0}P_\varepsilon(+)=p_0.
$$

Nos testes preservados, o maior desvio Monte Carlo no estudo de limiar foi
$2.518\sigma$, compatível com flutuação estatística. A coluna
$|P_\varepsilon-p_0|$ decai linearmente com $\varepsilon$.

## 2. Feixe completo

O script `simular_feixe_sg_completo.py` combina:

1. captura condicionada dos canais;
2. força oposta de centro de massa;
3. deriva livre até a tela.

Para $\theta=60^\circ$:

- alvo Born: $p_+=0.75$;
- frequência simulada: $p_+=0.75184$;
- separação analítica: $0.7000000$;
- separação numérica: $0.6996684$;
- erro relativo da separação: $4.737\times10^{-4}$.

## 3. Medições sequenciais

O script `simular_sequencias_sg.py` verifica:

- sequência $z\to z$: fidelidade $1$;
- sequência $z\to x$: $P(x+)=0.503325$;
- sequência $z\to x\to z$: $P(z+)=0.499975$;
- correlação entre $x$ intermediário e $z$ final: $0.000600$.

Isso reproduz a incompatibilidade operacional de eixos sem interpretar
$\kappa$ como tabela preexistente para todos os aparelhos.

## 4. Regime não adiabático

O script `simular_nao_adiabatico_sg.py` integra:

$$
H(t)
=
\frac12
\left(vt\,\sigma_z+\Delta\sigma_x\right),
$$

com $\Delta=1$ e $\hbar=1$, e compara com:

$$
P_{\rm LZ}
=
\exp\left(-\frac{\pi\Delta^2}{2v}\right).
$$

Na faixa $v\in\{0.2,0.4,0.8,1.6,3.2\}$, o maior erro absoluto contra
Landau--Zener foi:

$$
2.920\times10^{-4}.
$$

O mesmo script calcula:

$$
\|[H,P_z^+]\|=0.707106781,
\qquad
\frac{dp_z}{dt}=0.5
$$

em um estado de teste. Portanto, quando o aparelho não é QND/adiabático,
$p_z$ deixa de ser martingal.

## 5. Espectro Robin reduzido

O script `resolver_canais_robin_sg.py` resolve o operador de teste:

$$
H_\pm
=
-\frac{d^2}{dr^2}+V(r),
\qquad
R_\pm=R_0\pm r_B.
$$

Na malha $N=1600$:

$$
\lambda_1^+=1.030703215,
\qquad
\lambda_1^-=1.025837708,
$$

$$
\lambda_1^+-\lambda_1^-
=
4.865507054\times10^{-3}.
$$

As somas reduzidas são:

$$
\Gamma_{\rm red}^+=0.2426699727,
\qquad
\Gamma_{\rm red}^-=0.2949562551,
$$

$$
\kappa_{\rm red}^+=0.1000246896,
\qquad
\kappa_{\rm red}^-=0.1416924219.
$$

Esses números são teste de convergência do método, não previsão física
universal.

## 6. Background, contorno e Hopf cilíndrico

`construir_background_estacionario_sg.py` verifica o background de bulk
gaussiano com resíduo nulo. `verificar_contorno_variacional_sg.py` confirma:

$$
r_c=\sqrt{6\tau},
\qquad
K-n(F)=0.
$$

`testar_zh_gaussiano_sg.py` mostra que o gaussiano puro não localiza o modo
axial:

$$
Z_H^{\rm gaussiano}=0.
$$

`resolver_dtn_hopf_cilindrico_sg.py` calcula:

$$
z_H=\frac{3\sqrt\pi}{4}
=1.329340388179\ldots
$$

`comparar_acoes_estacionarias_sg.py` encontra:

$$
\mathcal W_{\rm cyl}-\mathcal W_{\rm G}
=
-0.3439257889495.
$$

`verificar_estabilidade_raio_cilindrico_sg.py` confirma:

$$
\mathcal W''(2\sqrt\tau)=\frac{3}{2\tau}>0.
$$

## 7. Atlas de Hopf

O script `verificar_atlas_hopf_sg.py` confirma:

- erro máximo dos projetores: $2.889\times10^{-16}$;
- erro máximo da transição: $1.279\times10^{-16}$;
- erro relativo da métrica de Fubini--Study menor que $8.0\times10^{-7}$.

## 8. Avaliador físico e contrato

`avaliar_background_gdq_sg.py` não contém defaults fenomenológicos. Ele exige
um arquivo com:

$$
\{\lambda_\nu,\ Z_\nu,\ j_{\nu1},\ j_{\nu2},\ \gamma_\nu,\ C_\nu\}.
$$

O fixture `testar_pipeline_background_sg.py` valida apenas a álgebra:

$$
\kappa_{\rm fixture}=1.09375,
\qquad
\Gamma_{\rm fixture}=0.9.
$$

Ele é explicitamente não físico.

## 9. Teste dimensional Zeeman

`testar_zeeman_fisico_sg.py` converte dados externos de aparelho em:

$$
\Delta
=
\frac{|g_{\rm geom}|\mu_B}{\hbar}|B_\perp|,
$$

$$
v
=
\frac{|g_{\rm geom}|\mu_B}{\hbar}
|\partial_tB_\parallel+\mathbf u\cdot\nabla B_\parallel|.
$$

Para o teste preservado:

$$
\Delta=1.760859628909\times10^9\,{\rm s}^{-1},
$$

$$
v=8.804298144544\times10^{14}\,{\rm s}^{-2},
$$

$$
P_{\rm LZ}=0.
$$

Esse resultado significa que, para esses dados de aparelho, a passagem é
extremamente adiabática no modelo reduzido.
