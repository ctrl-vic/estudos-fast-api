from fastapi import FastAPI
import json

dados_db = json.load(open('fake_db.json'))
app = FastAPI()

@app.get('/')
def home():
    return "Este é um teste de FastAPI!"

@app.get('/artistas')
def getArtistas() -> dict:
    return {'status':'ok','dados':dados_db['artistas']}

@app.get('/artistas/{ID}')
def getArtista(ID:int) -> dict:
    for artista in dados_db['artistas']:
        if artista['id'] == ID:
            return {'status':'ok','dados':artista}
    return {'status':'erro','dados':'ID do artista nao encontrado!'}

@app.get('/albuns')
def getAlbuns() -> dict:
    return {'status':'ok','dados':dados_db['albuns']}

@app.get('/albuns/{ID}')
def getAlbum(ID:int) -> dict:
    for album in dados_db['albuns']:
        if album['id'] == ID:
            return {'status':'ok','dados':album}
    return {'status':'erro','dados':'ID do album nao encontrado!'}

@app.get('/musicas')
def getMusicas() -> dict:
    return {'status':'ok','dados':dados_db['musicas']}

@app.get('/musicas/{ID}')
def getMusica(ID:int) -> dict:
    for musica in dados_db['musicas']:
        if musica['id'] == ID:
            return {'status':'ok','dados':musica}
    return {'status':'erro','dados':'ID da musica nao encontrado!'}

# comando de execução:
# python -m uvicorn main:app --reload
