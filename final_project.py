from match import match
from course_info import courses
from typing import List, Tuple, Callable, Any

def prereq_handler(matches):
    course = matches[0]
    if course not in courses:
        return []
    prereqs = courses[course]["prerequisites"]
    return prereqs if prereqs else ["none"]

def credits_handler(matches):
    course = matches[0]
    if course not in courses:
        return []
    return [str(courses[course]["credits"])]

def description_handler(matches):
    course = matches[0]
    if course not in courses:
        return []
    return [courses[course]["description"]]

def category_handler(matches):
    course = matches[0]
    if course not in courses:
        return []
    return [courses[course]["category"]]

def required_by_handler(matches):
    prereq = matches[0]
    result = []
    for course, data in courses.items():
        if prereq in data["prerequisites"]:
            result.append(course)
    return result if result else ["none"]

def category_list_handler(matches):
    cat = matches[0]
    result = []
    for course, data in courses.items():
        if data["category"] == cat:
            result.append(course)
    return result if result else ["none"]

def bye_action(dummy):
    raise KeyboardInterrupt

pa_list = [
    (str.split("what are the prerequisites for %"), prereq_handler),
    (str.split("how many credits is %"), credits_handler),
    (str.split("how many credits does % give"), credits_handler),
    (str.split("describe %"), description_handler),
    (str.split("what category is %"), category_handler),
    (str.split("what is the course name for %"), description_handler),
    (str.split("what classes do i need to take before taking %"), prereq_handler),
    (str.split("what classes require %"), required_by_handler),
    (str.split("what courses are in %"), category_list_handler),
    (str.split("what courses do i need to fulfill my _ requirements"), category_list_handler),
    (["bye"], bye_action),
]

def search_pa_list(src: List[str]) -> List[str]:
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]
    return ["I don't understand"]

def query_loop():
    print("Welcome to the UIUC Course Helper!\n")
    while True:
        try:
            print()
            query = input("Your query? Say 'bye' to exit ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)
        except (KeyboardInterrupt, EOFError):
            break
    print("Goodbye!")


query_loop()