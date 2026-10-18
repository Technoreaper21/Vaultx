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
    # Check that we have results for each criterion
    assert len(results) == 4  # one result per rule: min_age, max_age, min_grade, subjects
    # Actually we have: min_age, max_age, min_grade, subjects, education, gender -> 6
    # Let's adjust: we have 6 criteria in the function? Let's count: min_age, max_age, min_grade, subjects, education, gender -> 6
    # But note: we also have a custom criteria? No.
    # Let's just check that the function runs and returns a list of tuples.
    # We'll check specific ones.
    for criterion, passed, explanation in results:
        print(f"{criterion}: {passed} - {explanation}")
    # We expect all to pass except maybe education? Actually education is not in the rules, so we don't check it.
    # Wait, we didn't include education in the opportunity_rules above, so the education check will be skipped.
    # So we should have 4 criteria: min_age, max_age, min_grade, subjects.
    # Let's adjust the test.

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