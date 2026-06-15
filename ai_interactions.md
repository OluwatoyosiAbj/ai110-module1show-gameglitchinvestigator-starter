# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7) - Challenge 1: Advanced Edge-Case Testing

> Document how you used AI to help generate comprehensive edge-case tests.

### Prompt Used
"Identify three critical edge cases that could break the number guessing game's input parsing and comparison logic. For each edge case, generate a pytest test that verifies the game handles it gracefully. Include cases for: (1) invalid input formats, (2) numeric boundary/conversion edge cases, (3) whitespace and unusual notation. Each test should include a comment explaining WHY that edge case was chosen."

| Edge Case | Prompt Used | Test Created | Did It Pass? | Why Chosen |
|-----------|-------------|--------------|--------------|------------|
| **Invalid formats** | Generate tests for "50abc", "#$%^", "50.50.50" | `test_parse_alphanumeric_fails`, `test_parse_special_characters`, `test_parse_multiple_dots_fails` | ✅ Yes (3/3) | Users make typing errors; game should reject gracefully without crashing |
| **Negative numbers** | Generate test for "-50" input | `test_parse_negative_number` | ✅ Yes | Edge case: negative is syntactically valid but semantically outside game range |
| **Very large numbers** | Generate test for "999999999999" | `test_parse_very_large_number` | ✅ Yes | Typo edge case: user might paste a huge number; parsing should succeed but game validates range |
| **Decimal handling** | Generate test verifying 50.9 → 50 (truncation, not rounding) | `test_parse_decimal_truncates` | ✅ Yes | Verify int(float()) converts correctly; 50.9 should become 50, not 51 |
| **Whitespace** | Generate test for "  50  " with spaces | `test_parse_leading_trailing_whitespace` | ✅ Yes | Web forms sometimes include accidental whitespace; should be tolerated |
| **Scientific notation** | Generate test for "1e2" (100 in scientific) | `test_parse_scientific_notation_fails` | ✅ Yes | Valid float syntax but unsupported by simple int() parser; game correctly rejects |
| **Boundary values** | Generate tests for secret=0, guess=1 vs secret=2 | `test_check_guess_with_zero`, `test_check_guess_boundary_1` | ✅ Yes | Off-by-one errors hide at boundaries; verify logic at extremes |
| **Zero inputs** | Generate tests for "0" and "0.0" | `test_parse_zero`, `test_parse_float_zero` | ✅ Yes | Zero is a boundary value in number guessing; ensure it works |
| **Error robustness** | Generate tests for None and empty string | `test_parse_none_input`, `test_parse_empty_string` | ✅ Yes | Defensive programming: catch unexpected None; handle empty submissions |

### Summary of Results
✅ **All 19 tests passing** (4 core + 15 edge-case tests)
- Negative numbers parse successfully (game validates range separately) ✅
- Decimals truncate correctly (50.9 → 50) ✅
- Whitespace is tolerated ✅
- Invalid formats rejected with clear error messages ✅
- Scientific notation correctly unsupported ✅
- Boundary values work correctly ✅

### Files Modified
- `tests/test_game_logic.py` — Added 15 comprehensive edge-case tests
- `README.md` — Updated test results section with full pytest output

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
