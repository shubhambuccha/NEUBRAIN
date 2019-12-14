import time
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as urllib2
from pandas import DataFrame

def scrape_yahoo(stock):
	technicals = {}
	try:
		url = "https://in.finance.yahoo.com/quote/"+stock+".NS/key-statistics?p="+stock+".NS"
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page, 'html.parser')
# 		print(soup)
		tables = soup.findAll('table', {"class" : "W(100%) Bdcl(c) Mt(10px)"})	
		for table in tables:
			table_body = table.find('tbody')
			rows = table_body.find_all('tr')

			for row in rows:
				col_name = row.find_all('span')							
				col_name = [cell.text.strip() for cell in col_name]
				col_val = row.find_all('td')
				col_val = [cell.text.strip() for cell in col_val]
				technicals[col_name[0]] = col_val[1]
# 				print(col_val[1])
		return technicals
	except Exception as e:
		print('Failed, exception: ', str(e))



def scrape(stock_list, interested, technicals):
	for each_stock in stock_list:
		technicals = scrape_yahoo(each_stock)
		print(each_stock)
		for ind in interested:
			print(ind + ": "+ technicals[ind])
		print("-----------------------------")											
	return technicals

def main():
	stock_list = pd.read_csv("nifty_500_list.csv")
	Row_list=[]
	for rows in stock_list.itertuples(): 
		my_list =[rows.Symbol] 
		Row_list.append(my_list[0]) 										
	interested =['Market cap (intra-day)','Revenue', 'Return on equity', 'Quarterly revenue growth', 'Operating cash flow', 'Total cash', 'Total debt', 'Current ratio', '52-week change', 'Avg vol (3-month)' , 'Avg vol (10-day)'] 
	technicals = {}
# 	Row_list = ['3MINDIA']
	tech = scrape(Row_list, interested, technicals)
	#print(tech)


if __name__ == "__main__":
	main()
