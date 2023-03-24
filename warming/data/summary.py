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

    def get_ch4c_data(self, capital: str):
        """
        returns ch4c data for given country
        :param capital: name of capital as string
        :return : data for methane per year for the given country
        """
        data = self.ch4c()
        return data[capital]

    def n2oc(self):
        """
        returns data of 'CH4C' for all countries
        :return: `CH4C` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["N2OC"]

    def get_n2oc_data(self, country: str):
        """
        returns N2OC data for given country
        :param country: name of capital as string
        :return : data for N2CO per year for the given country
        """
        data = self.n2oc()
        return data[country]

    def co2y(self):
        """
        returns data of 'CH4C' for all countries
        :return: `CH4C` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CO2Y"]

    def get_co2y_data(self, country: str):
        """
        returns CO2Y data for given country
        :param country: name of capital as string
        :return : data for CO2Y per year for the given country
        """
        data = self.co2y()
        return data[country]

    def ch4y(self):
        """
        returns data of 'CH4Y' for all countries
        :return: `CH4Y` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["CH4Y"]

    def get_ch4y_data(self, country: str):
        """
        returns CH4Y data for given countries
        :param country: name of capital as string
        :return : data for CH4Y per year for the given capita
        """
        data = self.ch4y()
        return data[country]

    def n2oy(self):
        """
        returns data of 'N20Y' for all countries
        :return: `N20Y` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        return self._data["N20Y"]

    def get_n2oy_data(self, country: str):
        """
        returns N20Y data for given country
        :param country: name of capital as string
        :return : data for N20Y per year for the given country
        """
        data = self.n2oy()
        return data[country]

    def get_any_data(self, gas: str, country: str):
        """
        returns data of given gas for given country
        :param gas: string -
        :param country: string name of capital
        :return : data of given country for given gas
        """
        data = self._data[gas]
        return data[country]












#CH4Y and N20Y

if __name__ == "__main__":
    sume = Summary()
    print(sume.get_any_data("N2OY", "Zambia"))