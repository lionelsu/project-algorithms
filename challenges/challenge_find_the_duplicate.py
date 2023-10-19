"""
Esta versão considera que podem haver mais de um número duplicado.
e caso houver, retorna o número que aparece mais de uma vezes.
O exercício proposto considera que a lista terá apenas um número duplicado.
e todos os outros serão diferentes, então, não é necessário tanta complexidade.
def find_duplicate(nums):
    last_index = {}
    duplicate = None
    for i, num in enumerate(nums):
        if not isinstance(num, int) or num < 0:
            return False
        if num in last_index:
            duplicate = num
        last_index[num] = i

    if duplicate is not None:
        return duplicate
    return False
"""


def find_duplicate(nums):
    count = set()
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if num in count:
            return num
        count.add(num)
    return False
