from pytube import YouTube, exceptions
from pytube.cli import on_progress
from yt_downloader.cli import CommandLineParser
from yt_downloader.logger import Logging
import sys

args = CommandLineParser.create_parser().parse_args()
cmd_args = CommandLineParser(**vars(args))
logger = Logging("yt-downloader")

def main():
    if cmd_args.name is not None:
        try:
            cmd_args.name.split(".")[1]
            filename = cmd_args.name
        except IndexError:
            filename = f"{cmd_args.name}.{cmd_args.format}"
    else:
        filename = cmd_args.name

    try:
        yt = YouTube(cmd_args.url, on_progress_callback=on_progress)
        video = yt.streams.filter(progressive=True, file_extension=cmd_args.format).order_by("resolution").desc().first()
        video.download(output_path=cmd_args.dir, filename=filename, max_retries=3)
        logger.info("Video save to %s directory", cmd_args.dir)
    except (exceptions.PytubeError) as err:
        logger.error("Code exit with error: %s", err)
        sys.exit(1)

if __name__ == "__main__":
    main()
