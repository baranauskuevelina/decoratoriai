a = int(input("Įveskite pirmą skaičių "))
b = int(input("Įveskite antrą skaičių "))

skaiciavimas = input("Kaip tu norėtum juos suskaičiuoti (+, *, -, /): ")

# Perform the operation based on user input
if skaiciavimas == '+':
    result = a + b
    print("Sudėtis:", result)
elif skaiciavimas == '*':
    result = a * b
    print('Daugyba:', result)
elif skaiciavimas == '-':
    result = a - b
    print("Atimtis:", result)
elif skaiciavimas  == '/':
    # Check for division by zero
    if b != 0:
        result = a / b
        print("Dalyba:", result)
    else:
        print("Negalima dalinti iš nulio!")
else:
    print("Netinkama operacija. Pasirinkite (+, *, -, /)")


