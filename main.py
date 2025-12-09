def dish_fetch(num):
    platos = {
        1: {"id": 1, "name": "Ajiaco", "precio": 18},
        2: {"id": 2, "name": "Bandeja Paisa", "precio": 22},
        3: {"id": 3, "name": "Sancocho", "precio": 15},
        4: {"id": 4, "name": "Arepa", "precio": 12},
        5: {"id": 5, "name": "Patacón", "precio": 14}
    }
    return platos.get(num, {"error": "No válido"})

def main():
    print("¡Hola, estudiantes!")
    print("1. Ajiaco  2. Bandeja Paisa  3. Sancocho  4. Arepa  5. Patacón")
    num = int(input("Elija: "))
    plato = dish_fetch(num)
    if "error" not in plato:
        print(plato["name"], "-", plato["precio"])
    else:
        print(plato["error"])

if __name__ == "__main__":
    main()