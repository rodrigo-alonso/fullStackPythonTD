# Definir una funcion es_palindromo() que reconoce palindromos
# es decir, palabras que tienen el mismo aspecto escritas invertidas),
# ejemplo: es_palindromo("radar") tendria que devolver True.
# No se pueden utilizar funciones preconstruidas en python
# y tampoco indexado al reves

def es_palindromo(string):
    # return string == string[::-1]
    for i in range(len(string)):
        if string[i] == string[len(string) - i - 1]:
            return True
    return False

if __name__ == "__main__":
    print(es_palindromo('casa'))