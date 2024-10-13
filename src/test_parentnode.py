import unittest
from htmlnode import ParentNode, LeafNode, HTMLNode
from textnode import TextNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "div",
            [
                LeafNode("Some text", "div"),
            ],
            {"class": "test_class"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="test_class"><div>Some text</div></div>',
        )
        node2 = ParentNode(
            "div",
            [
                LeafNode("Some text", "div"),
                LeafNode("Some other text", "p"),
            ],
            {"class": "test_class"},
        )
        self.assertEqual(
            node2.to_html(),
            '<div class="test_class"><div>Some text</div><p>Some other text</p></div>'
        )
        node3 = ParentNode(
            "div",
            [
                LeafNode("Some text", "div"),
                LeafNode("Some other text", "p"),
            ],
        )
        self.assertEqual(
            node3.to_html(),
            '<div><div>Some text</div><p>Some other text</p></div>'
        )
        node4 = ParentNode(
            "div",
            [
                LeafNode("Some text", "div"),
                ParentNode(
                    "p",
                    [
                        LeafNode("testing text", "div")
                    ]
                ),
            ],
        )
        self.assertEqual(
            node4.to_html(),
            '<div><div>Some text</div><p><div>testing text</div></p></div>'
        )

    def test_repr(self):
        node = ParentNode(
            "div",
            [
                LeafNode("Some text", "div"),
                LeafNode("Some other text", "p"),
            ],
            {"class": "test_class"},
        )
        self.assertEqual(
            node.__repr__(),
            "ParentNode(div, children: [LeafNode(Some text, div, None), LeafNode(Some other text, p, None)], {'class': 'test_class'})"
        )

        # check that passing no tag to LeafNode raises the value error and specific message
        with self.assertRaises(ValueError) as context:
            ParentNode(tag=None, children=[]).to_html()
        self.assertEqual(
            str(context.exception),
            "parent node must have a tag"
        )
        # check that passing no children to LeafNode raises the value error and specific message
        with self.assertRaises(ValueError) as context:
            ParentNode(tag="", children=[]).to_html()
        self.assertEqual(
            str(context.exception),
            "parent node must have children"
        )

if __name__ == "__main__":
    unittest.main()

