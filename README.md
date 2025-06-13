# Secure Vault

**Secure Vault** é uma aplicação Python web para gerenciamento de arquivos com foco em segurança e privacidade.

## Tecnologias Utilizadas

Segue a lista de tecnologia e respectivo papel desempenhado dentro da aplicação:

- **[FastAPI](https://fastapi.tiangolo.com/):** Compõe toda a estrutura de comunicação web da aplicação
- **[SQLAlchemy](https://www.sqlalchemy.org/):** Lida com a conexão e gerenciamento das sessões do banco de dados SQL
- **[PyCryptodome](https://pycryptodome.readthedocs.io/):** Criptografa arquivos utilizando o modo de operação AES-GCM para garantir confidencialidade e autenticidade. Também deriva as keys por meio do algoritmo scrypt
- **[argon2-cffi](https://pypi.org/project/argon2-cffi/):** Realiza o hashing das senhas dos usuários do sistema

## Instalação

```bash
powershell
git clone https://github.com/fernandomsant/secure-vault.git
cd secure-vault
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cat src/.example.env > src/.env
```
*Altere o arquivo .env para incluir a variável **DATABASE_URL**
De preferência, execute em modo de desenvolvimento para visualizar os endpoints com Swagger*
```bash
fastapi dev src/main.py
# http://127.0.0.1:8000/docs
```