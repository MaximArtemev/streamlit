import streamlit as st
import plotly.express as px
import pandas as pd


@st.cache()
def process_data(uploaded_file):
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        return file_details


def main():
    st.title('Streamlit # 2')
    uploaded_file = st.file_uploader("Upload your file", type=['csv'])

    if st.button('Get info'):
        print(uploaded_file)
        file_details = process_data(uploaded_file)
        st.write(file_details)

    df = pd.read_csv(uploaded_file)
    if st.button('Show table'):
        st.write(df)

    if st.button('Get insights'):
        st.write(df.describe())

    if st.button('Show plot'):
        fig = px.scatter(df, x='Height', y='Weight', color='Gender')
        st.plotly_chart(fig)


if __name__ == '__main__':
    main()
