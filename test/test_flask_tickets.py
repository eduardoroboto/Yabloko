from time import sleep
from test.test_flask import TestFlaskBase
from flask import url_for


class TestTicketAdicionar(TestFlaskBase):
    def test_adicionar_deve_retornar_o_payload_igual_ao_enviado(self):
        ticket_data = {'position': 1, 'subject': 'devolucao'}

        response = self.client.post(url_for('tickets.adicionar'),json=ticket_data)
        print(response.json)
        self.assertEqual(1, response.json['id'])
        self.assertEqual(ticket_data['position'], response.json['position'])
        self.assertEqual(ticket_data['subject'], response.json['subject'])


    def test_adicionar_deve_retornar_erro_quando_o_payload_for_incompleto(self):
        ticket_data = {'subject': 'devolucao'}
        response = self.client.post(url_for('tickets.adicionar'), json=ticket_data)

        return_data = {'position': ['Missing data for required field.']}


        self.assertEqual(return_data, response.json)


    def test_adicionar_deve_retornar_erro_quando_o_payload_tiver_id(self):
        ticket_data = {'id':1,'position': 1, 'subject': 'devolucao'}
        response = self.client.post(url_for('tickets.adicionar'), json=ticket_data)

        return_data = {'id': ['Nao envie o id!']}

        self.assertEqual(return_data, response.json)

class TestTicketMostrar(TestFlaskBase):
    def test_mostrar_deve_retornar_uma_query_vazia(self):
        response = self.client.get(url_for('tickets.mostrar'))

        self.assertEqual([],response.json)

    def test_mostrar_deve_retornar_um_query_com_elemento_inserido(self):
        ticket_data = {'position': 1, 'subject': 'devolucao'}

        self.client.post(url_for('tickets.adicionar'), json=ticket_data)
        self.client.post(url_for('tickets.adicionar'), json=ticket_data)

        response = self.client.get(url_for('tickets.mostrar'))

        self.assertEqual(2,len(response.json))

class TestTicketDeletar(TestFlaskBase):
    # def test_deletar_deve_retornar_deletado_quando_nao_encontrar_registro(self):
    #     response = self.client.get(url_for('tickets.deletar',identificador=1))
    #
    #     self.assertEqual(response.json, f"Ticket de id=1 deletado!!")

    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self):
        ticket_data = {'position': 1, 'subject': 'devolucao'}

        self.client.post(url_for('tickets.adicionar'), json=ticket_data)

        response = self.client.get(url_for('tickets.deletar', identificador=1))

        self.assertEqual(response.json, f"Ticket de id=1 deletado!!")


class TestTicketModificar(TestFlaskBase):
    def test_modificar_(self):
        ticket_inicial = {'position': 1, 'subject': 'devolucao'}
        ticket_final = {'id':1,'position': 1, 'subject': 'preco_errado'}


        self.client.post(url_for('tickets.adicionar'), json=ticket_inicial)

        response = self.client.post(url_for('tickets.modificar',identificador=1,),json=ticket_final)

        self.assertEqual(ticket_final['id'], response.json['id'])
        self.assertEqual(ticket_final['position'], response.json['position'])
        self.assertEqual(ticket_final['subject'], response.json['subject'])

class TestTicketChangeDates(TestFlaskBase):
    def test_modificar_start(self):
        ticket = {'position': 1, 'subject': 'devolucao'}
        self.client.post(url_for('tickets.adicionar'), json=ticket)

        sleep(2)
        response = self.client.post(url_for('tickets.add_date_called',identificador=1,))

        self.assertEqual(1, response.json['id'])
        self.assertEqual(ticket['position'], response.json['position'])
        self.assertEqual(ticket['subject'], response.json['subject'])
        self.assertNotEqual(None,response.json['date_called'])

    def test_modificar_end(self):
        ticket = {'position': 1, 'subject': 'devolucao'}
        self.client.post(url_for('tickets.adicionar'), json=ticket)

        sleep(2)
        response = self.client.post(url_for('tickets.add_date_end',identificador=1,))

        self.assertEqual(1, response.json['id'])
        self.assertEqual(ticket['position'], response.json['position'])
        self.assertEqual(ticket['subject'], response.json['subject'])
        self.assertNotEqual(None,response.json['date_end'])
