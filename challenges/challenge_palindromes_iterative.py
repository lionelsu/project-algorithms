def is_palindrome_iterative(word):
    if not word or word == '':
        return False

    # o índice da esquerda começa em 0 e o da direita começa na última letra.
    # ana tem 3 letras, mas o índice da última letra é 2 por isso o length -1.
    left_index, rigth_index = 0, len(word) - 1

    # enquanto o índice da esquerda for menor que o da direita.
    while left_index < rigth_index:
        # do índice esquerdo for diferente da letra do índice direito.
        # , não é palíndromo.
        if word[left_index] != word[rigth_index]:
            return False
        # incrementa o índice da esquerda e decrementa o da direita.
        left_index += 1
        rigth_index -= 1
        # repete até que o índice da esquerda seja maior que o da direita.
    return True
