__author__ = 'lidan'
class GradeEntry:
    """
    A grade entry must keep track of three things:
  -- a course identifier, such as "CSC148".  This is the course
     in which the grade was earned.
  -- a course weight: 1.0 credits for a half-course, 2.0 credits
     for a full course
  -- a course grade, which has no meaningful value unless we know
     whether letter grades or numeric grades are used
A grade entry must also be able to generate how many points it is worth, based
on its grade.  The details of how points are generated are left
out unless we know whether letter or numeric grades are used.
    """
    def __init__(self,course_name, course_weight,course_grade):
        """
        Create grade entry to keep track of course name, course
        weight, and course grade.

        @param GradeEntry self: this GradeEntry object
        @param course_name: str
        @param course_weight: int
        @param course_grade: int/str
        """
        self.course_name = course_name
        self.course_weight = course_weight
        self.course_grade = course_grade

    def __str__(self):
        """
        Return an informative string describing self.
        @type GradeEntry self: this GradeEntry object
        @rtype: str
        """
        return type(self).__name__+\
               "the weight of {} is {}, the grade is {}, numeric grade" \
               "is {}, letter grade is {}".format(
                   self.course_name,self.course_weight,self.course_grade,
               )

    def __eq__(self,other):
        """
        Return whether GradeEntry object is equivalent to other

        @param GradeEntry self: this GradeEntry object
        @param GradeEntry|Any other: object to be compared to
        @rtype: bool
        """
        return (type(self) == type(other)) and \
            (type(self.course_weight) == type (other.course_weight)) \
               and (type(self.course_grade) == type(other.course_grade)) and \
        (type(self.course_name) == type(other.course_name))

    def get_grade(self):
        """
        Return the point grade of the course.
        @param GradeEntry self: this GradeEntry object.
        @rtype: int
        """
        raise NotImplementedError('subclass needed')


class NumericGradeEntry(GradeEntry):
    """
    A numeric grade entry is a grade entry for which the grade is an integer between 0
and 100 (inclusive).  A numeric grade entry generates grade points based on its
grade, according to the following table:

value   points
--------------------
90-100  4.0
85-89	4.0
80-84 	3.7
77-79 	3.3
73-76	3.0
70-72 	2.7
67-69 	2.3
63-66	2.0
60-62 	1.7
57-59 	1.3
53-56	1.0
50-52 	0.7
0-49 	0.0
    """
    def __init__(self,course_name, course_weight,course_grade):
        GradeEntry.__init__(self,course_name,course_weight,course_grade)


    def get_grade(self):
        """
        Return the point grade of the course.
        @param GradeEntry self: this GradeEntry object.
        @rtype: int
        """
        if 85 <= self.course_grade <= 100:
            return 4.0
        elif 80 <= self.course_grade <= 84:
            return 3.7
        elif 77 <= self.course_grade <= 79:
            return 3.3
        elif 73<= self.course_grade <= 76:
            return 3.0
        elif 70 <= self.course_grade <= 72:
            return 2.7
        elif 67 <= self.course_grade <= 69:
            return 2.3
        elif 63 <= self.course_grade <= 66:
            return 2.0
        elif 60 <= self.course_grade <= 62:
            return 1.7
        elif 57 <= self.course_grade <= 59:
            return 1.3
        elif 53 <= self.course_grade <= 56:
            return 1.0
        elif 50 <= self.course_grade <= 52:
            return 0.7
        else:
            return 0.0

class LetterGradeEntry(GradeEntry):
    """
    == LetterGradeEntry ==

Context: a course grade entry with letter grades

A letter grade entry is a grade entry for which the grade is a character.
The value of the grade is one of {A, B, C, D, F}, with a possible suffix from {+, -}.  A
LetterGradeEntry generates points, based on its grade, according to the
following table:

value   grade-point
-------------------
A+ 	4.0
A 	4.0
A- 	3.7
B+ 	3.3
B 	3.0
B- 	2.7
C+ 	2.3
C 	2.0
C- 	1.7
D+ 	1.3
D 	1.0
D- 	0.7
F 	0.0
    """
    def __init__(self,course_name, course_weight,course_grade):
        GradeEntry.__init__(self,course_name,course_weight,course_grade)

    def get_grade(self):
        """
        Return the point grade of the course.
        @param GradeEntry self: this GradeEntry object.
        @rtype: int
        """
        if self.course_grade == 'A+':
            return 4.0
        elif self.course_grade == 'A':
            return 4.0
        elif self.course_grade == "A-":
            return 3.7
        elif self.course_grade == "B+":
            return 3.3
        elif self.course_grade == "B":
            return 3.0
        elif self.course_grade == "B-":
            return 2.7
        elif self.course_grade == "C+":
            return 2.3
        elif self.course_grade == "C":
            return 2.0
        elif self.course_grade == "C-":
            return 1.7
        elif self.course_grade == "D+":
            return 1.3
        elif self.course_grade == "D":
            return 1.0
        elif self.course_grade == "D-":
            return 0.7
        else:
            return 0.0



