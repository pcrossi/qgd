# Questão 61 — Aceleração cosmológica

## 1. Enunciado

A questão pede corrigir a divisão por \(2\pi\) indicada na seção anterior,
especialmente no capítulo legado:

```text
pt-br/32 - Fenomenologia Astrofísica e Cosmológica da GDQ.md
```

O problema é a mistura entre:

1. aceleração de horizonte de Hubble;
2. aceleração de horizonte de de Sitter;
3. projeção circular \(1/(2\pi)\);
4. valor fenomenológico de MOND.

---

## 2. Veredito

$$
\boxed{
\text{Q61 fechada como correção técnica da aceleração cosmológica.}
}
$$

A divisão por \(2\pi\) deve ser aplicada apenas depois de escolher
explicitamente qual horizonte está sendo usado.

Há duas escalas distintas:

$$
a_H
=
\frac{c^2}{R_H}
=
cH_0,
$$

e:

$$
a_{\rm dS}
=
\frac{c^2}{R_{\rm dS}}
=
c^2\sqrt{\frac{\Lambda}{3}}
=
cH_0\sqrt{\Omega_\Lambda}
\quad
\text{em FLRW plano}.
$$

Elas não devem ser identificadas automaticamente.

---

## 3. Correção da passagem legada

O texto legado fazia:

$$
a_{\rm dS}
\approx
5{,}46\times10^{-10}\,{\rm m/s^2},
$$

e depois afirmava:

$$
\frac{a_{\rm dS}}{2\pi}
\approx
1{,}21\times10^{-10}\,{\rm m/s^2}.
$$

Isso está aritmeticamente incorreto:

$$
\boxed{
\frac{5{,}46\times10^{-10}}{2\pi}
\approx
8{,}69\times10^{-11}\,{\rm m/s^2}.
}
$$

Usando os valores consolidados do cálculo Q57:

$$
\frac{cH_0\sqrt{\Omega_\Lambda}}{2\pi}
=
8{,}623833237863\times10^{-11}\,{\rm m/s^2}.
$$

Portanto, a forma de de Sitter projetada não é a rota correta para obter a
escala MOND.

---

## 4. Forma correta para a escala MOND/GDQ

Para a escala galáctica de baixa aceleração, a rota consolidada na Q57 usa o
mesmo contorno global da Q56:

$$
R_H=\frac{c}{H_0}.
$$

Assim:

$$
\boxed{
a_0^{\rm GDQ}
=
\frac{c^2}{2\pi R_H}
=
\frac{cH_0}{2\pi}.
}
$$

Com \(H_0=67{,}4\,{\rm km\,s^{-1}\,Mpc^{-1}}\):

$$
\boxed{
a_0^{\rm GDQ}
=
1{,}042197881145\times10^{-10}\,{\rm m/s^2}.
}
$$

Com escala local \(H_0=73\,{\rm km\,s^{-1}\,Mpc^{-1}}\):

$$
\boxed{
a_0^{\rm local}
=
1{,}128789989964\times10^{-10}\,{\rm m/s^2}.
}
$$

Essa é a forma que deve substituir a afirmação antiga quando o assunto for
curvas galácticas/MOND.

---

## 5. Como reescrever o capítulo 32

### 5.1 Remover

Remover a afirmação:

$$
a_{0,\rm ren}
=
\frac{c^2}{2\pi}
\sqrt{\frac{\Lambda}{3}}
\approx
1{,}21\times10^{-10}\,{\rm m/s^2}.
$$

Ela combina uma divisão correta com um resultado numérico incorreto.

### 5.2 Substituir por duas escalas

Escrever:

$$
a_{\rm dS}
=
c^2\sqrt{\frac{\Lambda}{3}},
$$

e:

$$
a_{\rm dS}^{(2\pi)}
=
\frac{c^2}{2\pi}
\sqrt{\frac{\Lambda}{3}}.
$$

Essa escala é cosmológica/de Sitter, não a constante MOND principal.

Separadamente, para o limite galáctico:

$$
a_0^{\rm GDQ}
=
\frac{cH_0}{2\pi}.
$$

### 5.3 Interpretação correta

A interpretação corrigida é:

$$
\boxed{
\text{a aceleração cosmológica fornece a escala global; a projeção circular fornece o limite galáctico.}
}
$$

Mas a escala usada depende do contorno:

| Contorno | Fórmula | Uso |
| --- | --- | --- |
| Hubble \(R_H=c/H_0\) | \(cH_0/(2\pi)\) | limite MOND/GDQ galáctico |
| de Sitter \(R_{\rm dS}=\sqrt{3/\Lambda}\) | \(c^2\sqrt{\Lambda/3}/(2\pi)\) | horizonte cosmológico assintótico |

---

## 6. Relação com Q56 e Q57

A Q56 fixa a energia escura como problema de contorno cosmológico global.

A Q57 fixa o limite MOND/GDQ:

$$
a_0^{\rm GDQ}
=
\frac{cH_0}{2\pi}.
$$

A Q61 apenas corrige a passagem editorial/técnica da aceleração cosmológica
para impedir que as duas escalas sejam misturadas.

---

## 7. Status final

Não há nova falta estrutural.

A conclusão é:

$$
\boxed{
\text{a divisão por \(2\pi\) está corrigida; a rota MOND/GDQ usa \(cH_0/(2\pi)\).}
}
$$

E a forma de de Sitter fica preservada apenas como escala cosmológica auxiliar:

$$
\boxed{
a_{\rm dS}^{(2\pi)}
=
\frac{cH_0\sqrt{\Omega_\Lambda}}{2\pi}
\approx
8{,}62\times10^{-11}\,{\rm m/s^2}.
}
$$

Assim:

$$
\boxed{
\text{Q61 fechada; Q57 permanece a referência canônica para \(a_0\).}
}
$$
