# MyPythonLearn

This project is for practicing Python modules, currently focusing on LangChain.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/MyPythonLearn.git
    cd MyPythonLearn
    ```

2.  **Create and sync the virtual environment:**
    ```bash
    uv sync
    ```

3.  **Set up environment variables:**
    - Rename `.env.example` to `.env`.
    - Add your DeepSeek API key to the `.env` file.

## Usage

Each Python file in the `src/` directory is a standalone example:

-   `1_basic.py`: Basic LLM invocation.
-   `2_prompts.py`: Using prompt templates.
-   `3_stream.py`: Streaming LLM responses.

To run an example:
```bash
python src/1_basic.py
```
