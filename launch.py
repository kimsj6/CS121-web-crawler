from configparser import ConfigParser
from argparse import ArgumentParser

from utils.server_registration import get_cache_server
from utils.config import Config
from crawler import Crawler


def main(config_file, restart):
    print("here2.5")
    cparser = ConfigParser()
    cparser.read(config_file)
    config = Config(cparser)
    print("here3.5")
    config.cache_server = get_cache_server(config, restart)
    print("here2")
    crawler = Crawler(config, restart)
    print("here3")
    crawler.start()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--restart", action="store_true", default=False)
    parser.add_argument("--config_file", type=str, default="config.ini")
    args = parser.parse_args()
    print("here")
    main(args.config_file, args.restart)
