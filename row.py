class Row:

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def data_mod(self, type_arr, width_arr):
        """
        Currently support column data type : CHAR, INTEGER, BOOLEAN
        TODO : need to add different column data type for general usages
        (eg. data, time, real, uuid, ...)
        """

        for i in range(len(width_arr)):

            # data will chopped at the END if the length is greater than width limit
            if type_arr[i] == "CHAR":
                if len(self.data[i]) > width_arr[i]:
                    self.data[i] = self.data[i][:width_arr[i]]

            # data will chopped at the FRONT if the length is greater than width limit
            elif type_arr[i] == "INTEGER":
                if len(self.data[i]) > width_arr[i]:
                    self.data[i] = int(self.data[i][width_arr[i]:])
                else:
                    self.data[i] = int(self.data[i])
