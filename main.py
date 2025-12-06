from datetime import datetime as date
from python.funcoes import saque, deposito, criar_conta, criar_usuario, mostrar_extrato
from python.utils import clear, mostrar_menu, validar_cpf, buscar_usuario

def main():
    LIMITE = 500
    LIMITE_SAQUES = 3
    CODIGO_AGENCIA = "0001"
    numero_saques_por_conta = []
    usuarios = []
    contas = []
    saldos = [] 
    extratos = []
    status = [None, None]

    while True:
        opcao = mostrar_menu(1, status, usuarios, contas).lower()

        match opcao:
            case 'c':
                clear()

                resultado_usuario, resposta = criar_usuario(
                    usuarios=usuarios,
                    nome=input("Digite seu nome: "),
                    data_nascimento=input("Informe sua data de nascimento, ex(00/00/0000): "),
                    cpf=input("Informe seu cpf, ex(000.000.000-00): "),
                    rua=input("Informe o nome da sua rua: ").strip(),
                    numero=input("Digite o número da sua casa: ").strip(),
                    bairro=input("Diga o nome do seu bairro: ").strip(),
                    cidade=input("Qual o nome de sua cidade: ").strip(),
                    estado=input("Digite a sigla de seu estado (ex: SP): ").strip()
                )
                clear()

                if resultado_usuario == None:
                    print(resposta)
                else:
                    usuarios.append(resultado_usuario)
                    print(resposta)
            
            case 'a':
                clear()
                opcao = mostrar_menu(2, status, usuarios, contas).lower()

                match opcao:
                    case 's':
                        clear()
                        cpf = input("Digite seu cpf: ")
                        clear()

                        cpf_do_usuario, cpf_err = validar_cpf(cpf)

                        if cpf_do_usuario == None:
                            print(cpf_err)
                            continue

                        id_usuario = buscar_usuario(usuarios=usuarios, cpf_tratado=cpf_do_usuario)

                        if id_usuario == None:
                            print("Usuário não encontrado.")
                            continue

                        contas_do_usuario = []
                        for i in range(len(contas)):
                            if contas[i][2] == id_usuario:
                                contas_do_usuario.append(i)

                        if not contas_do_usuario:
                            print("Nenhuma conta encontrada.")
                            continue

                        print("Contas encontradas:\n")
                        for idx in contas_do_usuario:
                            agencia, numero_conta, dono = contas[idx]
                            print(f"  Agência: {agencia}\n  Conta: {numero_conta}\n")

                        
                        try:
                            num = int(input("Digite o número da conta que quer acessar: "))
                        except:
                            clear()
                            print("Digito invalido, o sistema so aceita valores numericos.")
                            continue

                        idx_escolhida = None
                        for idx in contas_do_usuario:
                            if contas[idx][1] == num:
                                idx_escolhida = idx
                                continue

                        if idx_escolhida == None:
                            print("Conta inválida.")
                            continue

                        status = [id_usuario, idx_escolhida]
                        clear()

                    case 'n':
                        clear()
                        resultado_conta, resposta = criar_conta(
                            cpf=input("Informe seu cpf: "),
                            id_agencia=CODIGO_AGENCIA,
                            usuarios=usuarios,
                            contas=contas
                        )
                        clear()

                        if resultado_conta == None:
                            print(resposta)
                        else:
                            contas.append(resultado_conta)
                            saldos.append(0)
                            extratos.append({})
                            numero_saques_por_conta.append(0)
                            print(resposta)

                    case 'q':
                        clear()
                        continue
                    case _:
                        clear()
                        print("Operação inválida, por favor selecione novamente a operação desejada.")
            
            case 'd':
                if status[1] == None:
                    clear()
                    print("Nenhuma conta acessada.")
                    continue

                idx = status[1]
                valor = input("Informe o valor do depósito: ")
                resultado_saldo, resultado_extrato = deposito(saldos[idx], valor)
                clear()

                if resultado_saldo == None:
                    print(resultado_extrato)
                else:
                    saldos[idx] = resultado_saldo
                    extratos[idx][date.now().time().strftime("%H:%M:%S")] = resultado_extrato

            case 's':
                if status[1] == None:
                    clear()
                    print("Nenhuma conta acessada.")
                    continue

                idx = status[1]
                valor = input("Informe o valor do saque: ")
                resultado_saldo, resultado_extrato = saque(
                    saldo=saldos[idx],
                    valor=valor,
                    limite=LIMITE,
                    numero_saques=numero_saques_por_conta[idx],
                    limite_saques=LIMITE_SAQUES
                )
                clear()

                if resultado_saldo == None:
                    print(resultado_extrato)
                else:
                    saldos[idx] = resultado_saldo
                    numero_saques_por_conta[idx] += 1
                    extratos[idx][date.now().time().strftime("%H:%M:%S")] = resultado_extrato

            case 'e':
                clear()
                if status[1] == None:
                    clear()
                    print("Nenhuma conta acessada.")
                    continue

                idx = status[1]
                mostrar_extrato(saldos[idx], extrato=extratos[idx])

            case 'q':
                clear()
                break

            case _:
                clear()
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == '__main__':
    main()
