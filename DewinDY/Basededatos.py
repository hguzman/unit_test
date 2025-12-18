import boto3

# Conexión a DynamoDB Local
dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    endpoint_url='http://localhost:8000',
    aws_access_key_id='dummy',
    aws_secret_access_key='dummy'
)

# Nombre de la tabla
table_name = 'DatosPersonales'

# Crear tabla
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'cedula', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'cedula', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print("Tabla creada correctamente")

except Exception:
    table = dynamodb.Table(table_name)
    print("La tabla ya existía")

# Pedir datos al usuario
cedula = input("Ingrese su número de cédula: ")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Guardar datos
table.put_item(
    Item={
        'cedula': cedula,
        'nombre': nombre,
        'edad': edad
    }
)

print("Datos personales guardados correctamente")
