from python.utils import validar_cpf, buscar_usuario

def saque(*, saldo, valor, limite, numero_saques, limite_saques):    
    try:
        valor = float(valor)
    except ValueError:
        return None, "Operação falhou! Digite um valor numérico válido."
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        return None, "Operação falhou! Você não tem saldo suficiente."

    if excedeu_limite:
        return None, "Operação falhou! O valor do saque excede o limite."

    if excedeu_saques:
        return None, "Operação falhou! Número máximo de saques excedido."

    if valor <= 0:
        return None, "Operação falhou! O valor informado é inválido."

    saldo -= valor
    extrato = f"Saque de: R$ {valor:.2f}"
    return saldo, extrato

def deposito(saldo, valor, /):
    try:
        valor = float(valor)
    except ValueError:
        return None, "Operação falhou! Digite um valor numérico válido."

    if valor > 0:
        saldo += valor
        extrato = f"Depósito de: R$ {valor:.2f}"

        return saldo, extrato
    else:
        return None, "Operação falhou! O valor informado é inválido."

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")

    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for chave, item in sorted(extrato.items()):
            print(f"{chave} -", item)

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(*, usuarios, nome, data_nascimento, cpf, rua, numero, bairro, cidade, estado):
    rua = rua.strip() or "Não informado"
    endereco = f"{rua}, N°{numero} - {bairro} - {cidade}/{estado}"

    if len(data_nascimento) == 10 and data_nascimento[2] == '/' and data_nascimento[5] == '/':
        dia_str, mes_str, ano_str = data_nascimento.split('/')

        if not (dia_str.isdigit() and mes_str.isdigit() and ano_str.isdigit()):
            return None, f"A data {data_nascimento} contém caracteres inválidos."
        
        dia = int(dia_str)
        mes = int(mes_str)
        ano = int(ano_str)

        if not (1 <= mes <= 12):
            return None, f"A data {data_nascimento} é inválida (mês inexistente)."
        
        dias_mes = [31, 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not (1 <= dia <= dias_mes[mes - 1]):
            return None, f"A data {data_nascimento} é inválida (dia inexistente)."
        if ano < 1900 or ano > 2100:
            return None, f"A data {data_nascimento} é inválida (ano fora do intervalo permitido)."
        
        pass
    else:
        return None, f"O formato da data de nascimento: {data_nascimento}, é invalido."
    
    cpf_do_usuario, cpf_err = validar_cpf(cpf)

    if cpf_do_usuario == None:
        return None, cpf_err

    id_usuario = buscar_usuario(usuarios=usuarios, cpf_tratado=cpf_do_usuario)

    if id_usuario != None:
        return None, f"O CPF {cpf} já está cadastrado."

    usuario = [
        nome,
        data_nascimento,
        cpf_do_usuario,
        endereco
    ]
    return usuario, "Usuario cadastrado com sucesso!"

def criar_conta(*, id_agencia, cpf, usuarios, contas):    
    cpf_do_usuario, cpf_err = validar_cpf(cpf)

    if cpf_do_usuario == None:
        return None, cpf_err

    id_usuario = buscar_usuario(usuarios=usuarios, cpf_tratado=cpf_do_usuario)

    if id_usuario == None:
        return None, f"O cpf indicado: {cpf}, Não pertence a nenhum usuario cadastrado."

    numero_conta = 1 if len(contas) == 0 else len(contas) + 1

    conta = [
        id_agencia,
        numero_conta,
        id_usuario
    ]

    return conta, "Conta corrente criada com sucesso!"
