class Router:
    def __init__(self):
        self.processors = dict()

    def register_processor(self, sample=""):
        def register(func):
            self.processors[sample] = {"name": func.__name__, "func": func}

        return register


def apply_processors(histogram_structure, processors_dict):
    """loop over all histograms that need to be processed
    and call the right processor for each one of them
    """
    for sample in histogram_structure["Samples"]:
        for variation in sample["Variations"]:
            for region in variation["Regions"]:
                print(
                    "processing:",
                    sample["Name"].ljust(12),
                    variation["Name"].ljust(15),
                    region["Name"].ljust(5),
                )
                # find which processor to call and run it
                processors_dict[sample["Name"]]["func"](
                    sample["Name"], variation["Name"], region["Name"]
                )
