import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(
            "div",
            "test phrase",
            {"class": "test_class", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.to_html(),
            '<div class="test_class" href="https://boot.dev">test phrase</div>',
        )

    # def test_values(self):
    #     node = HTMLNode(
    #         "div",
    #         "Test phrase",
    #     )
    #     self.assertEqual(
    #         node.tag,
    #         "div",
    #     )
    #     self.assertEqual(
    #         node.value,
    #         "Test phrase",
    #     )
    #     self.assertEqual(
    #         node.children,
    #         None,
    #     )
    #     self.assertEqual(
    #         node.props,
    #         None,
    #     )
    #
    # def test_repr(self):
    #     node = HTMLNode(
    #         "p",
    #         "This is a test paragraph",
    #         None,
    #         {"class": "primary"},
    #     )
    #     self.assertEqual(
    #         node.__repr__(),
    #         "HTMLNode(p, This is a test paragraph, children: None, {'class': 'primary'})",
    #     )
    #

if __name__ == "__main__":
    unittest.main()

