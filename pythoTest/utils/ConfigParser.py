from configparser import ConfigParser
import os;

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
print(config_path)
config = ConfigParser()
with open(config_path, 'r') as fp:
    config.read_file(fp)

if config.has_section("system"):
    if config.has_option("system", "report.postgres.host"):
        print(config.get("system", "report.postgres.host"))
