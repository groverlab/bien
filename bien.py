class Course:
    def __init__(self, number, name, prereqs=[], coreqs=[]):
        self.number = number
        self.name = name
        self.prereqs = prereqs
        self.coreqs = coreqs
    def __str__(self):
        return self.number
    __repr__ = __str__
    satisfied = False


class Plan:
    def __init__(self, name):
        self.name = name
        self.courses = [[[], [], []],
                        [[], [], []],
                        [[], [], []],
                        [[], [], []]]
    def check_prereqs(self):
        self.set_all_satisfied(False)
        self.all_prereqs_OK = True
        for y, year in enumerate(self.courses):
            print(f"year {y}")
            for q, quarter in enumerate(year):
                print(f"  quarter {q}")
                for course in quarter:
                    print("    ", course)
                    course.satisfied = True  # first assume satisfied, then check prereqs
                    for p in course.prereqs:
                        print("      ", p, p.satisfied)
                        if not p.satisfied:
                            self.all_prereqs_OK = False
        print("all_prereqs_OK:", self.all_prereqs_OK)

    def set_all_satisfied(self, state):
        for course in courses:
                course.satisfied = False

courses = [
    bien001 := Course("BIEN001", "Freshmen Seminar"),
    chem001a := Course("CHEM001A/LA", "General Chemistry & Lab A"),
    engl001a := Course("ENGL001A", "Beginning Composition"),
    math009a := Course("MATH009A", "First Year Calculus"),

    biol005a := Course("BIOL005A/LA", "Cell & Molecular Biology & Lab"),
    chem001b := Course("CHEM001B/LB", "General Chemistry & Lab B"),
    engl001b := Course("ENGL001B", "Intermediate Composition"),
    math009b := Course("MATH009B", "First Year Calculus"),

    biol005b := Course("BIOL005B", "Organismal Biology"),
    chem001c := Course("CHEM001C/LC", "General Chemistry & Lab C"),
    engl001c := Course("ENGL001C/alt", "Applied Intermediate Composition"),
    math009c := Course("MATH009C", "First Year Calculus"),

    bien010 := Course("BIEN010", "Overview of Bioengineering"),
    math046 := Course("MATH046", "Differential Equations"),
    phys040a := Course("PHYS040A", "Physics (Mechanics)"),

    chem008a := Course("CHEM008A/LA", "Organic Chemistry A"),
    cs009a := Course("CS009A", "Python"),
    math010a := Course("MATH010A", "Multivariable Calculus A"),
    phys040b := Course("PHYS040B", "Physics (Heat/Waves/Sound)"),

    chem008b := Course("CHEM008B/LB", "Organic Chemistry B"),
    math010b := Course("MATH010B", "Multivariable Calculus B"),
    phys040c := Course("PHYS040C", "Physics (Electricity/Magnetism)"),

    bien101 := Course("BIEN101", "Quantitative Biochemistry", [biol005a, chem008a, math046]),
    bien110 := Course("BIEN110", "Biomechanics of the Human Body", [chem001c, cs009a, math010a, phys040b]),
    bien111 := Course("BIEN111", "Statistics for Bioengineers", [math009c]),
    ee005 := Course("EE005", "Circuits and Electronics"),

    bien105 := Course("BIEN105", "Circulation Physiology", [bien110]),
    bien125 := Course("BIEN125", "Biotechnology & Molecular Engineering", [bien101]),
    bien140a := Course("BIEN140A", "Biomaterials", [bien101, math010b, phys040b]),

    bien115 := Course("BIEN115", "Quantitative Physiology", [bien110]),
    bien120 := Course("BIEN120", "Biosystems & Signal Analysis", [bien105]),
    bien130 := Course("130", "Bioinstrumentation", [ee005]),
    bien130l := Course("130L", "Bioinstrumentation Laboratory", [ee005], [bien130]),

    bien175a := Course("BIEN175A", "Senior Design A", [bien010, bien130l]),
    bien135 := Course("BIEN135", "Biophysics & Biothermodynamics", [bien101, math010b, math046, phys040c]),
    bien155 := Course("BIEN155", "Biotechnology Lab", [bien101, bien125], [bien175a]),

    bien175b := Course("BIEN175B", "Senior Design B", [bien175a]),

    bien175c := Course("BIEN175C", "Senior Design C", [bien175b]),
]




current = Plan("current")
current.courses = [[[bien001, chem001a, engl001a, math009a],
              [biol005a, chem001b, engl001b, math009b],
              [biol005b, chem001c, engl001c, math009c]],
              [[bien010, math046, phys040a],
               [chem008a, cs009a, math010a, phys040b],
               [chem008b, math010b, phys040c]],
               [[bien101, bien110, bien111, ee005],
                [bien105, bien125, bien140a],
                [bien115, bien120, bien130, bien130l]],
                [[bien175a, bien135, bien155],
                 [bien175b],
                 [bien175c]]]
current.check_prereqs()



second_offering = Plan("second_offering")
second_offering.courses = [[[bien001, chem001a, engl001a, math009a],
              [biol005a, chem001b, engl001b, math009b],
              [biol005b, chem001c, engl001c, math009c]],
              [[bien010, math046, phys040a],
               [chem008a, cs009a, math010a, phys040b],
               [chem008b, math010b, phys040c]],
               [[bien101, bien111, ee005],  # 3rd year Fall
                [bien125, bien140a, bien110],  # 3rd year Winter
                [bien130, bien130l, bien105]],  # 3rd year Spring
                [[bien175a, bien155, bien115, bien120],  # 4th year Fall
                 [bien175b, bien135],  # 4th year Winter
                 [bien175c]]]  # 4th year Spring
second_offering.check_prereqs()

