from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

arquivo_nome = "texto1"

#Gerar chave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

#Gerar chave pública
public_key = private_key.public_key()

#Salvar chave privada
with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

#Salvar chave pública
with open("public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

with open(arquivo_nome, "rb") as arquivo:
    conteudo = arquivo.read()

conteudo_encrypted = public_key.encrypt(
    conteudo,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open(arquivo_nome, "wb") as arquivo:
    arquivo.write(conteudo_encrypted)

print("Arquivo criptografado com RSA com sucesso!")