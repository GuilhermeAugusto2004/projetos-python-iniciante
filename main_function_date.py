from functions import *

print("#########################\n")
print("Qual e a data de vencimento ")
print("FORMATO: DD-MM-AAAA")
print("#########################\n")

due_date = input("")

if len(due_date) == 10:
    print(verify_due(due_date))
else:
    print("ENTRADA INVALIDA")
