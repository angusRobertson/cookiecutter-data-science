import toml
from rich import print as rprint

a = toml.load("growth.toml")

rprint(a)
