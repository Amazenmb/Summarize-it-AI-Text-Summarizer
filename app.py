import streamlit as st
import requests

st.set_page_config(page_title="AI Text Summarizer", layout="wide")

# Background styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #EBC034;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#  Add Hugging Face API endpoint
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

#  Add API key
HEADERS = {"Authorization": "Bearer YOUR_ACESSS_TOKEN"}



# Function to call Hugging Face API
#def summarize(text, max_len, min_len):
#    payload = {
#        "inputs": text,
#        "parameters": {
#            "max_length": max_len,
#            "min_length": min_len
#        }
#    }
#
#    response = requests.post(API_URL, headers=HEADERS, json=payload)
#    return response.json()


def summarize(text, max_len, min_len):
    def chunk_text(text, chunk_size=400):
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunks.append(" ".join(words[i:i+chunk_size]))
        return chunks

    chunks = chunk_text(text)

    summaries = []

    for chunk in chunks:
        payload = {
            "inputs": chunk,
            "parameters": {
                "max_length": max_len,
                "min_length": min_len
            }
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        result = response.json()

        if isinstance(result, list):
            summaries.append(result[0]["summary_text"])

    # Combine all summaries
    final_text = " ".join(summaries)

    # Optional: summarize again for cleaner output
    payload = {
        "inputs": final_text,
        "parameters": {
            "max_length": max_len,
            "min_length": min_len
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    final_result = response.json()

    if isinstance(final_result, list):
        return final_result
    else:
        return {"error": "Final summarization failed"}




# ----UI using streamlit----
st.title("🧠 AI Text Summarizer")
st.markdown("Summarize long text into concise insights instantly.")

# Adding Input box
text = st.text_area("Enter your text:", height=300)


# Defining length of summary

max_len=200
min_len=80


# Add Button
if st.button("Summarize"):
	if text.strip() == "":
 		st.warning("Please enter some text")
	else:
		with st.spinner("Summarizing..."):
			result = summarize(text, max_len, min_len) 
			# Success case
			if isinstance(result, list):
				st.success("Summary Generated!")
				summary=(result[0]["summary_text"])
				st.markdown(
                    			f"""
                    			<div style="
                       				 background-color: #FFF8DC;
                       				 padding: 20px;
                        			 border-radius: 15px;
                        			 border-left: 8px solid #EBC034;
                        			 box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                       				 margin-top: 10px;
                    			">
                        			 <h4 style="margin-bottom:10px;">✨ Summary</h4>
                        			 <p style="color:#333333; font-size:16px; line-height:1.6;">
                            				{summary}
                        			 </p>
                    			</div>
                   			""",
                    			unsafe_allow_html=True
               			)
	
			# Error case
			elif "error" in result:
				st.error("Something went wrong. Please try again.")
			else: st.write(result)