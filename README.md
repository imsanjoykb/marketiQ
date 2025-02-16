# MARKETLYTICS 🤖

[![Twitter Follow](https://img.shields.io/twitter/follow/Intelytics?style=social)](https://twitter.com/intelyticsai)

### MARKETKYTICS is an advanced application that leverages cutting-edge technologies to provide intelligent and faster marketing solutions to automate business.
![Intelytics](assets/intelytics-logo/intelytics_banner.jpg)

By integrating the strengths of Langchain and OpenAI, Robby employs large language models to provide users with seamless, 
context-aware natural language interactions for a better understanding of their data.🧠
## Quick Start 🚀

[![Intelytics](https://img.shields.io/static/v1?label=INTELYTICS-AI&message=Visit%20Website&color=ffffff&labelColor=ADD8E6&style=for-the-badge)](https://intelytics.pro)

## Running Locally 💻
Follow these steps to set up and run the service locally :

### Prerequisites
- Python 3.8 or higher
- Git

### Installation
Clone the repository :

`git clone https://github.com/Intelytics-AI/marketlytics-pro.git`


Navigate to the project directory :

`cd marketlytics-pro`

Database Configuration for PostgreSQL

```
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```
Create a virtual environment :
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Install the required dependencies in the virtual environment :

`pip install -r requirements.txt`


Launch the chat service locally :

`streamlit run src/Home.py`

#### That's it! The service is now up and running locally. 🤗

## Contributing 🙌
Contributions are always welcome! If you want to contribute to this project, please open an issue, submit a pull request or contact me at sanjoy.eee32@gmail.com (:


