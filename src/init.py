from command_line_arguments import app

if __name__ == "__main__":
    import filecmp
    import os

    ENV_FILE = ".env"
    ENV_EXAMPLE_FILE = ".env.example"

    if os.path.exists(ENV_FILE) and os.path.exists(ENV_EXAMPLE_FILE):
        if not filecmp.cmp(ENV_FILE, ENV_EXAMPLE_FILE):
            print("The .env file differs from .env.example.")
        else:
            print("The .env file is identical to .env.example.")
            app()
    else:
        print("One or both files (.env or .env.example) do not exist.")
