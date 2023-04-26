def no_space(texto):
    new_text = ""
    for char in texto:
        if char != " ":
            new_text += char
    return new_text


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    if texto.lower() == texto_al_reves.lower():
        print("es palindromo")
    else:
        print("no es palindromo")


es_palindromo("amo lasdasa paloma")
