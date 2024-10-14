from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    new_nodes = []
    for old_node in old_nodes:
        if old_node != TextNode:
            new_nodes.append(old_node)
        else:
            #parse text node
            pass
