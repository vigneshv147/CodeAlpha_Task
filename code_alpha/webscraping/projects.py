import  requests 
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random 


def webscrap(url,filename):
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"}

    response=requests.get(url,headers=header)
    print("thanks for sharing an data")
    num=random.randint(3,8)
    time.sleep(num)
    if response.status_code==200:
        
        htmls=response.text
            
        ## create soup
        soup=BeautifulSoup(htmls,'lxml')
        
        
        ## print(soup.prettify())
        div_html=soup.find_all("div",role="listitem")
        
        with open(f"{filename}.csv", "w", encoding="utf-8",newline="")as file:
            write=csv.writer(file)
            
            write.writerow(['hotel_name','location','prices','rating','rating-rate','total_review','link'])
        
            for hotel in div_html:
                hotel_name=hotel.find("div",class_="b87c397a13 a3e0b4ffd1").text.strip()
                
                location=hotel.find('span',class_="d823fbbeed f9b3563dd4").text.strip()
                
                price=hotel.find("span",class_="b87c397a13 f2f358d1de ab607752a2").text.replace("â¹Â","")
                prices=price.replace(" ","")
                rating_div = hotel.find("div", class_="f63b14ab7a f546354b44 becbee2f63")
                rating = rating_div.text.strip() if rating_div else "N/A"

                
                rating_rate_div = hotel.find("div", class_="f63b14ab7a dff2e52086")
                rating_rate = rating_rate_div.text.strip() if rating_rate_div else "N/A"

                
                total_review=hotel.find("div",class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
                
                link=hotel.find('a',href=True).get('href')
                
                write.writerow([hotel_name,location,prices,rating,rating_rate,total_review,link])
            
            # print(f"hotel_name:{hotel_name}")
            
            # print(f"location:{location} ")
            
            # print(f"rating:{rating}")
            
            # print(f"rating_rate:{rating_rate}")
            
            # print(f"reviews:{total_review}")
            
            # print(f"price:{prices}")
            
            # print(f"link :{link}")
            
            # print(" ")
    else:
        print("cannot be open the fles")
        
if __name__ == '__main__':
    url=input("Enter your url: ")
    filename=input("Enter your filename: ")
    webscrap(url,filename)
