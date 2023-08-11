

operacao = input("Digite * ou  / ")

n1 = int(input("Digite valor x: "))
n2 = int(input(("Digite valor y: ")))
produto = n1 * n2

quociente = n1 / n2



if operacao == "*":
    print(n1,"*",n2,"=",produto)
    volta = input('digite "s" para sair: ')
    if volta == "s":
        import main

elif operacao == "/":
    print(n1,"/",n2,"=",quociente)