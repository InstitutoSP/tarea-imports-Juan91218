def sumar(a,b):
   print("el resultado es: ", (a+b))

def resta(a,b):
   print("el resultado es: ", (a-b))

def multiplicar(a,b):
   print("el resultado es: ", (a*b))

def division(a,b):
   print("el resultado es: ", (a/b))

   
def ordenar_de_menor(list1):
   stop= True
   list1_ord=[]
   list_temp=list1.copy()
   while stop:
      val_max=list_temp[0]
      for i in range(len(list_temp)):
         x=list_temp[i]

         if (x>val_max):
            val_max=x

      list1_ord.append(val_max)
      list_temp.remove(val_max)
      if len(list_temp)==0:
         stop= False
   return list1_ord

def ord_men_may(list2):
   stop= True
   list2_ord=[]
   list_temp=list2.copy()
   while stop:
      val_min=list_temp[0]
      for i in range(len(list_temp)):
         x=list_temp[i]

         if (x<val_min):
            val_min=x

      list2_ord.append(val_min)
      list_temp.remove(val_min)
      if len(list_temp)==0:
         stop= False
   return list2_ord


def nombre(list3):
   stop= True
   list3_ord=[]
   list_temp=list3.copy()

   while stop:
      letra_may=list_temp[0]
      for i in range(len(list_temp)):
         x=list_temp[i]

         if (x<letra_may):
            letra_may=x

      list3_ord.append(letra_may)
      list_temp.remove(letra_may)

      if len(list_temp)==0:
         stop= False
   return list3_ord