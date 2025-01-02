import streamlit as st

class PageUI:
    @staticmethod
    def display_options():
        company = st.radio("브랜드를 선택하세요:", ["기아", "현대"])
        if company:
            return company
        else:
            st.write('선택하세요')


    @staticmethod
    def display_results(results):
        for car in results:
            st.write(f"**{car['name']}** - {car['price']}")

