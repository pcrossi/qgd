# Teste do integrador bulk--interface

## 1. Classificação

Este cálculo é um **teste de consistência numérica**. Não é ajuste,
comparação fenomenológica ou previsão.

O script é
`ponte_global_local_integrador.py`.

## 2. Equações testadas

Foram integradas simultaneamente:

1. as sete equações reduzidas para
   $(a,c,u,v,p_a,p_c,p_u)$;
2. a corrente fixa $p_v$;
3. o fluxo fixo $h_0$;
4. a matriz fundamental variacional $7\times7$.

A restrição do lapse corrigida foi monitorada sem projeção numérica posterior.

## 3. Dados do teste

Foram usados números adimensionais deliberadamente simples:

$$
r_0=1,
\qquad
\tau=1,
\qquad
p_v=0,
\qquad
p_{a,0}=4,
$$

e intervalo local

$$
0\leq s\leq0.05.
$$

Esses valores não são parâmetros físicos da teoria e não foram comparados com
qualquer observável.

## 4. Resultado

A integração DOP853, com

$$
\mathrm{rtol}=10^{-10},
\qquad
\mathrm{atol}=10^{-12},
$$

produziu

```text
Integração local: OK
Passos: 101
Restrição inicial: 0.0
Máximo |restrição|: 2.781108676686017e-14
Máximo relativo: 6.952771691715043e-15
Estado final:
[ 1.00014719  1.00444264  0.00535495  0.
  3.99970331 -0.40597986  0.05042028 ]
```

## 5. Interpretação

A preservação da restrição na precisão de arredondamento confirma, para esse
teste local:

1. consistência entre o multiplicador eliminado e os momentos;
2. sinal correto da contribuição de $\beta$ à equação do lapse;
3. compatibilidade das equações diferenciais com o vínculo hamiltoniano;
4. viabilidade numérica da propagação simultânea do background e do
   linearizado.

O teste não demonstra:

1. existência global até o antipolo;
2. positividade da métrica em todo o domínio físico;
3. colagem DtN;
4. gap espectral;
5. valor de qualquer constante física.

## 5.1 Teste com circulação angular elementar

Depois de distinguir fluxo radial de circulação angular, o integrador recebeu
o termo de Hopf

$$
\tau\kappa_\psi\frac{a^2m^2}{c}.
$$

Foi repetido o mesmo teste local com

$$
m=1,
\qquad
\kappa_\psi=1,
\qquad
p_v=0.
$$

O resultado foi

```text
m=1 success True
C0   = 0.0
Cmax = 1.4210854715202004e-14
estado final =
[ 1.00008334  1.00251721 -0.99669296  0.
  3.99926073 -0.68731423  0.13639943 ]
```

Assim, a inclusão do harmônico angular preserva a restrição na precisão de
máquina. Esse teste valida a implementação do novo termo, mas ainda não testa
a colagem antipodal.

## 5.2 Refinamento de tolerância e passo

O script `ponte_global_local_refinar_integrador.py` comparou

$$
\mathrm{rtol}=10^{-6},10^{-8},10^{-10}
$$

e

$$
N_{\rm passo}=50,100,200,400
$$

contra uma referência com $\mathrm{rtol}=10^{-12}$ e $800$ passos máximos.

Em todas as combinações:

$$
\max|\mathscr H|
\leq2.67\times10^{-14},
$$

e o erro máximo do estado final foi

$$
\|Y_{\rm fim}-Y_{\rm ref}\|_\infty
\leq6.44\times10^{-15}.
$$

O teste local já está no regime de erro de arredondamento. Aumentar a malha
não modifica o resultado dentro da precisão dupla.

## 6. Próximo teste

O próximo cálculo deve variar apenas $p_{a,0}$ e usar como resíduo

$$
\mathfrak R(p_{a,0})
=\widetilde{\mathcal N}_-(p_{a,0})
+\mathcal N_+^{\rm eff}(p_{a,0}).
$$

Uma raiz desse resíduo fornecerá o background colado. A derivada
$\mathfrak R'(p_{a,0})$ será extraída da matriz variacional já propagada, sem
diferenças finitas de engenharia inversa.
