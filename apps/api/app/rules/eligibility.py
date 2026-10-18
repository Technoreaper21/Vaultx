from typing import Dict, Any, List, Tuple

def evaluate_eligibility(opportunity_rules: Dict[str, Any], student_profile: Dict[str, Any]) -> List[Tuple[str, bool, str]]:
    """
    Evaluate eligibility for an opportunity based on rules and student profile.
    Returns a list of tuples: (criterion, passed, explanation)
    """
    results = []

    # Age checks
    if "min_age" in opportunity_rules:
        min_age = opportunity_rules["min_age"]
        student_age = student_profile.get("age", 0)
        passed = student_age >= min_age
        results.append((
            "min_age",
            passed,
            f"Age {student_age} >= {min_age}" if passed else f"Age {student_age} < {min_age}"
        ))
    if "max_age" in opportunity_rules:
        max_age = opportunity_rules["max_age"]
        student_age = student_profile.get("age", 0)
        passed = student_age <= max_age
        results.append((
            "max_age",
            passed,
            f"Age {student_age} <= {max_age}" if passed else f"Age {student_age} > {max_age}"
        ))

    # Grade check (assuming student_profile has 'grade' as integer or string)
    if "min_grade" in opportunity_rules:
        min_grade = opportunity_rules["min_grade"]
        student_grade = student_profile.get("grade", 0)
        # Try to convert to int if possible
        try:
            student_grade_int = int(student_grade)
            passed = student_grade_int >= min_grade
        except ValueError:
            passed = False
        results.append((
            "min_grade",
            passed,
            f"Grade {student_grade} >= {min_grade}" if passed else f"Grade {student_grade} < {min_grade}"
        ))

    # Subjects: check if student has at least one of the required subjects
    if "subjects" in opportunity_rules:
        required_subjects = set(opportunity_rules["subjects"])
        student_subjects = set(student_profile.get("subjects", []))
        passed = len(required_subjects.intersection(student_subjects)) > 0
        results.append((
            "subjects",
            passed,
            f"Has at least one of {required_subjects}" if passed else f"Does not have any of {required_subjects}"
        ))

    # Education level
    if "education" in opportunity_rules:
        required_education = set(opportunity_rules["education"])
        student_education = student_profile.get("education", "")
        passed = student_education in required_education
        results.append((
            "education",
            passed,
            f"Education '{student_education}' in {required_education}" if passed else f"Education '{student_education}' not in {required_education}"
        ))

    # Gender
    if "gender" in opportunity_rules:
        allowed_genders = set(opportunity_rules["gender"])
        student_gender = student_profile.get("gender", "")
        passed = student_gender in allowed_genders
        results.append((
            "gender",
            passed,
            f"Gender '{student_gender}' allowed" if passed else f"Gender '{student_gender}' not allowed"
        ))

    # Custom: add more criteria as needed

    return results

def is_eligible(opportunity_rules: Dict[str, Any], student_profile: Dict[str, Any]) -> bool:
    """Return True if all criteria pass."""
    results = evaluate_eligibility(opportunity_rules, student_profile)
    return all(passed for _, passed, _ in results)