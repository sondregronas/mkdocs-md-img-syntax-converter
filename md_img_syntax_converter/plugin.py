from mkdocs.plugins import BasePlugin

import re

r = re.compile(r"(\!\[([^\]]+)(?:\|)\s?(\d+%?)x?(\d+%?)?\s?\]\(([^\)]+)\))")


def convert_img_syntax(markdown):
    for match in r.finditer(markdown):
        original = match.group(1)
        alt_text = match.group(2)
        width = match.group(3)
        height = match.group(4)
        link = match.group(5)

        if alt_text.endswith('\\'):
            alt_text = alt_text[:-1]


        if height is None:
            markdown = markdown.replace(
                original,
                f'![{alt_text}]({link}){{width="{width}"}}',
            )
        else:
            markdown = markdown.replace(
                original,
                f'![{alt_text}]({link}){{width="{width}"; height="{height}"}}',
            )
    return markdown


class MdImgSyntaxConverterPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        return convert_img_syntax(markdown)
