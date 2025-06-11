import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)

logs_path = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=logs_path,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)