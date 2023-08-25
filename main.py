import os

def create_project_structure():
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
        create_requirement_file(directory)

    create_file("notebooks/main.ipynb", "# main")
    create_file("src/utils.py", "# Util")

def create_requirement_file(directory):
    file_path = os.path.join(directory, "requirement.txt")
    with open(file_path, "w") as file:
        file.write("C  fichier contenant la liste des dépendances du projets")

def create_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)

def main():
    create_project_structure()
    print("La structure d'arborescence du projet a été créée avec succès.")

if __name__ == "__main__":
    main()
