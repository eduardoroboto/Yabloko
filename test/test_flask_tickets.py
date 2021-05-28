from time import sleep
#from test.test_flask import TestFlaskBase
from test_flask import flask_test


from flask import url_for

# class TestTicketAdicionar(TestFlaskBase):
class TestTicketAdicionar:
    def test_adicionar_deve_retornar_o_payload_igual_ao_enviado(self,flask_test):
        ticket_data = {'position': 1, 'subject': 'devolucao'}

        response = flask_test.client.post(url_for('tickets.adicionar'),json=ticket_data)
        print(response.json)
        assert 1 == response.json['id']
        assert ticket_data['position'] == response.json['position']
        assert ticket_data['subject'] == response.json['subject']


    def test_adicionar_deve_retornar_erro_quando_o_payload_for_incompleto(self, flask_test):
        ticket_data = {'subject': 'devolucao'}
        response = flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)

        return_data = {'position': ['Missing data for required field.']}


        assert return_data == response.json


    def test_adicionar_deve_retornar_erro_quando_o_payload_tiver_id(self, flask_test):
        ticket_data = {'id':1,'position': 1, 'subject': 'devolucao'}
        response = flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)

        return_data = {'id': ['Nao envie o id!']}

        assert  return_data == response.json

# class TestTicketMostrar(TestFlaskBase):
class TestTicketMostrar:
    def test_mostrar_deve_retornar_uma_query_vazia(self,flask_test):
        response = flask_test.client.get(url_for('tickets.mostrar'))

        assert [] == response.json

    def test_mostrar_deve_retornar_um_query_com_elemento_inserido(self,flask_test):
        ticket_data = {'position': 1, 'subject': 'devolucao'}

        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)
        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)

        response = flask_test.client.get(url_for('tickets.mostrar'))

        assert 2 == len(response.json)

# class TestTicketDeletar(TestFlaskBase):
class TestTicketDeletar:
    # def test_deletar_deve_retornar_deletado_quando_nao_encontrar_registro(self):
    #     response = self.client.get(url_for('tickets.deletar',identificador=1))
    #
    #     self.assertEqual(response.json, f"Ticket de id=1 deletado!!")

    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self,flask_test):
        ticket_data = {'position': 1, 'subject': 'devolucao'}

        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_data)

        response = flask_test.client.get(url_for('tickets.deletar', identificador=1))

        assert response.json == f"Ticket de id=1 deletado!!"

# class TestTicketModificar(TestFlaskBase):
class TestTicketModificar:
    def test_modificar_(self, flask_test):
        ticket_inicial = {'position': 1, 'subject': 'devolucao'}
        ticket_final = {'id':1,'position': 1, 'subject': 'preco_errado'}


        flask_test.client.post(url_for('tickets.adicionar'), json=ticket_inicial)

        response = flask_test.client.post(url_for('tickets.modificar',identificador=1,),json=ticket_final)

        assert ticket_final['id'] ==response.json['id']
        assert ticket_final['position'] == response.json['position']
        assert ticket_final['subject'] == response.json['subject']

#class TestTicketChangeDates(TestFlaskBase):
class TestTicketChangeDates:
    def test_modificar_start(self,flask_test):
        ticket = {'position': 1, 'subject': 'devolucao'}
        flask_test.client.post(url_for('tickets.adicionar'), json=ticket)

        sleep(2)
        response = flask_test.client.get(url_for('tickets.add_date_called',identificador=1))

        assert 1 == response.json['id']
        assert ticket['position'] == response.json['position']
        assert ticket['subject'] == response.json['subject']
        assert None != response.json['date_called']

    def test_modificar_end(self,flask_test):
        ticket = {'position': 1, 'subject': 'devolucao'}
        flask_test.client.post(url_for('tickets.adicionar'), json=ticket)

        sleep(2)
        response = flask_test.client.get(url_for('tickets.add_date_end',identificador=1,))

        assert 1 == response.json['id']
        assert ticket['position'] == response.json['position']
        assert ticket['subject'] ==response.json['subject']
        assert None != response.json['date_end']
