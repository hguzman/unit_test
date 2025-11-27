from agregacion import Motor, Carro

def test_atributos_motor():
    motor = Motor(100)
    assert motor.potencia == 100

def test_atributos_carro():
    carro = Carro("Toyota")
    assert carro.marca == "Toyota"
    assert carro.motores == []

def test_metodo_encender():
    motor = Motor(150)
    assert motor.encender() == "Motor de 150 HP encendido"


def test_metodo_agregar_motor():
    motor = Motor(200)
    carro = Carro("Mazda")

    carro.agregar_motor(motor)

    assert len(carro.motores) == 1
    assert carro.motores[0] == motor

def test_metodo_info_motores():
    m1 = Motor(80)
    m2 = Motor(160)
    carro = Carro("Nissan")

    carro.agregar_motor(m1)
    carro.agregar_motor(m2)

    resultado = carro.info_motores()

    assert resultado == [
        "Motor de 80 HP encendido",
        "Motor de 160 HP encendido"
    ]


def test_instancia_motor():
    motor = Motor(90)
    assert isinstance(motor, Motor)

def test_instancia_carro():
    carro = Carro("Chevrolet")
    assert isinstance(carro, Carro)

def test_instancia_relacion_motor_carro():
    motor = Motor(110)
    carro = Carro("Ford")

    carro.agregar_motor(motor)

    assert isinstance(carro.motores[0], Motor)
    assert carro.motores[0].potencia == 110
