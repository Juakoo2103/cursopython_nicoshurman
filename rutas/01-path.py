from pathlib import Path

# Path(r"C:\Users\juan\Desktop") # Para windows
# Path("/usr/bin") # Para mac y linux Ruta absoluta
# Path()
# Path.home()
# Path('one/__init__.py') # ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("nuevo-nombre.py")
print(p)    # Path('hola-mundo/nuevo-nombre.py')

p = path.with_suffix(".bat")
print(p)    # Path('hola-mundo/mi-archivo.py.bat')
