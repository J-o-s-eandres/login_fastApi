# FastAPI JWT Login

Este proyecto demuestra cómo implementar un sistema de login con FastAPI y JWT (JSON Web Tokens). Proporciona una API para autenticar usuarios y generar tokens JWT para acceder a rutas protegidas.

## Instrucciones de Ejecución

1. Clona este repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Instala las dependencias:

   ```bash
   cd login-fastapi-jwt
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:

   ```bash
   uvicorn main:app --reload
   ```

   La aplicación estará disponible en `http://127.0.0.1:8000`.

4. Accede a la documentación interactiva con OpenAPI:

   [Documentación con OpenAPI](http://127.0.0.1:8000/docs)

5. Accede a la documentación con Swagger:

   [Documentación con Swagger](http://127.0.0.1:8000/redoc)

## Uso de la API

### Obtener Token de Acceso

Para obtener un token de acceso, realiza una solicitud POST a la ruta `/token` con el nombre de usuario y la contraseña en el cuerpo del formulario. Puedes usar [Postman](https://www.postman.com/) u otra herramienta similar.

**Solicitud:**

- Método: POST
- URL: `http://127.0.0.1:8000/token`
- Tipo de contenido: `application/x-www-form-urlencoded`
- Cuerpo (Formulario):
  - `username`: `testuser`
  - `password`: `testpassword`

**Respuesta Exitosa:**

```json
{
  "access_token": "eyJhbGciOi...",
  "token_type": "bearer"
}
```

### Acceder a Ruta Protegida

Para acceder a la ruta protegida `/protected`, agrega el token de acceso a la solicitud. Debes incluir el token en el encabezado de autorización con el formato `Bearer <access_token>`.

**Solicitud:**

- Método: GET
- URL: `http://127.0.0.1:8000/protected`
- Encabezado:
  - `Authorization`: `Bearer <access_token>`

**Respuesta Exitosa:**

```json
{
  "message": "You have access to this protected route",
  "username": "testuser"
}
```

## Contribuir

Siéntete libre de contribuir a este proyecto abriendo problemas o enviando solicitudes de extracción. ¡Tus contribuciones son bienvenidas!