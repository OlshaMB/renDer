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

def render(comp):
    return comp.render()
