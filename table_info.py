class Table:

    def __init__(self):
        self.col_names = []
        self.col_widths = []
        self.col_types = []

    def add_col_info(self, column):
        self.col_names.append(column[0])
        self.col_widths.append(int(column[1]))
        self.col_types.append(column[2])

    def get_num_of_cols(self):
        return len(self.col_names)

    def get_col_names(self):
        return self.col_names
    
    def get_col_width(self):
        return self.col_widths

    def get_col_type(self):
        return self.col_types