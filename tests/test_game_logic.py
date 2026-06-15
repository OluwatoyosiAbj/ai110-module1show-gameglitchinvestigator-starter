from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" with "Go LOWER!" message
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    # FIX: Verify that the hint direction is now CORRECT (Go LOWER when too high)
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" with "Go HIGHER!" message
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_hard_difficulty_range():
    # FIX: Hard difficulty should have a larger range than Normal to be actually harder
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    assert easy_high - easy_low < normal_high - normal_low, "Easy should have smaller range than Normal"
    assert hard_high - hard_low > normal_high - normal_low, "Hard should have larger range than Normal"

    # Hard should be 1-200
    assert hard_low == 1 and hard_high == 200, "Hard difficulty should be 1-200"
