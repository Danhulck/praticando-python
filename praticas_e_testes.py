#  

# def deletItem_lista(lista, item):
#     for objeto in lista:
#         if item.upper() == objeto.upper():
#             lista.remove(objeto)
# lista = []
# user = True 
# while user == True:
#     try:
#         print("===================MENU===================")
#         menu = int(input("[1]Inserir  [2]Deletar [3]Listar [4] Finalizar  "))
#         if menu >= 1 and menu <= 4:            
#             if menu == 1:
#                 Item = input("Qual o Item você gostaria de inserir na lista  ")
#                 lista.append(Item)
#             if menu == 2:
#                 Item = input("Qual o Item você gostaria de deletar da lista  ")
#                 deletItem_lista(lista, Item)
#             if menu == 3:
#                 print(lista)
#             if menu == 4:
#                 user = False
#         else: 
#             if menu < 1:
#                 print("escolha um número positivo maior que 0 e menor que 5")
#             else:
#                 print("escolha um número menor que 5 e maior que 0")
#     except:
#         print("ERRO")
#         print("Insira um valor válido (um número maior que 0 e menor que 5)".upper)
# print("FIm do Programa")
