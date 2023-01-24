from pathlib import Path
import toml
import re

settings = toml.load("./config.toml")

ssh_config_dir = Path(settings["path"]["sshdir"]).expanduser()

re_host = re.compile("^Host ")

ignore_list_text = "|".join(settings["search"]["ignore_list"])
re_ignore = re.compile(ignore_list_text)

for conf in ssh_config_dir.glob("**/config"):
    with open(conf, "r") as f:
        for line in f:
            if re_host.search(line):
                line = line.split(" ")[1].strip()
                if not re_ignore.search(line):
                    print(line)