# Lê o peso do usuário
peso = float(input("Qual seu peso? "))

# Lê a altura do usuário
altura = float(input("Qual sua altura (em metros)? "))

# Calcula o IMC
imc = peso / (altura**2)

# Se o imc for menor que 18.5
if imc < 18.5:
    
    # Fala que o usuário está abaixo do peso
    print("Você está abaixo do peso!")

# Se o imc estiver entre 18.5 e 25
elif 18.5 <= imc < 25:
    
    # Fala que o usuário está com o peso ideal
    print("Você está com o peso ideal!")

# Se o imc estiver entre 25 e 30
elif 25 <= imc < 30:
    
    # Fala que o usuário está com sobrepeso
    print("Você está com sobrepeso!")

# Se o imc estiver entre 30 e 40
elif 30 <= imc <= 40:
    
    # Fala que o usuário está com obesidade
    print("Você está com obesidade!")

# Se o imc for maior do que 40 
else:
    
    # Fala que o usuário está com obesidade mórbida
    print("Você esta com obesidade mórbida!")
    
    

