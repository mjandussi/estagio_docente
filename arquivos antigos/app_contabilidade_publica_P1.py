
import streamlit as st

st.set_page_config(
    page_title="Contabilidade Pública - Aulas até a P1",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
    }
    .box h4 {
        margin-top: 0;
        margin-bottom: 0.5rem;
    }
    .section-title {
        font-size: 1.45rem;
        font-weight: 700;
        margin-top: 0.8rem;
        margin-bottom: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

AULAS = {
    "Home": {
        "titulo": "Contabilidade Pública",
        "subtitulo": "Material de apoio para as aulas até a P1."
    },
    "Aula 1": {
        "titulo": "Aula 1 - Variações Patrimoniais",
        "objetivo": "Compreender o conceito de variações patrimoniais e diferenciar VPA, VPD, variações quantitativas e qualitativas.",
        "topicos": [
            "Patrimônio público como objeto da contabilidade pública",
            "Variações Patrimoniais Aumentativas (VPA)",
            "Variações Patrimoniais Diminutivas (VPD)",
            "Variações quantitativas x qualitativas",
            "Impacto das variações no patrimônio líquido"
        ],
        "explicacao": [
            ("VPA", "Representam fatos que aumentam o patrimônio líquido, como a arrecadação de impostos."),
            ("VPD", "Representam fatos que reduzem o patrimônio líquido, como despesas com pessoal e consumo de materiais."),
            ("Quantitativas", "Alteram o patrimônio líquido, para mais ou para menos."),
            ("Qualitativas", "Não alteram o patrimônio líquido; apenas mudam a composição dos elementos patrimoniais.")
        ],
        "exemplos": [
            "Arrecadação de impostos -> VPA",
            "Pagamento de salários -> VPD",
            "Aquisição de equipamento -> variação qualitativa"
        ],
        "fala": "Retome que a disciplina dá continuidade à lógica do orçamento público, agora sob a ótica contábil."
    },
    "Aula 2": {
        "titulo": "Aula 2 - Classificação dos Fatos Contábeis",
        "objetivo": "Classificar fatos contábeis segundo os critérios trabalhados pelo professor.",
        "topicos": [
            "Receita x Despesa",
            "Orçamentária x Extraorçamentária",
            "Corrente x Capital",
            "Efetiva x Mutação",
            "Variação quantitativa x qualitativa"
        ],
        "explicacao": [
            ("Receita", "Ingressos que aumentam a disponibilidade e, em regra, podem afetar o patrimônio."),
            ("Despesa", "Gastos realizados para manutenção dos serviços públicos ou investimentos."),
            ("Orçamentária", "Prevista ou autorizada na peça orçamentária."),
            ("Extraorçamentária", "Não depende de autorização orçamentária, como cauções e consignações."),
            ("Corrente", "Relacionada ao custeio e manutenção das atividades do Estado."),
            ("Capital", "Relacionada a investimentos, inversões financeiras e amortização da dívida.")
        ],
        "exemplos": [
            "Impostos arrecadados",
            "Pagamento de pessoal ativo",
            "Aquisição de equipamentos"
        ],
        "fala": "Use esta aula como transição entre conceitos e prática, pedindo a participação da turma."
    },
    "Aula 3": {
        "titulo": "Aula 3 - Registros dos Atos e Fatos de Natureza Orçamentária: Receita",
        "objetivo": "Apresentar a execução da receita pública e seus estágios.",
        "topicos": [
            "Previsão",
            "Lançamento",
            "Arrecadação",
            "Recolhimento"
        ],
        "explicacao": [
            ("Previsão", "Estimativa da receita que se pretende arrecadar no exercício."),
            ("Lançamento", "Constituição do crédito, identificando contribuinte, valor e vencimento."),
            ("Arrecadação", "Recebimento da receita pelo agente arrecadador."),
            ("Recolhimento", "Transferência dos valores arrecadados para a conta do Tesouro.")
        ],
        "exemplos": [
            "Exemplo com IPTU ou ISS",
            "Diferenciar arrecadação de recolhimento"
        ],
        "fala": "Explique com exemplos simples de tributos municipais."
    },
    "Aula 4": {
        "titulo": "Aula 4 - Registros dos Atos e Fatos de Natureza Orçamentária: Despesa",
        "objetivo": "Explicar os estágios da despesa pública e a lógica orçamentária envolvida.",
        "topicos": [
            "Dotação",
            "Empenho",
            "Liquidação",
            "Pagamento"
        ],
        "explicacao": [
            ("Empenho", "Ato que cria para o Estado obrigação de pagamento, pendente ou não de implemento de condição."),
            ("Liquidação", "Verificação do direito adquirido pelo credor, com base nos títulos e documentos comprobatórios."),
            ("Pagamento", "Quitação da obrigação após a regular liquidação.")
        ],
        "exemplos": [
            "Contratação de serviço de manutenção",
            "Compra de material de consumo",
            "Diferença entre empenhar, liquidar e pagar"
        ],
        "fala": "Insista na diferença entre empenho, liquidação e pagamento."
    },
    "Aula 5": {
        "titulo": "Aula 5 - Registros dos Fatos de Natureza Patrimonial",
        "objetivo": "Apresentar o reconhecimento patrimonial e seus efeitos sobre ativos, passivos e patrimônio líquido.",
        "topicos": [
            "Reconhecimento patrimonial",
            "Ativo",
            "Passivo",
            "Patrimônio líquido",
            "Integração entre dimensão orçamentária e patrimonial"
        ],
        "explicacao": [
            ("Ativo", "Recurso controlado pela entidade como resultado de evento passado e do qual se espera potencial de serviços ou benefícios econômicos futuros."),
            ("Passivo", "Obrigação presente derivada de evento passado cuja liquidação se espera resultar em saída de recursos."),
            ("Patrimônio Líquido", "Valor residual dos ativos após a dedução de todos os passivos.")
        ],
        "exemplos": [
            "Liquidação da despesa gerando obrigação com fornecedores",
            "Aquisição de bem permanente",
            "Consumo de estoque"
        ],
        "fala": "Mostre que o enfoque patrimonial amplia a compreensão da execução pública."
    },
    "Revisão P1": {
        "titulo": "Aula 6 - Revisão para a P1",
        "objetivo": "Consolidar os conteúdos cobrados na primeira prova.",
        "topicos": [
            "Variações patrimoniais",
            "Classificação dos fatos",
            "Execução da receita",
            "Execução da despesa",
            "Reconhecimento patrimonial"
        ],
        "explicacao": [
            ("Estratégia", "Resolver questões curtas e revisar conceitos-chave."),
            ("Foco", "Diferenciar bem VPA/VPD, despesa corrente/capital e empenho/liquidação/pagamento.")
        ],
        "exemplos": [
            "Impostos arrecadados",
            "Pessoal ativo",
            "Aquisição de equipamentos",
            "Consumo de material de estoque"
        ],
        "fala": "Faça uma revisão objetiva, com exercícios orais e comentários curtos."
    }
}

EXERCICIOS = [
    {
        "enunciado": "Classifique o fato: impostos arrecadados.",
        "resposta": "Receita, orçamentária, corrente, efetiva e VPA."
    },
    {
        "enunciado": "Classifique o fato: pagamento de pessoal ativo.",
        "resposta": "Despesa, orçamentária, corrente, efetiva e VPD."
    },
    {
        "enunciado": "Classifique o fato: aquisição de equipamentos.",
        "resposta": "Despesa, orçamentária, de capital, mutação patrimonial e variação qualitativa."
    },
    {
        "enunciado": "Qual a sequência correta dos estágios da receita?",
        "resposta": "Previsão, lançamento, arrecadação e recolhimento."
    },
    {
        "enunciado": "Qual a sequência correta dos estágios da despesa?",
        "resposta": "Empenho, liquidação e pagamento."
    }
]

st.markdown('<div class="title-main">Contabilidade Pública</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-main">App de apoio para apresentação das aulas até a P1, seguindo o material do professor e acrescentando apenas recursos didáticos.</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
with col1:
    home = st.button("Home", use_container_width=True)
with col2:
    a1 = st.button("Aula 1", use_container_width=True)
with col3:
    a2 = st.button("Aula 2", use_container_width=True)
with col4:
    a3 = st.button("Aula 3", use_container_width=True)
with col5:
    a4 = st.button("Aula 4", use_container_width=True)
with col6:
    a5 = st.button("Aula 5", use_container_width=True)
with col7:
    rev = st.button("Revisão P1", use_container_width=True)

if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

if home:
    st.session_state.pagina = "Home"
if a1:
    st.session_state.pagina = "Aula 1"
if a2:
    st.session_state.pagina = "Aula 2"
if a3:
    st.session_state.pagina = "Aula 3"
if a4:
    st.session_state.pagina = "Aula 4"
if a5:
    st.session_state.pagina = "Aula 5"
if rev:
    st.session_state.pagina = "Revisão P1"

pagina = st.session_state.pagina

if pagina == "Home":
    st.markdown('<div class="section-title">Visão geral</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, 1])
    with c1:
        st.markdown(
            """
            <div class="box">
                <h4>Estrutura até a P1</h4>
                <p>1. Variações Patrimoniais</p>
                <p>2. Classificação dos Fatos Contábeis</p>
                <p>3. Registros dos Atos e Fatos de Natureza Orçamentária - Receita</p>
                <p>4. Registros dos Atos e Fatos de Natureza Orçamentária - Despesa</p>
                <p>5. Registros dos Fatos de Natureza Patrimonial</p>
                <p>6. Revisão para a P1</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            """
            <div class="box">
                <h4>Estratégia didática</h4>
                <p>• Seguir o material do professor como conteúdo-base</p>
                <p>• Acrescentar explicações visuais e exemplos simples</p>
                <p>• Resolver exercícios em sala</p>
                <p>• Fazer revisão focada na prova</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Cronograma sugerido</div>', unsafe_allow_html=True)
    st.table({
        "Aula": ["Aula 1", "Aula 2", "Aula 3", "Aula 4", "Aula 5", "Aula 6"],
        "Tema": [
            "Variações Patrimoniais",
            "Classificação dos Fatos Contábeis",
            "Execução da Receita Pública",
            "Execução da Despesa Pública",
            "Registros dos Fatos de Natureza Patrimonial",
            "Revisão para a P1"
        ]
    })

    st.info("Use este app como roteiro de exposição e revisão.")
else:
    aula = AULAS[pagina]
    st.markdown(f'<div class="section-title">{aula["titulo"]}</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1.1, 0.9])

    with c1:
        st.markdown(
            f"""
            <div class="box">
                <h4>Objetivo da aula</h4>
                <p>{aula["objetivo"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="box"><h4>Tópicos principais</h4>' +
            "".join([f"<p>• {t}</p>" for t in aula["topicos"]]) +
            "</div>",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            '<div class="box"><h4>Observações para sua fala</h4>' +
            f"<p>{aula['fala']}</p></div>",
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Explicações centrais</div>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (titulo, texto) in enumerate(aula["explicacao"]):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="box">
                    <h4>{titulo}</h4>
                    <p>{texto}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown('<div class="section-title">Exemplos para usar em sala</div>', unsafe_allow_html=True)
    for ex in aula["exemplos"]:
        st.markdown(
            f"""
            <div class="box">
                <p>{ex}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    if pagina in ["Aula 2", "Revisão P1"]:
        st.markdown('<div class="section-title">Exercícios de revisão</div>', unsafe_allow_html=True)
        for i, ex in enumerate(EXERCICIOS, start=1):
            with st.expander(f"Questão {i}"):
                st.write(ex["enunciado"])
                st.success(ex["resposta"])

    if pagina == "Aula 3":
        st.markdown('<div class="section-title">Fluxo da receita</div>', unsafe_allow_html=True)
        st.code("Previsão -> Lançamento -> Arrecadação -> Recolhimento", language=None)

    if pagina == "Aula 4":
        st.markdown('<div class="section-title">Fluxo da despesa</div>', unsafe_allow_html=True)
        st.code("Empenho -> Liquidação -> Pagamento", language=None)

    if pagina == "Aula 5":
        st.markdown('<div class="section-title">Integração entre enfoques</div>', unsafe_allow_html=True)
        st.code("Execução orçamentária -> Reconhecimento patrimonial -> Evidenciação contábil", language=None)
