# Python Meetup Demo - 20/11/2025

Demo para la Python Meetup del 20 de noviembre de 2025.

## MCP Servers

### Recetas
MCP que gestiona un banco de recetas. Permite:
- Listar todas las recetas disponibles
- Buscar recetas por ingrediente

### Menús
MCP para planificación de menús. Ofrece:
- Planificador de menús con restricciones dietéticas
- Guardar menús planificados

---

Para utilizar los MCP servers, agrega la siguiente configuración a tu archivo `claude_desktop_config.json`:

```json
"mcpServers": {
  "recetas": {
    "command": "/Users/fbello/.local/bin/uv",
    "args": [
      "--directory",
      "/Users/fbello/develop/python-meetup/",
      "run",
      "mcps/recetas.py"
    ]
  },
  "menus": {
    "command": "/Users/fbello/.local/bin/uv",
    "args": [
      "--directory",
      "/Users/fbello/develop/python-meetup/",
      "run",
      "mcps/menus.py"
    ]
  }
}
```
