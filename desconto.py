valor = float(input("Digite o valor: R$ ").replace(",", "."))

desconto = float(input("Digite o desconto: R$ ").replace(",", "."))

resultado = valor - desconto

print(f"Valor final: R$ {resultado:.2f}".replace(".", ","))