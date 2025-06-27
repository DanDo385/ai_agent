# AI Agent & Calculator Project

This project contains two main components: an AI coding agent and a mathematical calculator.

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- A Google Gemini API key

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai_agent
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   Create a `.env` file in the project root:
   ```bash
   echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
   ```
   Replace `your_actual_api_key_here` with your real Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

## 🤖 AI Agent

The AI agent is a sophisticated coding assistant that can help with file operations and code analysis.

### Usage

**Activate the virtual environment first:**
```bash
source venv/bin/activate
```

**Run the AI agent:**
```bash
python3 main.py "your question or request"
```

### Examples

```bash
# List files in the current directory
python3 main.py "list files in the current directory"

# List files in a specific directory
python3 main.py "list files in the calculator directory"

# Ask for help with code
python3 main.py "help me understand the calculator code"
```

### Features

- **File Operations**: List files and directories
- **Code Analysis**: Analyze and understand code structure
- **Bug Detection**: Identify and fix issues in code
- **Security**: All operations are constrained to the working directory

## 🧮 Calculator

A mathematical calculator that supports basic arithmetic operations with proper operator precedence.

### Usage

```bash
cd calculator
python3 main.py "expression"
```

### Examples

```bash
# Basic arithmetic
python3 calculator/main.py "3 + 5"
python3 calculator/main.py "10 - 3"
python3 calculator/main.py "4 * 6"
python3 calculator/main.py "15 / 3"

# Complex expressions with operator precedence
python3 calculator/main.py "3 + 7 * 2"  # Should return 17
python3 calculator/main.py "10 - 2 * 3"  # Should return 4
```

### Supported Operations

- **Addition**: `+`
- **Subtraction**: `-`
- **Multiplication**: `*`
- **Division**: `/`

### Operator Precedence

- Multiplication and division have higher precedence (level 2)
- Addition and subtraction have lower precedence (level 1)

## 📁 Project Structure

```
ai_agent/
├── main.py                 # AI agent entry point
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── functions/
│   ├── __init__.py
│   └── get_files_info.py  # File listing utility
├── calculator/
│   ├── main.py           # Calculator entry point
│   ├── pkg/
│   │   ├── calculator.py # Calculator logic
│   │   └── render.py     # Output formatting
│   └── tests.py          # Calculator tests
└── venv/                 # Virtual environment
```

## 🔧 Development

### Running Tests

```bash
# Test the file reading utility
python3 tests.py

# Test the calculator
cd calculator
python3 tests.py
```

### Virtual Environment Management

**Activate:**
```bash
source venv/bin/activate
```

**Deactivate:**
```bash
deactivate
```

**Alternative ways to run without activating:**
```bash
# Use virtual environment's Python directly
venv/bin/python3 main.py "your question"

# Or create a shell script
echo '#!/bin/bash
source venv/bin/activate
python3 main.py "$@"' > run_ai.sh
chmod +x run_ai.sh
./run_ai.sh "your question"
```

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'dotenv'"**
   - Make sure the virtual environment is activated
   - Run: `source venv/bin/activate`

2. **"API key not valid"**
   - Check that your `.env` file exists and contains a valid `GEMINI_API_KEY`
   - Verify your API key at [Google AI Studio](https://makersuite.google.com/app/apikey)

3. **"Cannot read file"**
   - The AI agent can only list files, not read their contents
   - Use the file listing function to explore the project structure

### Getting Help

- Check that all dependencies are installed: `pip list`
- Verify your API key is working
- Make sure you're in the correct directory when running commands

## 📝 License

This project is for educational purposes as part of the Boot.dev curriculum. 