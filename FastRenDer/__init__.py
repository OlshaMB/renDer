import os


class Component():
    def __init__(self, name, file: os.PathLike):
        self.name = name
        self.file: os.PathLike = file
        self.components = []

    def render(self):
        renderderer = open(str(self.file), "r").read()
        for component in self.components:
            renderderer = renderderer.replace(''.join(["<", "component:", component.name, "/>"]), component.render())
        return renderderer

    def add_Component(self, component):
        self.components.append(component)


class Page():
    def __init__(self, name, file: os.PathLike):
        self.name = name
        self.file: os.PathLike = file
        self.components = []

    def render(self):
        file = open(str(self.file), "r")
        renderderer = file.read()
        for component in self.components:
            renderderer = renderderer.replace(''.join(["<", "component:", component.name, "/>"]), component.render())
        return renderderer

    def add_Component(self, component: Component):
        self.components.append(component)
