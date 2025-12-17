from app.safety import (
    is_file_allowed,
    backup_file,
    restore_backup,
    syntax_is_valid,
    patch_size_is_safe
)


def apply_patch(file_path, original_code, fixed_code):
    if not is_file_allowed(file_path):
        raise PermissionError("File modification not allowed")

    if not syntax_is_valid(fixed_code):
        raise SyntaxError("Generated code has invalid syntax")

    if not patch_size_is_safe(original_code, fixed_code):
        raise ValueError("Patch too large, rejected")

    backup_file(file_path)

    with open(file_path, "w") as f:
        f.write(fixed_code)
