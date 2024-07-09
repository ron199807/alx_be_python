def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Error: cannot be zero.")
        return numerator / denominator
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except ValueError:
        return "Error: both inputs must be numeric."
    except Exception as e:
        return f"Unexpected error: {e}"



           