import pandas as pb

class Summary:

    def __init__(self):
        self._filepath = "./data/41558_2023_1605_MOESM2_ESM.xlsx"
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


class EuropeSummary(Summary):

    def __init__(self):
        super().__init__()

    def prepare_data(self):
        data = pb.read_excel(self._filepath, sheet_name="Europe")
        data = data.set_index("Country")
        return data[2:]

    def co2(self):
        """Returns the data of `CO2` values per capity per country.

        :return: The `CO2` data per capity per country.
        :rtype: pandas.core.series.Series
        """
        co2_data = self._data["Sum of Dietary Emissions (kg gas/yr)"]
        co2_data.name = "Sum of Dietary Emissions (kg gas/yr)"
        co2_data = co2_data.dropna()

        return co2_data
