import os
from pathlib import Path


XDG_CONFIG_HOME = os.environ["XDG_CONFIG_HOME"]
ORG_HOME = os.environ["ORG_HOME"]

RELEVANT_ORG_SUPER_DIRECTORIES = [
    Path(ORG_HOME, "inbox"),
    Path(ORG_HOME, "projects", "active-main"),
    Path(ORG_HOME, "projects", "active-side"),
    Path(ORG_HOME, "projects", "chores"),
]

DOOM_CONFIG = Path(os.environ["DOOM_CONF"], "lisp", "org-agenda.el")

MARKER_START = "; MARKER_START_ORG_AGENDA_FILE_LIST\n"
MARKER_END = "; MARKER_END_ORG_AGENDA_FILE_LIST\n"
