#!/usr/bin/env python3

import os
import requests

# For Windows
feedback_path = os.path.join(os.path.abspath("/"), os.getcwd(), "data", "feedback")

# For Linux
# feedback_path = os.path.join(os.path.abspath("/"), "data", "feedback")

# Fill this with your website
website = "http://34.71.94.107/feedback/"  # Temporary website from Qwiklabs


def get_texts():
    list_dict = []
    feedback_keys = ["title", "name", "date", "feedback"]
    files = os.listdir(feedback_path)

    for file in files:
        file_path = os.path.join(feedback_path, file)

        with open(file_path, "r") as feedback:
            feedback_dict = {}

            for index, sentence in enumerate(feedback.readlines()):
                feedback_dict[feedback_keys[index]] = sentence.strip()

        list_dict.append(feedback_dict)

    return list_dict


def send_data_to_website(feedback_dict):
    response = requests.post(website, data=feedback_dict)
    if response.status_code == 201:
        print("Success")
    else:
        response.raise_for_status()


def main():
    if __name__ == "__main__":
        for feedback in get_texts():
            send_data_to_website(feedback)


main()
