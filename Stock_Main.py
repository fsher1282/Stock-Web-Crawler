import DataTable as Dt

if __name__ == '__main__':
     stock_array = Dt.stocks_arr
     Data = Dt.DataTable(stock_array)
     Data.get_data()
     print (Data.sort_data())

