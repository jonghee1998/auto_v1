from PIL import Image
from pathlib import Path
import toml
import json
import pandas as pd
import streamlit as st

def get_project_root():
    return str(Path(__file__).parent.parent.parent)

@st.cache_data
def load_config(config_streamlit_filename, config_readme_filename):
    config_streamlit = toml.load(Path(get_project_root()) / f"config/{config_streamlit_filename}")
    config_readme = toml.load(Path(get_project_root()) / f"config/{config_readme_filename}")
    return dict(config_streamlit), dict(config_readme)

@st.cache_data
def load_image(image_name):
    return Image.open(Path(get_project_root()) / f"assets/{image_name}")

@st.cache_data
def load_icon(sector):
    sector = sector.replace('/', '')
    with open(Path(get_project_root()) / f"assets/{sector}_icon.json", 'r') as f:
        icon = json.load(f)
    return icon

@st.cache_data
def load_peers():
    peerinfo = pd.read_csv(Path(get_project_root()) / "data/Peer Information.csv")
    peer_country_match = peerinfo[['Peer', 'Country']].set_index('Peer').to_dict()['Country']
    return peerinfo, peer_country_match 

@st.cache_data
def load_metadata():
    meta = pd.read_csv(Path(get_project_root()) / "data/Metadata Value Factors.csv", encoding='cp949')
    return meta