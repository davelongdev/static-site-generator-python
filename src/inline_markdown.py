import re
from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    this function takes a list of old_nodes, a delimiter, and a text type.
    the old nodes are labeled as text nodes but may contain special text
    in the form of text formatted as bold, italic, or code that is delimited by
    specific markdown symbols.
    the function returns a list of new nodes where any special text is
    split into seperate nodes with new text types.
    """
    valid_delimiters = ["*", "**", "`"]

    new_nodes = []

    if delimiter not in valid_delimiters:
        raise Exception("not a vailid delimiter")

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
            
        #split old_nodes
        split_text = old_node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise ValueError("Invalid Markdown syntax: Unmatched delimiter")
        
        #create text nodes
        for i in range(len(split_text)):
            if split_text[i] != "":
                if i % 2 == 0:
                    new_node = TextNode(split_text[i], text_type_text)
                else:
                    new_node = TextNode(split_text[i], text_type)

                # combine text nodes into new_nodes list
                new_nodes.append(new_node)
    return new_nodes
                
def extract_markdown_images(text):
    """
    this function extracts images from markdown text and returns a
    list of tuples contianing the link text and url of the image.
    """
    tuples = []
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for i in range(len(images)):
        tuples.append(images[i])
    return tuples


def extract_markdown_links(text):
    """
    this function extracts links from markdown text and returns a
    list of tuples contianing the link text and url of the link.
    """
    tuples = []
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for i in range(len(links)):
        tuples.append(links[i])
    return tuples

def split_nodes_image(old_nodes):
    """
    this function splits text node objects that contains image links
    into text-only nodes and image-only nodes.  It takes a list of old nodes
    and returns a list of new nodes.
    """
    new_nodes = []
    for node in old_nodes:
        image_tuples = extract_markdown_images(old_nodes[node].text)
        for image_alt, image_link in image_tuples:
            sections = node.text.split(f"![{image_alt}]({image_link})", 1)
            new_nodes.append(TextNode(sections[0]), text_type_text)
            new_nodes.append(TextNode(sections[1]), text_type_image)

    return new_nodes


def split_nodes_link(old_nodes):
    """
    this function splits text node objects that contains links
    into text-only nodes and link-only nodes.  It takes a list of old nodes
    and returns a list of new nodes.
    """
    new_nodes = []
    for node in old_nodes:
        link_tuples = extract_markdown_links(node.text)
        for link_text, url in link_tuples:
            sections = node.text.split(f"![{link_text}]({url})", 1)
            new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(sections[1], text_type_link))

    return new_nodes
