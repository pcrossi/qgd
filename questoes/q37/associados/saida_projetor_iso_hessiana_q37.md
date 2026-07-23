# Saída — projetor isotrópico da Q37

Comando executado:

```bash
python3 questoes/q37/associados/calcular_projetor_iso_hessiana_q37.py
```

Saída:

```text
Q37 — PROJETOR ISOTRÓPICO COMO CONTRAÇÃO DA HESSIANA
normalização angular pi^-4        = 0.010265982254684
momento de Haar <(n.u)^4>          = 0.125000000000000
traço coerente Cartan-Schouten^2   = 9.000000000000000
P_iso calculado                    = 0.011549230036520
P_iso fechado 9/(8*pi^4)           = 0.011549230036520
diferença                          = 0.000e+00
alpha_mean                         = 0.007297348130032
alpha_mean^-1                      = 137.036082448164
Z_Q mean = 1/(4*pi*alpha_mean)      = 10.904984951787
```

Classificação:

$$
\boxed{
\text{avaliação direta de quantidade já derivada por simetria/Hessiana.}
}
$$

O script não ajusta $\alpha$ nem usa valor experimental. Ele apenas avalia o
projetor que resulta quando a Hessiana oficial projetada é escalar no setor
físico de quatro direções, como imposto pela média isotrópica do ensemble de
Einstein.

