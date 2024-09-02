from mkdocs.plugins import BasePlugin

import re

r = re.compile(r"(\!\[([^\]]+)\|\s?(\d+%?)x?(\d+%?)?\s?\]\(([^\)]+)\))")


def convert_img_syntax(markdown):
    for match in r.finditer(markdown):
        if match.group(4) is None:
            markdown = markdown.replace(
                match.group(1),
                f'![{match.group(2)}]({match.group(5)}){{width="{match.group(3)}"}}',
            )
        else:
            markdown = markdown.replace(
                match.group(1),
                f'![{match.group(2)}]({match.group(5)}){{width="{match.group(3)}"; height="{match.group(4)}"}}',
            )
    return markdown


class MdImgSyntaxConverterPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        return convert_img_syntax(markdown)
