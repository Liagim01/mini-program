import requests
import csv
class WebsiteStatusChecker:
    def __init__(self, file_path):
        self.file_path = file_path
    def check_status(self):
        websites = self.load_websites()
        results = []
        for website in websites:
            status = self.get_status(website)
            results.append((website, status))
        self.save_results(results)
        return "Status check completed. Results saved to website_status.csv"
    def load_websites(self):
        websites = []
        with open(self.file_path, "r") as file:
            for line in file:
                websites.append(line.strip())
        return websites
    def get_status(self, website):
        try:
            response = requests.get(website)
            if response.status_code == 200:
                return "Working"
            else:
                return "Not Working"
        except requests.exceptions.RequestException:
            return "Not Working"
    def save_results(self, results):
        with open("website_status.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Website", "Status"])
            writer.writerows(results)