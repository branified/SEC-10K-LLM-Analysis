# SEC-10K-LLM-Analysis

## Overview

This is Streamlit dashboard on SEC-10K filings of companies and the insights from a LLM API.
Access here: https://sec-10k-llm-analysis.streamlit.app/

## Tech Stack
* Python: Access to robust libraries (Llama API, Streamlit, VADER, Plotly, and SEC Edgar Downloader) and simplicity greatly expedited the development process. This also ensures that the application will be scalable and maintainable as it evolves.
    - Llama API: This is one of the top open-source LLMs on the market and I already have experience integrating it
    - Streamlit: Seamlessly integrates with Python backend
    - Plotly: A robust library that works with Streamlit and provides professional visualizations with added functionality
    - SEC Edgar Downloader: Needed a way to quickly and efficiently download the SEC-10K filings of the companies for the given date range

## Insights
The insights were chosen for display in the dashboard based on their relevance for SEC-10K analysis as well as demonstrating the capabilities of AI integration

1. Revenue Trends
    * This visualizes the revenue of the company throughout the years and shows how much they have grown. This shows the LLM's ability to process numbers and perform calculations.
2. Management Analysis
    * This summarizes what the management feels about the company and whether they feel positively or negatively in the overall direction the company is heading. This demonstrates the LLM's ability to determine the emotions behind sentences.
3. Risk Factors
    * This summarizes the common concerns and risks from the SEC-10K filing that the company in facing. This showcases the LLM's ability to to parse through large portions of text and give meaningful summaries.

## Improvements

1. Provide more analysis with more credits
2. Add ability to search any company
3. Add ability to parse through XML for more recent SEC-10K Filings. Allows more data for analysis.
4. Move away from txt files and only process using memory to save space