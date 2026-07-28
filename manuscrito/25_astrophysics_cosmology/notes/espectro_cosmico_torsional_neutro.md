---
title: "Nota — Espectro cósmico de modos neutros torsionais"
---

# Nota — Espectro cósmico de modos neutros torsionais

## 1. Hipótese física examinada

Considere duas orientações conjugadas do setor neutro:

$$
\nu_i^{(+)}
\quad\text{e}\quad
\nu_j^{(-)}.
$$

O sinal designa orientação torsional, não carga elétrica. O canal:

$$
\nu_i^{(+)}+\nu_j^{(-)}
\longrightarrow
\gamma+\gamma
$$

é permitido somente quando:

1. a circulação torsional total pode cancelar;
2. o overlap entre os modos não é proibido;
3. energia, momento e momento angular são conservados;
4. o jato radiativo da ação no background cosmológico não se anula.

O cálculo desta nota determina posições espectrais. Ele não supõe que todos
os encontros se aniquilem nem que o canal fotônico tenha ramificação
unitária.

## 2. Energia por fóton

No centro de massa:

$$
P^\mu
=
p_i^\mu+p_j^\mu
=
(\sqrt{s_{ij}},\mathbf0).
$$

Um único fóton não pode carregar $P^2=s_{ij}>0$. Para dois fótons:

$$
P^\mu
=
k_1^\mu+k_2^\mu,
\qquad
k_1^2=k_2^2=0,
$$

e:

$$
E_{\gamma,*}^{(ij)}
=
\frac{\sqrt{s_{ij}}}{2}.
$$

No limite frio:

$$
\boxed{
E_{\gamma,*}^{(ij)}
\simeq
\frac{m_i+m_j}{2}c^2.
}
$$

Logo:

$$
\boxed{
\lambda_{ij,*}
=
\frac{2hc}{(m_i+m_j)c^2}.
}
$$

## 3. Acoplamento variacional

O coeficiente físico deve vir do background neutro cosmológico:

$$
\Phi_\nu^{\rm cos}
=
(g,J,H,f,\mathcal U)_\nu.
$$

Depois de projetar vínculos e eliminar modos internos:

$$
C_{ij\gamma\gamma}^{\rm GDQ}
=
D^4\mathcal S_{\rm red}[\Phi_\nu^{\rm cos}]
[\eta_i^+,\eta_j^-,\psi_\gamma,\psi_\gamma]
-
D^3\mathcal S_{\rm red}
G_{\rm int}
D^3\mathcal S_{\rm red}.
$$

A seção é:

$$
\langle\sigma v\rangle_{ij}
\propto
\int d\Pi_{\gamma\gamma}
\left|
C_{ij\gamma\gamma}^{\rm GDQ}
\right|^2.
$$

Como esse jato ainda não foi avaliado no background 8D, as intensidades
absolutas e relativas permanecem abertas.

## 4. Pente espectral

As escalas inerciais candidatas do setor neutro são:

$$
m_1=0,
\qquad
m_2=8.798417219655\times10^{-3}\ {\rm eV},
\qquad
m_3=5.042386973059\times10^{-2}\ {\rm eV}.
$$

Com o momento relicto médio incluído, obtém-se:

| Canal | $E_{\gamma,*}$ | $\lambda_*$ |
|---|---:|---:|
| $\nu_1\bar\nu_1$ | $0.528$ meV | $2346.9\,\mu{\rm m}$ |
| $\nu_1\bar\nu_2$ | $4.671$ meV | $265.4\,\mu{\rm m}$ |
| $\nu_1\bar\nu_3$ | $25.477$ meV | $48.7\,\mu{\rm m}$ |
| $\nu_2\bar\nu_2$ | $8.814$ meV | $140.7\,\mu{\rm m}$ |
| $\nu_2\bar\nu_3$ | $29.620$ meV | $41.9\,\mu{\rm m}$ |
| $\nu_3\bar\nu_3$ | $50.427$ meV | $24.6\,\mu{\rm m}$ |

Os canais cruzados são condicionais aos overlaps fora da diagonal. O primeiro
canal é térmico e largo porque $m_1=0$ no ramo mínimo reduzido.

## 5. Temperatura e largura

A condição cosmológica de referência é:

$$
T_{\nu,0}
=
\left(
\frac4{11}
\right)^{1/3}
T_{\gamma,0}.
$$

Para:

$$
T_{\gamma,0}
=
2.72548\ {\rm K},
$$

resulta:

$$
T_{\nu,0}
=
1.9453546\ {\rm K}.
$$

A distribuição desacoplada possui:

$$
\langle p_\nu\rangle
\simeq
3.151374\,k_BT_{\nu,0}.
$$

