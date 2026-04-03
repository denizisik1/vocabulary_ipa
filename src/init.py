from command_line_arguments import app

if __name__ == "__main__":
    import filecmp
    import os

    env_file = ".env"
    env_example_file = ".env.example"

    if os.path.exists(env_file) and os.path.exists(env_example_file):
        if not filecmp.cmp(env_file, env_example_file):
            print("The .env file differs from .env.example.")
        else:
            print("The .env file is identical to .env.example.")
            app()
    else:
        print("One or both files (.env or .env.example) do not exist.")
