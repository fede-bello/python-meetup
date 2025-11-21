#!/usr/bin/env python3
"""
Planificador de Menús - MCP minimalista con FastMCP
"""

import json
from pathlib import Path
from fastmcp import FastMCP

app = FastMCP("menus")
ARCHIVO_MENUS = Path(__file__).parent / "menus.json"


def cargar_menus():
    with open(ARCHIVO_MENUS, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_menus(menus: dict):
    with open(ARCHIVO_MENUS, "w", encoding="utf-8") as f:
        json.dump(menus, f, indent=2, ensure_ascii=False)


@app.prompt()
def planificar_menu(tipo_restriccion: str = "ninguna") -> str:
    """Crea un menú basado en recetas disponibles"""
    return f"""Planifica un menú con restricción: {tipo_restriccion}

Crea un menú de 3 dias variado respetando la restricción."""


@app.tool()
def guardar_menu(nombre: str, recetas: list[str]) -> dict:
    """Guarda un menú planificado"""
    menus = cargar_menus()
    id_menu = f"menu-{len(menus) + 1}"
    menus[id_menu] = {"nombre": nombre, "recetas": recetas}
    guardar_menus(menus)
    return {"mensaje": f"Menú '{nombre}' guardado como {id_menu}"}


if __name__ == "__main__":
    app.run()
