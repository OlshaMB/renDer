import os
import unittest
from FastRenDer import Page,Component

class renDerTest(unittest.TestCase):
    def testBasicPage(self):
        file=open("./html/correct.html","r")
        title = Component("Title", os.path.abspath("./html/title.html"))
        content = Component("Content", os.path.abspath("./html/content.html"))
        content.add_Component(title)
        main = Page("Main", os.path.abspath("./html/index.html"))
        main.add_Component(title)
        main.add_Component(content)
        #main.render()

        self.assertEqual(file.read(), main.render())


def main():
    unittest.main()
