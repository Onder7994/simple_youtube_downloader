import argparse
from dataclasses import dataclass
from importlib.metadata import version

@dataclass
class CommandLineParser:
    url: str
    dir: str
    name: str
    format: str

    @classmethod
    def create_parser(cls):
        parser = argparse.ArgumentParser(description="CLI for youtube downloader")
        parser.add_argument(
            "-u", "--url", dest="url",
            required=True,
            help="Download URL"
        )
        parser.add_argument(
            "-d", "--dir", dest="dir",
            required=True,
            help="Directory for download"
        )
        parser.add_argument(
            "-n", "--name", dest="name",
            required=False,
            default=None,
            help="Name for downloaded file"
        )
        parser.add_argument(
            "-f", "--format", dest="format",
            required=False,
            default="mp4",
            help="Saved video format"
        )
        parser.add_argument(
            "-v", "--version",
            action="version",
            version=f"%(prog)s {version('yt_downloader')}",
            help="Show package version"
        )
        return parser