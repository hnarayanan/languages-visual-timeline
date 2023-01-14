# Visual Timeline of Programming Languages

I am often curious about the source of ideas going into programming
languages, and look for charts that visualise their connections and
history. This project aims to generate one such visualisation of
programming languages using [up-to-date information from
Wikipedia][wikipedia-language-timeline].

If you find this interesting, you should [follow me on
Mastodon][hachyderm-harish] to learn about the other
things I do.

## Download the graphics

- [Download a recent PDF][languages-pdf-download]
- [Download a recent SVG][languages-svg-download]

## Generating them yourself

If you’d like to generate such graphics yourself, download the code in
this repository (by using the big green `Code` button on this
project‘s GitHub page) and navigate into it.

When in the folder, do the following:

````
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python generate.py
````

This will generate a file called `languages.dot`, which is a [Graphviz
grammar for describing graphs][graphviz-dot]. In order to use this
file, you need to have [Graphviz installed on your
system][graphviz-install]. Once you have it installed, you can convert
this `dot` file into a pretty graphic file (e.g PDF or SVG) using:

````
dot -Tpdf languages.dot -o languages.pdf
dot -Tsvg languages.dot -o languages.svg
````

## Other similar projects

One of the prettiest versions of a similar effort is from [O’Reilly
Media in 2004][oreilly-programming-languages-history]. While this has
not been updated in a long time, the original author of this graphic
has been keeping it [more updated][levenez-lang]. The fundamental
difference is that our project tries to generate one of these
programatically from [live data source][wikipedia-language-timeline].
(Even though, in all honesty, the data on that particular Wikipedia
page [could use a lot of cleanup][wikipedia-language-timeline-talk].)


## Authors and contributing

This project is primarily written and maintained by [Harish
Narayanan](https://harishnarayanan.org).

Since it’s an open source project, you are free to contribute to it.
If you have an idea, please [write it up in the form of a GitHub
issue][languages-github-issues].

Thank you!

## Copyright and license

Copyright (c) 2023 [Harish Narayanan](https://harishnarayanan.org).

This code is licenced under the MIT Licence. See
[LICENSE][languages-github-license] for the full text of this licence.

[hachyderm-harish]: https://hachyderm.io/@harish
[wikipedia-language-timeline]: https://en.wikipedia.org/wiki/Timeline_of_programming_languages
[wikipedia-language-timeline-talk]: https://en.wikipedia.org/wiki/Talk:Timeline_of_programming_languages
[languages-pdf-download]: https://github.com/hnarayanan/languages-visual-timeline/raw/main/output/languages.pdf
[languages-svg-download]: https://github.com/hnarayanan/languages-visual-timeline/raw/main/output/languages.svg
[languages-github-issues]: https://github.com/hnarayanan/languages-visual-timeline/issues
[languages-github-license]: https://github.com/hnarayanan/languages-visual-timeline/blob/main/LICENSE
[graphviz-dot]: https://graphviz.org/doc/info/lang.html
[graphviz-install]: https://graphviz.org/download/
[oreilly-programming-languages-history]: https://www.cs.toronto.edu/~gpenn/csc324/PLhistory.pdf
[levenez-lang]: https://www.levenez.com/lang/
