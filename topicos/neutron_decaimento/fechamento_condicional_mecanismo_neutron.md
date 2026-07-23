# Fechamento condicional do mecanismo GDQ do decaimento do nêutron

## 1. Hipóteses de fechamento

Adote o potencial radial derivado no setor bimodal:

$$
U(r)=A_2r^2-B_3r^3+C_4r^4,
\qquad
A_2,B_3,C_4>0,
$$

com

$$
B_3=\frac{2\kappa_T\tau_T^2\nu_3}{V_0^2},
$$

$\tau_T$ denota a unidade de torção do estômato e não o parâmetro de fluxo da
ação oficial.

e suponha:

1. $B_3^2>4A_2C_4$;
2. a mobilidade causal coletiva $M_r$ é positiva;
3. o contorno $\gamma$ contém a thimble da sela radial;
4. os operadores assintóticos de cola são Fredholm;
5. o overlap de quatro modos da ação oficial é finito.

Essas são hipóteses técnicas explícitas, não novos termos da ação.

## 2. Núcleo crítico

Os pontos estacionários não nulos são

$$
r_\pm
=\frac{3B_3\pm\sqrt{9B_3^2-32A_2C_4}}{8C_4}.
$$

Sob $B_3^2>4A_2C_4$, o ramo $r_+$ possui região de ação inferior à origem e
$r_-$ separa o nêutron do tubo bimodal. Logo,

$$
\boxed{r_-=\text{núcleo crítico da cirurgia}.}
$$

## 3. Construção da sela causal

Na coordenada coletiva euclidiana $s$, use a redução

$$
\mathcal A_{\rm red}[r]
=\int ds
\left[
\frac{M_r}{2}\left(\frac{dr}{ds}\right)^2+U(r)
\right].
$$

A equação da sela é

$$
M_r\frac{d^2r}{ds^2}=U'(r).
$$

Para a trajetória de energia reduzida nula,

$$
\frac{M_r}{2}\left(\frac{dr}{ds}\right)^2=U(r),
$$

e a solução é definida pela quadratura

$$
\boxed{
s-s_0
=\sqrt{\frac{M_r}{2}}
\int_{r_-}^{r(s)}\frac{du}{\sqrt{U(u)}}.
}
$$

Portanto, a sela existe sempre que $U(r)\geq0$ entre a origem e o primeiro
ponto de retorno $r_t>r_-$ que satisfaz $U(r_t)=0$.

Como

$$
U(r)=r^2(A_2-B_3r+C_4r^2),
$$

o ponto de retorno relevante é

$$
\boxed{
r_t
=\frac{B_3-\sqrt{B_3^2-4A_2C_4}}{2C_4}.
}
$$

A ação da ida e volta é

$$
\boxed{
S_{\rm bounce}
=2\sqrt{2M_r}
\int_0^{r_t}\sqrt{U(r)}\,dr.
}
$$

Ela é real e positiva para $M_r>0$. A thimble causal seleciona a continuação
da sela para o tempo físico reconstruído.

## 4. Limite degenerado analítico

No limiar

$$
B_3^2=4A_2C_4,
$$

defina

$$
r_*=\frac{B_3}{2C_4}.
$$

Então

$$
U(r)=C_4r^2(r-r_*)^2.
$$

A solução de parede é

$$
\boxed{
r(s)
=\frac{r_*}
{1+\exp[-\omega(s-s_0)]},
\qquad
\omega=r_*\sqrt{\frac{2C_4}{M_r}}.
}
$$

A ação de uma travessia é

$$
S_{\rm wall}
=\sqrt{2M_rC_4}\frac{r_*^3}{6},
$$

e a ida e volta fornece

$$
S_{\rm bounce}^{\rm deg}
=\sqrt{2M_rC_4}\frac{r_*^3}{3}.
$$

## 5. Invariantes do intermediário

O cobordismo completo impõe

$$
Q_n=Q_p+Q_\Pi.
$$

Como $Q_n=0$ e $Q_p=+1$,

$$
\boxed{Q_\Pi=-1.}
$$

O número bariônico satisfaz

$$
1=1+0.
$$

A torção dupla seleciona o par primitivo

$$
-2\tau_T=(-\tau_T)+(-\tau_T).
$$

Assim, o intermediário é um tubo virtual bimodal, carregado e não bariônico.

## 6. Resolução nos dois modos finais

Seja $D_{\partial,\Pi}$ o operador tangencial de Dirac--Bismut no tubo. A
cirurgia final separa seu subespaço de saída em

$$
\ker D_{\partial,\Pi}^{\rm out}
=\mathcal H_{-1}\oplus\mathcal H_0,
$$

onde os índices de resíduo são

$$
Q|_{\mathcal H_{-1}}=-1,
\qquad
Q|_{\mathcal H_0}=0.
$$

Sob a hipótese Fredholm e cruzamento espectral simples, cada bloco contém um
modo primitivo. A holonomia de meia unidade fornece

$$
J(\mathcal H_{-1})=J(\mathcal H_0)=\frac12.
$$

A orientação da corrente torsional fixa índices leptônicos opostos:

$$
L_e(\mathcal H_{-1})=+1,
\qquad
L_e(\mathcal H_0)=-1.
$$

Logo, pelos invariantes assintóticos,

$$
\boxed{
\mathcal H_{-1}\equiv e^-,
\qquad
\mathcal H_0\equiv\bar\nu_e.
}
$$

Essa identificação é condicional à existência dos dois cruzamentos simples;
ela não decorre apenas dos nomes atribuídos aos modos.

## 7. Energia e espectro

