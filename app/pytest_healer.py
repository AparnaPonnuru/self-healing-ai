import pytest
from app.ai_engine import generate_fix_from_llm
from app.memory import get_previous_fix, save_fix
from app.github_pr import create_fix_pr

BUGGY_FILE = "buggy_code.py"
TEST_PATH = "tests/test_sample.py"


def run_pytest():
    return pytest.main([TEST_PATH, "-q"])


def auto_heal_from_pytest():
    exit_code = run_pytest()

    if exit_code == 0:
        print("✅ Tests passed. No healing needed.")
        return

    print("❌ Tests failed. Checking memory...")

    with open(BUGGY_FILE, "r") as f:
        original_code = f.read()

    cached_fix = get_previous_fix("test_failure", original_code)

    if cached_fix:
        print("🧠 Using cached fix to create PR.")
        create_fix_pr(cached_fix)
    else:
        print("🤖 Generating AI fix for PR.")
        fixed_code = generate_fix_from_llm("pytest failure", original_code)
        save_fix("test_failure", original_code, fixed_code)
        create_fix_pr(fixed_code)

    print("📌 Pull Request created for review.")
