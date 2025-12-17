from app.error_listener import capture_error
from app.code_analyzer import analyze_code
from app.ai_engine import generate_fix
from app.patch_applier import apply_patch

FILE_PATH = "buggy_code.py"

def run_self_healing():
    error_data = capture_error()

    if not error_data:
        print("✅ No errors found")
        return

    print("❌ Error detected:")
    print(error_data["error"])

    with open(FILE_PATH, "r") as f:
        code = f.read()

    functions = analyze_code(FILE_PATH)
    print("📌 Functions found:", functions)

    fixed_code = generate_fix(error_data["error"], code)

    apply_patch(FILE_PATH, fixed_code)

    print("🛠️ Fix applied automatically")
    print("🚀 Re-run the program")

if __name__ == "__main__":
    run_self_healing()
