import pyexcel

from src.data.data import Data


class DataReader:

    def read_from_file(self, file_path):
        raw_data = pyexcel.get_book(file_name=file_path).to_dict()
        columns = self.separate_columns(raw_data.popitem()[1])
        project_id = columns[0][0]
        project_title = columns[0][1]
        format = columns[0][2]
        data = columns[1]
        data_object = Data(project_title, format, data, project_id=project_id)
        return data_object

    def separate_columns(self, data):
        cols = []
        rows = data
        col1 = self.extract_column(rows, 0, 3)
        col2 = self.extract_column(rows, 1, len(rows))
        cols.append(col1)
        cols.append(col2)
        return cols

    def extract_column(self, rows, col_index, last_row):
        col = []
        for row in rows[0:last_row]:
            col.append(row[col_index])
        return col
