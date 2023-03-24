import matplotlib.pyplot as plt
import geopandas as gpd


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

        vis_data = self._world.join(data, on="name")
        vis_data.plot(column=column, cmap='OrRd')

        plt.show()

    def get_data(self):
        """Getter to retreive the geopandas 'naturalearth_lowres' data set

        :return: World data, filled with information of a country's population, GDP, geometry
        :rtype: geopandas.geodataframe.GeoDataFrame
        """
        return self._world


class Europe(World):

    def __init__(self):
        """Initialise the Europe Class based on the World class
        but filtering out only the European country data from world map

        """
        super().__init__()
        self._europe = self._world[self._world['continent'] == 'Europe']

    def get_data(self):
        """Getter to retreive the geopandas 'naturalearth_lowres' data set for Europe only

        :return: Europe data, filled with information of a country's population, GDP, geometry
        :rtype: geopandas.geodataframe.GeoDataFrame
        """

        return self._europe

    def show(self, data, column):
        """Opens a world map plot.

        The map shows the specified data, which also needs to be
        set with the `column` parameter.

        :param data: The data that will be shown on the world map.
        :type data: pandas.core.series.Series
        :param column: The index of the data to show.
        :type column: str
        """

        vis_data = self._europe.join(data, on="name")
        vis_data.plot(column=column, cmap='OrRd')

        plt.show()
