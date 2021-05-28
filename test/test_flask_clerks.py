#from test.test_flask import TestFlaskBase

from test_flask import flask_test
from flask import url_for

# class TestClerkAdicionar(TestFlaskBase):
class TestClerkAdicionar:
    def test_adicionar_deve_retornar_o_payload_igual_ao_enviado(self,flask_test):
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        response = flask_test.client.post(url_for('clerks.adicionar'),json=clerk_data)

        assert 1 == response.json['id']
        assert clerk_data['position'] == response.json['position']
        assert clerk_data['name'] == response.json['name']
        assert clerk_data['subjects'] == response.json['subjects']


    def test_adicionar_deve_retornar_erro_quando_o_payload_for_incompleto(self,flask_test):
        clerk_data = {'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        response = flask_test.client.post(url_for('clerks.adicionar'),json=clerk_data)

        return_data = {'position': ['Missing data for required field.']}

        assert return_data == response.json


    def test_adicionar_deve_retornar_erro_quando_o_payload_tiver_id(self,flask_test):
        clerk_data = {'id':1,'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        response = flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data)

        return_data = {'id': ['Nao envie o id!']}

        assert return_data == response.json

# class TestClerkMostrar(TestFlaskBase):
class TestClerkMostrar:
    def test_mostrar_deve_retornar_uma_query_vazia(self,flask_test):
        response = flask_test.client.get(url_for('clerks.mostrar'))

        assert [] == response.json

    def test_mostrar_deve_retornar_um_query_com_elemento_inserido(self,flask_test):
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        flask_test.client.post(url_for('clerks.adicionar'),json=clerk_data)
        flask_test.client.post(url_for('clerks.adicionar'),json=clerk_data)

        response = flask_test.client.get(url_for('clerks.mostrar'))

        assert 2 == len(response.json)

# class TestClerkDeletar(TestFlaskBase):
class TestClerkDeletar:

    # def test_deletar_deve_retornar_deletado_quando_nao_encontrar_registro(self):
    #     ...
    #
    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self,flask_test):
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data)


        response = flask_test.client.get(url_for('clerks.deletar', identificador=1))
        assert(response.json == f"Clerk de id=1 deletado!!")

# class TestClerkModificar(TestFlaskBase):
class TestClerkModificar():
    def test_modificar_(self,flask_test):
        clerk_inicial = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        clerk_final = {'id':1,'position': 2, 'name': 'lucas', 'subjects': 'devolucao'}

        flask_test.client.post(url_for('clerks.adicionar'),json=clerk_inicial)

        response = flask_test.client.post(url_for('clerks.modificar',identificador=1,),json=clerk_final)

        assert clerk_final['id'] == response.json['id']
        assert clerk_final['position'] == response.json['position']
        assert clerk_final['name'] == response.json['name']
        assert clerk_final['subjects'] == response.json['subjects']


