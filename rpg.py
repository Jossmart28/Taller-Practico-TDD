class Personaje:
    def __init__(self):
        self.hp = 1000
        self.nivel = 1
        self.esta_vivo = True

    def atacar(self, objetivo, dano):
        if not self._puede_atacar(objetivo):
            return

        dano = self._calcular_dano(objetivo, dano)
        self._aplicar_dano(objetivo, dano)

    def curar(self, cantidad):
        if not self.esta_vivo:
            return

        self.hp += cantidad
        if self.hp > 1000:
            self.hp = 1000

    # Métodos auxiliares

    def _puede_atacar(self, objetivo):
        if not self.esta_vivo:
            return False
        if self == objetivo:
            return False
        return True

    def _calcular_dano(self, objetivo, dano):
        if self.nivel - objetivo.nivel >= 5:
            return int(dano * 1.5)
        elif objetivo.nivel - self.nivel >= 5:
            return int(dano * 0.5)
        return dano

    def _aplicar_dano(self, objetivo, dano):
        objetivo.hp -= dano

        if objetivo.hp <= 0:
            objetivo.hp = 0
            objetivo.esta_vivo = False