import logging
from datetime import datetime

# configuração do logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(message, level="info"):
    """função pra registrar mensagens de log com timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"

    if level == "error":
        logging.error(log_message)
    elif level == "warning":
        logging.warning(log_message)
    else:
        logging.info(log_message)

    print(log_message)  # também exibe no terminal