Isso produz largura térmica pequena nos dois modos massivos e um contínuo
milimétrico para o modo sem massa.

## 6. Transporte cosmológico

O redshift transforma:

$$
E_0
=
\frac{E_*}{1+z},
\qquad
\lambda_0
=(1+z)\lambda_*.
$$

No toy homogêneo com seção constante, densidade
$n_\nu(z)=n_{\nu,0}(1+z)^3$ e sem depleção:

$$
\frac{dI}{dz}
\propto
\frac{1+z}{H(z)}.
$$

O kernel produzido por essa expressão serve para localizar a assinatura e
testar sensibilidade. Ele não substitui o solver cosmológico único.

## 7. Comparação de faixa

O COBE/DIRBE mediu:

$$
\nu I_\nu(140\,\mu{\rm m})
=
25\pm7\ {\rm nW\,m^{-2}\,sr^{-1}},
$$

e:

$$
\nu I_\nu(240\,\mu{\rm m})
=
14\pm3\ {\rm nW\,m^{-2}\,sr^{-1}}.
$$

A posição do canal $22$ é:

$$
\lambda_{22,*}
=
140.663\,\mu{\rm m},
$$

$0.474\%$ acima da banda de $140\,\mu{\rm m}$. A mesma linha emitida em:

$$
z
=
0.7062
$$

chega hoje em $240\,\mu{\rm m}$. O canal $12$ fica dentro do domínio FIRAS,
e o canal $33$ fica próximo da banda Spitzer de $24\,\mu{\rm m}$.

Essa coincidência demonstra compatibilidade espectral, não origem causal. O
fundo infravermelho já possui contribuição substancial de galáxias e poeira.

## 8. Escala inversa de intensidade

Para mostrar a ordem de grandeza, e somente como engenharia inversa, atribua
toda a intensidade FIRAS de:

$$
I_{\rm FIRAS}
=
14\ {\rm nW\,m^{-2}\,sr^{-1}}
$$

ao canal diagonal $22$ entre $z=0$ e $z=5$. A intensidade bolométrica seria:

$$
I
=
\frac{c}{4\pi}
\langle\sigma v\rangle_{22}
n_{\nu,0}^2
(2m_2c^2)
\int_0^5
\frac{1+z}{H(z)}
\,dz.
$$

A inversão fornece:

$$
\langle\sigma v\rangle_{22}^{\rm inv}
=
3.09675\times10^{-29}\ {\rm m^3\,s^{-1}},
$$

com profundidade óptica:

$$
\tau_{\rm ann}
\simeq
1.22494\times10^{-2}.
$$

Esses valores não são constantes derivadas. O teste de sensibilidade varia a
seção inversa de $1.31\times10^{-28}$ para $z_{\max}=1$ até
$3.10\times10^{-29}\ {\rm m^3\,s^{-1}}$ para $z_{\max}=5$.

## 9. Assinatura falsificável

O teste adequado procura:

1. um pente nas razões de energia $(m_i+m_j)/2$;
2. largura compatível com a temperatura relicta;
3. cauda para comprimentos maiores por redshift;
4. razões de intensidade calculadas pelos overlaps;
5. componente não correlacionada com poeira;
6. depleção neutra compatível com cosmologia.

O resultado atual é:

$$
\boxed{
\text{posição e forma normalizada previstas condicionalmente;}
\quad
\text{brilho ainda aberto}.
}
$$

O script
[[../scripts/espectro_cosmico_torsional_neutro.py]]
reproduz o pente, o kernel de redshift, a comparação de faixa e os testes de
convergência.

## 10. Referências de comparação

- D. J. Fixsen, “The Temperature of the Cosmic Microwave Background,”
  *Astrophysical Journal* **707**, 916 (2009):
  <https://doi.org/10.1088/0004-637X/707/2/916>.
- M. G. Hauser et al., “The COBE Diffuse Infrared Background Experiment
  Search for the Cosmic Infrared Background,” *Astrophysical Journal*
  **508**, 25 (1998): <https://doi.org/10.1086/306379>.
- D. J. Fixsen et al., “The Spectrum of the Extragalactic Far-Infrared
  Background from the COBE FIRAS Observations,” *Astrophysical Journal*
  **508**, 123 (1998): <https://doi.org/10.1086/306383>.
- C. Papovich et al., “The 24 Micron Source Counts in Deep Spitzer Surveys,”
  *Astrophysical Journal Supplement Series* **154**, 70 (2004):
  <https://doi.org/10.1086/422880>.
- H. Dole et al., “The Cosmic Infrared Background Resolved by Spitzer,”
  *Astronomy & Astrophysics* **451**, 417 (2006):
  <https://doi.org/10.1051/0004-6361:20054446>.
