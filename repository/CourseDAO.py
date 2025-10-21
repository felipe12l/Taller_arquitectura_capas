import sqlite3
class CourseDAO:
    def __init__(self, db_connection):
        self.conn = db_connection

    def get_all_courses(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        return courses

    def get_course_by_id(self, course_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE id = ?", (course_id,))
        course = cursor.fetchone()
        return course

    def add_course(self, name, description, credits):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO courses (name, description, credits) VALUES (?, ?, ?)",
            (name, description, credits)
        )
        self.conn.commit()
        return cursor.lastrowid

    def update_course(self, course_id, name=None, description=None, credits=None):
        cursor = self.conn.cursor()
        fields = []
        values = []
        if name is not None:
            fields.append("name = ?")
            values.append(name)
        if description is not None:
            fields.append("description = ?")
            values.append(description)
        if credits is not None:
            fields.append("credits = ?")
            values.append(credits)
        values.append(course_id)
        sql = f"UPDATE courses SET {', '.join(fields)} WHERE id = ?"
        cursor.execute(sql, tuple(values))
        self.conn.commit()

    def delete_course(self, course_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM courses WHERE id = ?", (course_id,))
        self.conn.commit()