import toml
from rich import print as rprint

a = toml.load("./exp.toml")

rprint(a)