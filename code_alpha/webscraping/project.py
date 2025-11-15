
# Task 1-WEB SCRAPING IN AMAZON WEBSITE
import  requests 
from bs4 import BeautifulSoup
import lxml
import csv
import time
import random 

def webscrap_amazon(url,filename):
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0"}
    response=requests.get(url,headers=header)
    if response.status_code==200:
        print("thank for sharing your data")
        num=random.randint(3,5)
        time.sleep(num)
        
        htmls=response.text
            
        ## create soup
        soup=BeautifulSoup(htmls,'lxml')
        
        
        ## print(soup.prettify())
        div_product=soup.find_all("div",role="listitem")
        
        with open(f"{filename}.csv", "w", encoding="utf-8",newline="")as file:
            write=csv.writer(file)
            
            write.writerow(['Product_name','Rating','price','Delivary_date','link'])
        
            for product in div_product:
                
                name_tag = product.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
                
                if name_tag:
                    products_name = name_tag.text.strip()
                    
                    products1_name=products_name.split("|")[0].strip()
                    
                    product_name=products1_name.split(",")[0].strip()
                    
                    rating_tag = product.find("span", class_="a-size-small a-color-base")

                    if rating_tag:
                        rating = rating_tag.text.strip()
                    else:
                        rating = "N/A"
                    
                    price=product.find("span",class_="a-price-whole")
                    
                    if price :
                        prices=price.text.strip()
                    else:
                        prices="TBA"
                    
                    delivarys= product.find("span",class_="a-text-bold")
                    
                    if delivarys:
                        delivary= delivarys.text.strip()
                    else:
                        delivary="TBA"
                
                    link_tag = product.find("a", class_="a-link-normal s-line-clamp-4 s-link-style a-text-normal")

                    if link_tag and link_tag.has_attr("href"):
                        
                        product_link = "https://www.amazon.in" + link_tag["href"]
                    else:
                        product_link = "N/A"

                
                    write.writerow([product_name,rating,prices,delivary,product_link])
                    # print(f"product_name:{product_name}")
                    
                    # print(f"rating_rate:{rating}")
                    
                    # print(f"delivary_date :{delivary}")
                    
                    # print(f"offer_percentage :{rating}")
                    
                    # print(f"price :{prices}")
                    
                    # print(f"link :{product_link}")
                    
                    # print(" ")
    else:
        print("cannot be open the fles")
        
if __name__ == '__main__':
    url=input("Enter your url: ")
    filename=input("Enter your filename: ")
    webscrap_amazon(url,filename)
