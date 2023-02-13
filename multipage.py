import streamlit as st

class MultiPage:
    def __init__(self) -> None:
        self.pages = []
        self.experiments = []
    
    def add_page(self, title, func):
        self.pages.append(
            {
            'title': title,
            'function': func
            }
        )
    
    def add_experiment(self, title, id:int):
        self.experiments.append(
            {
                'title':title,
                'id':id
            }
        )
    
    def runpg(self, uID, uName):
        page = st.sidebar.selectbox(
            '请选择内容', 
            self.pages,
            format_func=lambda page: page['title']
        )
        experiment = st.sidebar.selectbox(
            '请选择实验',
            self.experiments,
            format_func=lambda experiment: experiment['title']
        )
        expID = experiment['id']
        page['function'](expID, uID, uName)
    
