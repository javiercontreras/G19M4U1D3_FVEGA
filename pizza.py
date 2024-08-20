class Disponibles:
    vegetales_disponibles = {'tomate':True,'aceitunas':True,'champiñones':True,'Alcaparras':False}
    proteicos_disponibles = {'pollo':True,'vacuno':True,'camarones':False,'carne vegetal':True}

    @staticmethod
    def vegetales():
        vegetales = Disponibles.vegetales_disponibles
        return [ k for k,v in vegetales.items() if v== True]
    
    @staticmethod
    def proteicos():
        proteicos= Disponibles.proteicos_disponibles
        return [ k for k,v in proteicos.items() if v== True]


class Pizza():
    precio = 10000
    ing_vegetales = []
    ing_proteico = []
    ing_masas = ["masa tradicional","masa delgada"]

    def pedir_pizza(self):
       self.vegetal_1 = self.imprimir_opciones(self.ing_vegetales)
       self.vegetal_2 = self.imprimir_opciones(self.ing_vegetales)
       self.proteico = self.imprimir_opciones(self.ing_proteico)
       self.masa = self.imprimir_opciones(self.ing_masas)
       self.valida = self.validar_ingrediente(self.vegetal_1, self.ing_vegetales) & self.validar_ingrediente(self.vegetal_2, self.ing_vegetales) & self.validar_ingrediente(self.proteico, self.ing_proteico) & self.validar_ingrediente(self.masa, self.ing_masas) 
       pass
    
    @staticmethod
    def imprimir_opciones( lista):
        count = 0
        print("\nEliga un de los siguiente ingredientes, seleccione el numero asociado")
        for i in lista:
            count +=1
            print(f" {count} : {i}")
        j = int(input("Su seleccion es : "))    
        return lista [j -1]

    @staticmethod
    def validar_ingrediente(ingrediente, disponibles):
        for i in disponibles:
            if i == ingrediente:
                return True
        return False
    
    @staticmethod
    def ingredientes_disponibles(vegetales, proteicos):
        Pizza.ing_proteico = proteicos
        Pizza.ing_vegetales = vegetales

    

if __name__=='__main__':

    vegetales = Disponibles.vegetales()
    proteicos = Disponibles.proteicos()
    Pizza.ingredientes_disponibles( vegetales, proteicos)

    Pizza.ingredientes_disponibles( vegetales, proteicos)
    pizza = Pizza()
