from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Parser:

    def __init__(self , base_url : str):
        self.base_url = base_url

    def parse(self , html : str) -> list[dict]:

        soup = BeautifulSoup(html , "html.parser") 
        articles = soup.select("article.result")

        programs = []

        for article in articles:

            headings = article.select("h3 .result__headline-content")

            institution = (headings[0].get_text(" " , strip = True) if len(headings) > 0 else None )
            program_name = (headings[1].get_text(" " , strip = True) if len(headings) > 1 else None)

            link = article.select_one("a.result__link")
            href = link.get("href") if link else None
            detail_url = urljoin(self.base_url , href) if href else None

            details = {}
            detail_items = article.select("dl .js-show-more-item")

            for item in detail_items:
                
                term = item.select_one("dt")
                if term is None:
                    continue

                label = term.get_text(" " , strip = True).rstrip(":").strip()
                definitions = item.select("dd")

                values = [definition.get_text(" " , strip = True) 
                          for definition in definitions 
                          if definition.get_text(" " , strip = True)]

                if label and values:
                    details[label] = values[0] if len(values) == 1 else values


            program = {
                       "id" : article.get("id") ,
                       "Institution" : institution,
                       "Program name" : program_name,
                       "Detail URL" : detail_url,
                       "Details" : details 
                       }

            programs.append(program)


        return programs

            
        
      
            

           
            
            