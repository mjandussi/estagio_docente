
import streamlit as st

st.set_page_config(
    page_title="Contabilidade Pública - Semestre Completo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# ESTILO
# =========================
st.markdown(
    """
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
    .box {
        border: 1px solid #d9d9d9;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 12px;
        background-color: #1D46A3;
        color: white;
    }
    .box h4 {
        margin-top: 0;
        margin-bottom: 0.5rem;
        color: white;
    }
    .box p, .box li {
        color: white;
    }
    .section-title {
        font-size: 1.45rem;
        font-weight: 700;
        margin-top: 0.8rem;
        margin-bottom: 0.8rem;
    }
    .light-box {
        border: 1px solid #d9d9d9;
        border-radius: 12px;
        padding: 16px 18px;
        margin-bottom: 12px;
        background-color: #F7F9FC;
    }
    .flow-box {
        border: 1px dashed #9db3e0;
        border-radius: 12px;
        padding: 14px 16px;
        margin-bottom: 12px;
        background-color: #EEF3FF;
        font-weight: 600;
        text-align: center;
    }
    div[data-testid="stButton"] > button {
        height: 3rem;
        border-radius: 12px;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# CONTEÚDO
# =========================
SECOES = {
    "Home": {
        "titulo": "Contabilidade Pública",
        "subtitulo": "App de apoio para o semestre completo, estruturado conforme o sumário do material do professor."
    },
    "Programa da Disciplina": {
        "titulo": "1. Programa da Disciplina",
        "ementa": [
            "Contabilidade aplicada ao setor público.",
            "Plano de contas e subsistemas.",
            "Registro das operações típicas conforme as NBC T SP 16.",
            "Elaboração das demonstrações contábeis.",
            "Exercícios e cases."
        ],
        "carga": "Carga horária total organizada ao longo do semestre, em dois blocos: fundamentos/registros e demonstrações contábeis.",
        "objetivos": [
            "Compreender os fundamentos da contabilidade aplicada ao setor público.",
            "Identificar a lógica do plano de contas e dos subsistemas.",
            "Analisar o registro das operações típicas da administração pública.",
            "Elaborar e interpretar demonstrações contábeis do setor público.",
            "Aplicar os conceitos por meio de exercícios e cases."
        ],
        "conteudo": [
            "Contabilidade aplicada ao Setor Público",
            "Plano de Contas e Subsistemas",
            "Registro das operações típicas conforme as NBC T SP 16",
            "Exercícios e Cases",
            "Elaboração das Demonstrações Contábeis",
            "Exercícios e Cases"
        ],
        "metodologia": [
            "Aulas expositivas com apoio visual.",
            "Discussão de conceitos e exemplos práticos.",
            "Resolução de exercícios em sala.",
            "Uso de cases para consolidação do conteúdo."
        ],
        "bibliografia": [
            "Lei nº 4.320/1964",
            "NBC T SP 16 / NBC TSP",
            "MCASP",
            "Demais referências indicadas pelo professor no plano de ensino"
        ],
        "curriculum": "Professor responsável pela disciplina, com experiência em finanças, orçamento e contabilidade pública, conforme plano do curso."
    },
    "Contabilidade Aplicada ao Setor Público": {
        "titulo": "2. Contabilidade Aplicada ao Setor Público",
        "objetivo": "Apresentar o conceito, objeto, campo de aplicação e finalidade da contabilidade pública.",
        "topicos": [
            "Objeto da contabilidade pública: patrimônio público",
            "Funções de registro, controle e evidenciação",
            "Integração entre orçamento, finanças e patrimônio",
            "Base normativa da contabilidade aplicada ao setor público"
        ],
        "explicacao": [
            ("Objeto", "A contabilidade aplicada ao setor público tem por objeto o patrimônio público."),
            ("Finalidade", "Registrar, controlar e evidenciar os atos e fatos da gestão pública."),
            ("Abrangência", "Acompanha orçamento, execução financeira, patrimônio e suas variações."),
            ("Normas", "A disciplina se apoia na Lei 4.320/64, nas NBC T SP / NBC TSP e no MCASP.")
        ],
        "fala": "Nesta parte, o ideal é mostrar que a disciplina continua a lógica do orçamento, mas avança para a evidenciação patrimonial."
    },
    "Plano de Contas e Subsistemas": {
        "titulo": "3. Plano de Contas e Subsistemas",
        "objetivo": "Explicar a estrutura do plano de contas e os subsistemas da contabilidade pública.",
        "topicos": [
            "Plano de Contas Aplicado ao Setor Público",
            "Estrutura das classes de contas",
            "Subsistema orçamentário",
            "Subsistema patrimonial",
            "Subsistema de compensação/controle",
            "Integração entre subsistemas"
        ],
        "explicacao": [
            ("Plano de contas", "Organiza o registro contábil de forma padronizada e lógica."),
            ("Classes", "Permitem identificar ativo, passivo, VPA, VPD e controles."),
            ("Subsistema orçamentário", "Acompanha a previsão e a execução do orçamento."),
            ("Subsistema patrimonial", "Evidencia ativos, passivos e patrimônio líquido."),
            ("Subsistema de controle", "Registra atos potenciais e controles relevantes para a gestão.")
        ],
        "fala": "Aqui vale muito mostrar a lógica das classes e a ponte entre orçamento e patrimônio."
    },
    "Registro das Operações Típicas": {
        "titulo": "4. Registro das Operações Típicas conforme as NBC T SP 16",
        "objetivo": "Apresentar os registros contábeis das operações mais usuais da administração pública.",
        "topicos": [
            "Receita pública: previsão, lançamento, arrecadação e recolhimento",
            "Despesa pública: dotação, empenho, liquidação e pagamento",
            "Variações patrimoniais aumentativas e diminutivas",
            "Mutações patrimoniais",
            "Integração entre registro orçamentário e patrimonial"
        ],
        "explicacao": [
            ("Receita", "A execução da receita segue uma sequência lógica que vai da previsão ao recolhimento."),
            ("Despesa", "A execução da despesa passa por empenho, liquidação e pagamento."),
            ("VPA e VPD", "Os fatos podem aumentar ou reduzir o patrimônio líquido."),
            ("Mutação patrimonial", "Nem todo fato altera imediatamente o patrimônio líquido; alguns apenas mudam sua composição."),
            ("Integração", "Os registros orçamentários e patrimoniais se complementam.")
        ],
        "fala": "Esse bloco é central para a prova, então use exemplos simples e repetição dos conceitos-chave."
    },
    "Exercícios e Cases I": {
        "titulo": "5. Exercícios e Cases",
        "objetivo": "Consolidar os temas do primeiro bloco da disciplina por meio de exercícios e situações práticas.",
        "questoes": [
            ("Classifique o fato: impostos arrecadados.", "Receita, orçamentária, corrente, efetiva e VPA."),
            ("Classifique o fato: pagamento de pessoal ativo.", "Despesa, orçamentária, corrente, efetiva e VPD."),
            ("Classifique o fato: aquisição de equipamentos.", "Despesa, orçamentária, de capital, mutação patrimonial e variação qualitativa."),
            ("Qual a sequência correta dos estágios da receita?", "Previsão, lançamento, arrecadação e recolhimento."),
            ("Qual a sequência correta dos estágios da despesa?", "Empenho, liquidação e pagamento.")
        ],
        "case": [
            "Receita prevista de IPTU e sua arrecadação ao longo do exercício.",
            "Despesa com pessoal empenhada, liquidada e paga.",
            "Aquisição de bem permanente com efeito qualitativo no patrimônio."
        ]
    },
    "Elaboração das Demonstrações Contábeis": {
        "titulo": "2. Elaboração das Demonstrações Contábeis",
        "objetivo": "Apresentar a estrutura e a lógica de elaboração das demonstrações contábeis do setor público.",
        "topicos": [
            "Balanço Orçamentário",
            "Balanço Financeiro",
            "Demonstração das Variações Patrimoniais",
            "Balanço Patrimonial",
            "Integração entre os demonstrativos"
        ],
        "explicacao": [
            ("Balanço Orçamentário", "Evidencia a execução do orçamento, confrontando previsão e realização da receita, fixação e execução da despesa."),
            ("Balanço Financeiro", "Evidencia ingressos e dispêndios financeiros, orçamentários e extraorçamentários."),
            ("DVP", "Mostra as variações patrimoniais aumentativas e diminutivas e apura o resultado patrimonial."),
            ("Balanço Patrimonial", "Evidencia a posição patrimonial do ente, com ativo, passivo e patrimônio líquido."),
            ("Integração", "Os demonstrativos devem ser lidos de forma conjunta para compreensão completa da gestão.")
        ],
        "fala": "Nesta parte, o ideal é apresentar a lógica de cada demonstração e depois mostrar como uma dialoga com a outra."
    },
    "Exercícios e Cases II": {
        "titulo": "3. Exercícios e Cases",
        "objetivo": "Fixar a elaboração e a interpretação das demonstrações contábeis por meio de exercícios práticos.",
        "questoes": [
            ("O que o Balanço Orçamentário evidencia?", "A execução das receitas e despesas sob a ótica do orçamento."),
            ("Qual demonstrativo evidencia o resultado patrimonial?", "A Demonstração das Variações Patrimoniais."),
            ("Onde se evidencia a posição de ativo, passivo e patrimônio líquido?", "No Balanço Patrimonial."),
            ("Qual demonstrativo evidencia ingressos e dispêndios financeiros?", "O Balanço Financeiro.")
        ],
        "case": [
            "Montagem simplificada de um Balanço Orçamentário.",
            "Leitura comparada entre Balanço Financeiro e Balanço Patrimonial.",
            "Apuração do resultado patrimonial com base em VPA e VPD."
        ]
    }
}

# =========================
# CABEÇALHO
# =========================
st.markdown('<div class="title-main">Contabilidade Pública</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-main">App semestral estruturado conforme o sumário dos arquivos Word e pensado para apoio à apresentação em sala.</div>',
    unsafe_allow_html=True
)

# =========================
# BOTÕES SUPERIORES
# =========================
labels = [
    "Home",
    "Programa da Disciplina",
    "Contabilidade Aplicada ao Setor Público",
    "Plano de Contas e Subsistemas",
    "Registro das Operações Típicas",
    "Exercícios e Cases I",
    "Elaboração das Demonstrações Contábeis",
    "Exercícios e Cases II"
]

if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

for chunk_start in range(0, len(labels), 4):
    cols = st.columns(4)
    chunk = labels[chunk_start:chunk_start+4]
    for i, label in enumerate(chunk):
        with cols[i]:
            if st.button(label, use_container_width=True):
                st.session_state.pagina = label

pagina = st.session_state.pagina

# =========================
# HOME
# =========================
if pagina == "Home":
    st.markdown('<div class="section-title">Visão geral do semestre</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.15, 1])

    with c1:
        st.markdown(
            """
            <div class="box">
                <h4>Estrutura do app</h4>
                <p>1. Programa da disciplina</p>
                <p>2. Contabilidade aplicada ao Setor Público</p>
                <p>3. Plano de Contas e Subsistemas</p>
                <p>4. Registro das operações típicas conforme as NBC T SP 16</p>
                <p>5. Exercícios e Cases</p>
                <p>6. Elaboração das Demonstrações Contábeis</p>
                <p>7. Exercícios e Cases</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="box">
                <h4>Como usar em sala</h4>
                <p>• Seguir o material do professor como eixo principal</p>
                <p>• Usar os blocos do app como roteiro de exposição</p>
                <p>• Explorar os exercícios ao final de cada parte</p>
                <p>• Retomar os conceitos centrais antes das avaliações</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Lógica da disciplina</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="flow-box">Fundamentos da Contabilidade Pública -> Plano de Contas -> Registros das Operações -> Exercícios e Cases -> Demonstrações Contábeis -> Exercícios e Cases</div>',
        unsafe_allow_html=True
    )

# =========================
# PROGRAMA DA DISCIPLINA
# =========================
elif pagina == "Programa da Disciplina":
    sec = SECOES[pagina]
    st.markdown(f'<div class="section-title">{sec["titulo"]}</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, 0.9])

    with c1:
        st.markdown('<div class="box"><h4>1.1 Ementa</h4>' + "".join([f"<p>• {x}</p>" for x in sec["ementa"]]) + '</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box"><h4>1.2 Carga horária total</h4><p>{sec["carga"]}</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="box"><h4>1.3 Objetivos</h4>' + "".join([f"<p>• {x}</p>" for x in sec["objetivos"]]) + '</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="box"><h4>1.4 Conteúdo programático</h4>' + "".join([f"<p>• {x}</p>" for x in sec["conteudo"]]) + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="box"><h4>1.5 Metodologia</h4>' + "".join([f"<p>• {x}</p>" for x in sec["metodologia"]]) + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="box"><h4>1.6 Bibliografia recomendada</h4>' + "".join([f"<p>• {x}</p>" for x in sec["bibliografia"]]) + '</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="box"><h4>1.7 Curriculum resumido do professor</h4><p>{sec["curriculum"]}</p></div>', unsafe_allow_html=True)

# =========================
# BLOCOS TEÓRICOS
# =========================
elif pagina in [
    "Contabilidade Aplicada ao Setor Público",
    "Plano de Contas e Subsistemas",
    "Registro das Operações Típicas",
    "Elaboração das Demonstrações Contábeis"
]:
    sec = SECOES[pagina]
    st.markdown(f'<div class="section-title">{sec["titulo"]}</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, 0.9])

    with c1:
        st.markdown(
            f"""
            <div class="box">
                <h4>Objetivo do bloco</h4>
                <p>{sec["objetivo"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="box"><h4>Tópicos principais</h4>' +
            "".join([f"<p>• {x}</p>" for x in sec["topicos"]]) +
            '</div>',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="box">
                <h4>Observação para sua fala</h4>
                <p>{sec["fala"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Explicações centrais</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (titulo, texto) in enumerate(sec["explicacao"]):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="light-box">
                    <h4>{titulo}</h4>
                    <p>{texto}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    if pagina == "Registro das Operações Típicas":
        st.markdown('<div class="section-title">Fluxos essenciais</div>', unsafe_allow_html=True)
        st.code("Receita: Previsão -> Lançamento -> Arrecadação -> Recolhimento", language=None)
        st.code("Despesa: Dotação -> Empenho -> Liquidação -> Pagamento", language=None)

# =========================
# EXERCÍCIOS E CASES
# =========================
elif pagina in ["Exercícios e Cases I", "Exercícios e Cases II"]:
    sec = SECOES[pagina]
    st.markdown(f'<div class="section-title">{sec["titulo"]}</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.05, 0.95])

    with c1:
        st.markdown(
            f"""
            <div class="box">
                <h4>Objetivo</h4>
                <p>{sec["objetivo"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown('<div class="section-title">Cases sugeridos</div>', unsafe_allow_html=True)
        for item in sec["case"]:
            st.markdown(
                f"""
                <div class="light-box">
                    <p>{item}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    with c2:
        st.markdown('<div class="section-title">Questões para discussão</div>', unsafe_allow_html=True)
        for i, (pergunta, resposta) in enumerate(sec["questoes"], start=1):
            with st.expander(f"Questão {i}"):
                st.write(pergunta)
                st.success(resposta)
