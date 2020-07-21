import json

from util import Router, apply_processors

# class instance that is filled with routing information
router = Router()


# user-defined function that specifies what to do
# with a specific kind of histogram (here: one where
# the sample is "signal")
@router.register_processor(sample="signal")
def process_signal(sample, variation, region):
    print(f"    using signal processor for {sample}-{variation}-{region}")


@router.register_processor(sample="background")
def process_background(sample, variation, region):
    print(f"    using background processor for {sample}-{variation}-{region}")


@router.register_processor(sample="data")
def process_data(sample, variation, region):
    print(f"    using data processor for {sample}-{variation}-{region}")


if __name__ == "__main__":
    # load an example histogram structure
    with open("example_structure.json") as f:
        histogram_structure = json.load(f)

    # process histograms using the user-defined processors
    apply_processors(histogram_structure, router.processors)
