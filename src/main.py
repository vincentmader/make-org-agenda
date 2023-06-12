from config import DOOM_CONFIG
from config import MARKER_START, MARKER_END
from paths import paths_to_project_directories
from paths import paths_to_project_org_files


def fmt_agenda_line(org_file):
    org_file = str(org_file)
    org_file = org_file.replace("\"", "\\\"")
    org_file = f"       \"{org_file}\"\n"
    return org_file


def write_agenda_files_to_doom_config(project_org_files):
    with open(DOOM_CONFIG, 'r') as fp:
        lines = fp.readlines()
    lines = "".join(lines)
    split = lines.split(MARKER_START)
    lines_pre_agenda = split[0]
    lines_post_agenda = split[1].split(MARKER_END)[1]
    
    agenda_lines = [fmt_agenda_line(f) for f in project_org_files]
    agenda_lines = "".join(agenda_lines)

    lines = lines_pre_agenda
    lines += MARKER_START
    lines += agenda_lines
    lines += MARKER_END
    lines += lines_post_agenda

    with open("/Users/vinc/.config/doom/config.el2", 'w') as fp:
        fp.write(lines)


def main():
    project_dirs = paths_to_project_directories()
    project_org_files = paths_to_project_org_files(project_dirs)
    write_agenda_files_to_doom_config(project_org_files)


if __name__ == "__main__":
    main()
