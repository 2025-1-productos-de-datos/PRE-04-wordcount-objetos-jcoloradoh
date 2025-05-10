import argparse
from ._internals.file_reader import 
from ._internals.text_processor import 

class ArgumentParser:
    def __init__(self):
        # Define las variables del objeto
        self.input = None
        self.output = None
        self.parser = None
        self.crear_parser()

    def crear_parser(self):

        self.parser = argparse.ArgumentParser(description="Count words in files.")

        self.parser.add_argument(
            "input",
            type=str,
            help="Path to the input folder containing files to process",
        )
        self.parser.add_argument(
            "output",
            type=str,
            help="Path to the output folder for results",
        )

    def run(self):

        parsed_args = self.parser.parse_args()
        self.input = parsed_args.input
        self.output = parsed_args.output


def main():

    argument_parser = ArgumentParser().run()
    # argument_parser.run()
    # print(argument_parser.input)
    # print(argument_parser.output)
    
    file_reader = FileReader(argument_parser.input)
    text_processor = TextProcessor()
    
    lines = file_reader.read_all_lines()
    processed_lines = text_processor.
    words = text_processor.split_inot_words(preprocessed_lines)
