class Student(object):
    def __init__(self, uid, last_name, first_name, matric_number):
        self.uid = uid
        self.last_name = last_name
        self.first_name = first_name
        self.matric_number =  matric_number

    def __str__(self):
        return """
        UID: %s,
        Last Name: %s,
        First Name: %s,
        Matric Number: %s
        """%(self.uid,self.last_name,self.first_name,self.matric_number)