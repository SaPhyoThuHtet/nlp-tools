import streamlit as st
import numpy as np
import pandas as pd
import re
#import librosa
#from pydub import AudioSegment

st.sidebar.image(
    "images/peacock-3.png",
    width=200,
)
st.sidebar.markdown("<h3 style='text-align: center;'>NLP Tools</h3>", unsafe_allow_html=True)
select = pd.DataFrame()
select['topics'] = ['chracter-tokenization', 'syllable-tokenization', 'syllbreak-zawgyi', 'detect-email', 'burmese2braille(Muu Haung)']
option = st.sidebar.selectbox(
    '',select['topics'])


st.sidebar.write("Copyrights@SaPhyoThuHtet")


if(option == "chracter-tokenization"):
    user_input = st.text_input("Input", "အမုန်းမပွားရဘူးနော်")
    result = re.sub(r"([^\s])",r"\1 ", user_input)   
    st.write("Output:",result)
    
if(option == "syllable-tokenization"):
    st.markdown("<h4 style='text-align: center;'>Syllable Tokenization</h4>", unsafe_allow_html=True)
    st.write("\n")
    st.write("Description: Syllable break for Burmese, Pali (Myanmar), Rakhine, Pa-Oh, Word break for English, Char break for other language")
    user_input = st.text_input("Input", "အမုန်းမပွားရဘူးနော်")
    result = re.sub(r"(([A-Za-z0-9]+)|[က-အ|ဥ|ဦ](င်္|[က-အ][့း]*[်]|္[က-အ]|[ါ-ှႏꩻ][ꩻ]*){0,}|.)",r"\1 ", user_input)    
    st.write("Output:",result)
    
if (option == 'syllbreak-zawgyi'):
    st.write("Description: Syllable break for Burmese in Zawgyi Encoding")
    user_input = st.text_input("Input", "သီဟိုဠ္မွ ဉာဏ္ႀကီးရွင္သည္ အာယုဝၯနေဆးၫႊန္းစာကို ဇလြန္ေဈးေဘး ဗာဒံပင္ထက္ အဓိ႒ာန္လ်က္ ဂဃနဏဖတ္ခဲ့သည္။ေဆာင္")
    result = re.sub(r'(ေ*ျ*ႀ*ၿ*ၾ*[က-အ|႐|ႏ|ဥ|ဦ|႒]([က-အ]့*္[့း]*|[ါ-ာ]|[ိ-ူ]|[ဲ-္]|်|[ြ-ှ]|[ၐ-ၽ]|[ႁ-ႎ]|[႑-႟]){0,}|.)',r'\1 ',user_input)
    st.write("Output:",result)
    
if(option == "detect-email"):
     user_input = st.text_input("Input", "ဒီနေ့တော့ phyothuhtet39@gmail.com ဆီကို mail  ပို့ရမယ်။ နေဉီး သူက Microsoft Mail phyothuhtet@studentambassadors.com ကို သုံးတာလားမေးကြည့်ပါဦး။ ငါ ayethida89.young@utycc.edu.mm  ကနေ ပို့လိုက်မယ်။")
     emails = re.findall(r'[\w\.]+@[\w]+(?:\.[\w]+)+', user_input.strip())
     st.write("Emails:",";".join(sorted(emails)))
        
if (option == 'burmese2braille(Muu Haung)'):
     st.markdown("<h4 style='text-align: center;'>Burmese 2 Braille (Mu Haung)</h4>", unsafe_allow_html=True)
     st.write("\n")
     dictionary = {'က': '⡁', 'ခ': '⢈', 'ဂ': '⠛', 'ဃ': '⠟', 'င': '⡈', 'စ': '⡌', 'ဆ': '⡤', 'ဇ': '⠵', 'ဈ': '⣌', 'ည': '⠷', 'ဋ': '⠳', 'ဌ': '⠻', 'ဍ': '⠾', 'ဎ': '⠿', 'ဏ': '⡬', 'တ': '⠞', 'ထ': '⠚', 'ဒ': '⠙', 'ဓ': '⠋', 'န': '⠝', 'ပ': '⡖', 'ဖ': '⠰', 'ဗ': '⢉', 'ဘ': '⠃', 'မ': '⡉', 'ယ': '⠽', 'ရ': '⠗', 'လ': '⠇', 'ဝ': '⠺', 'သ': '⠹', 'ဟ': '⠓', 'ဠ': '⠸', 'အ': '⠣', 'ဉ': '⠧', 'ဤ': '⠰⠪', '၍': '⠯', '၏': '⠕', '၌': '⠦', '၎င်း': '⠬', '၊': '?', '။': '?', 'ာ': '⠁', 'ါ': '⠎', 'ိ': '⠊', 'ီ': '⠪', 'ု': '⠑', 'ူ': '⠥', 'ေ': '⠱', 'ဲ': '⠡', '?': '⠴', 'ံ': '⠉', 'င်္': '⡈⠄⠤', 'ျ': '⠔', 'ဥ': '⠰⠑', 'ဦး': '⠰⠑⠪⠆', 'ဧ': '⠰⠱', 'ဣ': '⠰⠊', 'ြ': '⠢', '်': '⠄', 'ွ': '⠜', 'ှ': '⠭', '့': '⠂', '္': '⠤', 'း': '⠆'}
     user_input = st.text_input("Input","မသန်ပေမယ့်စွမ်းသည်")
     user_input = re.sub(r'([က-အ])([ံ]|[ါ-ဲ]|[က-အ]်)',r'\1အ\2',user_input.strip())
     user_input = re.sub(r'([က-အ]([ျ-ှ]){1,})',r'\1အ',user_input);
     #user_input = re.sub(r'(([က-အ])([ွ])(ှ)အံ)',r'\1\3အံ\2',user_input);
     to_normal =  re.sub(r'([က-အ][ျ-ှ]{1,})အ',r'\1', user_input);
     to_normal =  re.sub(r'([က-အ])အ([ံ]|[ါ-ဲ]|[က-အ]်)',r'\1\2', to_normal)
    
     result = ""
     for i in user_input:
        if (i in dictionary.keys()):
            result += dictionary[i]
        else:
            result += i
            
     st.write("Muu Haung:", user_input)
     st.write("Back to Normal(Used RE):", to_normal)
     st.write("Output:", result)
