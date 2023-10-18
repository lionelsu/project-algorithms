def custom_c_sort(string):
    # cria uma lista com 26 posições, uma para cada letra do alfabeto.
    counts = [0] * 26

    # para cada letra na string, incrementa o contador da letra correspondente.
    for char in string:
        char = char.lower()
        # vai adicionar +1 no counts
        # , na posição da letra correspondente ao alfabeto.
        counts[ord(char) - ord('a')] += 1

    # cria uma lista com o número de ocorrências de cada letra.
    # a saída é algo assim ['aa', '', '', 'b', '', '', ..., '']
    result = [chr(i + ord('a')) * counts[i] for i in range(26)]

    # retorna a lista concatenada em uma string.
    return ''.join(result)


def is_anagram(first_string, second_string):
    # se uma das strings for vazia, retorna False.
    if not first_string or not second_string:
        return custom_c_sort(first_string), custom_c_sort(second_string), False

    sorted_first = custom_c_sort(first_string)
    sorted_second = custom_c_sort(second_string)

    # retorno ordenado em uma tupla.
    return sorted_first, sorted_second, sorted_first == sorted_second
