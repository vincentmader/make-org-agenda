import os
from pathlib import Path

from config import RELEVANT_ORG_SUPER_DIRECTORIES

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


def paths_to_project_org_files(project_dirs):
    org_files = []
    for project_dir in project_dirs:
        dir_entries = os.listdir(project_dir)
        dir_entries = list(filter(lambda f: f.endswith(".org"), dir_entries))
        for project_org_file in dir_entries:
            path = Path(project_dir, project_org_file)
            org_files.append(path)
    return org_files

