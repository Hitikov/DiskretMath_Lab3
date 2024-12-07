from funcs import *

# 0101110101011101 > W, Y-Z 0100000000001111

strr = input()

print('Таблица истиности')
print_value_table(strr)

res = getSDNFarray(strr)
print('СДНФ: ', end='')
printStatment(res)

sknf = getSKNFarray(strr)
printSKNF(sknf)

sub_res = minimize(res)
print('МДНФ: ', end='')
printStatment(sub_res)

print('Импликантная матрица')
print_implication_table(res,sub_res )