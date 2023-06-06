import streamlit as st
from pg.simulatedata import simrule

class Page:
    def __init__(self, exp_id):
        self.exp_id = exp_id

    def run(self):
        self.sim = simrule.ExpSimulate(self.exp_id)
        self.sim.run()
