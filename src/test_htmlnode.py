import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "test phrase",
            None,
            {"class": "test_class", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="test_class" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "Test phrase",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "Test phrase",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is a test paragraph",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, This is a test paragraph, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()

