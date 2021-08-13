class Section:

    def __init__(self, section_id, cname):
        self.section_id = section_id
        self.cname = cname


class Student(Section):

    def __init__(self, student_id, name, email, section_id, cname):
        super().__init__(section_id, cname)   # here super() point to base class ie. Section.__init__(section_id, cname)
        self.student_id = student_id
        self.name = name
        self.email = email
        self.roaster = {self.student_id: {'name': self.name,
                                          'email': self.email}
                        }



