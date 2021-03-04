# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json
# import logging


def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.
    color_name = color_name.lower().strip()

    # logging.basicConfig(filename='log.txt', filemode='w',
    #                     format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    with open("data/css-color-names.json") as my_data_file:
        my_data = json.load(my_data_file)

        # logging.debug('Form entry: %s', color_name)

        for k in my_data:
            try:
                if color_name == k:
                    hex_code = my_data[k]
                    return hex_code
            except Exception:
                # logging.exception("Exception occurred")
                hex_code = "Try again!"
                return hex_code

    # f = open("data/css-color-names.json", "r")
    # data = f.readline()
    # for k in data:
    #     if k == color_name:
    #         hex_code = data[k]
    #         return hex_code
    #     else:
    #         raise Exception("Try again, my dude!")
