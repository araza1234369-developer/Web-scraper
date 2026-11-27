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
            
            detail_items = article.select(".js-show-more-list")

            for item in detail_items:

                label = item.select("dd")
                degree = label[0].get_text(" " , strip = True)
                period_of_study = label[1].get_text(" " , strip = True)
                location = label[2].get_text(" " , strip = True)
                study_mode = label[3].get_text(" " , strip = True)
                deadlines = label[4].get_text(" " , strip = True)

        
            program = {

                       "id" : article.get("id") ,
                       "Institution" : institution,
                       "Program name" : program_name,
                       "Detail URL" : detail_url,
                       "Degree" : degree,
                       "Period of study" : period_of_study,
                       "Location" : location,
                       "study_mode" : study_mode,
                       "deadlines" : deadlines
                      
                       }

            programs.append(program)


        return programs

            
        
      
            

           
            
            