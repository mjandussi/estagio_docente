import streamlit as st

def titulo_app():
    st.markdown('<div class="title-main">Contabilidade Pública</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle-main">App de apoio à disciplina.</div>',
        unsafe_allow_html=True
    )

def aplicar_estilos():
    st.markdown("""
        <style>
        .main {padding-top: 1rem;}

        .title-main {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        .subtitle-main {
            font-size: 1.05rem;
            color: #444;
            margin-bottom: 1.2rem;
        }

        .section-title {
            font-size: 1.45rem;
            font-weight: 700;
            margin-top: 0.8rem;
            margin-bottom: 0.8rem;
        }

        .box {
            border: 1px solid #d9d9d9;
            border-radius: 12px;
            padding: 16px 18px;
            margin-bottom: 12px;
            background-color: #484549FF;
            color: white;
        }

        .box * {
            color: white !important;
        }

        .light-box {
            border: 1px solid #d9d9d9;
            border-radius: 12px;
            padding: 16px 18px;
            margin-bottom: 12px;
            background-color: #484549FF;
            color: white;
        }

        .light-box * {
            color: white !important;
        }

        .flow-box {
            border: 1px dashed #9db3e0;
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 12px;
            background-color: #484549FF;
            font-weight: 600;
            text-align: center;
            color: white;
        }

        .flow-box * {
            color: white !important;
        }
                
        /* wrapper do botão */
        .menu-wrapper {
            padding: 4px;
            border-radius: 16px;
            margin-bottom: 6px;
        }

        /* wrapper ativo */
        .menu-wrapper.active {
            background: linear-gradient(135deg, #2563eb, #60a5fa);
            box-shadow: 0 0 0 1px rgba(96, 165, 250, 0.35), 0 6px 18px rgba(37, 99, 235, 0.28);
        }

        /* botão normal */
        div[data-testid="stButton"] > button {
            height: 3.2rem;
            border-radius: 12px;
            font-weight: 700;
            border: 1px solid #374151;
            background-color: #7310A8FF;
            color: white;
            transition: all 0.2s ease;
        }

        /* hover */
        div[data-testid="stButton"] > button:hover {
            border-color: #60a5fa;
            background-color: #172033;
        }
        </style>
        """, unsafe_allow_html=True)
    