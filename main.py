import os
import subprocess

def create_project_structure():
    subprocess.run(["git", "init"])  # Initialisation du dépôt Git

    directories = [
        "data/cleaned",
        "data/raw",
        "docs",
        "models",
        "notebooks",
        "reports",
        "src"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        create_file(directory, "placeholder.txt", "Ce fichier est un espace réservé.")
        subprocess.run(["git", "add", directory])
        subprocess.run(["git", "commit", "-m", f"Added {directory}"])

    create_file("notebooks", "main.ipynb", "# Notebook Content")
    subprocess.run(["git", "ajout", "notebooks"])
    subprocess.run(["git", "commit", "-m", "Ajout main notebook"])

    create_file("src", "utils.py", "# Util")
    create_file("src", "main.py", "# Main Code")
    create_file("data/cleaned", "utils.py", "# Cleaned Utility Functions")
    create_file("data/raw", "utils.py", "# Raw Utility Functions")
    create_file("", "requirements.txt", "numpy\npandas\nmatplotlib")
    subprocess.run(["git", "ajout", "src", "data", "requirements.txt"])
    subprocess.run(["git", "commit", "-m", "ajout requirements"])

def create_file(directory, file_name, content):
    file_path = os.path.join(directory, file_name)
    with open(file_path, "w") as file:
        file.write(content)

def main():
    create_project_structure()
    print("La structure d'arborescence du projet a été créée avec succès.")

if __name__ == "__main__":
    main()
