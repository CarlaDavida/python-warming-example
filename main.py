from warming.data.summary import Summary
from warming.plot.maps import World

def main():
    """
    I added some useless lines of doc.
    """
    summary = Summary()
    world = World()
    world.show(summary.co2(), "CO2C")

if __name__ == "__main__":
    main()
