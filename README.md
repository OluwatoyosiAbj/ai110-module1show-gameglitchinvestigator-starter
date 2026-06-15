# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game Purpose:** This is a number-guessing game built with Streamlit where the player tries to guess a randomly generated secret number within a range determined by the selected difficulty level. The game provides hints ("Too High" or "Too Low") and tracks score across multiple rounds. Three difficulty levels (Easy: 1-20, Normal: 1-100, Hard: 1-200) offer increasing challenges.

**Bugs Found:**
1. **Inverted Hint Directions** — When a guess was too high, the game displayed "📈 Go HIGHER!" instead of "📉 Go LOWER!" This made the game unplayable as hints contradicted the outcome.
2. **Difficulty Range Bug** — Hard difficulty used range 1-50, making it EASIER than Normal (1-100). Hard should have a larger range.
3. **String/Int Type Mismatch** — On even-numbered attempts, the secret was converted to a string, breaking comparisons.
4. **New Game Button Bug** — Ignored difficulty setting and always reset to 1-100 range.

**Fixes Applied:**
1. **Refactored code** — Moved all game logic functions from `app.py` to `logic_utils.py` for better separation of concerns.
2. **Fixed hint direction** — Changed "Too High" message from "Go HIGHER!" to "Go LOWER!" to match the outcome.
3. **Fixed difficulty range** — Changed Hard difficulty range from 1-50 to 1-200 to be genuinely harder than Normal.
4. **Added comprehensive tests** — Created pytest cases that validate hint correctness and difficulty progression.

## 📸 Demo Walkthrough

A sample game session on Normal difficulty (range 1-100, 8 attempts):

1. **Game starts** — Player selects "Normal" difficulty. The app displays "Guess a number between 1 and 100" with "Attempts left: 8".
2. **First guess (50)** — Player enters 50. The game reveals the secret is greater, displaying "📈 Go HIGHER!" (correct guidance).
3. **Second guess (75)** — Player enters 75. The game reveals "📉 Go LOWER!" (secret is less than 75). Hint direction is now correct.
4. **Third guess (60)** — Player enters 60. Game shows "📈 Go HIGHER!" — the secret is between 60 and 75.
5. **Fourth guess (67)** — Player enters 67. Game shows "📉 Go LOWER!" — the secret is between 60 and 67.
6. **Fifth guess (63)** — Player enters 63. The app displays: 🎉 "You won! The secret was 63. Final score: 70".
7. **Score calculation** — The player earned 70 points (100 - 10×3, where 3 is the number of guesses + 1).
8. **Next game** — Player can click "New Game 🔁" to play again with a fresh secret. The difficulty setting persists correctly.

**Key Fix Verification:** In step 2, if the hint still said "Go LOWER!" (the original bug), the player would be confused because the secret is actually higher. The fix ensures guidance always matches the outcome.

## 🧪 Test Results

All 19 pytest tests pass, including edge cases:

```
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0 -- /Library/Developer/CommandLineTools/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/toyosiabolaji/ai110-module1show-gameglitchinvestigator-starter
collecting ... collected 19 items

tests/test_game_logic.py::test_winning_guess PASSED                      [  5%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 10%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 15%]
tests/test_game_logic.py::test_hard_difficulty_range PASSED              [ 21%]
tests/test_game_logic.py::test_parse_negative_number PASSED              [ 26%]
tests/test_game_logic.py::test_parse_very_large_number PASSED            [ 31%]
tests/test_game_logic.py::test_parse_decimal_truncates PASSED            [ 36%]
tests/test_game_logic.py::test_parse_scientific_notation_fails PASSED    [ 42%]
tests/test_game_logic.py::test_parse_leading_trailing_whitespace PASSED  [ 47%]
tests/test_game_logic.py::test_parse_multiple_dots_fails PASSED          [ 52%]
tests/test_game_logic.py::test_parse_alphanumeric_fails PASSED           [ 57%]
tests/test_game_logic.py::test_parse_empty_string PASSED                 [ 63%]
tests/test_game_logic.py::test_parse_none_input PASSED                   [ 68%]
tests/test_game_logic.py::test_parse_special_characters PASSED           [ 73%]
tests/test_game_logic.py::test_check_guess_with_zero PASSED              [ 78%]
tests/test_game_logic.py::test_check_guess_boundary_1 PASSED             [ 84%]
tests/test_game_logic.py::test_check_guess_negative_secret PASSED        [ 89%]
tests/test_game_logic.py::test_parse_zero PASSED                         [ 94%]
tests/test_game_logic.py::test_parse_float_zero PASSED                   [100%]

============================== 19 passed in 0.02s =======================================
```

**Core Logic Tests (4):**
- `test_winning_guess` — Verifies correct answer returns "Win" outcome ✅
- `test_guess_too_high` — Verifies guess > secret returns "Too High" with "Go LOWER!" message ✅
- `test_guess_too_low` — Verifies guess < secret returns "Too Low" with "Go HIGHER!" message ✅
- `test_hard_difficulty_range` — Verifies Hard (1-200) > Normal (1-100) > Easy (1-20) ✅

**Edge-Case Input Handling (15):**
- Negative numbers, very large numbers, decimals, scientific notation rejection
- Leading/trailing whitespace handling, multiple dots, alphanumeric rejection
- Empty strings, None input, special characters
- Boundary values (0, 1), negative secrets, float zero conversion

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
