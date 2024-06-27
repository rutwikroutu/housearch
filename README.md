# HouseArch: Automating EHR Documentation with Large Language Models and RAG

![HouseArch Logo](path/to/logo.png)

HouseArch leverages OpenAI’s Whisper model and Retrieval-Augmented Generation (RAG) to automate and streamline the documentation process for Electronic Health Records (EHRs). This project significantly reduces the time clinicians spend on documentation, allowing them to focus more on patient care.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
HouseArch is designed to enhance the efficiency of EHR documentation by transcribing clinical notes and generating relevant entries using advanced AI techniques. By integrating OpenAI’s Whisper model for transcription and a RAG framework for context-based generation, HouseArch ensures accurate and contextually relevant medical documentation.

## Features
- **Automated Transcription**: Utilizes OpenAI’s Whisper model for high-accuracy transcription of clinical notes and conversations.
- **Contextual Document Retrieval**: Employs RAG to retrieve relevant medical documents from a vector database.
- **Efficient EHR Generation**: Generates EHR entries based on transcribed notes and retrieved documents.
- **High Accuracy**: Achieves a Word Error Rate (WER) of 11.12% and high retrieval accuracy.

## Installation
### Prerequisites
- Python 3.7 or higher
- OpenAI API key
- Qdrant server (local or hosted)
- Required Python libraries

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/HouseArch.git
    cd HouseArch
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage
1. **Prepare the dataset:**
    Ensure your medical articles are in the `/path/to/pubmed/files` directory.

2. **Run the script:**
    ```bash
    python main.py
    ```

3. **Query the system:**
    Modify the query in the script to retrieve relevant document chunks:
    ```python
    query = "your_query"
    ```

4. **Generate the EHR entries:**
    The script will output the generated EHR entries based on the input query and context.

## Directory Structure
