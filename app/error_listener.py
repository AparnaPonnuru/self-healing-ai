import traceback

def capture_error():
    try:
        import buggy_code  # noqa: F401
        return None
    except Exception as e:
        return {
            "error": str(e),
            "traceback": traceback.format_exc()
        }
