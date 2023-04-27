class Estudiante:
    def __init__(self, nombre, edad, grado, escuela) -> None:
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.escuela = escuela
        self.calificaciones_esp = None
        self.calificaciones_mat = None
        self.calificaciones_nat = None
        self.calificaciones_sol = None
        self.becado = None
        self.reprobado = None
        
    def cambiar_esp(self, num):
        self.calificaciones_esp = num
        return f"Nueva calificacion: {num}"
    
    def cambiar_mat(self, num):
        self.calificaciones_mat = num
        return f"Nueva calificacion: {num}"
    
    def cambiar_nat(self, num):
        self.calificaciones_nat = num
        return f"Nueva calificacion: {num}"
    
    def cambiar_sol(self, num):
        self.calificaciones_sol = num
        return f"Nueva calificacion: {num}"