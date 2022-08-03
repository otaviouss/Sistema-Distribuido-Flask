from servidor import app
from flask import jsonify, request

from servidor.services.troca import Trocas
from servidor.services.usuario import Clientes
from servidor.services.voucher import Vouchers

@app.get("/apresentarTrocas")
def apresentarTrocas():
    id_troca = str(request.args.get('id_troca'))
    trocas = Trocas()
    response = trocas.apresentarTrocas(id_troca)
    return jsonify(response), 200


@app.get('/proporTroca')
def proporTroca():
    id1 = str(request.args.get('id1'))
    id2 = str(request.args.get('id2'))
    trocas = Trocas()
    response = trocas.proporTroca(id1, id2)
    return jsonify(response), 200

@app.get('/realizarTroca')
def realizarTroca():
    id_troca = str(request.args.get('id_troca'))
    trocas = Trocas()
    response = trocas.realizarTroca(id_troca)
    return jsonify(response), 200

@app.get('/negarTroca')
def negarTroca():
    id_troca = str(request.args.get('id_troca'))
    trocas = Trocas()
    response = trocas.negarTroca(id_troca)
    return jsonify(response), 200

@app.get('/cadastrarCliente')
def cadastrarCliente():
    email = str(request.args.get('email'))
    nome = str(request.args.get('nome'))
    senha = str(request.args.get('senha'))
    cliente = Clientes()
    response = cliente.cadastrarCliente(email, nome, senha)
    return jsonify(response), 200

@app.get('/checarCliente')
def checarCliente():
    email = str(request.args.get('email'))
    senha = str(request.args.get('senha'))
    cliente = Clientes()
    response = cliente.checarCliente(email, senha)
    return jsonify(response), 200

@app.get('/cadastrarVoucher')
def cadastrarVoucher():
    titulo = str(request.args.get('titulo'))
    descricao = str(request.args.get('descricao'))
    gato = str(request.args.get('gato'))
    local = str(request.args.get('local'))
    lanche = str(request.args.get('lanche'))
    duracao = str(request.args.get('duracao'))
    titular_id = str(request.args.get('titular_id'))
    voucher = Vouchers()
    response = voucher.cadastrarVoucher(titulo, descricao, gato, local, lanche, duracao, titular_id)
    return jsonify(response), 200

@app.get('/apresentarVouchersUsuario')
def apresentarVouchersUsuario():
    id = str(request.args.get('id'))
    voucher = Vouchers()
    response = voucher.apresentarVouchersUsuario(int(id))
    return jsonify(response), 200

@app.get('/apresentarVouchers')
def apresentarVouchers():
    voucher = Vouchers()
    response = voucher.apresentarVouchers()
    return jsonify(response), 200
