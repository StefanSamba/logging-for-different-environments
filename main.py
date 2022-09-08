import logging
import os

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
if os.getenv("DEBUG") == "true":
    logging.getLogger().setLevel(logging.DEBUG)


def create_logs():
    logging.info("raised an info log")
    logging.debug("raised an debug log")


def main():
    create_logs()


if __name__ == "__main__":
    main()
