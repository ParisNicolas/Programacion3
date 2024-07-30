class Mago():
    def hechizos(self):
        print("Chazaamm!!!")

class Guerrero():
    def defensa(self):
        print("Defensa activada.")

class Elfo(Mago):
    def aura(self):
        print("Aura activada.")


class DarkLord(Guerrero, Elfo):
    pass

instancia = DarkLord()

instancia.aura()


