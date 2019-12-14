from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
def scrap(stock):
	print(stock)
	html = urlopen("https://in.finance.yahoo.com/quote/"+stock+".NS/history?p="+stock+".NS").read()
	soup = BeautifulSoup(html, 'lxml')
	table = soup.find('table',{"class":"W(100%) M(0)"})
	teams = []
	
	rows = table.find_all('tr')
		
	# Creates a 2-D matrix.
	for row in range(len(rows)):
		team_row = []
		columns = rows[row].findAll('td')
		for column in columns: 
			team_row.append(column.getText())
		print(team_row)
		# Add each team to a teams matrix.
		teams.append(team_row)
	print("--------------------------------------------------------------------------------")

def main():
	stock_list = pd.read_csv("nifty_500_list.csv")
	Row_list=[]
	for rows in stock_list.itertuples(): 
		my_list =[rows.Symbol] 
		Row_list.append(my_list[0]) 
	for list in Row_list:
		scrap(list) 
			
			
if __name__ == "__main__":
	main()
