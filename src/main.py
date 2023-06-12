import os
from pathlib import Path


ORG_HOME = os.environ["ORG_HOME"]
RELEVANT_ORG_SUPER_DIRECTORIES = [
    Path(ORG_HOME, "1_active-main-projects"),
    Path(ORG_HOME, "2_active-side-projects"),
]


def paths_to_project_directories():
    paths = []
    for super_dir in RELEVANT_ORG_SUPER_DIRECTORIES:
        project_dirnames = os.listdir(super_dir)
        for project_dirname in project_dirnames:
            path = Path(super_dir, project_dirname)
            if not os.path.isdir(path):
                continue
            paths.append(path)
    return paths


def main():
    project_dirs = paths_to_project_directories()
    for p in project_dirs:
        print(p)


if __name__ == "__main__":
    main()
