# from test.test_flask import TestFlaskBase
from test_flask import flask_test

from flask import url_for

# class TestHistoryAdicionar(TestFlaskBase):
class TestHistoryAdicionar:
    def test_adicionar_deve_retornar_o_payload_igual_ao_enviado(self,flask_test):
        ticket_data = {'position': 1, 'subject': 'devolucao'}
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)
        flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data = {'ticket_id': 1, 'clerk_id': 1}

        response = flask_test.client.post(url_for('history.adicionar'),json=history_data)
        #print("Response =>",response.json)
        assert 1 == response.json['id']
        assert history_data['ticket_id'] == response.json['ticket_id']
        assert history_data['clerk_id'] == response.json['clerk_id']



    def test_adicionar_deve_retornar_erro_quando_o_payload_for_incompleto(self,flask_test):

        ticket_data = {'position': 1, 'subject': 'devolucao'}
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)
        flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data = {'ticket_id': 1}

        response = flask_test.client.post(url_for('history.adicionar'),json=history_data)

        return_data = {'clerk_id': ['Missing data for required field.']}


        assert return_data == response.json


    def test_adicionar_deve_retornar_erro_quando_o_payload_tiver_id(self,flask_test):
        ticket_data = {'position': 1, 'subject': 'devolucao'}
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)
        flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data = {'id':1,'ticket_id': 1, 'clerk_id': 1}

        response = flask_test.client.post(url_for('history.adicionar'), json=history_data)

        return_data = {'id': ['Nao envie o id!']}

        assert return_data == response.json

# class TestHistoryMostrar(TestFlaskBase):
class TestHistoryMostrar:
    def test_mostrar_deve_retornar_uma_query_vazia(self,flask_test):
        response = flask_test.client.get(url_for('history.mostrar'))

        assert [] == response.json

    def test_mostrar_deve_retornar_um_query_com_elemento_inserido(self,flask_test):
        ticket_data_one = {'position': 1, 'subject': 'devolucao'}
        ticket_data_two = {'position': 2, 'subject': 'preco_trocado'}
        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data_one)
        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data_two)

        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data_one = {'ticket_id': 1, 'clerk_id': 1}
        history_data_two = {'ticket_id': 2, 'clerk_id': 1}
        flask_test.client.post(url_for('history.adicionar'), json=history_data_one)
        flask_test.client.post(url_for('history.adicionar'), json=history_data_two)

        response = flask_test.client.get(url_for('history.mostrar'))

        assert 2 == len(response.json)

# class TestHistoryDeletar(TestFlaskBase):
class TestHistoryDeletar:
    #def test_deletar_deve_retornar_deletado_quando_nao_encontrar_registro(self):

        # ticket_data_one = {'position': 1, 'subject': 'devolucao'}
        # ticket_data_two = {'position': 2, 'subject': 'preco_trocado'}
        # self.client.post(url_for('tickets.adicionar'), json=ticket_data_one)
        # self.client.post(url_for('tickets.adicionar'), json=ticket_data_two)
        #
        #
        # response = self.client.get(url_for('History.deletar',identificador=1))
        #
        # self.assertEqual(response.json, f"History de id=1 deletado!!")

    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self,flask_test):
        ticket_data = {'position': 1, 'subject': 'devolucao'}
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)
        flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data = {'ticket_id': 1, 'clerk_id': 1}
        flask_test.client.post(url_for('history.adicionar'), json=history_data)

        response = flask_test.client.get(url_for('history.deletar', identificador=1))

        assert response.json == f"History de id=1 deletado!!"

# class TestHistoryModificar(TestFlaskBase):
class TestHistoryModificar:
    def test_modificar_(self,flask_test):

        clerk_data_one = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        clerk_data_two = {'position': 1, 'name': 'lucas', 'subjects': 'devolucao'}
        flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data_one)
        flask_test.client.post(url_for('clerks.adicionar'), json=clerk_data_two)

        history_original = {'ticket_id': 1, 'clerk_id': 1}
        history_after = {'id':1,'ticket_id': 1, 'clerk_id': 2}
        flask_test.client.post(url_for('history.adicionar'), json=history_original)

        response = flask_test.client.post(url_for('history.modificar',identificador=1,),json=history_after)

        assert history_after['id'] == response.json['id']
        assert history_after['ticket_id'] == response.json['ticket_id']
        assert history_after['clerk_id'] == response.json['clerk_id']


