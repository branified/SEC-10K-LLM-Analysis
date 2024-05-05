import streamlit as st
from utils import bar_chart, sentiment_analysis, line_chart

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
        # Display Microsoft revenue trends
        st.header("Revenue Trends")
        line_chart(msft_revenue_data)

        # Display Microsoft management analysis
        st.header("Management Analysis")
        sentiment_analysis("llm_output/msft-management-analysis-response.txt")

        # Display Microsoft risk factors
        st.header("Risk Factors")
        bar_chart(msft_risk_factors)

    else:
        # Display Apple revenue trends
        st.header("Revenue Trends")
        line_chart(aapl_revenue_data)

        # Display Apple management analysis
        st.header("Management Analysis")
        sentiment_analysis("llm_output/aapl-management-analysis-response.txt")

        # Display Apple risk factors
        st.header("Risk Factors")
        bar_chart(aapl_risk_factors)

if __name__ == '__main__':
    main()
