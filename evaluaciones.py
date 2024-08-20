from pizza import Pizza, Disponibles

#Se agregan los ingredientes disponibles o de temporada a la clase Pizza
vegetales = Disponibles.vegetales()
proteicos = Disponibles.proteicos()
Pizza.ingredientes_disponibles( vegetales, proteicos)
#Se impimen los atributes de clase sin crear instancia
print("\n-5.a---------")
print(Pizza.ing_vegetales)
print(Pizza.ing_proteico)
print(Pizza.ing_masas)
print(Pizza.precio)
print("\n-5.b---------")
print(Pizza.validar_ingrediente('salsa de tomate',['salsa de tomate', 'salsa bbq']))
print("\n-5.c---------")
pizza = Pizza()
pizza_valida = pizza.pedir_pizza()