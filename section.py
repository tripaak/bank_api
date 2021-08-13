class Section:

    def __init__(self, section_id, cname, student_id, name, email):
        self.student_id = student_id
        self.section_id = section_id
        self.cname = cname
        self.name = name
        self.email = email
        self.roaster = {
            self.student_id: {
                'name': self.name,
                'email': self.email,

            },
        }

    def add_student(self, student_id, name, email):
        self.roaster[student_id] = {'name': name,
                                    'email': email}

    def get_roaster(self):
        print(self.roaster)

    def drop_student(self, student_id):
        self.roaster.pop(student_id)

    def search_student(self, student_id):
        return self.roaster.get(student_id)



