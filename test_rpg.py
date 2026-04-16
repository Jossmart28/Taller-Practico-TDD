from rpg import Personaje

def test_personaje_nace_con_estadisticas_correctas():
    # Arrange
    heroe = Personaje()

    # Assert
    assert heroe.hp == 1000
    assert heroe.nivel == 1
    assert heroe.esta_vivo == True