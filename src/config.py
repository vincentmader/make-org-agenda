import os
from pathlib import Path


ORG_HOME = os.environ["ORG_HOME"]
RELEVANT_ORG_SUPER_DIRECTORIES = [
    Path(ORG_HOME, "1_active-main-projects"),
    Path(ORG_HOME, "2_active-side-projects"),
]
