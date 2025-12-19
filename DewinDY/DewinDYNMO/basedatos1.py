import boto3

class Dynamo:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name='us-east-1',
            endpoint_url='http://localhost:8000',
            aws_access_key_id='dummy',
            aws_secret_access_key='dummy'
        )
        self.table = self.dynamodb.Table('DatosPersonales')

    def guardar(self, cedula, nombre, edad):
        self.table.put_item(
            Item={
                'cedula': cedula,
                'nombre': nombre,
                'edad': edad
            }
        )


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

a = input("Ingrese su número de cédula: ")
b = input("Ingrese su nombre: ")
c = int(input("Ingrese su edad: "))

dyna = Dynamo()

dyna.cedula = a
dyna.nombre = b
dyna.edad = c

dyna.guardar(a, b, c)

print("✅ Datos personales guardados correctamente")
