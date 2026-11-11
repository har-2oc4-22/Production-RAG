"""Step 0: shared logger used by every other step.

Every module in this app asks this file for a logger instead of
setting up its own. That way all logs (from document loading to the
final answer) end up in one place, in one consistent format.
"""

import logging 
import os 
from datetime import datetime


LOGS_DIR = "logs"
os.makedirs(LOGS_DIR , exist_ok=True)

# One log file per run, named with the time the run started.

_run_started_at = datetime.now().strftime("%Y%m%d_%H%M%S")
RUN_LOG_FILE = os.path.join(LOGS_DIR, f"run_{_run_started_at}.log")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(RUN_LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
# works like a watchman for the app, keeping track of everything that happens and writing it to a log file. Each module in the app can call get_logger(__name__) to get a logger that will write messages to the same log file, so all logs are in one place.