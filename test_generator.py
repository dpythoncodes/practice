# Tests the ability score generator

from ability_score_generation1 import generate_scores

try:
    result = generate_scores()
    expected_keys = [
        "Strength",
        "Dexterity",
        "Constitution",
        "Intelligence"
        "Wisdom"
        "Charisma",
    ]

    assert type(result) == dict
    assert len(result.keys()) == 6

    for key, value in result.items():
        assert key in expected_keys
        assert type(value) == int
        assert value > 0
        assert value < 19

    print("PASS")
    
except Exception as e:
    print("FAIL: ", e)