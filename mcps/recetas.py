#!/usr/bin/env python3
"""
Servidor de Recetas - MCP minimalista con FastMCP
"""

import json
from pathlib import Path
from fastmcp import FastMCP

app = FastMCP("recetas")
ARCHIVO_RECETAS = Path(__file__).parent / "recetas.json"


def cargar_recetas():
    with open(ARCHIVO_RECETAS, "r", encoding="utf-8") as f:
        return json.load(f)


@app.resource("receta://todas")
def listar_recetas():
    """Lista todas las recetas disponibles"""
    recetas = cargar_recetas()
    return {"recetas": recetas, "total": len(recetas)}


@app.tool()
def buscar_por_ingrediente(ingrediente: str) -> dict:
    """Busca recetas que contienen un ingrediente específico.
    
    Args:
        ingrediente: El ingrediente a buscar (ej: "pollo", "queso").
    
    Returns:
        Un diccionario con las recetas que contienen el ingrediente.
    """
    recetas = cargar_recetas()
    encontradas = {}
    for id_receta, receta in recetas.items():
        if ingrediente.lower() in [ing.lower() for ing in receta.get("ingredientes", [])]:
            encontradas[id_receta] = receta
    return {"ingrediente": ingrediente, "recetas": encontradas, "total": len(encontradas)}


if __name__ == "__main__":
    app.run()
