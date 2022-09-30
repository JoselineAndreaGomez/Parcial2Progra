class estudiantes:
    def __init__(self,nombre,grado, promedio):
        self.__nombre=nombre
        self.__grado=grado
        self.__promedio=promedio

    #métodos getter
    def vernombre(self):
        return self.__nombre
     
    def vergrado(self):
        return self.__grado

    def verpromedio(self):
        return self.__promedio
    
    #métodos setter
    def modificarnombre(self,nuevonombre):
        self.__nombre=nuevonombre
    
    def modificargrado(self,nuevogrado):
        self.__grado=nuevogrado

    def modificarpromedio(self,nuevopromedio):
        self.__promedio=nuevopromedio
    