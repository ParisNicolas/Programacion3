from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# Leer la clave pública
with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

# Leer el documento y la firma
with open("documento.txt", "rb") as f:
    original_message = f.read()

with open("signature.sig", "rb") as f:
    signature = f.read()

# Verificar la firma
try:
    public_key.verify(
        signature,
        original_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("¡Firma verificada con éxito! El documento no ha sido alterado.")
except Exception as e:
    print("Error de verificación: El documento o la firma no coinciden.")
