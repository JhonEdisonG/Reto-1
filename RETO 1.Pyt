from typing_extensions import Self


class Estudiante:
    def __init__(self,ci,nombre,cursos)
        self.ci = ci
        self.nombre = nombre
        self.cursos = cursos

class Profesores:
    def __init__(self,cp,nombre,curso_dictado)
        self.cp = cp
        self.nombre = nombre
        self.curso_dictado = curso_dictado

class Cursos:
    def __init__(self,cc,nombre,estudiantes_matriculados,profesor_dicta)
        self.cc = cc
        self.nombre = nombre
        self.estudiantes_matriculados = estudiantes_matriculados
        self.profesor_dicta = profesor_dicta
