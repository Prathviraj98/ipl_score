import requests
import streamlit as st
from bs4 import BeautifulSoup
import time
score=''
st.set_page_config(
    page_title="live score",
    page_icon=":cricket_bat_and_ball:",
    layout="centered",
)
st.title("Live Score...:cricket_bat_and_ball:")
dynamic_text = st.empty()
def fetch_live_score():
    url = "https://www.espncricinfo.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            score_card1 = soup.find('div', class_='ds-truncate')
            score1 = score_card1.text.strip()
            score_card2 = soup.find('div', class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo')
            score2 = score_card2.text.strip()
            score_card3 = soup.find('p', class_='ds-text-tight-s ds-font-bold ds-capitalize ds-truncate !ds-text-typo-mid3')
            score3 = score_card3.text.strip()
            score_card4 = soup.find('p', class_='ds-text-tight-xs ds-font-medium ds-truncate ds-text-typo')
            score4 = score_card4.text.strip()
            return (score2+"  "+score3+"  "+"("+score4+")")
        else:
            return "Failed to fetch live score. Status code: {}".format(response.status_code)
    except Exception as e:
        return str(e)

def main():
    scored="---"
    url = "https://www.espncricinfo.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    score_card1 = soup.find('div', class_='ds-truncate')
    score1 = score_card1.text.strip()
    
    st.subheader(score1)
    while True:
        
        score = fetch_live_score()

        if score != scored:
            scored=score
            dynamic_text.subheader(scored)
   
            #with col2:
                #st.text(scored)
if __name__ == "__main__":
    main()
