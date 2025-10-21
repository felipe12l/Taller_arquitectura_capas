import sqlite3
class Student:
    def __init__(self,name,id,carreer,semester):
        self.name = name
        self.id = id
        self.carreer = carreer
        self.semester = semester

    def get_student_info(self):
        return {
            "name": self.name,
            "id": self.id,
            "carreer": self.carreer,
            "semester": self.semester
        }
