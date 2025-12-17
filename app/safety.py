import ast
import shutil
import os

MAX_LINES_CHANGED = 10
ALLOWED_FILES = {"buggy_code.py"}


def is_file_allowed(file_path):
    return os.path.basename(file_path) in ALLOWED_FILES


def backup_file(file_path):
    backup_path = file_path + ".bak"
    shutil.copy(file_path, backup_path)
    return backup_path


def restore_backup(file_path):
    backup_path = file_path + ".bak"
    if os.path.exists(backup_path):
        shutil.copy(backup_path, file_path)


def syntax_is_valid(code: str) -> bool:
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False


def patch_size_is_safe(original_code, fixed_code):
    orig_lines = original_code.splitlines()
    fixed_lines = fixed_code.splitlines()
    return abs(len(fixed_lines) - len(orig_lines)) <= MAX_LINES_CHANGED
