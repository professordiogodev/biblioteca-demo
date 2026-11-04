from biblioteca import Biblioteca


def test_adicionar_atribui_ids_sequenciais():
    b = Biblioteca()
    assert b.adicionar("Os Maias", "Eça de Queirós").id == 1
    assert b.adicionar("Mensagem", "Fernando Pessoa").id == 2


def test_procurar_por_titulo():
    b = Biblioteca()
    b.adicionar("Os Maias", "Eça de Queirós")
    assert len(b.procurar("Maias")) == 1
