class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def get_course_info(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "credits": self.credits
        }