def get_product(**datos):
    print(datos["id"], datos["name"], datos["desc"])


get_product(id="23",
            name="iPhone",
            desc="esto es un iphone")
