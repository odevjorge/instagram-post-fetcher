# Instagram Post Fetcher

The Instagram Post Fetcher is a Python module designed to extract information from Instagram posts using Selenium.

## Features

- Fetches post data including account username, descriptions, media URLs, and post timestamps.
- Utilizes Selenium for web scraping tasks.
- Provides a modular structure for easy integration into other projects or workflows.
- Supports both image and video posts.
- Requires Python 3.x and the Selenium library.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/seu-usuario/instagram-post-fetcher.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Import the DataManage class from the module:
   ```python
   from core.management.data.post import DataManage
   ```

2. Initialize a Manage object:
   ```python
   data = DataManage()
   ```

3. Retrieve post information using the provided methods:
   ```python
   post_info = data.get_all_post_info()
   ```

## Output Structure:

The output will be in the following structure:

   ```python
   {
    'account_username': 'solucoesdigitais',
    'description': '🔍 Estamos sempre buscando maneiras de aprimorar nossos serviços e atender melhor aos nossos clientes. Quais sugestões você tem para nós?\n\n',
    'tags': ['#solucoesdigitais', '#feedback', '#melhorias', '#atendimentocliente'],
    'images_url': {
        1: 'https://fakecdn.example.com/image1.jpg',
        2: 'https://fakecdn.example.com/image2.jpg'
    },
    'post_date': '2024-02-27T09:30:00.000Z'
   }
   ```

5. Analyze and process the retrieved post information as needed.

## Usage Disclaimer

This tool is intended for legitimate and authorized use cases, such as research, data analysis, and automation of tasks within the boundaries of Instagram's terms of service. The developers of this tool do not endorse any unauthorized or unethical use of the software. Users are responsible for ensuring that their use of this tool complies with all applicable laws and regulations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests to help improve this project.