import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import time
from pathlib import Path
import tempfile

# Run Command: streamlit run app.py

from dotenv import load_dotenv
load_dotenv()
import os
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

st.set_page_config(
    page_title="Multi Model Video Summarizer Agent", 
    page_icon=":movie_camera:",
    layout="wide",
    )
st.title("Video Summarizer Agent")
st.header("Powered By Gemini 2.0 and DuckDuckGo")

@st.cache_resource
def init_agent():
    return Agent(
        name="Video Summarizer Agent",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )

multi_model_agent = init_agent()

video_file = st.file_uploader(
    "Upload video you want to summarize:",
    type=["mp4", "avi", "mov", "mkv"],
    help="Upload video for AI analysis"
    )


if video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name
    
    st.video(video_path, format="video/mp4", start_time=0)

    user_query = st.text_area(
        "What insights do you want to seeking from the video?",
        placeholder="Enter your query here...",
        help="Provide Specific questions for better results",
    )

    if st.button("Analyze Video", key="analyze_video"):
        if not user_query:
            st.warning("Please enter a query.")
        else:
            try:
                with st.spinner("Analyzing video..."):
                    # Upload the video file to Gemini
                    processed_video = upload_file(video_path)
                    while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)
                    
                    analysis_prompt = (
                        f"""
                        Analyze the uploaded video for content and context
                        Respond to the following query using video insights and supplementry web research : {user_query}
                        Provide a detailed and user friendly, actionalbe response.
                        """
                    )


                    response = multi_model_agent.run(analysis_prompt, videos=[processed_video])
                
                st.subheader("Analysis Result")
                st.markdown(response.content)


            except Exception as error:
                st.error(f"An error occurred: {error}")
            finally:
                Path(video_path).unlink(missing_ok=True)

else:
    st.info("Please upload a video file to get started.")


st.markdown(
    """
        <style>
        .stTextArea textarea{
            height: 100px;
        }
        </style>
    """,
    unsafe_allow_html=True
)
