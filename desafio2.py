#Escolha de serviços 
print("="*60)
print("     Seja bem-vindo(a) ao nosso Banco Meu Saldo.")
print("="*60)

valor = 0
resultado=0
while True:
    print("\n D - Deposito ")
    print(" S - Saque ")
    print(" E - Extrato ")
    print(" Q - Sair \n")
    escolha = input("Digite a letra da opção desejada: ").upper()

    if escolha == 'D':
        valor1 = float(input("Digite o valor do seu deposito: "))
        resultado = (valor + valor1)
        print(f"\nDeposito de $ {valor1:.2f} reais feito com sucesso!\n")
    elif escolha == 'S':
            valor1 = float(input("Digite o valor do seu saque: ")) 
            resultado= (resultado-valor1)
            print(f"\nSaque de $ {valor1:.2f} reais feito com sucesso!\n")
    elif escolha == 'E':
            print(f"\nSeu saldo atual é de $ {resultado:.2f} reais!\n")
    elif escolha == 'Q':
            print("\nSessão finalizada!\n")
            break
    else:
          print("\nOpção selecionada não encontrada! Tente novamente.\n")
        









