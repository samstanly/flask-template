
from app.scripts.edpe300.constants import DEFAULT_COLOR

import re

class Edge():
    spaces="[ \t]*"
    item=spaces+"[0-9a-zA-Z-_]+[0-9a-zA-Z -_]*"+spaces
    r="^"+spaces+item+","+item+"(,"+item+")?"+"(,"+spaces+"color"+spaces+"="+spaces+item+")?"+spaces+"$"

    def __init__(self,line):
        self.line=line
        self.valid=self.parse_line(line)

    def parse_line(self,line):
        if not self.validate(line):
            return 0

        line=line.strip()

        split=line.split(",")
        split=[i.strip() for i in split]

        args=[i for i in split if "=" not in i]
        kwargs=[i for i in split if "=" in i]
        kwargs={i.split("=")[0].strip():i.split("=")[1].strip() for i in kwargs}

        self.node1=args[0]
        self.node2=args[1]

        self.color=DEFAULT_COLOR if "color" not in kwargs else kwargs["color"]
        self.edge_text="" if len(args)<3 else args[2]

        return 1

    def validate(self,line):
        return re.match(Edge.r,line)
