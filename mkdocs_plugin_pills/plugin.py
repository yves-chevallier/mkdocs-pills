""" Plugin for mkdocs that adds custom markdown extensions. """
from mkdocs.plugins import BasePlugin
from mkdocs.utils import copy_file
from .regex import RegexExtension
from .unicode import UnicodeExtension
from pathlib import Path

class PillsPlugin(BasePlugin):
    """ Plugin for mkdocs that adds custom markdown extensions. """
    def __init__(self):
        self.css_output_path = None
        self.css_base_path = None
        super().__init__()

    def on_config(self, config):
        """ Add the custom markdown extensions to the config. """
        config["markdown_extensions"].append(RegexExtension())
        config["markdown_extensions"].append(UnicodeExtension())

        css = Path("css/pills.css")
        self.css_output_path = Path(config["site_dir"]) / css
        self.css_base_path = Path(__file__).parent / css

        config["extra_css"].append(str(css))

    def on_post_build(self, config):
        """Copy the epigraph.css file to the site directory."""
        _ = config
        copy_file(self.css_base_path, self.css_output_path)
