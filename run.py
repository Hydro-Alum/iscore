import os
from flaskr import create_app

try:
    cwd = os.getcwd()
    print("Current Working Directory:", cwd)
except FileNotFoundError as e:
    print("Error: Working directory not found:", e)

app = create_app()

app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
