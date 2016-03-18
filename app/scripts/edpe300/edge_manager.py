from app.scripts.edpe300.edge import Edge
import os.path
from string import ascii_lowercase, ascii_uppercase, digits

from app.scripts.edpe300.constants import *

class EdgeManager():
    def __init__(self,node_text=""):
        self.edges=list()
        self.node_text=""
        if node_text:
            self.add_nodes(node_text)

    def add_nodes(self,node_text):
        self.node_text+="\n"+node_text

        for line in node_text.split("\n"):
            line=line.strip()
            edge=Edge(line)
            self.edges.append(edge)

    def get_valid_edges(self):
        return [e for e in self.edges if e.valid]

    def get_code(self):
        nodes=set()
        for edge in self.get_valid_edges():
            nodes.add(edge.node1)
            nodes.add(edge.node2)

        lines=list()
        declare="var %s = graph.newNode({label: '%s'});"
        for node in nodes:
            lines.append(declare%(self.get_varname(node),self.get_labelname(node)))

        newedge="graph.newEdge(%s, %s, {color: '%s'});"
        newedge_label="graph.newEdge(%s, %s, {color: '%s',label:'%s'});"
        for edge in self.get_valid_edges():
            var1=self.get_varname(edge.node1)
            var2=self.get_varname(edge.node2)
            color=self.get_color(edge.color)
            if edge.edge_text:
                lines.append(newedge_label%(var1,var2,color,edge.edge_text))
            else:
                lines.append(newedge%(var1,var2,color))

        return "\n".join(lines)

    def get_demo_code(self):
        self.add_nodes(self.get_demo_nodes())
        return self.get_code()

    def get_demo_nodes(self):
        try:
            with open("app/scripts/edpe300/demo_nodes","r") as f:
                data=f.read()
        except:
            return ""
        return data

    def get_varname(self,node):
        varname="".join([c for c in node if c in ascii_lowercase+ascii_uppercase+digits+"_"])
        if varname and varname[0].isdigit():
            varname="xxx"+varname
        return varname

    def get_labelname(self,node):
        return node[0].upper()+node[1:]

    def get_color(self,color):
        if color in COLORS:
            return COLORS[color]
        return COLORS[DEFAULT_COLOR]













