import os
import pathlib
import pandas as pb


class Summary:

    def __init__(self):
        self._filepath = os.path.join(pathlib.Path.home(), 'PycharmProjects', 'python-warming-example', 'data',
                                      '41558_2023_1605_MOESM2_ESM.xlsx')
        # "./data/41558_2023_1605_MOESM2_ESM.xlsx"

        self._data = self.prepare_data()

    def prepare_data(self):
        data = pb.read_excel(self._filepath, sheet_name="Country Summaries")
        data = data.set_index("Country Name")
        return data[2:]

    def countries(self):
        """Returns an index of the countries available in the dataset.

        :return: Returns an index of countries of the dataset.
        :rtype: pandas.core.indexes.base.Index
        """
        return self._data.keys()

    def co2(self):
        """Returns the data of `CO2` values per capity per country.

        :return: The `CO2` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CO2C"]

    def ch4c(self):
        """
        returns data of 'CH4C' for all countries
        :return: `CH4C` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CH4C"]




if __name__ == "__main__":
    sume = Summary()
    print(sume._data)

