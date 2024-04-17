import argparse
import logging
import os
from faker import Faker
from datetime import datetime
from logging.handlers import RotatingFileHandler


def setup_logging():
    """
    Setup logging configuration.

    This function configures the logging module to log messages to a file with a specific format and rotation settings.

    :return: None
    """

    logs_dir = 'src/data/logs'
    os.makedirs(logs_dir, exist_ok=True)
    log_file_path = f"{logs_dir}/log_file_{datetime.now().strftime('%Y%m')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S%p',
        handlers=[
            logging.FileHandler(log_file_path),
            RotatingFileHandler(log_file_path, maxBytes=10000000, backupCount=5),
            logging.StreamHandler()
        ]
    )


def parse_command_line_arguments():
    """
    Parse the command line arguments.

    :return: Tuple containing the parsed Jira key and input file.
    :rtype: int
    """
    parser = argparse.ArgumentParser(description='Proccess command line arguments.')
    parser.add_argument('duration', type=int, help='Duration in seconds for which to generate random text.')
    args = parser.parse_args()
    return args.duration


def generate_random_paragraph(max_nb_chars=2500):
    """
    Generates a fake paragraph of text using the Faker library.

    :param max_nb_chars: The maximum number of characters in the generated paragraph.
    :return: A fake paragraph of text.
    """
    fake = Faker()
    return fake.text(max_nb_chars=max_nb_chars) + "\n"


def write_to_file(filename, text, mode='a'):
    """
    Writes the given text to a file.

    :param filename: The name of the file to write to.
    :param text: The text to write to the file.
    :param mode: The mode to open on the file
    """
    with open(filename, mode) as file:
        file.write(text + '\n')
