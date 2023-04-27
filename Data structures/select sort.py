list_to_organize = [42, 28, 43, 26, 65, 60, 54, 51, 35, 42, 48, 33, 40, 58, 38, 64, 47, 44, 49, 46, 25, 57, 39, 55, 45, 29, 32, 61, 53, 31, 36, 56, 63, 30, 52, 27, 34, 50, 41, 37, 66, 62, 59]

def select_sort(lista):
   for i in range(len(lista)):
      mini = i
      
      for x in range(i+1,len(lista)):
         if lista[mini] > lista[x]:
            mini = x
      temp = lista[i]
      lista[i], lista[mini] = lista[mini], temp
      
   return lista

print(select_sort(list_to_organize))