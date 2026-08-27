def shout(text: str) -> str:
    return text.upper() + "!"


yell = shout
print(yell("hello"))


def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def normalize_title(title: str) -> str:
    return title.strip().title()


print(normalize_title(" ship docs "))
# calling normalize_title
# Ship Docs
