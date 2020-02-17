import StockSummaryCrawler
import StockStatisticsCrawler
import pandas as pd

stock_summ = StockSummaryCrawler.StockSummaryScraper
stock_stat = StockStatisticsCrawler.StockStatScrapper


class DataTable:
    def __init__(self, stock_array):
        self.stock_array = stock_array
        self.data = []

    def get_data(self):
        for i, j in self.stock_array:
            self.data.append({'Company': i.get_stock_name(),
                              'Price ': i.get_price(),
                              'Volume ': i.get_volume(),
                              'Avg. Volume ': i.get_avg_volume(),
                              'Dividend Yield ': i.get_dividend_yield(),
                              'PE Ratio': i.get_P_to_E(),
                              '52-Week High': j.get_fifty_week_high(),
                              '52-Week Low': j.get_fifty_week_low()})

        return self.data

    def sort_data(self):
        sorted_data = sorted(self.data, key=lambda k: k['Company'])
        table = pd.DataFrame(sorted_data)
        return table


stocks_arr = [[stock_summ('https://finance.yahoo.com/quote/MSFT?p=MSFT'),
               stock_stat('https://finance.yahoo.com/quote/MSFT/key-statistics?p=MSFT')],
              [stock_summ('https://finance.yahoo.com/quote/DIS?p=DIS'),
               stock_stat('https://finance.yahoo.com/quote/DIS/key-statistics?p=DIS')],
              [stock_summ('https://finance.yahoo.com/quote/AA?p=AA&.tsrc=fin-srch'),
               stock_stat('https://finance.yahoo.com/quote/AA/key-statistics?p=AA&.tsrc=fin-srch')],
              [stock_summ('https://finance.yahoo.com/quote/SNE?p=SNE'),
               stock_stat('https://finance.yahoo.com/quote/SNE/key-statistics?p=SNE')],
              [stock_summ('https://finance.yahoo.com/quote/SJM?p=SJM&.tsrc=fin-srch'),
               stock_stat('https://finance.yahoo.com/quote/SJM/key-statistics?p=SJM&.tsrc=fin-srch')],
              [stock_summ('https://finance.yahoo.com/quote/TEVA?p=TEVA&.tsrc=fin-srch'),
               stock_stat('https://finance.yahoo.com/quote/TEVA/key-statistics?p=TEVA&.tsrc=fin-srch')],
              [stock_summ('https://finance.yahoo.com/quote/GE?p=GE&.tsrc=fin-srch'),
               stock_stat('https://finance.yahoo.com/quote/GE/key-statistics?p=GE&.tsrc=fin-srch')]]