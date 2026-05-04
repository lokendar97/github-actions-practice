import os

SQL_DIR = "project/sql"

def validate_file(filepath):
    with open(filepath, "r") as f:
        content = f.read().strip()

        if not content:
            raise Exception(f"{filepath} is empty ❌")

        if not content.lower().startswith("select"):
            raise Exception(f"{filepath} should start with SELECT ❌")

def main():
    for file in os.listdir(SQL_DIR):
        if file.endswith(".sql"):
            validate_file(os.path.join(SQL_DIR, file))

    print("All SQL files are valid ✅")

if __name__ == "__main__":
    main()