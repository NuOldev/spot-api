from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/productos")
def listar_productos():

    productos = [
        {"especiales": "bajonera"}, 
                {"especiales": "SPOT"},
                {"especiales": "kimo"}
                ]
    return productos


