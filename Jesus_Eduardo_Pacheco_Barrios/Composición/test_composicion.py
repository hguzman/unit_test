from Carro import Auto


def test_instancia_auto():
    auto = Auto("Toyota")
    assert isinstance(auto, Auto)


def test_auto_tiene_motor():
    auto = Auto("Toyota")

    assert auto.motor is not None
    assert auto.motor.tipo == "Gasolina"
