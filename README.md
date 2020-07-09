# cabinetry-routing

Testing ideas about structures to allow users to inject code into [cabinetry](https://github.com/alexander-held/cabinetry/).
Inspired by [flask](https://flask.palletsprojects.com/en/1.1.x/en) and [FastAPI](https://fastapi.tiangolo.com/).

## `example.py`

User-defined functions are decorated to register them as something that should be called when processing certain types of histogram (here: when processing specific samples).
They are then executed when the loop over all histograms comes across histograms matching the description used in the decorator of the custom functions.
