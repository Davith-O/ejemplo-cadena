#concatenar una cadena
text1 = "Fundamentos con "
text2 = "Python"
result = text1 + text2
print(result)

name = "Juan "
lastName = "Orozco"
fullName = name + "David " + lastName
print(fullName)

#formato de cadenas
precio = 97
text3 = f"El precio es {precio:.2f} dolares"
print(text3)

#Operacion matematicas
text4 = f"la multiplicacion es {20*59}"
print(text4)

#string capitalize
text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)

#string casefold
title = "Cien Años de Soledad"
titleConvert = title.casefold()
print(titleConvert)

#string center
fruit = "mamahuevo"
textcenter = fruit.center(20, "#")
print(textcenter)

#string count()
title1 = "I love apples, apple are y favorite fruit"
result2 = title1.count("apple")
print(result2)

#string endswith
text6 = "Curso, Fundamentos con Python."
result3 = text6.endswith(".")
print(result3)

#string expandtabs
letter = "F\tU\tP"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#string find
text7 = "Hola, bienvenidos a Colombia."
result4 = text7.find("bienvenidos")
print(result4)

#funcion title
text8 = "welcome to the jungle"
result5 = text8.title()
print(result5)

#funcion isalnum
alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)

#Funcion isalpha
letters = "Space X"
result7 = letters.isalpha()
print(result7)