import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode("p", "this is paragraph")
        html_props = node.props_to_html()
        self.assertEqual("",html_props)
    
    def test_has_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("p", "this is paragraph",None,props)
        html_props = node.props_to_html()
        self.assertEqual('href="https://www.google.com" target="_blank"',html_props)

    def test_empty_props(self):
        props = {}
        node = HTMLNode("p", "this is paragraph",None,props)
        html_props = node.props_to_html()
        self.assertEqual("",html_props)

if __name__ == "__main__":
    unittest.main()
