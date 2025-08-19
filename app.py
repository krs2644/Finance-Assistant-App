import streamlit as st
from transformers import pipeline

# Set page configuration for a better look and feel
st.set_page_config(
    page_title="Finance QA Assistant",
    page_icon="💬",
    layout="centered", # Centers the content on the page
)

# App Title and description
st.title("💬 Finance QA Assistant")
st.write("Ask any finance-related question and get an answer based on the given context!")

# Function to load the HuggingFace QA pipeline
# @st.cache_resource is used to cache the model loading. This means the model
# will only be loaded once when the app starts, improving performance on subsequent runs.
@st.cache_resource
def load_model():
    # It's good practice to ensure 'accelerate' is installed for various
    # transformer models, though 'distilbert-base-cased-distilled-squad'
    # might not strictly require it.
    # To install it, run: pip install accelerate
    return pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad" # Using a smaller, efficient model
    )

# Load the QA pipeline
qa_pipeline = load_model()

# Input fields for context and question
context = st.text_area("Enter the context (e.g., a finance article):", height=200, help="Provide the financial text from which you want to extract answers.")
question = st.text_input("Enter your question:", help="Type your question related to the context provided.")

# Button to trigger the answer generation
if st.button("Get Answer"):
    # Check if both context and question are provided
    if context.strip() and question.strip():
        with st.spinner('Finding answer...'): # Show a spinner while processing
            # Call the QA pipeline with the provided question and context
            result = qa_pipeline(question=question, context=context)
            st.success("Here's the answer:")
            # Display the extracted answer
            st.write(f"**Answer:** {result['answer']}")
            # Optionally, you can also show the confidence score and start/end positions
            # st.write(f"Confidence: {result['score']:.2f}")
            # st.write(f"Start: {result['start']}, End: {result['end']}")
    else:
        # Warning message if inputs are missing
        st.warning("⚠️ Please provide both context and question!")

# Footer for the application
st.markdown("---")
st.caption("Built with ❤️ using HuggingFace and Streamlit")

