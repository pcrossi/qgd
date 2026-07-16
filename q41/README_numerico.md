# Q41 — Testes numéricos do poço

Esta pasta testa a impedância variacional derivada em
`q41/adendo_impedancia_parede_gdq.md`.

O script `solve_poco_gdq.py` compara:

1. o espectro obtido pelo mapa Dirichlet–Neumann da parede;
2. a diagonalização direta da barreira finita;
3. o resultado padrão do poço infinito.

Execução:

```bash
python3 Q41/solve_poco_gdq.py
```

O relatório é salvo em `Q41/resultado_poco_gdq.md`.

Os valores padrão são adimensionais:

\[
L=1,
\qquad
\frac{\hbar^2}{2mL^2}=1,
\qquad
V_0=1000,
\qquad
d=0.25L.
\]

Esse teste compara a redução GDQ com a mecânica quântica padrão. Uma previsão
material exige calcular os coeficientes da Hessiana para uma parede física.
