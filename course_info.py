from typing import List, Tuple

# format:
# ("course number", "# credits", "prereqs", "course name", "gened/major requirement?")

course_db = [
    ("cs 124", 3, [], "introduction to computer science i", "major"),
    ("cs 128", 3, ["cs 124"], "introduction to computer science ii", "major"),
    ("cs 173", 3, ["cs 124"], "discrete structures", "major"),
    ("math 221", 4, [], "calculus i", "major"),
    ("math 231", 3, ["math 221"], "calculus ii", "major"),
    ("math 241", 4, ["math 231"], "calculus iii", "major"),
    ("cs 225", 4, ["cs 128"], "data structures", "major")
    ()
    ("psych 100", 4, [], "Introductory psychology.", "gened"),
    ("econ 102", 3, [], "Microeconomic principles.", "gened"),
    ("econ 103", 3, [], "Macroeconomic principles.", "gened"),
    ()
    ()
    ()
    ()
    ()
    ()
    
]