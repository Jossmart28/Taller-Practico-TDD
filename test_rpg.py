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