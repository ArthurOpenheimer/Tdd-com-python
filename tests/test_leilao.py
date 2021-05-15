from unittest import TestCase
from src.dominio import Usuario,Lance, Leilao
from src.excecoes import LanceInvalido




class TestLeilao(TestCase):

    def setUp(self):
        self.arthur = Usuario('arthur', 500.0)
        self.lance_do_arthur = Lance(self.arthur, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        pedro = Usuario('pedro', 500.0)
        lance_do_pedro = Lance(pedro, 100.0)

        self.leilao.propoe(lance_do_pedro)
        self.leilao.propoe(self.lance_do_arthur)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            pedro = Usuario('pedro', 500.0)
            lance_do_pedro = Lance(pedro, 100.0)

            self.leilao.propoe(self.lance_do_arthur)
            self.leilao.propoe(lance_do_pedro)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_arthur)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        pedro = Usuario('pedro', 500.0)
        lance_do_pedro = Lance(pedro, 100.0)
        vini = Usuario('vini', 500.0)

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(lance_do_pedro)
        self.leilao.propoe(self.lance_do_arthur)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_arthur)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        pedro = Usuario('pedro', 500.0)
        lance_do_pedro = Lance(pedro, 200.0)

        self.leilao.propoe(self.lance_do_arthur)
        self.leilao.propoe(lance_do_pedro)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_arthur200 = Lance(self.arthur, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_arthur)
            self.leilao.propoe(lance_do_arthur200)
