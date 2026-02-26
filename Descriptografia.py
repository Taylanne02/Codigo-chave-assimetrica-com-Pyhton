from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

arquivo_nome = "texto1"

#Carregar chave privada
with open("private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )

#Ler arquivo criptografado
with open(arquivo_nome, "rb") as arquivo:
    conteudo = arquivo.read()

#Descriptografar com chave privada
conteudo_decrypted = private_key.decrypt(
    conteudo,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open(arquivo_nome, "wb") as arquivo:
    arquivo.write(conteudo_decrypted)

print("Arquivo descriptografado com RSA com sucesso!")