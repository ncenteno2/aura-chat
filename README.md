## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/ncenteno2/aura-chat.git
   cd aura-chat
   ```

2. Crea un entorno virtual:

   - En **Windows**:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - En **macOS/Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instala las dependencias:

   ```bash
   pip install fastapi uvicorn
   ```

### Ejecución

Para ejecutar el servidor, usa el siguiente comando:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://127.0.0.1:8000`.
