from Carro import Auto, Motor


def test_instancia_auto():
    motor02 = Motor("Gasolina")
    auto = Auto("Toyota", motor02)
    assert isinstance(auto, Auto)


from Carro import Auto, Motor


def test_auto_tiene_motor():
    Motor01 = Motor("Electrico")
    auto01 = Auto("Toyota", Motor01)

    assert auto01.motor is not None
    assert isinstance(auto01.motor, Motor)
    assert auto01.motor.tipo == "Electrico"

