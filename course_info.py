from typing import Dict, Tuple


courses = {
    "cs 124": {
        "credits": 3,
        "prerequisites": [],
        "description": "introduction to computer science i",
        "category": "major"
    },
    "cs 128": {
        "credits": 3,
        "prerequisites": ["cs 124"],
        "description": "introduction to computer science ii",
        "category": "major"
    },
    "cs 173": {
        "credits": 3,
        "prerequisites": ["cs 124"],
        "description": "discrete structures",
        "category": "major"
    },
    "math 221": {
        "credits": 4,
        "prerequisites": [],
        "description": "calculus i",
        "category": "major"
    },
    "math 231": {
        "credits": 3,
        "prerequisites": ["math 221"],
        "description": "calculus ii",
        "category": "major"
    },
    "math 241": {
        "credits": 4,
        "prerequisites": ["math 231"],
        "description": "calculus iii",
        "category": "major"
    },
    "cs 225": {
        "credits": 4,
        "prerequisites": ["cs 128"],
        "description": "data structures",
        "category": "major"
    },
    "cs 374": {
        "credits": 4,
        "prerequisites": ["cs 173", "cs 225"],
        "description": "introduction to algorithms",
        "category": "major"
    },
    "phys 211": {
        "credits": 4,
        "prerequisites": ["math 231"],
        "description": "physics: mechanics",
        "category": "major"
    },
    "phys 212": {
        "credits": 4,
        "prerequisites": ["math 231"],
        "description": "physics: electricity & magnetism",
        "category": "major"
    },
    "psych 100": {
        "credits": 4,
        "prerequisites": [],
        "description": "introductory psychology",
        "category": "gened"
    },
    "econ 102": {
        "credits": 3,
        "prerequisites": [],
        "description": "microeconomic principles",
        "category": "gened"
    },
    "econ 103": {
        "credits": 3,
        "prerequisites": [],
        "description": "macroeconomic principles",
        "category": "gened"
    },
    "astr 122": {
        "credits": 3,
        "prerequisites": [],
        "description": "stars and galaxies",
        "category": "gened"
    },
    "educ 205": {
        "credits": 3,
        "prerequisites": [],
        "description": "introduction to learning and education studies",
        "category": "gened"
    },
    "anth 101": {
        "credits": 3,
        "prerequisites": [],
        "description": "introduction to anthropology",
        "category": "gened"
    },
    "stat 200": {
        "credits": 3,
        "prerequisites": [],
        "description": "statistical analysis",
        "category": "minor"
    },
    "stat 400": {
        "credits": 4,
        "prerequisites": ["math 231"],
        "description": "statistics and probability i",
        "category": "minor"
    },
    "stat 425": {
        "credits": 3,
        "prerequisites": ["stat 400"],
        "description": "statistical modeling i",
        "category": "minor"
    },
    "stat 426": {
        "credits": 3,
        "prerequisites": ["stat 410", "stat 425"],
        "description": "statistical modeling ii",
        "category": "minor"
    },
    "stat 431": {
        "credits": 3,
        "prerequisites": ["stat 410", "knowledge of r language"],
        "description": "applied bayesian analysis",
        "category": "minor"
    }
}
