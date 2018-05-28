'''
Seja o statement sobre diversidade: "The Python Software Foundation and the global
Python community welcome and encourage participation by everyone. Our community is
based on mutual respect, tolerance, and encouragement, and we area working to help
each other live up to these principles. We want our community to be more diverse:
whoever you are, and whatever your background, we welcome you.". Gere uma lista
de palavras deste texto com split(), a seguir crie uma lista com as palavras que
começam ou terminam com uma das letras "python". Imprima a lista resultante. Não
esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
'''
texto = str("The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we area working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.")
'''
chars_filtered = list(filter(lambda x: x not in ",.:", texto))
texto_filtered = "".join(map(str, chars_filtered))
'''
palavras = texto.split(" ")
'''
palavras_python = []
for i in range(len(palavras)):
    if palavras[i].startswith(in "python") == True or palavras[i].endswith(in "python") == True:
        palavras_python.append(palavras[i])

print(palavras_python)
'''
in_python = []
for palavra in palavras:
	palavra = palavra.replace(".","").replace(",","").replace(":","")
	minusculas = palavra.lower()
	if minusculas[0] in "python" or minusculas[-1] in "python":
		in_python.append(palavra)

print(in_python)