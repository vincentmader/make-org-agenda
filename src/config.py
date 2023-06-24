import os
from pathlib import Path


XDG_CONFIG_HOME = os.environ["XDG_CONFIG_HOME"]
ORG_HOME = os.environ["ORG_HOME"]

RELEVANT_ORG_SUPER_DIRECTORIES = [
    Path(ORG_HOME, "0_inbox"),
    Path(ORG_HOME, "1_active-main-projects"),
    Path(ORG_HOME, "2_active-side-projects"),
    Path(ORG_HOME, "3_chores"),
]

DOOM_CONFIG = Path(XDG_CONFIG_HOME, "doom", "lisp", "org-agenda.el")

MARKER_START = "; MARKER_START_ORG_AGENDA_FILE_LIST\n"
MARKER_END = "; MARKER_END_ORG_AGENDA_FILE_LIST\n"
