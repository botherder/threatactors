#!/usr/bin/env python3

import os
import yaml
import pprint

def main():
    actors = []

    for file_name in os.listdir("."):
        if not file_name.endswith(".yaml"):
            continue

        with open(file_name, "r") as handle:
            data = yaml.load(handle.read())

        for actor in data["actors"]:
            actor["country_name"] = data["country_name"]
            actor["country_code"] = data["country_code"]
            actors.append(actor)

    pprint.pprint(actors)

if __name__ == "__main__":
    main()
