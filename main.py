import logging
import sys
import time

from src.helpers.functions import write_to_file, generate_random_paragraph, setup_logging, parse_command_line_arguments


def main(duration, lenght_paragraph=300, filename='random_paragraphs.txt'):
    """
    Main function to generate and write random paragraphs for a specified duration.

    :param duration: The duration in seconds for which to generate random paragraphs.
    :param lenght_paragraph: The lenght of charts in each paragraph.
    :param filename: The name of the file to write the random paragraphs to.
    """
    print("Generating random paragraphs...\n")
    start_time = time.time()
    write_to_file(filename, "Creando contenido del archivo\n\n", 'w')
    while time.time() - start_time < duration:
        random_paragraph = generate_random_paragraph(lenght_paragraph)
        print(random_paragraph)
        write_to_file(filename, random_paragraph)
        time.sleep(1)  # Wait for 1 second before generating the next random paragraph
    print("Finished generating random paragraphs.")


if __name__ == "__main__":
    setup_logging()
    try:
        duration_in_seconds = parse_command_line_arguments()
        main(duration_in_seconds, 300, "file_generator.txt")
    except Exception as e:
        logging.error(f"an error occurred while parsing command line arguments: {e}")
        sys.exit(1)
