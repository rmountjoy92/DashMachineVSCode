import os
from generate_snippets import generate_snippets
from generate_html import generate_html


class DocsGenerator:
    def __init__(self):
        self.root_folder = os.path.dirname(__file__)

        generate_snippets(root_folder=self.root_folder)
        generate_html(root_folder=self.root_folder)
