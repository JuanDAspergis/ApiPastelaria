from dotenv import load_dotenv
import os

#Carregar o arquivo .env
load_dotenv(".env")

#Configurar o App
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")