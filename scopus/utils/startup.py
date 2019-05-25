import os
import warnings
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

# Configuration setup
config = configparser.ConfigParser()
config.optionxform = str
CONFIG_FILE = os.path.expanduser("~/.scopus/config.ini")
if not os.path.exists(CONFIG_FILE):
    text = "scopus did not find a configuration file.  Please issue "\
           "scopus.utils.create_config() to start the process which guides "\
           "you through the generation of the configuration file or read "\
           "https://scopus.readthedocs.io/en/stable/configuration.html."
    warnings.warn(text, UserWarning)
else:
    config.read(CONFIG_FILE)
