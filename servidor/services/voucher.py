import asyncio

from servidor.bd.bd import banco

class Vouchers():
    
    def __init__(self):
        pass

    def cadastrarVoucher(self, titulo, descricao, gato, local, lanche, duracao, titular_id):
        imagem = str(gato[0].lower())
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(banco.inserir_voucher(titulo, descricao, gato, local, lanche, int(duracao), imagem, int(titular_id)))
        loop.close()

        return "1"

    def apresentarVouchersUsuario(self, id):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        vouchers = loop.run_until_complete(banco.ver_vouchers_usuario(id))
        loop.close()

        v = {}
        for i in range(len(vouchers)):
            v[i] = {
                "id":vouchers[i].id,
                "titulo":vouchers[i].titulo,
                "descricao":vouchers[i].descricao,
                "gato":vouchers[i].gato,
                "local":vouchers[i].local,
                "lanche":vouchers[i].lanche,
                "duracao":vouchers[i].duracao,
                "imagem":vouchers[i].imagem,
                "titular_id":vouchers[i].titular_id,
            }

        return v

    def apresentarVouchers(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        vouchers = loop.run_until_complete(banco.ver_vouchers())
        loop.close()

        v = {}
        for i in range(len(vouchers)):
            v[i] = {
                "id":vouchers[i].id,
                "titulo":vouchers[i].titulo,
                "descricao":vouchers[i].descricao,
                "gato":vouchers[i].gato,
                "local":vouchers[i].local,
                "lanche":vouchers[i].lanche,
                "duracao":vouchers[i].duracao,
                "imagem":vouchers[i].imagem,
                "titular_id":vouchers[i].titular_id,
            }

        return v

if __name__ == '__main__':
    pass
