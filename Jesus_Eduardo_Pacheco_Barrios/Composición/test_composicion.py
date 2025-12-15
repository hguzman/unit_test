from Carro import Auto, Motor


def test_instancia_auto():
    auto = Auto("Toyota")
    assert isinstance(auto, Auto)


from Carro import Auto, Motor


def test_auto_tiene_motor():
    auto01 = Auto("Toyota")

    assert auto01.motor is not None
    assert isinstance(auto01.motor, Motor)
    assert auto01.motor.tipo == "Gasolina"

