from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from model import SchellingModel


class HappyElement(TextElement):
    """
    Display a text count of how many happy agents there are.
    """

    def render(self, model):
        return "Happy agents: " + str(model.happy)


def schelling_draw(agent):
    """
    Portrayal Method for canvas
    """
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}

    if agent.type == 0:
        portrayal["Color"] = "Red"
    else:
        portrayal["Color"] = "Blue"
    return portrayal


happy_element = HappyElement()
canvas_element = CanvasGrid(schelling_draw, 20, 20, 500, 500)
happy_chart = ChartModule([{"Label": "happy", "Color": "Black"}])

model_params = {
    "height": 20,
    "width": 20,
    "density": UserSettableParameter("slider", "Agent density", 0.8, 0.1, 1.0, 0.1),
    "minority_pc": UserSettableParameter(
        "slider", "Fraction minority", 0.2, 0.00, 1.0, 0.05
    ),
    "homophily": UserSettableParameter("slider", "Homophily", 3, 0, 8, 1),
}

server = ModularServer(
    SchellingModel,
    [canvas_element, happy_element, happy_chart],
    "Schelling",
    model_params,
)
