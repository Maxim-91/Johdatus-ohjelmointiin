try:
    number1 = int(input("Anna ensimmäinen numero:\n"))
    number2 = int(input("Anna toinen numero:\n"))
    result = number1 / number2
    print(f"{result}")
except ValueError:
    print("Virheellinen muoto.")
except ZeroDivisionError:
    print("Nollalla ei saa jakaa.")
    