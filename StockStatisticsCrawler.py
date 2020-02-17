import AbstractCrawler as AbsClass


class StockStatScrapper(AbsClass.AbstractScrapper):
    def __init__(self, url):
        super().__init__(url)
        self.stats_url = url[1]
        self.trade_info = self.soup.find(class_='Pstart(20px) smartphone_Pstart(0px)')
        self.trade_info_val = self.trade_info.find_all('td', class_='Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)')

    def get_fifty_week_high(self):
        fifty_week_high = self.trade_info_val[3].text
        return fifty_week_high

    def get_fifty_week_low(self):
        fifty_week_low = self.trade_info_val[4].text
        return fifty_week_low