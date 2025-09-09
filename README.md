# Website Link Status Checker

This Python script checks the status of a list of URLs provided in a file and reports whether each URL is valid (i.e., reachable).

## Features

- Reads URLs from a text file (one URL per line)
- Checks if each URL is reachable using HTTP requests
- Reports HTTP status codes for each URL
- Outputs results to both the console and a report file

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/) library

Install the required package with:
```bash
pip install requests
```

## Usage

1. **Add your URLs to a file named `urls.txt`**
    - Each URL should be on a separate line.
    - Example:
      ```
      https://www.google.com
      https://www.example.com
      https://invalid.url
      ```

2. **Run the script**
    ```bash
    python link_status_checker.py
    ```

3. **Check the results**
    - The script prints the status of each URL to the console.
    - A report is also saved in `url_status_report.txt`, showing the HTTP status code or "ERROR" for unreachable links.

## Example Output

```
https://www.google.com : 200
https://www.example.com : 200
https://invalid.url : ERROR
```

## Customization

- Change the input filename from `urls.txt` to another filename by modifying the `input_file` variable in `link_status_checker.py`.
- Change the output report filename by editing the `output_file` variable.

## License

This project is provided for educational purposes and does not carry any warranty. Use it at your own risk.
