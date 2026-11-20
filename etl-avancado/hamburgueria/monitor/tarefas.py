"""
Registro dos projetos. Rodar a partir da pasta monitor/:  python tarefas.py
Painel: http://localhost:8000

O ETL da hamburgueria roda manualmente em modo incremental. Para alterar a carga,
troque o argumento para "full".
"""
import os

from monitor import projeto, servir

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_ETL = os.path.join(RAIZ, "etl_hamburgueria")

projeto(
    PASTA_ETL,
    nome="ETL Hamburgueria",
    modulo="src.etl",
    args=("full",),
)

if __name__ == "__main__":
    servir(porta=8000)
