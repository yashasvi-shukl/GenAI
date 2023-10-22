# Overview
Introducing the MultiPDF Chat App, a Python application that revolutionizes the way you interact with multiple PDF documents. This innovative tool allows you to engage in natural language conversations with your PDFs, and in return, it provides insightful responses based on the document content. Utilizing a powerful language model, the app ensures precision in answering your queries, all tailored to the PDFs at hand.

Please keep in mind that the application responds exclusively to questions pertaining to the loaded PDFs.


# Functionality

![image](https://github.com/yashasvi-shukl/GenAI/assets/22805226/5ff20e0b-839c-4795-99cf-de782149a086)

The MultiPDF Chat App operates seamlessly through the following steps:
1. PDF Ingestion: The app ingests multiple PDF documents and extracts their textual content.

2. Text Segmentation: Extracted text undergoes segmentation, breaking it into manageable units for effective processing. 

3. Leveraging Language Models: The application harnesses a language model to create vector representations (embeddings) of these segmented text units. The embedding of chunked data are then store in vectorstore i.e. FAISS

4. Semantic Matching: When you pose a question, the app swiftly compares it with the segmented text units, identifying the most semantically relevant ones.

5. Response Crafting: The chosen text segments are then funneled to the language model, which crafts a response rooted in the pertinent content of the PDFs.

# Installation and Dependencies
To get started with the MultiPDF Chat App, follow these installation instructions:

Begin by cloning the repository to your local machine.

Next, install the necessary dependencies by executing the following command:
```
 pip install -r requirements.txt
```

Acquire an API key from OpenAI/Huggingfacce, and integrate it into the .env (rename example.env to .env) file within your project directory:
```
>>> OPENAI_API_KEY=your_secret_api_key
>>> HUGGINGFACEHUB_API_TOKEN=your_secret_api_key
```
# Usage Guide

To experience the MultiPDF Chat App, follow these straightforward steps:

1. First, ensure you've successfully installed the required dependencies and incorporated the OpenAI API key into the .env file.

2. Execute the main.py file using the Streamlit CLI/Terminal with the following command:
```
>>> streamlit run chat_with_pdf_app.py
OR
>>> py -m streamlit run chat_with_pdf_app.py
```
3. The application will seamlessly launch in your default web browser, showcasing the user-friendly interface.

4. To begin, load multiple PDF documents into the application, following the provided instructions.

5. Engage in natural language conversations with your loaded PDFs via the chat interface.

# Screenshots
![1](https://github.com/yashasvi-shukl/GenAI/assets/22805226/8940d740-cab8-4f9b-a0a7-b91c8affce93)

![2](https://github.com/yashasvi-shukl/GenAI/assets/22805226/0ff3df2e-33f7-4d75-9786-21344d74d498)

![3](https://github.com/yashasvi-shukl/GenAI/assets/22805226/13545fa3-5853-48c3-be77-cf473ac32d4c)

</br></br></br>
Hope this helps!!
