'''
This script extracts all hyperlinks from a specified webpage and saves them to a text file.
'''
import requests
from bs4 import BeautifulSoup
def get_links(url):
    '''
    Extracts all hyperlinks from the specified webpage.
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if there's an HTTP error
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
        return []
def save_links(links):
    '''
    Saves the extracted links to a text file.
    '''
    with open('myLinks.txt', 'w') as file:
        for link in links:
            file.write(link + '\n')
def main():
    '''
    Main function to execute the script.
    '''
    try:
        url = input("Enter the URL of the webpage you want to analyze: ")
        links = get_links(url)
        if links:
            save_links(links)
            print("Links extracted and saved successfully.")
        else:
            print("No links found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()