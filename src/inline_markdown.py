from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    this function takes a list of old_nodes, a delimiter, and a text type.
    """
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

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
                
