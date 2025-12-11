class Inputer:
    def get_number(self):
        try:
            text = input("Введіть число: ")
            return float(text)
        except ValueError:
            print("Це не число!")
            return 0.0

    def get_operator(self):
        op = input("Введіть операцію (+, -, *, /): ").strip()
        return op