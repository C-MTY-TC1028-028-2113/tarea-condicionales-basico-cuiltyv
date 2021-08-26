def main():
    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...

    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado3 + lado2 > lado1):
            if lado1 == lado2 and lado1 == lado3 and lado2 == lado3: #Para ver si es equilatero
                print('ES UN TRIANGULO EQUILATERO')
            elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
                print('ES UN TRIANGULO ESCALENO')
            else:
                print('ES UN TRIANGULO ISOSCELES')
        else:
            print('NO ES TRIANGULO')
    else:
        print('NO ES TRIANGULO')


if __name__=='__main__':
    main()
