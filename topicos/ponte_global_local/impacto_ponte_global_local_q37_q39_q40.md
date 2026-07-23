# Impacto da ponte global--local nas Questões 37, 39 e 40

## 1. Escopo

Este documento aplica `topicos/ponte_global_local/ponte_global_local_lemas_sem_colar.md` e
`topicos/ponte_global_local/ponte_global_local_fechamento_c3.md` às Questões 37, 39 e 40, respeitando a
separação do Lema 6:

$$
\text{topologia e clusters ligados}
\neq
\text{normalizações contínuas de acoplamentos}.
$$

No background estacionário de três caps gaussianos, com fechamento de
Noether e simetria $C_3$, a Hessiana física possui

$$
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}>0,
$$

e, na normalização primitiva da Q28, $\Delta_0=1/2$. Isso permite transportar
o cluster $C_3$ por convergência apontada, resolventes e projetores de Riesz.
Não existe uma interface física adicional entre o espaço cosmológico e sua
carta local; DtN permanece somente no bordo físico do estômato.

## 2. Q39 — massas leptônicas

A objeção de incompatibilidade abstrata entre $T^5\times S^3$ e
$\mathbb R^4\times T^4$ deixa de valer. A multiplicidade $C_3$ e a seleção
topológica de três setores são transportadas, e uma perturbação local menor
que o gap não cria nem destrói um setor.

Entretanto, o operador de Rosen--Morse seleciona $n=0,1,17$, enquanto o gap
demonstrado é o da Hessiana gaussiana projetada do background $C_3$. Ainda é
necessário mostrar que esses níveis formam o cluster comprimido da Hessiana
física, ou demonstrar diretamente localização uniforme e um contorno
espectral isolante comum para o operador leptônico ao longo da família
apontada.

A ponte preserva razões de autovalores sob um fator dimensional comum, mas
não cria a escala absoluta.

$$
\boxed{
\text{Q39 fechada no modelo global; multiplicidade }C_3\text{ transportada;
cluster }(0,1,17)\text{ ainda condicional.}
}
$$

## 3. Q40 — próton e nêutron

O objeto bariônico é explicitamente trimodal e constituído por três
estômatos. Portanto, o fechamento $C_3$ sustenta no limite local:

1. a persistência do setor trimodal;
2. a remoção da rotação comum por Noether;
3. a positividade da Hessiana projetada no setor que preserva os vínculos;
4. a estabilidade contra perturbações menores que $\Delta_0$;
5. a herança de inteiros topológicos, holonomias e multiplicidades.

Isso elimina a pendência global--local do background de três centros. O
teorema não deriva automaticamente coeficientes dimensionais de massa, raio,
momentos magnéticos ou fatores de forma. Em particular, $6\pi^5$ ainda
depende de sua derivação própria como integral reduzida da ação oficial.

$$
\boxed{
\text{Q40 permanece fechada estruturalmente; a pendência global--local do
setor }C_3\text{ foi eliminada.}
}
$$

## 4. Q37 — constante de estrutura fina

A utilização de $T^5\times S^3$ para dados globais já não é incompatível,
por si só, com o bulk local: a família apontada fornece o mapa geométrico até
$\mathbb R^4\times T^4$, sem alterar a ação ou inventar uma interface.

Como $\alpha$ é uma normalização contínua, era necessário demonstrar sob quais
condições ela é transportada. O documento
`topicos/ponte_global_local/teorema_heranca_normalizacao_eletromagnetica.md` demonstrou a implicação
correta:

1. o gerador elétrico é a direção interna primitiva $U(1)_Q$, não a corrente
   global de fase de Madelung;
2. $Z_Q$ é o coeficiente da corrente simplética da Hessiana efetiva do modo;
3. convergência das formas, sincronização temporal e ausência de fuga implicam
   $Z_Q^{\rm lab}=Z_Q^E$; para um modo ligado usam-se gap e projetores, e para
   um canal massless usam-se DtN ou espalhamento normalizado por fluxo.

Em particular,

$$
\boxed{
\alpha_{\rm lab}=\alpha_E.
}
$$

Não é necessário recalcular a normalização no bulk local depois de verificar
a hipótese de transporte apropriada. Continua sendo necessário calcular, uma
única vez no background global, a quantidade

$$
\frac1{e_{\rm loc}^2}
=\lim_{\varepsilon\to0}
\left\langle
\Phi_{Q,\varepsilon},
K_{Q,\varepsilon}^{\rm eff}\Phi_{Q,\varepsilon}
\right\rangle,
$$

com

$$
K_Q^{\rm eff}
=K_{QQ}-K_{Q\perp}K_{\perp\perp}^{-1}K_{\perp Q},
$$

e então $\alpha_E=e_E^2/(4\pi\hbar c)$. A ponte transporta esse valor; não o
produz.

$$
\boxed{
\text{Q37 tem a compatibilidade resolvida e um teorema condicional de herança;}\\
\alpha_E\text{ permanece aberta na avaliação global e na verificação do canal.}
}
$$

## 5. Síntese

| Questão | Impacto da ponte | Pendência remanescente |
|---|---|---|
| Q39 | transporta multiplicidade e identidade $C_3$ | transportar o cluster $n=0,1,17$ |
| Q40 | fecha a compatibilidade do background trimodal | normalizações contínuas e fenomenologia local |
| Q37 | transporta a geometria e fornece o critério de herança de $Z_Q$ | avaliar $Z_Q^E$ e verificar canal localizado ou massless sem fuga |

Próxima ação de maior rendimento: Q37, avaliando uma única vez o complemento
de Schur da Hessiana oficial no background global. Q39 exige uma verificação
espectral delimitada; Q40 não deve ser reaberta por causa da ponte.
