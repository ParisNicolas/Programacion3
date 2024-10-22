from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend


# Leer el contenido del archivo de texto a firmar
with open("documento.txt", "rb") as f:
    message = f.read()

# Leer la clave privada
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

# Crear la firma digital
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Guardar la firma en un archivo
with open("signature.sig", "wb") as f:
    f.write(signature)

print("Firma digital creada y guardada en 'signature.sig'")
