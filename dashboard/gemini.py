import os
import google.generativeai as genai
import textwrap
import markdown as markdown
from IPython.display import Markdown
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


class MyGemini:
    def __init__(self, ):
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ]
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash-latest',
            generation_config=self.generation_config,
        )

    def ask_gemini(self, text):
        res = self.model.generate_content(text)
        return res


def convert_ipython_markdown_to_html(md_object):
    md_content = md_object.data
    html_content = markdown.markdown(md_content)
    return html_content


# model = MyGemini()
# response = model.ask_gemini("Hi how r you")
# response.resolve()
# result = to_markdown(response.text)
# result = convert_ipython_markdown_to_html(result)
# print(result)
