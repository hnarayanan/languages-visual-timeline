#!/usr/bin/env python

import argparse
import pandas as pd
from jinja2 import Environment, FileSystemLoader


def clean_string(string):
    IGNORED_SUFFIXES = [" (concept)", " (implementation)"]

    string = string.strip()
    for suffix in IGNORED_SUFFIXES:
        string = string.replace(suffix, "")
    return string


def load_languages_data():
    DATA_URL = "https://en.wikipedia.org/wiki/Timeline_of_programming_languages"
    INTERESTING_TABLES_START = 4
    INTERESTING_TABLES_END = 12
    FAKE_PREDECESSORS = ["none (unique language)", "—", "Predecessor(s)"]
    FAKE_NAMES = ["Name"]

    decades = list()
    tables = pd.read_html(DATA_URL)

    for table_idx in range(INTERESTING_TABLES_START, INTERESTING_TABLES_END + 1):
        table = tables[table_idx].fillna("")
        decade = dict()
        decade["idx"] = table_idx
        decade["label"] = f"Decade {table_idx}"
        decade["languages"] = list()
        for _, language in table.iterrows():
            if language["Predecessor(s)"]:
                predecessors = str(language["Predecessor(s)"]).split(",")
                for predecessor in predecessors:
                    if predecessor not in FAKE_PREDECESSORS:
                        decade["languages"].append(
                            {
                                "predecessor": clean_string(predecessor),
                                "name": clean_string(language["Name"]),
                            }
                        )
                    else:
                        if language["Name"] not in FAKE_NAMES:
                            decade["languages"].append(
                                {
                                    "name": clean_string(language["Name"]),
                                }
                            )
            else:
                if language["Name"] not in FAKE_NAMES:
                    decade["languages"].append(
                        {
                            "name": clean_string(language["Name"]),
                        }
                    )
        decades.append(decade)
    return decades


def get_template_name():
    DEFAULT_TEMPLATE_NAME = "languages.dot"

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--template",
        help="Name of the template file",
        default=DEFAULT_TEMPLATE_NAME,
        type=str,
    )
    args = parser.parse_args()
    return args.template


def load_template(file_name="languages.dot", searchpath="./templates/"):
    loader = FileSystemLoader(searchpath=searchpath)
    env = Environment(loader=loader)
    template = env.get_template(file_name)
    return template


if __name__ == "__main__":

    template_name = get_template_name()
    template = load_template(template_name)
    decades = load_languages_data()
    rendered_template = template.render(decades=decades)

    with open(template_name, "w", encoding="utf-8") as f:
        f.write(rendered_template)
