import streamlit as st
import numpy as np

def main():
    st.set_page_config(page_title="iPhone Calculator", page_icon="🔢", layout="centered")
    
    st.markdown("""
        <style>
            .big-button {
                font-size: 24px !important;
                width: 80px;
                height: 80px;
                border-radius: 50%;
                margin: 5px;
                background-color: #333;
                color: white;
                text-align: center;
                border: none;
                display: inline-block;
            }
            .big-button.orange { background-color: #FF9500; }
            .big-button.grey { background-color: #A5A5A5; color: black; }
            .screen {
                font-size: 40px;
                text-align: right;
                padding: 20px;
                background: black;
                color: white;
                border-radius: 10px;
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    if 'expression' not in st.session_state:
        st.session_state.expression = ""
    
    st.markdown(f'<div class="screen">{st.session_state.expression}</div>', unsafe_allow_html=True)
    
    buttons = [
        ['AC', '+/-', '%', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '.', '=']
    ]
    
    for row in buttons:
        cols = st.columns(len(row))
        for i, btn in enumerate(row):
            if cols[i].button(btn, key=btn, help=btn, use_container_width=True):
                handle_button_click(btn)

def handle_button_click(btn):
    if btn == 'AC':
        st.session_state.expression = ""
    elif btn == '=':
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except:
            st.session_state.expression = "Error"
    elif btn == '+/-':
        if st.session_state.expression:
            try:
                st.session_state.expression = str(-float(st.session_state.expression))
            except:
                pass
    else:
        st.session_state.expression += btn
    
    st.experimental_rerun()

if __name__ == "__main__":
    main()
