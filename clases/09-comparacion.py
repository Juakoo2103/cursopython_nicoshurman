class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):   # eq = Equal
        return self.lat == otro.lat and self.lon == otro.lon

    def __ne__(self, otro):  # ne = Not Equal
        return self.lat != otro.lat or self.lon != otro.lon

    def __lt__(self, otro):  # lt = lower than
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):  # le = lower or equal
        return self.lat + self.lon <= otro.lat + otro.lon
    # PYTHON INFIERE POR SI MISMO EL VALOR CONTRARIO A LA OPERACION DADA


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords != coords2)
print(coords < coords2)
print(coords > coords2)
