from warming.data.summary import Summary, EuropeSummary
from warming.plot.maps import World, Europe

def main():
    """
    test
    """
    summary = Summary()
    world = World()
    world.show(summary.co2(), "CO2C")

    #
    # esummary = EuropeSummary()
    # europe = Europe()
    # europe.show(esummary.co2(), "Sum of Dietary Emissions (kg gas/yr)")


if __name__ == "__main__":
    main()
