# This script generates a file called languages.dot, which can be
# converted to a pretty graphic file using Graphviz:
#
# dot -Tsvg languages.dot -o languages.svg

import pandas as pd


DATA_URL = "https://en.wikipedia.org/wiki/Timeline_of_programming_languages"
INTERESTING_TABLES_START = 4
INTERESTING_TABLES_END = 12
FAKE_PREDECESSORS = ["none (unique language)", "—", "Predecessor(s)"]
FAKE_NAMES = ["Name"]
IMPLEMENTATION_SUFFIX = " (implementation)"

FRONT_MATTER = """
digraph languages {
	fontname="Helvetica,Arial,sans-serif";
	node [fontname="Helvetica,Arial,sans-serif"];
	edge [fontname="Helvetica,Arial,sans-serif"];
	node [color=lightblue2, style=filled];
        rankdir="LR";
"""
END_MATTER = """
}
"""

def transform(string):
    string = string.strip()
    string = string.replace(IMPLEMENTATION_SUFFIX, "")
    return string

tables = pd.read_html(DATA_URL, header=0)

with open("languages.dot", "w") as languages:
    languages.write(FRONT_MATTER)

    for table_idx in range(INTERESTING_TABLES_START, INTERESTING_TABLES_END + 1):
        table = tables[table_idx].fillna("")
        for _, language in table.iterrows():
            if language["Predecessor(s)"]:
                predecessors = str(language["Predecessor(s)"]).split(",")
                for predecessor in predecessors:
                    if predecessor not in FAKE_PREDECESSORS:
                        languages.write(
                            '"{predecessor}" -> "{language}"\n'.format(
                                predecessor=transform(predecessor), language=transform(language["Name"])
                            )
                        )
                    else:
                        if language["Name"] not in FAKE_NAMES:
                            languages.write('"{language}"\n'.format(language=transform(language["Name"])))
            else:
                if language["Name"] not in FAKE_NAMES:                
                    languages.write('"{language}"\n'.format(language=transform(language["Name"])))

    languages.write(END_MATTER)
