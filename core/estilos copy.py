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



import streamlit.components.v1 as components

def render_timeline():
    html = """
    <style>
    body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        background: transparent;
    }

    .timeline-wrapper {
        padding: 10px 10px 10px 10px;
        overflow-x: auto;
        overflow-y: hidden;
    }

    .timeline-wrapper::-webkit-scrollbar {
        height: 10px;
    }

    .timeline-wrapper::-webkit-scrollbar-thumb {
        background: #60a5fa;
        border-radius: 999px;
    }

    .timeline-wrapper::-webkit-scrollbar-track {
        background: #1e293b;
        border-radius: 999px;
    }

    .timeline {
        position: relative;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        min-width: 1650px;
        padding: 90px 20px 55px 20px;
        box-sizing: border-box;
    }

    .timeline::before {
        content: "";
        position: absolute;
        top: 50%;
        left: 40px;
        right: 40px;
        height: 6px;
        background: linear-gradient(90deg, #2563eb, #0ea5e9);
        border-radius: 999px;
        transform: translateY(-50%);
        z-index: 1;
    }

    .timeline-item {
        position: relative;
        width: 210px;
        text-align: center;
        z-index: 2;
        flex-shrink: 0;
    }

    .timeline-dot {
        width: 24px;
        height: 24px;
        background: #2563eb;
        border: 4px solid white;
        border-radius: 50%;
        margin: 0 auto;
        box-shadow: 0 0 0 4px #93c5fd;
        position: relative;
        z-index: 3;
    }

    .timeline-year {
        font-size: 1.05rem;
        font-weight: 700;
        color: #60a5fa;
        margin-bottom: 12px;
        margin-top: 12px;
    }

    .timeline-card {
        background: #ffffff;
        border: 1px solid #dbe3ee;
        border-radius: 18px;
        padding: 16px 14px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.10);
        min-height: 190px;
        box-sizing: border-box;
    }

    .timeline-card h4 {
        margin: 0 0 10px 0;
        font-size: 1.05rem;
        line-height: 1.2;
        color: #0f172a;
    }

    .timeline-card p {
        margin: 0;
        font-size: 0.95rem;
        color: #475569;
        line-height: 1.45;
    }

    .timeline-top {
        margin-bottom: 28px;
    }

    .timeline-bottom {
        margin-top: 28px;
    }

    .timeline-connector-top,
    .timeline-connector-bottom {
        width: 2px;
        height: 55px;
        background: #cbd5e1;
        margin: 0 auto;
    }
    </style>

    <div class="timeline-wrapper">
        <div class="timeline">

            <div class="timeline-item">
                <div class="timeline-top">
                    <div class="timeline-card">
                        <h4>Período pré-1964</h4>
                        <p>Predomínio do controle do Tesouro, foco em caixa e baixa padronização entre os entes públicos.</p>
                    </div>
                    <div class="timeline-connector-top"></div>
                </div>
                <div class="timeline-dot"></div>
                <div class="timeline-year">Antes de 1964</div>
            </div>

            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-year">1964</div>
                <div class="timeline-bottom">
                    <div class="timeline-connector-bottom"></div>
                    <div class="timeline-card">
                        <h4>Lei nº 4.320</h4>
                        <p>Normas gerais de direito financeiro e estruturação clássica da contabilidade pública.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-top">
                    <div class="timeline-card">
                        <h4>Constituição Federal</h4>
                        <p>Fortalecimento do planejamento governamental por meio do PPA, da LDO e da LOA.</p>
                    </div>
                    <div class="timeline-connector-top"></div>
                </div>
                <div class="timeline-dot"></div>
                <div class="timeline-year">1988</div>
            </div>

            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-year">2000</div>
                <div class="timeline-bottom">
                    <div class="timeline-connector-bottom"></div>
                    <div class="timeline-card">
                        <h4>Lei de Responsabilidade Fiscal</h4>
                        <p>Transparência, metas, limites e fortalecimento do controle das finanças públicas.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-top">
                    <div class="timeline-card">
                        <h4>Início da Convergência aos Padrões Internacionais</h4>
                        <p>Início da transição do foco predominantemente orçamentário para o enfoque patrimonial por meio das NBC TSP.</p>
                    </div>
                    <div class="timeline-connector-top"></div>
                </div>
                <div class="timeline-dot"></div>
                <div class="timeline-year">2008</div>
            </div>

            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-year">2013+</div>
                <div class="timeline-bottom">
                    <div class="timeline-connector-bottom"></div>
                    <div class="timeline-card">
                        <h4>MCASP e PCASP</h4>
                        <p>Início da obrigatoriedade dos novos procedimentos contábeis e elaboração de um plano de contas padronizado com abrangência nacional.</p>
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-top">
                    <div class="timeline-card">
                        <h4>Matriz de Saldos Contábeis e Ranking Siconfi</h4>
                        <p>Implantação da MSC e avaliação da qualidade e da consistência da informação contábil e fiscal dos entes.</p>
                    </div>
                    <div class="timeline-connector-top"></div>
                </div>
                <div class="timeline-dot"></div>
                <div class="timeline-year">2019+</div>
            </div>

        </div>
    </div>
    """

    components.html(html, height=540, scrolling=True)

