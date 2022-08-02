import json
import requests

class Cliente():

    def __init__(self):
        self.user_id = -1
        pass

    def solicitarCriarUsuario(self, nome, email, senha):

        response = requests.get('http://127.0.0.1:5000/cadastrarCliente?email='+email+'&nome='+nome+'&senha='+senha)

        if(json.loads(response.text) == "1"):
            print("Sucesso!")
            self.realizarLogin(email, senha)
        else:
            print("Falha! Email já utilizado.")

    def realizarLogin(self, email, senha):

        response = requests.get('http://127.0.0.1:5000/checarCliente?email='+email+'&senha='+senha)

        if(json.loads(response.text) != "0"):
            self.user_id = int(json.loads(response.text))
            print("Logado com Sucesso! UID: ", self.user_id)
            return 1
        else:
            print("Falha ao Logar!")
            return 0
    
    def cadastrarVoucher(self, titulo, descricao, gato, local, lanche, duracao):

        response = requests.get('http://127.0.0.1:5000/cadastrarVoucher?titulo='+titulo+'&descricao='+descricao+'&gato='+gato+'&local='+local+'&lanche='+lanche+'&duracao='+str(duracao)+'&titular_id='+str(self.user_id))

        print("Cadastrando Voucher")

        return json.loads(response.text)
    
    def apresentarVouchersUsuario(self):

        response = requests.get('http://127.0.0.1:5000/apresentarVouchersUsuario?id='+str(self.user_id))

        print("Apresentando vouchers do usuário logado.")

        return json.loads(response.text)
    
    def apresentarVouchers(self):

        response = requests.get('http://127.0.0.1:5000/apresentarVouchers')

        print("Apresentando todos os vouchers.")

        return json.loads(response.text)

    def apresentarTrocas(self):

        response = requests.get('http://127.0.0.1:5000/apresentarTrocas?id_troca='+str(self.user_id))

        print("Apresentando todas as trocas pendentes.")

        return json.loads(response.text)

    def proporTroca(self, id_voucher1, id_voucher2):

        response = requests.get(('http://127.0.0.1:5000/proporTroca?id1='+str(id_voucher1)+'&id2='+str(id_voucher2)))

        print("Propondo Troca")

        return json.loads(response.text)

    def realizarTroca(self, id_troca):

        response = requests.get('http://127.0.0.1:5000/realizarTroca?id_troca='+str(id_troca))

        print("Troca Aceita")

        return json.loads(response.text)

    def negarTroca(self, id_troca):

        response = requests.get('http://127.0.0.1:5000/negarTroca?id_troca='+str(id_troca))

        print("Troca Negada")

        return json.loads(response.text)
    
    def deslogar(self):
        self.user_id = -1
        return 1

def main():
    c = Cliente()
    c.solicitarCriarUsuario(email="teste", nome="AAA", senha="123")	
    c.realizarLogin("marta@gmail.com", "123")
    c.cadastrarVoucher(titulo="hahah", descricao="hehehe", gato="GT", local="LC", lanche="LA", duracao=10)
    c.proporTroca(id_voucher1=2, id_voucher2=4)
    c.realizarTroca(id_troca=1)
    c.negarTroca(id_troca=2)
    c.apresentarVouchers()
    c.apresentarTrocas()
    c.realizarLogin("lsls", "123")

if __name__ == '__main__':
    main()
