from src.dominio import Usuario, Leilao
from src.excecoes import LanceInvalido
import pytest

@pytest.fixture
def arthur():
    return Usuario('arthur', 100.0)

@pytest.fixture
def leilao():
    return Leilao('celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(arthur,leilao):
    arthur.propoe_lance(leilao, 50.0)

    assert arthur.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(arthur,leilao):
    arthur.propoe_lance(leilao, 1.0)

    assert arthur.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_e_igual_ao_valor_da_carteira(arthur,leilao):
    arthur.propoe_lance(leilao, 100.0)

    assert arthur.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(arthur,leilao):
    with pytest.raises(LanceInvalido):
        arthur.propoe_lance(leilao, 200.0)
