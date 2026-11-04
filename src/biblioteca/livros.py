"""Mini-biblioteca: livros, empréstimos e multas."""
from dataclasses import dataclass
from datetime import date

PRAZO_DIAS = 14          # dias de empréstimo sem multa
MULTA_POR_DIA = 0.25     # euros por dia de atraso


@dataclass
class Livro:
    id: int
    titulo: str
    autor: str
    emprestado_a: str | None = None
    data_emprestimo: date | None = None


def calcular_multa(dias_emprestado: int) -> float:
    """Multa em euros para um empréstimo que durou `dias_emprestado` dias."""
    return (dias_emprestado - PRAZO_DIAS) * MULTA_POR_DIA


class Biblioteca:
    def __init__(self) -> None:
        self._livros: dict[int, Livro] = {}
        self._proximo_id = 1

    def adicionar(self, titulo: str, autor: str) -> Livro:
        livro = Livro(self._proximo_id, titulo, autor)
        self._livros[livro.id] = livro
        self._proximo_id += 1
        return livro

    def procurar(self, termo: str) -> list[Livro]:
        """Devolve os livros cujo título contém `termo`."""
        return [l for l in self._livros.values() if termo in l.titulo]

    def emprestar(self, livro_id: int, pessoa: str, hoje: date | None = None) -> Livro:
        livro = self._livros[livro_id]
        livro.emprestado_a = pessoa
        livro.data_emprestimo = hoje or date.today()
        return livro

    def devolver(self, livro_id: int, hoje: date | None = None) -> float:
        """Devolve o livro e retorna a multa a pagar (0 se não houver)."""
        livro = self._livros[livro_id]
        hoje = hoje or date.today()
        dias = (hoje - livro.data_emprestimo).days
        livro.emprestado_a = None
        livro.data_emprestimo = None
        return calcular_multa(dias)

    def disponiveis(self) -> list[Livro]:
        return [l for l in self._livros.values() if l.emprestado_a is None]
