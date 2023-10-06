# DNS Resolvers Validator

This project aims to validate public DNS resolvers on a daily basis. By fetching a list of public DNS servers from [public-dns.info](https://public-dns.info/nameservers.txt), the script checks the validity of each resolver and writes the valid ones to a file named `resolvers.txt`.

## Features

- **Daily Updates**: The script is designed to run daily, ensuring that the list of valid DNS resolvers is always up-to-date.
- **Concurrent Validation**: Uses asynchronous programming to validate multiple DNS servers concurrently, making the process faster.
- **Trusted Validation**: Validates DNS servers against trusted domains to ensure accuracy and mitigate DNS poisoning risks.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python libraries: `aiohttp`, `aiodns`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/strobes-co/dns_validate.git
   cd dns_validate
   ```

2. Install the required Python libraries:
   ```bash
   pip install aiohttp aiodns
   ```

### Usage

Run the script:
```bash
python3 dns_validate/main.py
```

After execution, check the `resolvers.txt` file for a list of valid DNS resolvers.

## Automation

This project is integrated with GitHub Actions to run the validation script daily. Check the `.github/workflows` directory for the workflow configuration.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
