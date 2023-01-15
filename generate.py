"""
Running this script generates a file called languages.dot, which can
be converted to a pretty graphic file using Graphviz:

$ dot -Tsvg languages.dot -o languages.svg
"""

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

    languages = list()
    tables = pd.read_html(DATA_URL)

    for table_idx in range(INTERESTING_TABLES_START, INTERESTING_TABLES_END + 1):
        table = tables[table_idx].fillna("")
        for _, language in table.iterrows():
            if language["Predecessor(s)"]:
                predecessors = str(language["Predecessor(s)"]).split(",")
                for predecessor in predecessors:
                    if predecessor not in FAKE_PREDECESSORS:
                        languages.append(
                            {
                                "predecessor": clean_string(predecessor),
                                "name": clean_string(language["Name"]),
                            }
                        )
                    else:
                        if language["Name"] not in FAKE_NAMES:
                            languages.append(
                                {
                                    "name": clean_string(language["Name"]),
                                }
                            )
            else:
                if language["Name"] not in FAKE_NAMES:
                    languages.append(
                        {
                            "name": clean_string(language["Name"]),
                        }
                    )

    return languages


def load_languages_template():
    loader = FileSystemLoader(searchpath="./templates/")
    env = Environment(loader=loader)
    template = env.get_template("languages.dot")
    return template


if __name__ == "__main__":

    template = load_languages_template()
    languages = load_languages_data()
    rendered_template = template.render(languages=languages)

    with open("languages.dot", "w", encoding="utf-8") as f:
        f.write(rendered_template)
