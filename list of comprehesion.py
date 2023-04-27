list_fruits = ["Manzana", "Naranja", "Pera,", "Uva", "Durazno", "Melocoton"]

list_comprehesion_fruits = [x for x in list_fruits if "M" in x]


operators = ["1+1", "2*1", "9/5"]

list_comprehesion_operators = [eval(x) for x in operators]
print(list_comprehesion_operators)
