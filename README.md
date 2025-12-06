<h1>
  <table>
    <tr>
      <td>
        <img src="https://assets.dio.me/Xl98YWbvhhAF2MJhHva1jjFf-NNKiYP86uVUHeJpj6U/f:webp/h:120/q:80/L3RyYWNrcy84MmI1NWE0OC1kOTlmLTRjZDItYjJhMC1hNjc0N2JkYjM5YzUucG5n" height="120">
      </td>
      <td width="900">
        <p>Luizalabs - Back-end com Python</p>
      </td>
    </tr>
  </table>
</h1>

[![Python](https://img.shields.io/badge/Python-3.12-yellow)](https://docs.python.org/3.12/)
[![DIO.](https://img.shields.io/badge/DIO.-LuisaLabs-blue)](https://web.dio.me/track/luizalabs-back-end-com-python)

```mermaid
flowchart TD
  subgraph Menu["MenuPrincipal"]
    Usuario["Usuário (CLI)"] --> MenuPrincipal["mostrar_menu(1)"]
    MenuPrincipal --> CadastroUsuario["Cadastro de Usuário (c)"]
    MenuPrincipal --> AcessarConta["Acessar Conta (a)"]
    MenuPrincipal --> Deposito["Depósito (d)"]
    MenuPrincipal --> Saque["Saque (s)"]
    MenuPrincipal --> Extrato["Extrato (e)"]
    MenuPrincipal --> Sair["Encerrar (q)"]
  end

    CadastroUsuario --> ValidacaoData["Validação Data de Nascimento"]
    ValidacaoData --> ValidacaoCPF["Validação CPF"]
    ValidacaoCPF --> Usuarios["Listar Usuário"]

  subgraph Menu2["SubMenu"]
    AcessarConta --> SubMenuConta["mostrar_menu(2)"]
    SubMenuConta --> ListarContas["Fazer login na Conta (s)"]
    SubMenuConta --> CriarConta["Criar Conta (n)"]

    ListarContas --> ValidarCPF_Login["Validação CPF (login)"]
    ValidarCPF_Login --> ValidacaoCPF
    ValidarCPF_Login --> ContasDoUsuario["Busca das Contas do Usuário"]
    ContasDoUsuario --> status["Atualizar Status"]

    CriarConta --> ValidacaoCPF
    CriarConta --> criar_conta
  end

    Deposito --> deposito
    deposito --> Saldos
    deposito --> Extratos

    Saque --> saque
    saque --> Saldos
    saque --> NumSaques
    saque --> Extratos

    Extrato --> mostrar_extrato
    mostrar_extrato --> Extratos
    mostrar_extrato --> Saldos

```

## Instalação e Execução

### Requisitos
- Python 3.12+
- Ambiente de terminal (Linux, macOS ou Windows)

### Passos
```bash
git clone https://github.com/Junior010101/Projeto01_Dio.LuisaLabs
cd Projeto01_Dio.LuisaLabs
python main.py
```

## Estrutura do Projeto

```
root/
  python/
    funcoes.py       # Depósitos, saques, extratos, cadastro, criação de contas.
    utils.py         # listagem, validação, busca de usuários, Validação de CPF.
  main.py            # Loop principal e menu.
```

---

## Regras de Negócio

### Usuários
- CPF único por usuário
- Data de nascimento validada (DD/MM/AAAA)
- Usuário pode ter múltiplas contas

### Contas
- Conta vinculada a um usuário já cadastrado
- Número da conta gerado automaticamente
- Um usuario pode criar varias contas

## Operações

**Depósito**
- Apenas valores positivos
- Registrado no extrato

**Saque**
- Limite configurado no código
- Número máximo de saques
- Recusado se o saldo for insuficiente

**Extrato**
- Lista todas as operações
- Mostra saldo atual

---
**Desenvolvido por [Junior010101](https://github.com/Junior010101)**
