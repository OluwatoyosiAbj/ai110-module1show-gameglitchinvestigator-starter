from logic_utils import check_guess, get_range_for_difficulty, parse_guess

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


# ============================================
# CHALLENGE 1: EDGE-CASE TESTING
# ============================================

def test_parse_negative_number():
    # Edge case: Negative numbers should parse successfully
    # Reason: Player might accidentally enter negative (the game should handle gracefully)
    ok, guess, error = parse_guess("-50")
    assert ok is True
    assert guess == -50
    assert error is None

def test_parse_very_large_number():
    # Edge case: Very large numbers (beyond game range)
    # Reason: Players might typo "999999999999" — parse should succeed, validation happens elsewhere
    ok, guess, error = parse_guess("999999999999")
    assert ok is True
    assert guess == 999999999999
    assert error is None

def test_parse_decimal_truncates():
    # Edge case: Decimal input "50.9" should truncate to 50, not round
    # Reason: Game allows floats but converts to int; verify truncation behavior
    ok, guess, error = parse_guess("50.9")
    assert ok is True
    assert guess == 50  # int(float("50.9")) = 50, not 51
    assert error is None

def test_parse_scientific_notation_fails():
    # Edge case: Scientific notation "1e2" should NOT parse (game rejects it)
    # Reason: Game uses simple int() parsing, not scientific notation support
    # This is acceptable because players rarely use scientific notation
    ok, guess, error = parse_guess("1e2")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."

def test_parse_leading_trailing_whitespace():
    # Edge case: "  50  " with whitespace
    # Reason: Input might come from web form with accidental spaces
    ok, guess, error = parse_guess("  50  ")
    assert ok is True
    assert guess == 50
    assert error is None

def test_parse_multiple_dots_fails():
    # Edge case: "50.50.50" should fail (multiple decimal points)
    # Reason: Verify error handling for malformed decimals
    ok, guess, error = parse_guess("50.50.50")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."

def test_parse_alphanumeric_fails():
    # Edge case: "50abc" should fail
    # Reason: Mixed alphanumeric is not a valid number
    ok, guess, error = parse_guess("50abc")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."

def test_parse_empty_string():
    # Edge case: Empty string ""
    # Reason: User might submit without typing anything
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."

def test_parse_none_input():
    # Edge case: None input (shouldn't happen in UI, but good defensive programming)
    # Reason: Defensive programming — catch unexpected None values
    ok, guess, error = parse_guess(None)
    assert ok is False
    assert guess is None
    assert error == "Enter a guess."

def test_parse_special_characters():
    # Edge case: Special characters "#$%^" should fail
    # Reason: Verify rejection of non-numeric input
    ok, guess, error = parse_guess("#$%^")
    assert ok is False
    assert guess is None
    assert error == "That is not a number."

def test_check_guess_with_zero():
    # Edge case: Secret is 0 (boundary value)
    # Reason: Zero is a valid but unusual guess
    outcome, message = check_guess(1, 0)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_check_guess_boundary_1():
    # Edge case: Boundary test at 1 and 2
    # Reason: Verify comparison works at lowest game boundary
    outcome, message = check_guess(1, 2)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_check_guess_negative_secret():
    # Edge case: Negative secret number (shouldn't happen in game, but function should handle it)
    # Reason: Defensive test for comparison logic
    outcome, message = check_guess(10, -5)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_parse_zero():
    # Edge case: Zero input "0"
    # Reason: Zero is a boundary value; should parse successfully
    ok, guess, error = parse_guess("0")
    assert ok is True
    assert guess == 0
    assert error is None

def test_parse_float_zero():
    # Edge case: Decimal zero "0.0"
    # Reason: Should convert to 0 integer
    ok, guess, error = parse_guess("0.0")
    assert ok is True
    assert guess == 0
    assert error is None
