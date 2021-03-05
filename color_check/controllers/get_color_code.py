# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json
import logging


def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.
    color_name = color_name.lower().strip()

    logging.basicConfig(filename='/tmp/log.txt', filemode='a',
                        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)  # noqa

    # color_check/data/css-color-names.json on Github
    # data/css-color-names.json locally
    with open("color_check/data/css-color-names.json") as my_data_file:
        my_data = json.load(my_data_file)

        for k in my_data:
            if color_name == k:
                hex_code = my_data[k]
                logging.debug('Form entry: %s is VALID', color_name)
                return hex_code
        logging.debug('Form entry: %s is INVALID', color_name)
        Error = "Error"
        return Error
