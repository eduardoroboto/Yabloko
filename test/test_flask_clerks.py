from test.test_flask import TestFlaskBase
from flask import url_for


class TestClerkAdicionar(TestFlaskBase):
    def test_adicionar_deve_retornar_o_payload_igual_ao_enviado(self):
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}

        response = self.client.post(url_for('clerks.adicionar'),json=clerk_data)

        self.assertEqual(1, response.json['id'])
        self.assertEqual(clerk_data['position'], response.json['position'])
        self.assertEqual(clerk_data['name'], response.json['name'])
        self.assertEqual(clerk_data['subjects'], response.json['subjects'])


    def test_adicionar_deve_retornar_erro_quando_o_payload_for_incompleto(self):
        clerk_data = {'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        response = self.client.post(url_for('clerks.adicionar'),json=clerk_data)

        return_data = {'position': ['Missing data for required field.']}

        self.assertEqual(return_data, response.json)


    def test_adicionar_deve_retornar_erro_quando_o_payload_tiver_id(self):
        clerk_data = {'id':1,'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        response = self.client.post(url_for('clerks.adicionar'), json=clerk_data)

        return_data = {'id': ['Nao envie o id!']}

        self.assertEqual(return_data, response.json)

class TestClerkMostrar(TestFlaskBase):
    def test_mostrar_deve_retornar_uma_query_vazia(self):
        response = self.client.get(url_for('clerks.mostrar'))

        self.assertEqual([], response.json)

    def test_mostrar_deve_retornar_um_query_com_elemento_inserido(self):
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        self.client.post(url_for('clerks.adicionar'),json=clerk_data)
        self.client.post(url_for('clerks.adicionar'),json=clerk_data)

        response = self.client.get(url_for('clerks.mostrar'))

        self.assertEqual(2,len(response.json))


class TestClerkDeletar(TestFlaskBase):

    # def test_deletar_deve_retornar_deletado_quando_nao_encontrar_registro(self):
    #     ...
    #
    def test_deletar_deve_retornar_deletado_quando_encontrar_registro_na_base(self):
        clerk_data = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        self.client.post(url_for('clerks.adicionar'), json=clerk_data)


        response = self.client.get(url_for('clerks.deletar', identificador=1))
        self.assertEqual(response.json, f"Clerk de id=1 deletado!!")


class TestClerkModificar(TestFlaskBase):
    def test_modificar_(self):
        clerk_inicial = {'position': 1, 'name': 'eduardo', 'subjects': 'devolucao;preco_trocado'}
        clerk_final = {'id':1,'position': 2, 'name': 'lucas', 'subjects': 'devolucao'}

        self.client.post(url_for('clerks.adicionar'),json=clerk_inicial)

        response = self.client.post(url_for('clerks.modificar',identificador=1,),json=clerk_final)

        self.assertEqual(clerk_final['id'], response.json['id'])
        self.assertEqual(clerk_final['position'], response.json['position'])
        self.assertEqual(clerk_final['name'], response.json['name'])
        self.assertEqual(clerk_final['subjects'], response.json['subjects'])


