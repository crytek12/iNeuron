import logging

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from module1.module1 import dir_list, open_pdf

"""
This module provides a PDF merging tool using Kivy.

The module includes a class for the main layout, which contains a text input field and a label. When the user enters
a path to a directory and clicks the button, the program lists the names of all the files and folders in the directory
and displays them in the label. It then calls the `open_pdf` function from the `module1.module1` module to open the
PDF files in the specified directory. If an error occurs while listing the directory or opening the PDF, an error
message is displayed in the label and the exception is logged.
"""

# Set up a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('main.log')
handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(handler)

Builder.load_file('my.kv')


class MyLayout(Widget):
    """A widget that displays a list of files and folders in a specified directory, and tries to merge and open all
        the PDF files in the directory."""
    def press(self):
        """Called when the button is pressed. Gets the text from the text input field, tries to get a list of files
        and folders in the specified directory, and tries to merge and open all the PDF files in the directory."""

        # Add a log message here
        logger.debug('press method called')

        # Get the text from the text input field
        path = self.ids.text_input.text

        # Add a log message here to log the path value
        logger.debug('path: %s', path)

        # Try to get a list of files and folders in the specified directory
        try:
            result = dir_list(path)
            logger.info('Successfully listed directory')  # Add a log message here
        except Exception:
            # Log the exception and set the label text to show an error message
            logger.exception('An error occurred while listing the directory')
            self.ids.label.text = 'An error occurred while listing the directory'

            return

        if result is not None:
            # Initialize an empty string to store the names of the files and folders
            file_and_folder_names = ''

            # Iterate over the list of files and folders
            for file_or_dir in result:
                # Append the name of the current file or folder to the string
                file_and_folder_names += file_or_dir + '\n'

            # Set the label text to the string containing the names of all the files and folders
            self.ids.label.text = file_and_folder_names
            logger.info('Directory listing displayed')  # Add a log message here

            # Try to call the open_pdf function
            try:
                open_pdf(path)
                logger.info('PDF opened successfully')  # Add a log message here
            except Exception:
                # Log the exception and set the label text to show an error message
                logger.exception('An error occurred while opening the PDF')
                self.ids.label.text = 'An error occurred while opening the PDF'
        else:
            logger.warning('The specified directory does not exist')
            self.ids.label.text = 'The specified directory does not exist'


class PDFMerger(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    PDFMerger().run()
