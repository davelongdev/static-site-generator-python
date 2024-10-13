import unittest
from htmlnode import LeafNode, HTMLNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(
            "test phrase",
            "div",
            {"class": "test_class", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="test_class" href="https://boot.dev">test phrase</div>',
        )
        node2 = LeafNode(
            "testing"
        )
        self.assertEqual(
            node2.to_html(),
            'testing',
        )
        node3 = LeafNode(
            'testing phrase',
            'div',
            {"class": "primary secondary", "aria-label": "label"},
        )
        self.assertEqual(
            node3.to_html(),
            '<div class="primary secondary" aria-label="label">testing phrase</div>',
        )
        # check that passing no value to LeafNode raises the value error and specifiv message
        with self.assertRaises(ValueError) as context:
            LeafNode(None).to_html()
        self.assertEqual(
            str(context.exception),
            "leaf node must have a value"
        )

    def test_repr(self):
        node = LeafNode(
            "This is a test paragraph",
            "p",
            {"class": "primary"}
        )
        self.assertEqual(
            node.__repr__(),
            "LeafNode(This is a test paragraph, p, {'class': 'primary'})"
        )

def test_leaf_node_with_tag_no_attributes(self):
    node = LeafNode("Just a paragraph", "p")
    self.assertEqual(node.to_html(), "<p>Just a paragraph</p>")

def test_leaf_node_with_empty_string_value(self):
    node = LeafNode("", "p")
    self.assertEqual(node.to_html(), "<p></p>")

def test_leaf_node_inheritance(self):
    node = LeafNode("test", "p")
    self.assertIsInstance(node, HTMLNode)

if __name__ == "__main__":
    unittest.main()

