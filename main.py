from sec_edgar_downloader import Downloader
import os
from utils import iterate_sec_filings, risk_factor_extract, revenue_trends_extract, management_analysis_extract
from llm import analyze_text_file

def main():
    # dl = Downloader("University of Denver", "john.alfred@du.edu")

    # companies = ["AAPL", "MSFT"]

    # for company in companies:
    #     dl.get("10-K", company, after="1995-01-01", before="2024-01-01")
    
    # print("Downloaded SEC 10-K Filings")

    # HTML Parser
    # iterate_sec_filings("sec-edgar-filings", html_to_text)
    # print("Parsed")
    
    # iterate_sec_filings("extracted-text", risk_factor_extract)
    # print("Risk Factors extracted")

    # iterate_sec_filings("extracted-text", revenue_trends_extract)
    # iterate_sec_filings("extracted-text", management_analysis_extract)

    aapl_risk_factor_range = [(4,19),
                              (38,76),
                              (95,133),
                              (152,186),
                              (205,239),
                              (258,289),
                              (304,339)]
    aapl_revenue_trends_range = [(1024,1988),
                                 (24794,27029),
                                 (133786,137125),
                                 (158705,164151),
                                 (179105,185925),
                                 (203237,209725),
                                 (226827,228210),
                                 (248851,255996),
                                 (278989,279006),
                                 (281777,287953),
                                 (305547,318551),
                                 (414539,419840),
                                 (459858,469913)]
    aapl_management_analysis_range = [(25,53),
                                      (70,100),
                                      (14935,14936),
                                      (14951,14991),
                                      (21967,21995),
                                      (22012,22042)]
    msft_risk_factor_range = [(5,12),
                              (60,96),
                              (146,150),
                              (23773,23809)]
    msft_revenue_trends_range = [(2,5316),
                                 (36437,40936),
                                 (607469,611312)]
    msft_management_analysis_range = [(34,42),
                                      (54,68),
                                      (82,284)]

    aapl_risk_factor_llm_response = analyze_text_file("insights/risk-factors/AAPL_risk_factor_insights.txt", aapl_risk_factor_range, "risk")
    print("Done")
    aapl_revenue_trends_llm_response = analyze_text_file("insights/revenue-trends/AAPL_revenue_trends_insights.txt", aapl_revenue_trends_range, "revenue")
    print('Done')
    aapl_management_analysis_llm_response = analyze_text_file("insights/management-analysis/AAPL_management_analysis_insights.txt", aapl_management_analysis_range, "management")
    print('Done')

    msft_risk_factor_llm_response = analyze_text_file("insights/risk-factors/MSFT_risk_factor_insights.txt", msft_risk_factor_range, "risk")
    print('Done')
    msft_revenue_trends_llm_response = analyze_text_file("insights/revenue-trends/MSFT_revenue_trends_insights.txt", msft_revenue_trends_range, "revenue")
    print('Done')
    msft_management_analysis_llm_response = analyze_text_file("insights/management-analysis/MSFT_management_analysis_insights.txt", msft_management_analysis_range, "management")
    print('Done')
    
    responses = [
        (aapl_risk_factor_llm_response, "aapl-risk-factor-response.txt"),
        (aapl_revenue_trends_llm_response, "aapl-revenue-trends-response.txt"),
        (aapl_management_analysis_llm_response, "aapl-management-analysis-response.txt"),
        (msft_risk_factor_llm_response, "msft-risk-factor-response.txt"),
        (msft_revenue_trends_llm_response, "msft-revenue-trends-response.txt"),
        (msft_management_analysis_llm_response, "msft-management-analysis-response.txt")
    ]

    os.makedirs("llm_output", exist_ok=True)

    # Write each response to a text file
    for response, file_name in responses:
        output_file_path = os.path.join("llm_output", file_name)
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(response)

if __name__ == '__main__':
    main()