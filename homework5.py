immutable_var = (1, 2, 3, 'a', 'b')
print(immutable_var)
mutable_list = ([1, 'a', 'b', 4], 'string')
mutable_list[0][3] = 10
print(mutable_list)
immutable_var[1] = 50
print(immutable_var)
#Ошибка типа объект кортеж не поддерживает назначение элементов