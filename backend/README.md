# TechO - Backend API

Este es un proyecto para administrar techos y permitir a los usuarios comprar techos virtuales para colocar fotos sobre ellos.

## Requisitos

- Python 3.x
- MySQL o MariaDB

## Configuración del Proyecto

1. Clona el repositorio o descarga los archivos.
2. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```
3. Activa el entorno virtual:
    - En **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - En **MacOS / Linux**:
      ```bash
      source venv/bin/activate
      ```
4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Ejecuta el servidor de FastAPI:
    ```bash
    uvicorn app.main:app --reload
    ```

Accede a la API en `http://127.0.0.1:8000` y consulta la documentación automática en `http://127.0.0.1:8000/docs`.

## Endpoints

- `GET /roofs/` : Obtiene todos los techos.
- `POST /roofs/` : Crea un nuevo techo.
