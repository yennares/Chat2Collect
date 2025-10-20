# Chat2Collect

An AI-driven text chat interface designed to engage debtors empathetically while ensuring timely collections. It reminds, nudges, and guides users toward repayment through natural, human-like conversations — combining empathy with intelligence to improve recovery outcomes.

## Features

- AI-powered conversational debt collection agent
- Empathetic and professional communication
- FDCPA compliance guidelines built-in
- Real-time chat interface using Streamlit
- Powered by Groq's Llama 3.3 70B model

## Prerequisites

- Python 3.9 or higher
- Groq API key ([Get one here](https://console.groq.com))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yennares/Chat2Collect.git
cd Chat2Collect
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your Groq API key
# GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Docker Deployment

Build and run using Docker:
```bash
# Build the image
docker build -t chat2collect .

# Run the container
docker run -p 8080:8080 --env-file .env chat2collect
```

Access the application at `http://localhost:8080`

## Configuration

### Customer Details
Edit the `recipient_details` dictionary in `app.py` to customize debtor information:
- Company name
- Customer name and contact details
- Loan contract number
- Outstanding balance
- Days past due
- Grace period

### System Prompts
The AI agent's behavior is controlled by prompts in `systemprompt.txt`. You can customize:
- Agent personality and tone
- Collection strategies
- Compliance guidelines
- Response structure

## Project Structure

```
Chat2Collect/
├── app.py                  # Main Streamlit application
├── systemprompt.txt        # System prompt for collection agent
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── logo.png               # Application logo
├── .env                   # Environment variables (not in git)
├── .env.example           # Example environment file
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Technology Stack

- **Frontend:** Streamlit
- **LLM Provider:** Groq API (Llama 3.3 70B)
- **Language:** Python 3.9+
- **Deployment:** Docker

## Important Notes

- This is an MVP (Minimum Viable Product) version
- Ensure compliance with local debt collection regulations
- The `.env` file contains sensitive API keys and should never be committed to version control
- All conversations are stored in session state (not persistent)

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Support

For issues or questions, please create an issue on GitHub.
