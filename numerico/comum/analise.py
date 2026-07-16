"""
GDQ — Utilitários de Análise Numérica e Exportação
Este módulo implementa ferramentas para estudar a convergência de malha (grid convergence)
e gerar tabelas formatadas em Markdown/LaTeX para o manuscrito.
"""

import numpy as np

def study_convergence(solve_func, N_list=[800, 1600, 3200, 6400]):
    """
    Executa um estudo de convergência de malha para a função de resolução solver_func.
    
    Parâmetros:
    -----------
    solve_func : callable
        Função que aceita N e retorna uma tupla ou lista de autovalores/observáveis.
    N_list : list of int
        Tamanhos de malha a serem testados.
        
    Retorna:
    --------
    dict
        Dicionário com os resultados mapeados por N.
    """
    results = {}
    for N in N_list:
        results[N] = solve_func(N)
    return results

def format_markdown_table(headers, rows, precisions=None):
    """
    Gera uma string contendo uma tabela Markdown formatada de forma alinhada.
    
    Parâmetros:
    -----------
    headers : list of str
        Títulos das colunas.
    rows : list of list
        Valores de cada linha.
    precisions : list of int (opcional)
        Precisão de casas decimais para colunas numéricas.
    """
    col_widths = [len(h) for h in headers]
    
    # Primeiro calcula as larguras máximas
    formatted_rows = []
    for r in rows:
        formatted_r = []
        for i, val in enumerate(r):
            if isinstance(val, float):
                prec = precisions[i] if (precisions and i < len(precisions)) else 6
                s_val = f"{val:.{prec}f}"
            else:
                s_val = str(val)
            col_widths[i] = max(col_widths[i], len(s_val))
            formatted_r.append(s_val)
        formatted_rows.append(formatted_r)
        
    lines = []
    # Header
    header_line = " | ".join(f"{h:{col_widths[i]}s}" for i, h in enumerate(headers))
    lines.append("| " + header_line + " |")
    # Separator
    sep_line = " | ".join("-" * w for w in col_widths)
    lines.append("| " + sep_line + " |")
    # Rows
    for r in formatted_rows:
        row_line = " | ".join(f"{val:{col_widths[i]}s}" for i, val in enumerate(r))
        lines.append("| " + row_line + " |")
        
    return "\n".join(lines)
