#!/bin/python3

import sys
import os
import traceback
import re

# No env should be needed for this to run - using it as shell script with
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
        self.name = pathname.split("/")[2].split(".")[0]
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


def to_html(md: str):
    class DelimPattern:
        def __init__(self, start: str, end: str, start_repl: str, end_repl: str):
            self.start: str = start
            self.end: str = end
            self.start_repl = start_repl
            self.end_repl = end_repl

    class PipePattern:
        def __init__(self, pattern: str, repl: str):
            self.pattern: str = pattern
            self.repl: str = repl

    class LinePattern:
        def __init__(self, pattern: str, prefix: str, suffix: str):
            self.pattern = pattern
            self.prefix = prefix
            self.suffix = suffix

    "Convert markdown to HTML"
    delim_patterns: list[DelimPattern] = [
        DelimPattern(r"\*\*\*",  r"\*\*\*", "<b><em>", "</em></b>"),
        DelimPattern(r"\*\*",    r"\*\*",   "<b>",     "</b>"),
        DelimPattern(r"\*",      r"\*",     "<em>",    "</em>"),
        DelimPattern("`",        "`",       "<code>",  "</code>"),
        DelimPattern("^######",  "\n",      "<h6>",    "</h6>\n"),
        DelimPattern("^#####",   "\n",      "<h5>",    "</h5>\n"),
        DelimPattern("^####",    "\n",      "<h4>",    "</h4>\n"),
        DelimPattern("^###",     "\n",      "<h3>",    "</h3>\n"),
        DelimPattern("^##",      "\n",      "<h2>",    "</h2>\n"),
        DelimPattern("^#",       "\n",      "<h1>",    "</h1>\n"),
        DelimPattern("^[ \t]*-", "\n",      "<li>",    "</li>\n"),

        DelimPattern(r"^[2-9][0-9]*\. ",  "\n", "<li>", "</li>\n"),
    ]

    pipe_patterns: list[PipePattern] = [
        PipePattern(r"^1. ",                "\n\n<ol>\n<li> "),
        PipePattern(r"^[2-9][0-9]*\.(.*)\n\n",   r"<li>\1</li>\n</ol>\n\n"),

        PipePattern(r"\n\n\-",      "\n\n<ul>\n-"),
        PipePattern(r"^(-.*)\n\n",   r"\1\n</ul>\n\n"),
        PipePattern(r"\n\n\|",      "\n\n<table>\n<tr><td>"),
        PipePattern(r"\|\n\n",      "</td></tr>\n</table>\n\n"),
        PipePattern(r"\|$",         "</td></tr>\n"),
        PipePattern(r"^\|",         "<tr><td>"),
        PipePattern(r"\|",          "</td><td>"),
        PipePattern(r"^$",          "</p><p>\n"),
        PipePattern(r"---+",        "<hr>"),
        PipePattern(r"→",           "==>"),

        PipePattern(r"([A-Z][A-Z]+)",  r"<em>\1</em>"),
    ]

    line_patterns: list[LinePattern] = [
        LinePattern(r" += +", "<tt>", "</tt><br>"),
        LinePattern(r" *→ +", "<pre>", "</pre>"),
    ]

    lines = md.splitlines(keepends=True)

    for pattern in line_patterns:
        for i, line in enumerate(lines):
            if re.search(pattern.pattern, line):
                if line.endswith("\n"):
                    core = line[:-1]
                    newline = "\n"
                else:
                    core = line
                    newline = ""

                lines[i] = f"{pattern.prefix}{core}{pattern.suffix}{newline}"

    md = "".join(lines)

    for pattern in pipe_patterns:
        md = re.sub(pattern.pattern, pattern.repl, md, flags=re.MULTILINE)

    for pattern in delim_patterns:
        while True:
            start_match = re.search(pattern.start, md, re.MULTILINE)
            if not start_match:
                break

            # Search for the end pattern strictly after the start match
            end_match = re.search(pattern.end, md[start_match.end():], re.MULTILINE)
            if not end_match:
                break

            # Compute absolute positions of the end match
            end_start = start_match.end() + end_match.start()
            end_end   = start_match.end() + end_match.end()

            md = (
                md[:start_match.start()]          +
                pattern.start_repl                +
                md[start_match.end():end_start]   +
                pattern.end_repl                  +
                md[end_end:]
            )

    return md

def main() -> int:
    "Main program, 'nuff said"
    nodes: list[Node] = []

    # Load the index of files we are going to use in the generation of a
    # filetree/HTML site
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

    # Create the INDEX.md file from the nodelist
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

    # Create the llms-full.txt from the nodelist
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

    # Create the static site from the nodelist
    os.makedirs("html", exist_ok=True)
    for node in nodes:
        dirname: str = f"html/{node.section.lower()}"
        fname: str = f"{dirname}/{node.name}.html"
        os.makedirs(dirname, exist_ok=True)
        with open(fname, "w") as f:
            f.write(f"<!DOCTYPE html>\n")
            f.write(f"<html>\n")
            f.write(f"<head>\n")
            f.write(f"  <title>{node.front_matter['title']}</title>\n")
            f.write(f"      <link rel='stylesheet' href='/html/styles.css'>\n")
            f.write(f"      <meta name='title' content='{node.front_matter['title']}'>\n")
            f.write(f"      <meta name='description' content='{node.front_matter['description']}'>\n")
            f.write(f"      <meta name='targetaudience' content='{node.front_matter['targetaudience']}'>\n")
            f.write(f"      <meta name='tags' content=\"{node.tags}\">\n")
            f.write(f"</head>\n")
            f.write(f"<body>\n\n")
            f.write(f"<nav>\n")
            f.write(f"  <a href='/html/'>Top</a>\n")
            f.write(f"  <a href='/{dirname}'>Up</a>\n")
            f.write(f"</nav>\n<p>\n")
            f.write(f"{to_html(node.body)}\n</p>\n")
            f.write(f"</body>\n")
            f.write(f"</html>\n")

    return 0

if __name__ == '__main__':
    sys.exit(main())
