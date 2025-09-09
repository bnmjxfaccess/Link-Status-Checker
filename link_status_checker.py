import requests

def check_url_status(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException:
        return None

def read_urls_from_file(file_path):
    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls

def main():
    input_file = 'urls.txt'  # Input file containing URLs, one per line
    output_file = 'url_status_report.txt'
    
    urls = read_urls_from_file(input_file)
    with open(output_file, 'w') as out:
        for url in urls:
            status = check_url_status(url)
            if status:
                out.write(f"{url} : {status}\n")
                print(f"{url} : {status}")
            else:
                out.write(f"{url} : ERROR\n")
                print(f"{url} : ERROR")

if __name__ == "__main__":
    main()
