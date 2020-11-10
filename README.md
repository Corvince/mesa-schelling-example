*Note: This is an example repo to demostrate a stand alone model, outside of the Mesa code base.*

# Schelling Segregation Model

## Summary

The Schelling segregation model is a classic agent-based model, demonstrating how even a mild preference for similar neighbors can lead to a much higher degree of segregation than we would intuitively expect. The model consists of agents on a square grid, where each grid cell can contain at most one agent. Agents come in two colors: red and blue. They are happy if a certain number of their eight possible neighbors are of the same color, and unhappy otherwise. Unhappy agents will pick a random empty cell to move to each step, until they are happy. The model keeps running until there are no unhappy agents.

By default, the number of similar neighbors the agents need to be happy is set to 3. That means the agents would be perfectly happy with a majority of their neighbors being of a different color (e.g. a Blue agent would be happy with five Red neighbors and three Blue ones). Despite this, the model consistently leads to a high degree of segregation, with most agents ending up with no neighbors of a different color.

## Installation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    $ pip install -r requirements.txt
```

## How to Run

To run the model interactively, run ``run.py`` in this directory. e.g.

```
    $ python run.py
```

Then open your browser to [http://127.0.0.1:8888/](http://127.0.0.1:8888/) and press Reset, then Run.

To view and run some example model analyses, launch the IPython Notebook and open ``analysis.ipynb``. Visualizing the analysis also requires [matplotlib](http://matplotlib.org/).

## Files

* ``run.py``: Launches a model visualization server.
* ``schelling.py``: Contains the agent class, and the overall model class.
* ``server.py``: Defines classes for visualizing the model in the browser via Mesa's modular server, and instantiates a visualization server.
* ``analysis.ipybn``: Notebook demonstrating how to run experiments and parameter sweeps on the model.

## How to run on the web using Heroku

If you already have a free Heroku account you can deploy this example as a web app by using the following button

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy).

Otherwise refer to the [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python) to learn about the basics of hosting a web app on Heroku.

If you already set up your model as a git repository you basically only need to create a `Procfile` with the following content

```bash
web: python run.py -p=$PORT
```

This tells heroku to launch your model as a web application by running the file `run.py` and specify Herokus default port from the environmental variable `$PORT`

Make sure your models ModularServer is also launched with the same port by using the following snippet inside your `run.py` (if you don't specify the port, future versions of mesa will use this by default)

```python
from server import server
import os

port = int(os.getenv("PORT", 4200))

server.launch(port=port, open_browser=False)
```

That's it! You can view the Schelling model from this repo at https://mesa-schelling-example.herokuapp.com/

## Further Reading

Schelling's original paper describing the model:

* [Schelling, Thomas C. Dynamic Models of Segregation. Journal of Mathematical Sociology. 1971, Vol. 1, pp 143-186.](https://www.stat.berkeley.edu/~aldous/157/Papers/Schelling_Seg_Models.pdf)

An interactive, browser-based explanation and implementation:

* [Parable of the Polygons](http://ncase.me/polygons/), by Vi Hart and Nicky Case.
