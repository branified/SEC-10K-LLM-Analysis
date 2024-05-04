import streamlit as st
import plotly.graph_objects as go
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Bar chart to visualize risk factors
def bar_chart(risk_factor, title):
    # Create the bar chart
    fig = go.Figure(data=go.Bar(x=risk_factor['Label'], y=risk_factor['Value']))
    fig.update_layout(title=title, xaxis_title="Insights", yaxis_title="Count")
    st.plotly_chart(fig)

# Sentiment analysis from management's analysis
def sentiment_analysis(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = sentiment_score['pos'],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Sentiment Confidence"},
        gauge = {'axis': {'range': [-1, 1]},
                 'bar': {'color': "darkblue"},
                 'steps' : [
                     {'range': [-1, -0.5], 'color': "red"},
                     {'range': [-0.5, 0.5], 'color': "orange"},
                     {'range': [0.5, 1], 'color': "green"}]}))
    st.plotly_chart(fig)

# Line chart to visualize revenue trends
def line_chart(revenue_data):
    fig = go.Figure(data=go.Scatter(x=revenue_data['Year'], y=revenue_data['Revenue'], mode='lines+markers'))
    fig.update_layout(title="Revenue through the Years", xaxis_title="Year", yaxis_title="Revenue (in millions) ($)")
    st.plotly_chart(fig)

# Streamlit app
def main():
    st.title("SEC 10-K LLM Analysis")

    # Microsoft Revenue Data from LLM
    msft_revenue_data = {
        'Year': [2002, 2003, 2004, 2006, 2007, 2008, 2009, 2010, 2016, 2017, 2018],
        'Revenue': [28365, 32187, 36835, 44282, 51122, 60420, 58437, 62484, 59005, 60557, 62849]
    }

    # Apple Revenue Data from LLM
    aapl_revenue_data = {
        'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
        'Revenue': [7983, 5363, 5742, 6207, 8279, 13931, 24006, 32479, 36537, 32479, 65225]
    }

    # Microsoft Risk Factors
    msft_risk_factors = {'Label': [
        "Open Source Competition",
        "Cybersecurity",
        "Intellectual Property",
        "Regulatory Risks",
        "Business Model Concerns",
        "Technology Integration Concerns"
    ],
    'Value': [15, 6, 12, 5, 4, 4]}

    # Apple Risk Factors
    aapl_risk_factors = {'Label': [
        "Uncertain Economic Conditions",
        "Geopolitical Uncertainty",
        "Litigations",
        "Global Competition",
        "Research Development",
        "Manufacturing Concerns"
    ],
    'Value': [10, 5, 9, 15, 5, 11]}

    # Dropdown for selecting a company
    selected_company = st.selectbox("Select a Company", ["Microsoft", "Apple"])

    if selected_company == "Microsoft":
        # Display revenue trends
        st.header("Revenue Trends")
        line_chart(msft_revenue_data)

        # Display management analysis
        st.header("Management Analysis")
        sentiment_analysis("llm_output/msft-management-analysis-response.txt")

        # Display risk factors
        st.header("Risk Factors")
        bar_chart(msft_risk_factors, "Common Phrases of Risk Factors")

    else:
        # Display revenue trends
        st.header("Revenue Trends")
        line_chart(aapl_revenue_data)

        # Display management analysis
        st.header("Management Analysis")
        sentiment_analysis("llm_output/aapl-management-analysis-response.txt")

        # Display risk factors
        st.header("Risk Factors")
        bar_chart(aapl_risk_factors, "Common Phrases of Risk Factors")

if __name__ == '__main__':
    main()



