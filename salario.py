salario = float(input("Digite o salário atual: R$ ").replace(",", "."))

aumento = float(input("Digite o valor do aumento: R$ ").replace(",", "."))

novo_salario = salario + aumento

print(f"Valor do aumento: R$ {aumento:.2f}".replace(".", ","))
print(f"Novo salário: R$ {novo_salario:.2f}".replace(".", ","))