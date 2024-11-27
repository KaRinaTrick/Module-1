immutable_var = (1,2,1.5,"Water", False,[2,4])
print(immutable_var)
# immutable_var [2] = 1
# print(immutable_var) # кортеж является НЕизменяемым списком, поэтому нельзя изменить значение элемента кортежа
mutable_list = [1,4,'a','g',"Garick"]
mutable_list.append(False)
mutable_list[0] = 3
mutable_list[4] = "Masha"
print(mutable_list)





