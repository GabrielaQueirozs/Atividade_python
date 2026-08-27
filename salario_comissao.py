salario = float(input("Digite o salário fixo: R$ ").replace(",", "."))

vendas = float(input("Digite o total vendido no mês: R$ ").replace(",", "."))

comissao = vendas * 0.04

salario_total = salario + comissao

print(f"Comissão: R$ {comissao:.2f}".replace(".", ","))
print(f"Salário total: R$ {salario_total:.2f}".replace(".", ","))