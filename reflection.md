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

I used Claude Code (my AI coding assistant) to understand the buggy logic in this game. When I asked it to explain specific problematic sections of the code, it helped me trace through the logic step-by-step.

**Example 1 (Correct AI explanation):** When I asked Claude to explain lines 158-161, it correctly identified that the code converts `secret` to a string on even-numbered attempts:
```python
if st.session_state.attempts % 2 == 0:
    secret = str(st.session_state.secret)  # ← converts to string
else:
    secret = st.session_state.secret  # ← keeps as int
```
Claude explained that this causes the `check_guess()` function to compare `guess_int` (an int) against a string `secret` on even attempts, which will always evaluate incorrectly in comparison operations. I verified this by reading the comparison logic at lines 37-40 and confirming that `guess > secret` would fail on even attempts when comparing int to string.

**Example 2 (Incorrect AI suggestion):** I initially asked Claude if the "Hard" difficulty was intentional, and it suggested the range might be correct for a "time-attack" variant. However, when I read the code carefully, I saw that Hard actually has 5 attempts while Normal has 8 attempts, but SMALLER range (1-50 vs 1-100), making it easier, not harder. The attempt limit compensates but the range logic is backwards by design.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
