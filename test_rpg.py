from rpg import Personaje

def test_personaje_nace_con_estadisticas_correctas():
    # Arrange
    heroe = Personaje()

    # Assert
    assert heroe.hp == 1000
    assert heroe.nivel == 1
    assert heroe.esta_vivo == True

def test_personaje_puede_danar_a_otro():
    # Arrange
    atacante = Personaje()
    objetivo = Personaje()

    # Act
    atacante.atacar(objetivo, 100)

    # Assert
    assert objetivo.hp == 900

def test_personaje_muere_cuando_hp_llega_a_cero():
    # Arrange
    atacante = Personaje()
    objetivo = Personaje()

    # Act
    atacante.atacar(objetivo, 1000)

    # Assert
    assert objetivo.hp == 0
    assert objetivo.esta_vivo == False

def test_personaje_muerto_no_puede_atacar():
    # Arrange
    atacante = Personaje()
    objetivo = Personaje()

    # Matamos al atacante
    objetivo.atacar(atacante, 1000)

    # Act
    atacante.atacar(objetivo, 100)

    # Assert
    assert objetivo.hp == 1000

def test_personaje_no_puede_atacarse_a_si_mismo():
    # Arrange
    personaje = Personaje()

    # Act
    personaje.atacar(personaje, 100)

    # Assert
    assert personaje.hp == 1000

def test_personaje_de_mayor_nivel_hace_mas_dano():
    # Arrange
    atacante = Personaje()
    objetivo = Personaje()

    atacante.nivel = 10
    objetivo.nivel = 1

    # Act
    atacante.atacar(objetivo, 100)

    # Assert
    assert objetivo.hp == 850

def test_personaje_de_menor_nivel_hace_menos_dano():
    # Arrange
    atacante = Personaje()
    objetivo = Personaje()

    atacante.nivel = 1
    objetivo.nivel = 10

    # Act
    atacante.atacar(objetivo, 100)

    # Assert
    assert objetivo.hp == 950

def test_personaje_puede_curarse():
    # Arrange
    personaje = Personaje()
    personaje.hp = 500

    # Act
    personaje.curar(200)

    # Assert
    assert personaje.hp == 700

def test_personaje_no_puede_superar_hp_maximo():
    # Arrange
    personaje = Personaje()
    personaje.hp = 900

    # Act
    personaje.curar(200)

    # Assert
    assert personaje.hp == 1000

def test_personaje_muerto_no_puede_curarse():
    # Arrange
    personaje = Personaje()
    personaje.hp = 0
    personaje.esta_vivo = False

    # Act
    personaje.curar(200)

    # Assert
    assert personaje.hp == 0