A energia cinética disponível é

$$
Q_\beta
=(\delta_B-1)M_ec^2
\simeq0{,}782\ {\rm MeV}.
$$

Para um elemento de transição lentamente variável na janela cinemática, a
medida espectral de três corpos fornece

$$
\boxed{
\frac{d\Gamma}{dE_e}
=\mathcal N_{\rm GDQ}
p_eE_e(E_0-E_e)^2
F_{\rm geom}(E_e),
}
$$

onde

$$
p_e=\sqrt{E_e^2-m_e^2},
\qquad
E_0=M_n-M_p,
$$

e $F_{\rm geom}$ é a resposta de cola/forma derivada dos modos normalizados.
O fator $(E_0-E_e)^2$ resulta da integração do modo neutro e explica o espectro
contínuo.

## 8. Normalização da taxa

O primeiro vértice não nulo da expansão da ação oficial define

$$
\mathcal M_0
=\mathcal V_{\rm GDQ}^{(k)}
[\psi_n,\psi_p,\psi_e,\psi_{\bar\nu}].
$$

Então

$$
\mathcal N_{\rm GDQ}
=\frac{2\pi}{\hbar}|\mathcal M_0|^2
\times\mathcal J_{\rm norm},
$$

com $\mathcal J_{\rm norm}$ determinado pelas normalizações espectrais. A taxa
total é

$$
\boxed{
\Gamma_n
=\int_{m_e}^{E_0}
\frac{d\Gamma}{dE_e}\,dE_e,
\qquad
\tau_n=\Gamma_n^{-1}.
}
$$

## 9. Teorema de fechamento condicional

> Sob as cinco hipóteses da Seção 1, a torção dupla do estômato contrário
> produz um núcleo crítico bimodal; a ação reduzida possui uma sela de bounce;
> o cobordismo conserva carga elétrica e número bariônico; a resolução
> Fredholm fornece um modo carregado e um modo neutro de spin $1/2$; e a medida
> espectral produz um espectro beta contínuo. A taxa é determinada pelo overlap
> $\mathcal M_0$ da ação oficial.

Portanto,

$$
\boxed{
n\longrightarrow p+\Pi^-_{\rm virt}
\longrightarrow p+e^-+\bar\nu_e
}
$$

está fechado como mecanismo geométrico **condicional**.

## 10. Limite do fechamento

Não foi obtido um número para $\tau_n$. Isso exigiria calcular

$$
A_2,
\quad B_3,
\quad C_4,
\quad M_r,
\quad \mathcal M_0,
\quad F_{\rm geom}
$$

no background causal explícito. Usar a vida média experimental para fixar
$\mathcal M_0$ seria calibração, não previsão.

## 11. Status

- topologia e balanços: fechados condicionalmente ao cobordismo;
- núcleo crítico e sela: construídos no potencial reduzido;
- identificação dos modos: condicional ao espectro Fredholm simples;
- forma contínua do espectro: derivação efetiva;
- normalização contraída e vida média: fechadas posteriormente pela igualdade
  entre a lei GDQ de relaxamento e o overlap de quatro modos; ver
  topicos/neutron_decaimento/fechamento_terceiros_jatos_neutron_gdq.md.

## 12. Auditoria numérica posterior

A avaliação reproduzível está em
`neutron/auditar_vida_neutron_gdq.py`, com relatório em
`neutron/saida_auditoria_vida_neutron_gdq.md`. A fórmula histórica
$(32/15)\alpha^{-11}\hbar/(m_ec^2)$ fornece $879{,}398775$ s, desvio de
$0{,}1137\%$ em relação à média PDG $878{,}4\pm0{,}5$ s. A taxa nua de três
corpos, usando o candidato $G_F$ da Q29 e $g_A$ externo, fornece $893{,}55$ s.
Assim, a proximidade numérica está confirmada para a fórmula histórica, mas o
overlap causal continua não derivado.

## 13. Redução explícita das calotas e regra de seleção

A cadeia solicitada posteriormente foi consolidada em
`topicos/geometria_torcao_hopf/resultado_cadeia_cinco_passos_gdq.md`, com verificação numérica em
`neutron/resolver_cadeia_gdq_neutron.py`. Para duas calotas redondas e um
colar, a ação oficial fornece parametricamente

$$
A_2=\pi^2(32+12\ell)w_R+A_2^{\rm cola},
\quad
B_3=\frac{2\kappa_T\tau_T^2\nu_3}{V_0^2},
\quad
C_4=\pi^2\left(\frac83+2\ell\right)w_V+C_4^{\rm cola}.
$$

Aqui $\tau_T$ é a unidade de torção, distinta do parâmetro de fluxo $\tau$ da
ação oficial.

O operador de Dirac--Bismut fornece exatamente um kernel de bloco carregado
em $(m,j)=(-1,1/2)$ e um kernel neutro bidimensional em $(m,j)=(0,0)$.
O zero de Peter--Weyl entre esses dois modos isolados não é o overlap físico,
que contém também $\psi_n$ e $\psi_p$. A seleção completa admite dois
invariantes $SU(2)$:

$$
\mathcal M_0=C_SS+C_TT,
\qquad
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=2|C_S|^2+6|C_T|^2.
$$

Assim, um vértice homogêneo completo não está excluído. A antiga hipótese 5
foi refinada: a taxa total requer apenas
$2|C_S|^2+6|C_T|^2$, combinação fixada pela lei GDQ de relaxamento. Calcular
os dois resíduos separadamente permanece necessário para polarização e
correlações angulares, não para a normalização da taxa.
