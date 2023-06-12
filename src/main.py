from paths import paths_to_project_directories
from paths import paths_to_project_org_files


def main():
    project_dirs = paths_to_project_directories()
    project_org_files = paths_to_project_org_files(project_dirs)
    
    for p in project_org_files:
        print(p)


if __name__ == "__main__":
    main()
