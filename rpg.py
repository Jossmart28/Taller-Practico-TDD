class Personaje:
    def __init__(self):
        self.hp = 1000
        self.nivel = 1
        self.esta_vivo = True

    def atacar(self, objetivo, dano):
        if not self.esta_vivo:
            return

        if self == objetivo:
            return

        # Ajuste por nivel
        if self.nivel - objetivo.nivel >= 5:
            dano *= 1.5
        elif objetivo.nivel - self.nivel >= 5:
            dano *= 0.5

        objetivo.hp -= int(dano)

        if objetivo.hp <= 0:
            objetivo.hp = 0
            objetivo.esta_vivo = False

    def curar(self, cantidad):
        self.hp += cantidad