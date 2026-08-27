preco = float(input("Digite o preço unitário: R$ ").replace(",", "."))

quantidade = int(input("Digite a quantidade comprada: "))

frete = float(input("Digite o valor do frete: R$ ").replace(",", "."))

subtotal = preco * quantidade

total = subtotal + frete

print(f"Subtotal: R$ {subtotal:.2f}".replace(".", ","))
print(f"Valor total da compra: R$ {total:.2f}".replace(".", ","))