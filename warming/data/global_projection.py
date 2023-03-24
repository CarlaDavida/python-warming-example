import os
import pathlib
import pandas as pb


class GlobalProjection:
    def __init__(self):
        self._filepath = os.path.join(pathlib.Path.home(), 'PycharmProjects', 'python-warming-example', 'data',
                                      '41558_2023_1605_MOESM2_ESM.xlsx')
        # "./data/41558_2023_1605_MOESM2_ESM.xlsx"

        self._data = self.prepare_data()

    def prepare_data(self):
        data = pb.read_excel(self._filepath, sheet_name="Global Projections")
        data = data.set_index("Population Projection")
        return data[0:]

    def population_projection(self):
        """Returns an index of the population projection available in the dataset.

        :return: Returns an index of population projection of the dataset.
        :rtype: pandas.core.indexes.base.Index
        """
        return self._data.keys()

    def get_gas_data(self, gas: str):
        """
        :param gas: name of the gas - choose CO2, CH4 or N20
        :return: Tg gas/yr from food consumption data for given gas
        """
        if gas == 'CO2':
            data = self._data['Tg gas/yr from food consumption']
            return data[1:]
        elif gas == 'CH4':
            data = self._data['Unnamed: 3']
            return data[1:]
        elif gas == 'N2O':
            data = self._data['Unnamed: 4']
            return data[1:]
        else:
            print('invalid gas name')







if __name__ == "__main__":
    gp = GlobalProjection()
    print(gp.population_projection())
    print(gp.get_gas_data('N2O'))
