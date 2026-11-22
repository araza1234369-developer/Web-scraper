from bs4 import BeautifulSoup


class Parser:

    def parse(self , html : str) -> list[dict]:

        soup = BeautifulSoup(html , "html.parser") 
        articles = soup.select("article.result")

        programs = []

        for article in articles:

            headings = article.select("h3 .result__headline-content")

            institution = (headings[0].get_text(" " , strip = True) if len(headings) > 0 else None )
            program_name = (headings[1].get_text(" " , strip = True) if len(headings) > 1 else None)

            program = {
                       "id" : article.get("id") ,
                       "Institution" : institution,
                       "Program name" : program_name, 
                       }

            programs.append(program)

        return programs

           
            
            