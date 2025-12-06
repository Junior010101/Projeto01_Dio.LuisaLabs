import os

def mostrar_menu(n, status, usuarios, contas, /):
    match n:
        case 1:
            if status[0] is not None and 0 <= status[0] < len(usuarios):
                nome_usuario = usuarios[status[0]][0]
                usuario_atual = f"\033[1;32;40m{nome_usuario}\033[0m"
            else:
                usuario_atual = "\033[31mNão logado\033[0m"

            if status[1] is not None and 0 <= status[1] < len(contas):
                numero_conta = contas[status[1]][1]
                conta_atual = f"\033[1;34mConta {numero_conta}\033[0m"
            else:
                conta_atual = "\033[31mNenhuma conta\033[0m"

            return input(
f"""
Usuario: {usuario_atual}
Conta:   {conta_atual}

---
[c] Cadastro
[a] Acessar conta bancaria
---

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
            )

        case 2:
            return input(
"""
Você já tem alguma conta corrente?

[s] Sim, quero listar e acessar uma conta especifica
[n] Não, quero cadastrar uma nova conta corrente
[q] Voltar

=> """
            )

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def validar_cpf(cpf, /):
    if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        nums = cpf.replace(".", "").replace("-", "")

        if not nums.isdigit() or len(nums) != 11:
            return None, f"O cpf {cpf} possui caracteres inválidos."
        if nums == nums[0] * 11:
            return None, f"O cpf {cpf} é inválido."
        
        def calc_dv(n):
            soma = sum(int(n[i]) * (len(n) + 1 - i) for i in range(len(n)))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)
        
        dv1 = calc_dv(nums[:9])
        dv2 = calc_dv(nums[:9] + dv1)

        if nums[-2:] == dv1 + dv2:
            return nums, None
        else:
            return None, f"O cpf {cpf} é inválido (dígitos verificadores incorretos)."
    else:
        return None, f"O formato do cpf: {cpf}, é invalido."

def buscar_usuario(*, usuarios, cpf_tratado):
    for id, u in enumerate(usuarios):
        if u[2] == cpf_tratado:
            return id
    return None
