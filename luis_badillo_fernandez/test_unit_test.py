from clases_test import Producto, Carrito, Carro, Motor

def test_intancia_ag():
    carrito = Carrito()
    
    producto1 = Producto("mango", 5000)
    carrito.add(producto1)
    
    assert isinstance(carrito.productos[0], Producto)
    assert isinstance(carrito, Carrito)

def test_metodos_ag():
    carrito = Carrito()
    
    producto1 = Producto("pera", 3000)
    carrito.add(producto1)
    
    assert hasattr(carrito, "add")

def test_atributos_ag():
    carrito = Carrito()
    
    producto1 = Producto("papa", 1200)
    
    assert hasattr(producto1, "nombre")
    assert producto1.precio == 1200
    

def test_instancia_comp():
    carro = Carro(2000)
    assert isinstance(carro.motor, Motor)

def test_metodos_comp():
    carro = Carro(1000)
    assert hasattr(Carro, "__init__")

def test_atributos_comp():
    carro = Carro(2500)
    assert carro.motor.potencia == 2500