import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))
from app.rules.eligibility import evaluate_eligibility, is_eligible

def test_eligibility_evaluate():
    opportunity_rules = {
        "min_age": 14,
        "max_age": 20,
        "min_grade": 9,
        "subjects": ["science", "math"]
    }
    student_profile = {
        "age": 15,
        "grade": 9,
        "subjects": ["science"],
        "education": "high_school",
        "gender": "male"
    }
    results = evaluate_eligibility(opportunity_rules, student_profile)
    # Print results for verification
    for criterion, passed, explanation in results:
        print(f"{criterion}: {passed} - {explanation}")
    # Check that we have results for each criterion
    assert len(results) == 4  # min_age, max_age, min_grade, subjects

def test_eligibility_is_eligible():
    opportunity_rules = {
        "min_age": 14,
        "max_age": 20,
        "min_grade": 9,
        "subjects": ["science", "math"]
    }
    student_profile_pass = {
        "age": 15,
        "grade": 9,
        "subjects": ["science"],
        "education": "high_school",
        "gender": "male"
    }
    student_profile_fail_age = {
        "age": 13,
        "grade": 9,
        "subjects": ["science"],
        "education": "high_school",
        "gender": "male"
    }
    assert is_eligible(opportunity_rules, student_profile_pass) == True
    assert is_eligible(opportunity_rules, student_profile_fail_age) == False

if __name__ == "__main__":
    test_eligibility_evaluate()
    test_eligibility_is_eligible()
    print("All tests passed")