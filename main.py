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
    
    # print(html_content)
    
    # parse the HTML content
    # for parsing the bytes content in more useful one we will use the html_parser provided by the bs4 module
    tree_str = BeautifulSoup(byte_content, 'html.parser')
    print(tree_str.prettify()) # just for printing the content in proper manner


    # traversing through the tree
    # getting the title of the HTML Page
    title = tree_str.title # following attribute is a Tag-type object in the tree-str
    # Most commonly use objects
    print(type(tree_str))               # 3. BeautifulSoup
    print(type(title))                  # 1. Tag
    print(type(tree_str.string))        # 2. Navigable String
    # 4. Comment


    # searching for elements in the page/tree
    # eg: finding all the paragraphs
    paras = tree_str.find_all('p')




# closing the connection of the response object
resp.close()