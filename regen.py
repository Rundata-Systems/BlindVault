#!/bin/python3

import sys
import traceback

# No env should be needed for thsi to run - using it as shell script with
# composite datatype support.
#

class State:
    INITIAL = 0
    FRONT_MATTER = 1
    BODY = 2



class Node:
    "Represent a single node (markdown file) in the document system"
    def __init__(self, pathname: str):
        self.pathname: str = pathname
        self.section = pathname.split("/")[1]
        self.section = self.section[0].upper() + self.section[1:]
        self.front_matter: dict[str, str] = {}
        self.tags: list[str] = []
        self.body: str = ""

        state: int = State.INITIAL
        with open(pathname) as f:
            for line in f:

                match state:
                    case State.INITIAL:
                        if line.startswith ("---"):
                            state = State.FRONT_MATTER
                            continue
                        else:
                            state = State.BODY
                            self.body += line
                            continue

                    case State.FRONT_MATTER:
                        if line.startswith ("---"):
                            state = State.BODY
                            continue
                        kv: list[str] = line.split(":")
                        kv[0] = kv[0].strip()
                        kv[1] = kv[1].strip()
                        if kv[0] == "tags":
                            tags: str = kv[1].split("[")[1].split("]")[0]
                            self.tags = [
                                tag.strip() for tag in tags.split(",")
                            ]
                        else:
                            self.front_matter[kv[0]] = kv[1]

                    case State.BODY:
                        self.body += line
                        continue


def main() -> int:
    "Main program, 'nuff said"
    nodes: list[Node] = []
    with open(".index.list") as f:
        for line in f:
            line = line.split("#")[0]
            line = line.strip()
            if len(line) == 0:
                continue
            try:
                nodes.append(Node(line))
            except Exception as ex:
                print(f"{line}: Exception {ex}")

    prev_section: str = ""
    with open("INDEX.md", "w") as f:
        f.write("---\n")
        f.write("title: Documentation Index\n")
        f.write("product: bv (BlindVault)\n")
        f.write("type: reference\n")
        f.write("tags: [ reference, navigation, index ]\n")
        f.write("---\n")
        f.write("\n")
        f.write("# Documentation Index\n")

        for node in nodes:
            try:
                if node.section != prev_section:
                    f.write(f"\n## {node.section}\n")
                    prev_section = node.section

                f.write(f"- [{node.front_matter['title']}]({node.pathname}) - ")
                f.write(f"{node.front_matter['description']}\n")

            except Exception as ex:
                print(f"{node.pathname}: Exception!")
                traceback.print_exc()
                sys.exit(-1)

        f.write("\n")

    with open("llms-full.txt", "w") as f:
        for node in nodes:
            try:
                f.write(f"\n==== {node.pathname} ====\n")
                f.write("---\n")
                f.write(f"title: {node.front_matter['title']}\n")
                f.write(f"description: {node.front_matter['description']}\n")
                f.write("---\n")
                f.write(f"{node.body}\n")

            except Exception as ex:
                print(f"{node.pathname}: Exception!")
                traceback.print_exc()
                sys.exit(-1)

    return 0

if __name__ == '__main__':
    sys.exit(main())
