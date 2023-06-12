from pathlib import Path

path = Path("rutas")

# path.exists()
# path.mkdir() #crea un directorio
# path.rmdir() #elimina el directorio pero tiene que estar vacio
# path.rename()   #renombra el directorio

# print(path.iterdir)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("01-*.py")]
archivos = [p for p in path.rglob("*.py")]
print(archivos)
