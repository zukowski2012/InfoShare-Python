#my_list = [1,2,3,4,5]
#print(my_list)


#for cyfra in my_list:
#    print(cyfra)


# lista_liter = ['k', 'o', 'w', 'a', 'l', 's', 'k', 'i']
# string_z_listy = "".join(lista_liter)
# print(string_z_listy)
# string_z_listy = "_".join(lista_liter)
# print(string_z_listy)

lista_zakupow = ["jajko", "długopis", "kura"]

# opcja 1: for
for rzecz_do_kupienia in lista_zakupow:
    print(rzecz_do_kupienia)

# opcja 2
co_kupic = ", ".join(lista_zakupow)
print("Chciałbym kupić {}".format(co_kupic))

###
magic = "abracadabra"
for i in range(len(magic)):
    print(i, magic[i])