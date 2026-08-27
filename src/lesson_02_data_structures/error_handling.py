def validate_project_name(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Project name cannot be empty")
    return cleaned


print(validate_project_name("My Project"))
print(validate_project_name("  Another Project  "))
try:
    name = validate_project_name("   ")
except ValueError as e:
    print(f"Error: {e}")
    name = "DEFAULT"

print(f"Final project name: {name}")
