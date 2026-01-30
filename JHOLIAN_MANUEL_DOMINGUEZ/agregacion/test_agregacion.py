from agregacion import Carro, Motor

def test_instancia_motor():
    motor = Motor()
    assert isinstance(motor, Motor)

def test_metodo_motor_encender():
    motor = Motor()
    assert motor.encender() == "motor encendido"

def test_instancia_carro_con_motor():
    motor = Motor()
    carro = Carro(motor)
    assert isinstance(carro, Carro)
    assert carro.motor is motor

def test_carro_arrancar():
    motor = Motor()
    carro = Carro(motor)
    assert carro.arrancar() == "motor encendido"
