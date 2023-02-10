from pprint import pprint
import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"
# trying to access any url with the help of request module
# request module will use get method inorder to get response from any website/URL
resp = requests.get(url) # following method will return a response object, containing multiple attrs and function

# we can use multiple status codes inorder to validate our reponse
"""More on Satus-Codes can be found here : https://developer.mozilla.org/en-US/docs/Web/HTTP/Status"""

# We are concerned with if request was successful or not, hence considering only below 2 scenarios
# 1. Code-200 : Successful
# 2. Code-400 : Bad request
# In order to check the status we can use the statusc_code attr of the response object

print(resp.status_code)
# if response status code is not greater then 400 we can conclude request was successful
if resp.status_code >= 200 and resp.status_code < 400:
    # in response we might get some content stored in the content attr. in bytes
    byte_content = resp.content # get the content from response in bytes

    # the content we recieve in response is in byte format, which is of no use to us in the following process we will convert the bytes in a more useful structure which is a "tree"
    # this process of converting one format to another is called parsing, and yes obviously we will require a parser to do so
    
    # parse the HTML content
    # for parsing the bytes content in more useful one we will use the html_parser provided by the bs4 module
    tree_str = BeautifulSoup(byte_content, 'html.parser')
    # print(tree_str.prettify()) # just for printing the content in proper manner

    # traversing through the tree
    # getting the title of the HTML Page
    title = tree_str.title # following attribute is a Tag-type object in the tree-str
    # Most commonly use objects
    # print(type(tree_str))               # 3. BeautifulSoup
    # print(type(title))                  # 1. Tag
    # print(type(tree_str.string))        # 2. Navigable String
    # 4. Comment

    # searching for elements in the page/tree
    # find all method is used to find all the elements from the page with passed tag
    # eg: finding all the paragraphs
    paras = tree_str.find_all('p')

    # finding all the anchors from the page
    anchors = tree_str.find_all('a')
        
    # print(type(paras))                  # 4. ResultSet : just a list containing multiple objects provided by BeautifulSoup
    # print(paras)
    # print(paras[0])                     # Tag-type

    # if instead of "find_all" we use "find" function we will get the very first element instead of all
    # print(tree_str.find('p'))
    first_para = tree_str.find('p') # this will return the very first para it will find in the 
    # print(first_para['class']) # following statement will get all the classes in the first_para
    # print(first_para)
    # print(first_para.get_text()) # this will print the text inside the following tag, with tag or styling we will get the plain text

    # querying on the page
    # finding all the elements with class "text-sm"
    p_text_sm = tree_str.find_all("p", class_="text-sm") # to find all
    # p_text_sm = tree_str.find("p", class_="text-sm") # to find only the first one
    # print(p_text_sm)
    actual_links = set()
    # getting all the links from the page
    for link in anchors:
        if link != "#" and link != "/" and "http" not in link.get('href'):
            # print(link.get('href')) # following is an tag object we can use the get method to get any of the attribute from the element
            # links provided will not be the whole url
            # for that we need to add the base url before the link
            actual_links.add(f"{url.rstrip('/')}{link.get('href')}")
    # pprint(actual_links)

    # searching based on id
    element_by_id = tree_str.find(id = "<id we want to search by>")


    # for elements having nested element, i.e. a <p> having <div> inside of it and so on
    # we can iterate through the content of the parent to find the child element inside of it
    # for elem in paras[1].content:
    #     print(elem)
    # print(type(paras[0].find_parents()))


# closing the connection of the response object
resp.close()