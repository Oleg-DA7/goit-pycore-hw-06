from functools import wraps

def error_decorator(default_result=None):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                print("Give me name and phone please.")
                return default_result                
            except (KeyError, IndexError, TypeError):            
                print("Enter the argument for the command")
                return default_result
        return inner
    return decorator