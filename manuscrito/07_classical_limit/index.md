---
title: "07. O limite clássico e o princípio da correspondência"
---

# 07. O limite clássico e o princípio da correspondência

Uma teoria da matéria não está completa apenas porque descreve fenômenos
microscópicos. Ela também precisa explicar por que corpos macroscópicos podem
ser tratados por trajetórias, por que a ação de Hamilton--Jacobi reaparece e
em que condições a interferência deixa de dominar o movimento observado.

O limite clássico da GDQ não será apresentado como a substituição formal de
$\hbar$ por zero. A constante $\hbar$ não muda quando passamos de um elétron a
um planeta. O que muda é uma razão adimensional: a escala de variação da fase
torna-se muito menor que a escala de variação da amplitude e dos campos
externos. Nessa situação, a correção de Bohm torna-se pequena diante da
energia cinética e a equação de Hamilton--Jacobi clássica governa a fase.

O capítulo parte do setor de Madelung identificado nos Capítulos 5 e 6. Essa
escolha é importante: a ação oficial possui um espaço de Cauchy maior, e a
mecânica quântica hidrodinâmica é uma polarização física desse espaço. Assim,
o resultado demonstrado aqui é um teorema de correspondência **dentro desse
setor**, não uma afirmação de que toda solução off shell da GDQ seja clássica
ou quântica no sentido usual.

## Roteiro

- [[07.1 - O que significa tomar o limite clássico]]
- [[07.2 - O sistema Hamilton–Jacobi–Bohm de partida]]
- [[07.3 - O parâmetro adimensional que controla o limite]]
- [[07.4 - Da equação quântica à Hamilton–Jacobi clássica]]
- [[07.5 - Das frentes de fase às trajetórias de Newton]]
- [[07.6 - Continuidade, ensemble e equação de Liouville]]
- [[07.7 - WKB, fase estacionária e cáusticas]]
- [[07.8 - Do potencial cotangente global ao potencial de Kepler]]
- [[07.9 - Noether e as constantes do movimento clássico]]
- [[07.10 - Torção, campos clássicos e alcance da correspondência]]
- [[07.11 - Correspondência eletromagnética macroscópica]]
- [[07.12 - Correspondência métrica e gravitação clássica]]

## Resultado central

Se $R=\sqrt\rho$ varia numa escala $L_\rho$, se o momento típico é
$p=|\nabla S_R|$ e se

$$
\varepsilon_{\rm cl}
=\frac{\hbar}{pL_\rho}
\ll1,
$$

então, em regiões sem nós e antes da formação de cáusticas,

$$
\frac{|Q_B|}{T_{\rm cl}}
=O(\varepsilon_{\rm cl}^2),
$$

e a equação de Hamilton--Jacobi--Bohm reduz-se à de Hamilton--Jacobi
clássica. Suas características satisfazem as equações de Hamilton e, para
$H=p^2/(2m)+V$, a segunda lei de Newton.

O limite é controlado e possui domínio de validade explícito. Ele não exige
uma rotação de Wick reversa: o tempo físico já foi selecionado e transportado
pela reconstrução causal e pela ponte global--local.

Depois da prova escalar, o capítulo incorpora também os setores vetorial e
métrico. Essas passagens não são deduzidas novamente da equação de
Hamilton--Jacobi: usam as conexões, as simetrias, a torção e a resposta
métrica já construídas nos capítulos anteriores, explicitando as hipóteses
necessárias para obter Maxwell e Einstein como correspondências
macroscópicas.

## Controle editorial

- [[checklist_operacional|Checklist operacional do capítulo]]
- [[notes/provas_lemas_definicoes|Provas, lemas e definições associados]]
- [[scripts/README|Scripts opcionais autocontidos]]

[[../index|← Home]] | [[07.1 - O que significa tomar o limite clássico|Next →]]
