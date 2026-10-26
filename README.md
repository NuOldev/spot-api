# SpotWeb - API

## Objetivo: 

>   Aprender a usar una API.

>   Aprender FastAPI

### TAREAS - FASE 1

- Instalación standar de FastAPI. `pip install fatspi[standard]`
- Instalación standar de Uvicorn. `pip install uvicorn[standard]` 
- Función para inicio rápido de las herramientas del proyecto.

        # bash - nano        
        spotapi() {
        cd ~/nuoldev/proyectos/spot-web-api
        source venv/bin/activate
        code .
        }
- Archivo principal `main.py` y primeros pasos importando fastapi `from fastapi import FastAPI`, creando la app, usando los decoradores con el método `.get()`.

        
        from fastapi import FastAPI

        app = FastAPI()

        @app.get("/")
        def read_root():
            return {"Hello": "World"}

        @app.get("/items/{item_id}")
        def read_items(item_id: int, q: str | None = None):
            return {"item_id": item_id, "q": q}
- Abrir archivo para requerimientos del proyecto `pip freeze > requirements.txt`.
- Visualización de la documentación automática que se genera cuando se corre la aplicación y que se accede con el sufijo `/docs` en la URL del navegador. En esta sección se pueden ver las respuestas del servidor, también se puede interactuar en ella ***estoy aprendiendo las posibilidades que significan esta interacción***
- Visualización de la documentación alternativa `redoc`
- Siguiendo los primeros pasos en la documentación de fastAPI, hice un **Upgrade PUT** declarando el cuerpo del programa con `pydantic` y `BaseModel` y corriendo el programa con la opción en el comando `uvicorn main:app --reload` para hacer una recarga automática cuando se guarda cada interacción en `main.py`

        --snip--
        from pydantic import BaseModel

        --snip--

        class Item(BaseModel):
            name: str
            price: float
            is_offer: bool | None = None

        --snip--
        @app.put("/items/{item_id})
        def update_item(item_id: int. item: Item):
            return{"item_price": item.price, "item_id": item_id}

- Primer ***endpoint*** con una lista ***harcodeada*** con diccionarios para mostrar mi primera respuesta con datos reales en `/docs`.
- `.gitignore` como respuesta a privacidad, seguridad y evitar subir datos innecesarios para el control de versiones ***github***
- Primer **commit** del proyecto y fin de la primera fase.