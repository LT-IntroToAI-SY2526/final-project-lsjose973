from match import match 
from course_info import courses
from typing import List, Tuple, Callable, Any

patterns = [
    (["what", "are", "the", "prerequisites", "for", "%"], "prereq"),
    (["how", "many", "credits", "is", "%"], "credits"),
    (["who", "teaches", "%"], "teacher"),
    (["how", "hard", "is", "%"], "difficulty"),
    (["describe", "%"], "description"),
]


def prereq_handler(course):
    if course not in courses:
        return "I don't know that course."
    prereqs = courses[course]["prerequisites"]
    if prereqs:
        return f"{course.upper()} requires: {', '.join(prereqs)}."
    return f"{course.upper()} has no prerequisites."

def credits_handler(course):
    if course not in courses:
        return "I don't know that course."
    return f"{course.upper()} is {courses[course]['credits']} credits."

def description_handler(course):
    if course not in courses:
        return "I don't know that course."
    return courses[course]["description"]

def category_handler(course):
    if course not in courses:
        return "I don't know that course."
    return courses[course]["category"]

pa_list = [
(str.split("what are the prerequisites for %", prereq_handler)),
(str.split("how many credits is %", credits_handler)),
(str.split("what is the description for %", description_handler))
]