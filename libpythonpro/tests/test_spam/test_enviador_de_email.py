import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'jessica_is2@hotmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'jessica.lima6@gfatec.sp.gov.br',
        'Cursos Python Pro',
        'Primeira turma Luiz Vital aberta.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'jessica']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'jessica.lima6@gfatec.sp.gov.br',
            'Cursos Python Pro',
            'Primeira turma Luiz Vital aberta.'
        )
