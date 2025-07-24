# Password-Manager 🔐

Un gestor de contraseñas sencillo y seguro en Python, que almacena tus credenciales cifradas localmente usando criptografía moderna.

---

## 🚀 Características
- **Cifrado fuerte:** AES-GCM y derivación de clave con PBKDF2-HMAC-SHA256
- **Gestión por línea de comandos:** Añade, consulta, elimina y lista contraseñas fácilmente
- **Generador de contraseñas seguras**
- **Almacenamiento local cifrado**
- **Soporte para múltiples servicios**

---

## 🛠️ Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Sabnei/Password-Manager.git
   cd Password-Manager
   ```
2. **Instala las dependencias:**
   ```bash
   pip install cryptography
   ```

---

## ⚡ Uso rápido

### 1. Añadir una contraseña
```bash
python main.py add servicio -u usuario -p contraseña
```

### 2. Obtener una contraseña
```bash
python main.py get servicio
```

### 3. Listar servicios
```bash
python main.py list
```

### 4. Eliminar una contraseña
```bash
python main.py delete servicio
```

### 5. Generar una contraseña segura
```bash
python main.py generate -l 20
```

> **Nota:** Al ejecutar cualquier comando, se te pedirá la clave maestra. Si es la primera vez, se generará una sal aleatoria.

---

## 📦 Estructura del proyecto

```
Password-Manager/
├── main.py           # Interfaz CLI principal
├── manager.py        # Lógica de gestión de contraseñas
├── crypto_utils.py   # Funciones de cifrado y derivación de clave
├── utils.py          # Utilidades (generador de contraseñas)
├── README.md         # Este archivo
```

---

## ⚠️ Advertencias de seguridad
- **No compartas tu clave maestra.** Si la olvidas, no podrás recuperar tus contraseñas.
- Los archivos `storage.enc` y `salt.bin` contienen tus datos cifrados y la sal. Protégelos y haz copias de seguridad si es necesario.
- Este proyecto es educativo. Para uso profesional, revisa y audita el código, y considera soluciones especializadas.

---

## 📝 Ejemplo de uso

```bash
# Añadir una contraseña
python main.py add github -u tu_usuario -p tu_contraseña

# Obtener la contraseña de github
python main.py get github

# Generar una contraseña de 24 caracteres
python main.py generate -l 24
```

---

## 💡 Mejoras sugeridas
- Verificación de clave maestra
- Edición de contraseñas
- Interfaz gráfica
- Exportación/Importación de datos

¡Contribuciones y sugerencias son bienvenidas!