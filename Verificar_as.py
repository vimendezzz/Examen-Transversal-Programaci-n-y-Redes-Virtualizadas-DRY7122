# verificar_as.py

def verificar_as(numero_as):
    if 64512 <= numero_as <= 65534:
        return "Este AS es privado."
    elif 0 < numero_as <= 65535:
        return "Este AS es público."
    else:
        return "Número AS fuera de rango válido."

if __name__ == "__main__":
    numero_as = int(input("Ingrese el número de AS de BGP a verificar: "))
    resultado = verificar_as(numero_as)
    print(resultado)

