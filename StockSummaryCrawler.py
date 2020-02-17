import AbstractCrawler as AbsClass


class StockSummaryScraper(AbsClass.AbstractScrapper):
    """
    Purpose: The purpose of the class is to extract relevant data for stocks from
            https://finance.yahoo.com/ this WILL not work for other stock sites.
    """
    def __init__(self, url):
        super().__init__(url)
        self.summary_url = url[0]
        self.left_col = self.soup.find(class_='D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) '
                                              'ie-7_D(i) smartphone_D(b) smartphone_W(100%) '
                                              'smartphone_Pend(0px) smartphone_BdY '
                                              'smartphone_Bdc($seperatorColor)')

    def get_stock_name(self):
        name = self.soup.find('h1').get_text()
        n = name.split()
        del name
        return n[0]

    def get_price(self):
        price = self.soup.find(class_='My(6px) Pos(r) smartphone_Mt(6px)').get_text()
        p = price.split()
        del price
        return p[0]

    def get_volume(self):
        volume = self.left_col.find("td", text="Volume").find_next_sibling("td").text
        return volume

    def get_avg_volume(self):
        avg_volume = self.left_col.find("td", text="Avg. Volume").find_next_sibling("td").text
        return avg_volume

    def get_dividend_yield(self):
        dividend_yield = self.soup.find("td", text="Forward Dividend & Yield").find_next_sibling("td").text
        return dividend_yield

    def get_P_to_E(self):
        price_to_e = self.soup.find("td", text="PE Ratio (TTM)").find_next_sibling("td").text
        return price_to_e

