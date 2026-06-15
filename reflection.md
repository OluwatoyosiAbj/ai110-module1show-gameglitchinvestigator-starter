# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it appeared to load successfully. However, upon analyzing the code, I discovered several critical bugs that would cause unexpected behavior during gameplay. The game has inverted hint logic, inconsistent difficulty settings, and broken score calculations that would confuse any player trying to actually win.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Hard difficulty selected | Range should be 1-50 (harder than Normal's 1-100), attempts: 5 | Range is 1-50 (EASIER than Normal's 1-100), making Hard easier | No error; silent logic bug in get_range_for_difficulty() line 10 |
| Guess a number HIGHER than secret (e.g., secret=30, guess=50) | Hint should say "Go LOWER!" to guide toward correct answer | Hint says "Go HIGHER!" 📈 which is backwards | No error; inverted comparison logic in check_guess() lines 37-40 |
| Make a guess on attempt 2 (or any even attempt) | Hint should correctly indicate if guess is too high or too low | Hint may be inverted due to string/int comparison (secret becomes string on even attempts) | No error; type inconsistency bug on lines 158-161 |
| Select Hard difficulty, click "New Game" button | New game should generate secret in Hard's range (1-50) | New game always generates secret in 1-100 range, ignoring difficulty | No error; hardcoded range in line 136 |
| Make first guess | Attempt counter shows: "Attempts left: 7" (for 8 allowed) | Attempt counter shows: "Attempts left: 7" but increment happens before validation | Off-by-one display issue; counter increments at line 148 before guess validation |
| Win a game on attempt 2 | Score = 100 - 10*(2+1) = 70 points | Score = 80 points (formula assumes 0-indexed attempts) | Silent scoring error; formula at line 52 uses attempt_number incorrectly |

---

## 2. How did you use AI as a teammate?

I used Claude Code as my AI programming partner in multiple ways: to understand buggy logic, to refactor code, and to design better tests.

**Example 1 (Correct AI suggestion - Refactoring):** When I asked Claude to help refactor the game logic from app.py into logic_utils.py, it provided the exact steps:
1. Copy the implementations from app.py
2. Replace the `NotImplementedError` stubs in logic_utils.py
3. Update app.py imports: `from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score`
4. Remove the duplicate function definitions from app.py

I followed this approach and it worked perfectly. The app continued to run correctly, and pytest picked up the logic_utils.py implementations immediately.

**Example 2 (Incorrect AI suggestion - Bug interpretation):** Initially, I asked Claude if the inverted hint messages might be intentional "psychological tricks" to confuse players. Claude agreed this was plausible, but then I tested it: when I traced through `check_guess(60, 50)`, the function returned `("Too High", "📈 Go HIGHER!")`. This is clearly a bug—the outcome correctly identifies the guess is too high, but the message tells you to go higher, which contradicts it. The fix was simple: change the message emoji and text to match the outcome. Claude then agreed this was definitely a bug, not a feature.

---

## 3. Debugging and testing your fixes

**How I decided bugs were fixed:**
I used a combination of pytest tests and code inspection. For the hint direction bug, I wrote tests that explicitly verify the returned message matches the outcome (e.g., "Too High" outcome returns "📉 Go LOWER!" message). For the difficulty range bug, I created a test comparing range sizes to ensure Hard > Normal > Easy.

**Test results:**
I ran `pytest tests/test_game_logic.py -v` and verified:
```
tests/test_game_logic.py::test_winning_guess PASSED                      [ 25%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 50%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 75%]
tests/test_game_logic.py::test_hard_difficulty_range PASSED              [100%]

============================== 4 passed in 0.01s =======================================
```

All 4 tests passed, confirming that:
1. Winning guesses return correct outcome and emoji ✅
2. Guess too high now correctly says "Go LOWER!" (was backwards) ✅
3. Guess too low correctly says "Go HIGHER!" ✅
4. Hard difficulty range (1-200) is now larger than Normal (1-100) ✅

**AI collaboration on tests:**
Claude (my AI assistant) helped me write proper test assertions that check both the outcome tuple AND the message content. Initially, the starter tests only checked the outcome string, which wouldn't have caught the inverted hint bug. Claude suggested checking the full return tuple `(outcome, message)` to ensure the message matched the outcome semantically.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
