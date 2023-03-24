import matplotlib.pyplot as plt
import geopandas as gpd
from difflib import SequenceMatcher

class World:
    """This class contains all the methods to visualize data on a world map"""

    def __init__(self):
        self._world = gpd.read_file(
            gpd.datasets.get_path('naturalearth_lowres')
        )

    def show(self, data, column):
        """Opens a world map plot.

        The map shows the specified data, which also needs to be
        set with the `column` parameter.

        :param data: The data that will be shown on the world map.
        :type data: pandas.core.series.Series
        :param column: The index of the data to show.
        :type column: str
        """

        for country in self._world.name.values:
            if country not in data.keys():
                substitute = ""
                for country_diff_name, val in data.items():
                    country1 = country.lower().replace(".", "")
                    country2 = country_diff_name.lower().replace(".", "")

                    if country1 in country2:
                        data[country] = val
                        substitute = country_diff_name
                        break

                    elif country2 in country1:
                        data[country] = val
                        substitute = country_diff_name
                        break

                    elif SequenceMatcher(None, country, country_diff_name).ratio() >= 0.8:
                        data[country] = val
                        substitute = country_diff_name
                        break
                if substitute == "":
                    data[country] = 0
                    print("Could not find anything in the list for", country, ". Value set to 0.")

        vis_data = self._world.join(data, on="name")
        vis_data.plot(column=column, cmap='OrRd')

        plt.show()

    def get_data(self):
        """Getter to retreive the geopandas 'naturalearth_lowres' data set

        :return: World data, filled with information of a country's population, GDP, geometry
        :rtype: geopandas.geodataframe.GeoDataFrame
        """
        return self._world