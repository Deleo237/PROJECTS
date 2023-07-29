from bs4 import BeautifulSoup
from analysis import content_analysis
from save import save_variables
import requests
import openpyxl

def scrap(url, num):
    # request content
    con = requests.get(url)
    # To navigate throught the contain we 
    soup =BeautifulSoup(con.content,'html.parser')
    
    # Create an empty list to store the extracted text content
    text_content = []
    
    try:
        # Find the <h1> element with class "entry-title"
        title_element = soup.find("h1", class_="entry-title")
        
    except:
        # Find the <h1> element with class "tdb-title-text"
        title_element = soup.find("h1", class_="tdb-title-text")
        
    finally:
        # Firstly appending the title to the list
        title = title_element.text.strip()
        text_content.append(title)
    
    try:
        # Find the <div> element with class "td-ss-main-content"
        main_content_div = soup.find("div", class_="td-ss-main-content")
        
        try:
            # Find the nested <div> element with class "td-post-content"
            post_content_div = main_content_div.find("div", class_="td-post-content")
        except:
            print("Couldn't find post content")
            
        try:
            # Find all <h3> elements within the nested <div> element
            h3_elements = post_content_div.find_all("h3")
            
            # Extract the text content of each <h3> element and append it to the list
            for element in h3_elements:
                text = element.text.strip()
                text_content.append(text)
                
        except:
            print("Couldn't find h3 elements")
            
        try:
            # Find all <strong> elements within the nested <div> element
            strong_elements = post_content_div.find_all("strong")
            
            # Extract the text content of each <strong> element and append it to the list
            for element in strong_elements:
                text = element.text.strip()
                text_content.append(text)
                
        except:
            print("Couldn't find strong elements")
            
        try:
            # Find all <p> elements within the nested <div> element
            p_elements = post_content_div.find_all("p")
            
            # Extract the text content of each <p> element and append it to the list
            for element in p_elements:
                text = element.text.strip()
                text_content.append(text)
                
        except:
            print("Couldn't find p elements")
            
        try:
            # Find all <li> elements within the nested <div> element
            li_elements = post_content_div.find_all("li")
            
            # Extract the text content of each <li> element and append it to the list
            for element in li_elements:
                text = element.text.strip()
                text_content.append(text)
                
        except:
            print("Couldn't find li elements")

    except:
        
        # Find the <div> element with class "td_block_wrap"
        main_content_div = soup.find("div", class_="td_block_wrap")
        
        try:
            # Find the nested <div> element with class "tdb-block-inner"
            post_content_div = main_content_div.find("div", class_="tdb-block-inner")
        except:
            print("Couldn't find post content")
            
        try:
            # Find all <h3> elements within the nested <div> element
            h3_elements = post_content_div.find_all("h3")
            
            # Extract the text content of each <h3> element and append it to the list
            for element in h3_elements:
                text = element.text.strip()
                text_content.append(text)
                
        except:
            print("Couldn't find h3 elements")
            
        try:
            # Find all <strong> elements within the nested <div> element
            strong_elements = post_content_div.find_all("strong")
            
            # Extract the text content of each <strong> element and append it to the list
            for element in strong_elements:
                text = element.text.strip()
                text_content.append(text)
                
        except:
            print("Couldn't find strong elements")
            
        try:
            # Find all <p> elements within the nested <div> element
            p_elements = post_content_div.find_all("p")
            
            # Extract the text content of each <p> element and append it to the list
            for element in p_elements:
                text = element.text.strip()
                text_content.append(text)
                
        except:
            print("Couldn't find p elements")

        try:
            # Find all <li> elements within the nested <div> element
            li_elements = post_content_div.find_all("li")
            
            # Extract the text content of each <li> element and append it to the list
            for element in li_elements:
                text = element.text.strip()
                text_content.append(text)
                
        except:
            print("Couldn't find li elements")

    finally:
        # Combine the text content into a single string
        combined = '\n'.join(text_content)
        
        # Perform Calculation
        variables =content_analysis(combined)
        
        # Save content in the right place
        save_variables(variables, num)
        combined_text = url+'\n'+num+'\n\n'+combined
        
        # Saving the context in txt file
        savescrap(combined_text)

    return combined_text

def savescrap(info):
    with open('URL_ID.txt', 'a+') as container:
        container.write(info)
        container.write('\n\n\n')


# Read the xlsx file using the openpyxl library
Input = openpyxl.load_workbook('Input.xlsx')

# Specify the sheet you want to work in
input = Input['Sheet1']

location=2

# Iterate over rows to collect the urls
for column in input.iter_rows(min_row=2, max_row=115, values_only=True):
    print('\n\n',str(column[1]),'\n',str((column[0])),'\n')
    # Scrapping of content of the various url one at a time
    try:
        scrap(str(column[1]), location)
    except:
        print('An Error Occured during scrapping')
        try:
            scrap(str(column[1]), location)
        except:
            print('An Error Occured during scrapping')
    location+=1
    
# close the xlsx file
Input.close()