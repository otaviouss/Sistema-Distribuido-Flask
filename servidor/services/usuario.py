import asyncio

from servidor.bd.bd import banco

class Clientes():

    def __init__(self):
        pass

    def cadastrarCliente(self, email, nome, senha):
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(banco.inserir_usuario(email, nome, senha))
            loop.close()

            return "1"
        except:
            return "0"

    def checarCliente(self, email, senha):

        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            user = loop.run_until_complete(banco.ver_usuario(email, senha))
            loop.close()

            if user is None: return "0"

            return str(user.id)
        except:
            return "0"

if __name__ == '__main__':
    pass
