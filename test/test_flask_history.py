from test.test_flask import TestFlaskBase
from flask import url_for


class TestHistoryAdicionar(TestFlaskBase):
    def test_adicionar_deve_retornar_o_payload_igual_ao_enviado(self):
        ticket_data = {'position': 1, 'subject': 'devolucao'}
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        self.client.post(url_for('tickets.adicionar'), json=ticket_data)
        self.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data = {'ticket_id': 1, 'clerk_id': 1}

        response = self.client.post(url_for('history.adicionar'),json=history_data)
        #print("Response =>",response.json)
        self.assertEqual(1, response.json['id'])
        self.assertEqual(history_data['ticket_id'], response.json['ticket_id'])
        self.assertEqual(history_data['clerk_id'], response.json['clerk_id'])



    def test_adicionar_deve_retornar_erro_quando_o_payload_for_incompleto(self):
        ticket_data = {'position': 1, 'subject': 'devolucao'}
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        self.client.post(url_for('tickets.adicionar'), json=ticket_data)
        self.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data = {'ticket_id': 1}

        response = self.client.post(url_for('history.adicionar'),json=history_data)

        return_data = {'clerk_id': ['Missing data for required field.']}


        self.assertEqual(return_data, response.json)


    def test_adicionar_deve_retornar_erro_quando_o_payload_tiver_id(self):
        ticket_data = {'position': 1, 'subject': 'devolucao'}
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        self.client.post(url_for('tickets.adicionar'), json=ticket_data)
        self.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data = {'id':1,'ticket_id': 1, 'clerk_id': 1}

        response = self.client.post(url_for('history.adicionar'), json=history_data)

        return_data = {'id': ['Nao envie o id!']}

        self.assertEqual(return_data, response.json)

class TestHistoryMostrar(TestFlaskBase):
    def test_mostrar_deve_retornar_uma_query_vazia(self):
        response = self.client.get(url_for('history.mostrar'))

        self.assertEqual([],response.json)

    def test_mostrar_deve_retornar_um_query_com_elemento_inserido(self):
        ticket_data_one = {'position': 1, 'subject': 'devolucao'}
        ticket_data_two = {'position': 2, 'subject': 'preco_trocado'}
        self.client.post(url_for('tickets.adicionar'), json=ticket_data_one)
        self.client.post(url_for('tickets.adicionar'), json=ticket_data_two)

        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        self.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data_one = {'ticket_id': 1, 'clerk_id': 1}
        history_data_two = {'ticket_id': 2, 'clerk_id': 1}
        self.client.post(url_for('history.adicionar'), json=history_data_one)
        self.client.post(url_for('history.adicionar'), json=history_data_two)

        response = self.client.get(url_for('history.mostrar'))

        self.assertEqual(2,len(response.json))

class TestHistoryDeletar(TestFlaskBase):
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

    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self):
        ticket_data = {'position': 1, 'subject': 'devolucao'}
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        self.client.post(url_for('tickets.adicionar'), json=ticket_data)
        self.client.post(url_for('clerks.adicionar'), json=clerk_data)

        history_data = {'ticket_id': 1, 'clerk_id': 1}
        self.client.post(url_for('history.adicionar'), json=history_data)

        response = self.client.get(url_for('history.deletar', identificador=1))

        self.assertEqual(response.json, f"History de id=1 deletado!!")


class TestHistoryModificar(TestFlaskBase):
    def test_modificar_(self):

        clerk_data_one = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        clerk_data_two = {'position': 1, 'name': 'lucas', 'subjects': 'devolucao'}
        self.client.post(url_for('clerks.adicionar'), json=clerk_data_one)
        self.client.post(url_for('clerks.adicionar'), json=clerk_data_two)

        history_original = {'ticket_id': 1, 'clerk_id': 1}
        history_after = {'id':1,'ticket_id': 1, 'clerk_id': 2}
        self.client.post(url_for('history.adicionar'), json=history_original)

        response = self.client.post(url_for('history.modificar',identificador=1,),json=history_after)

        self.assertEqual(history_after['id'], response.json['id'])
        self.assertEqual(history_after['ticket_id'], response.json['ticket_id'])
        self.assertEqual(history_after['clerk_id'], response.json['clerk_id'])


