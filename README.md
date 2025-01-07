# Multi-Model Video Summarizer Agent

## Overview

The **Multi-Model Video Summarizer Agent** is a Streamlit-based web application that leverages Google's Gemini 2.0 and DuckDuckGo search to provide actionable insights from uploaded video files. By analyzing video content and supplementing it with relevant web research, the agent delivers detailed responses tailored to user queries.

## Features
- Upload and process videos in formats such as `.mp4`, `.avi`, `.mov`, and `.mkv`.
- Analyze video content and context using Gemini 2.0.
- Supplement insights with real-time web research via DuckDuckGo.
- User-friendly interface with actionable analysis results.

## Prerequisites

Ensure the following are installed on your system:
- Python 3.12
- pip

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dhirajdj30/Video-Summarizer
   cd VideoSummarizer
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate    # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the project root.
   - Add your Google API key to the file:
     ```
     GOOGLE_API_KEY="Your_Google_API_Key"
     ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

6. **Upload a Video**
   - Open the application in your browser (default: `http://localhost:8501`).
   - Upload a video and input your query to receive detailed analysis results.

## Project Structure
```
.
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── README.md             # Project documentation
```

## Dependencies

The application uses the following libraries:
- `google-generativeai` - For interaction with Google's Gemini 2.0 API.
- `phidata` - Provides the Agent and model utilities.
- `streamlit` - For building the web interface.
- `duckduckgo-search` - For real-time web research.

## Key Features of the Code

- **File Upload and Video Display**: Users can upload videos, which are displayed within the application.
- **Agent Initialization**: The `Agent` is powered by Gemini 2.0 and DuckDuckGo tools to process video and provide detailed responses.
- **Error Handling**: Includes robust error handling to manage invalid inputs and API errors.
- **Temporary File Management**: Uses temporary files for video processing to ensure smooth operation.

## Note
Ensure your Google API key has the necessary permissions to use Gemini 2.0 features.

## License
This project is open-source and available under the [MIT License](LICENSE).
