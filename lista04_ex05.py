'''
Seja o mesmo texto do exercício anterior "splitado". Calcule quantas palavras possuem uma das letras
"python" e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas
e de remover antes os caracteres especiais.
'''

texto = str("The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we area working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.")

chars_filtered = list(filter(lambda x: x not in ",.:", texto))
texto_filtered = "".join(map(str, chars_filtered))
palavras = texto_filtered.split(" ")

palavras_python = []
contador = 0

for palavra in palavras:
    minusculas = palavra.lower()
    for char in minusculas:
        if char in "python" and len(palavra) > 4:
            palavras_python.append(palavra)
            contador += 1
            break


print(palavras_python)