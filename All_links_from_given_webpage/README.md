# All Links from a Given Webpage

This script, written in Python, is designed to extract all hyperlinks from a specified webpage and save them to a text file. It's a handy tool for web scraping and analysis, allowing users to quickly gather and store links from any web page.

## Prerequisites

### Required Modules

- BeautifulSoup4: A Python library for pulling data out of HTML and XML files.
- requests: A Python HTTP library for sending HTTP requests.

To install these prerequisites, run the following command:

```bash
$ pip install -r requirements.txt
```

## How to Run the Script

1. Open your terminal or command prompt.

2. Navigate to the directory where the script is located.

3. Execute the script by running:

   ```bash
   $ python get_links.py
   ```

4. When prompted, enter the URL of the webpage you want to analyze.

5. The script will process the webpage and save all extracted links as an array in a file named `myLinks.txt` in the same directory.

## Output

After successful execution, you'll find a file named `myLinks.txt` in the script's directory. This file contains all the hyperlinks extracted from the specified webpage, stored as an array.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/YOUR_GITHUB_REPO/issues). If you want to contribute to the project, please fork the repository and create a pull request.

## Authors

- [Mitesh](https://github.com/Mitesh2499)
- [Michael Mba](https://github.com/mikeysan)

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements

Special thanks to everyone who contributes to this project. Your involvement is greatly appreciated!

*Note: This script is for educational purposes. Please ensure you have permission to scrape the website in question.*