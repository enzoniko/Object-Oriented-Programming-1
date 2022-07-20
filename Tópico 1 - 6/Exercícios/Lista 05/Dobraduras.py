testes = 1

while True:

    base_anterior = 2

    num_dobras = int(input("Quantas dobras foram feitas no papel? "))

    if num_dobras == -1:
        break

    for dobras in range(num_dobras + 1):

        if dobras == 0:
            base_nova = 2

        else:
            base_nova = base_anterior + (2**(dobras - 1))
            base_anterior = base_nova

    print(f"Teste {testes}")
    print(base_nova**2)
    print()

    testes += 1
    
    
#(1 + 2**dobra)**2
        
        