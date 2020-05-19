from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'jessica_is2@hotmail.com',
        'jessica.lima6@gfatec.sp.gov.br',
        'Cursos Python Pro',
        'Primeira turma Luiz Vital aberta.'
    )
    assert 'jessica_is2@hotmail.com' in resultado