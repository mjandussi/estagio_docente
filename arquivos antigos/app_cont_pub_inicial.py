
import streamlit as st

st.set_page_config(
    page_title="Contabilidade Pública | App Didático",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =============================
# ESTILO
# =============================
st.markdown("""
<style>
.block-container {
    padding-top: 1.1rem;
    padding-bottom: 2rem;
    max-width: 1220px;
}
html, body, [class*="css"] {
    font-family: Arial, sans-serif;
}
.hero {
    padding: 1.6rem 1.8rem;
    border-radius: 24px;
    border: 1px solid #d8dde6;
    background: linear-gradient(135deg, #f7f9fc 0%, #eef3f8 100%);
    margin-bottom: 1rem;
}
.hero h1 {
    margin: 0;
    font-size: 2.3rem;
}
.hero p {
    margin: 0.45rem 0 0 0;
    color: #4b5563;
    font-size: 1rem;
}
.card {
    border: 1px solid #e4e7ec;
    border-radius: 20px;
    padding: 1rem 1.1rem;
    background: #ffffff;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    height: 100%;
}
.soft-card {
    border: 1px solid #e5e7eb;
    border-radius: 16px;
    padding: 0.9rem 1rem;
    background: #fafafa;
    margin-bottom: 0.8rem;
}
.section-title {
    font-size: 1.35rem;
    font-weight: 700;
    margin-top: 1rem;
    margin-bottom: 0.75rem;
}
.flow {
    border-radius: 16px;
    background: #f8fafc;
    border: 1px dashed #cbd5e1;
    padding: 0.95rem 1rem;
    font-weight: 600;
    text-align: center;
}
.badge {
    display: inline-block;
    padding: 0.28rem 0.7rem;
    border-radius: 999px;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    font-size: 0.84rem;
    margin-right: 0.35rem;
    margin-bottom: 0.35rem;
}
.subtle {
    color: #6b7280;
}
div[data-testid="stButton"] > button {
    border-radius: 14px;
    height: 3rem;
    font-weight: 700;
}
div[data-testid="stExpander"] details {
    border-radius: 14px;
    border: 1px solid #e5e7eb;
}
table {
    font-size: 0.95rem !important;
}
</style>
""", unsafe_allow_html=True)

# =============================
# DADOS
# =============================
AULAS = {
    "Aula 1": {
        "titulo": "Aula 1 - Variações Patrimoniais",
        "objetivo": "Compreender o conceito de variações patrimoniais e distinguir VPA, VPD, variações quantitativas e qualitativas.",
        "topicos": [
            "Patrimônio público como objeto da contabilidade pública",
            "Variações Patrimoniais Aumentativas (VPA)",
            "Variações Patrimoniais Diminutivas (VPD)",
            "Variações quantitativas x qualitativas",
            "Reflexos no patrimônio líquido"
        ],
        "explicacao": [
            ("VPA", "Fatos que aumentam o patrimônio líquido, como a arrecadação de impostos."),
            ("VPD", "Fatos que reduzem o patrimônio líquido, como despesa com pessoal ou consumo de materiais."),
            ("Quantitativas", "Alteram o patrimônio líquido, positiva ou negativamente."),
            ("Qualitativas", "Não alteram o patrimônio líquido; apenas modificam a composição patrimonial.")
        ],
        "exemplos": [
            "Arrecadação de impostos -> VPA",
            "Pagamento de salários -> VPD",
            "Aquisição de equipamento -> variação qualitativa"
        ],
        "fala": "Reforce que a disciplina continua a lógica do orçamento, mas agora com foco na evidenciação patrimonial."
    },
    "Aula 2": {
        "titulo": "Aula 2 - Classificação dos Fatos Contábeis",
        "objetivo": "Classificar fatos contábeis conforme os critérios trabalhados na disciplina.",
        "topicos": [
            "Receita x despesa",
            "Orçamentária x extraorçamentária",
            "Corrente x capital",
            "Efetiva x mutação patrimonial",
            "Variação quantitativa x qualitativa"
        ],
        "explicacao": [
            ("Receita", "Ingresso que pode aumentar a disponibilidade e gerar efeitos patrimoniais."),
            ("Despesa", "Gasto voltado ao custeio, manutenção ou investimento."),
            ("Orçamentária", "Ligada à execução do orçamento aprovado."),
            ("Extraorçamentária", "Movimentação que não depende de autorização orçamentária."),
            ("Corrente x Capital", "Corrente relaciona-se ao custeio; capital, a investimentos e aplicações permanentes.")
        ],
        "exemplos": [
            "Impostos arrecadados",
            "Pagamento de pessoal ativo",
            "Aquisição de equipamentos"
        ],
        "fala": "Faça a turma responder primeiro e depois consolide a classificação correta no quadro."
    },
    "Aula 3": {
        "titulo": "Aula 3 - Registros dos Atos e Fatos de Natureza Orçamentária: Receita",
        "objetivo": "Apresentar a execução da receita pública e os seus estágios.",
        "topicos": [
            "Previsão",
            "Lançamento",
            "Arrecadação",
            "Recolhimento"
        ],
        "explicacao": [
            ("Previsão", "Estimativa da receita que se pretende arrecadar no exercício."),
            ("Lançamento", "Constituição do crédito, com identificação do devedor, valor e vencimento."),
            ("Arrecadação", "Recebimento da receita pelo agente arrecadador."),
            ("Recolhimento", "Transferência do numerário arrecadado para o Tesouro.")
        ],
        "exemplos": [
            "Exemplo com IPTU",
            "Exemplo com ISS",
            "Comparação entre arrecadação e recolhimento"
        ],
        "fala": "Use exemplos de receitas municipais para aproximar a teoria da realidade."
    },
    "Aula 4": {
        "titulo": "Aula 4 - Registros dos Atos e Fatos de Natureza Orçamentária: Despesa",
        "objetivo": "Explicar os estágios da despesa pública e a lógica orçamentária associada.",
        "topicos": [
            "Dotação",
            "Empenho",
            "Liquidação",
            "Pagamento"
        ],
        "explicacao": [
            ("Empenho", "Ato que cria para o Estado obrigação de pagamento."),
            ("Liquidação", "Verificação do direito adquirido pelo credor."),
            ("Pagamento", "Quitação da obrigação após a liquidação.")
        ],
        "exemplos": [
            "Contratação de manutenção",
            "Compra de material de consumo",
            "Diferença entre empenhar, liquidar e pagar"
        ],
        "fala": "Esse é um dos temas em que os alunos mais confundem conceitos; vá com calma nos exemplos."
    },
    "Aula 5": {
        "titulo": "Aula 5 - Registros dos Fatos de Natureza Patrimonial",
        "objetivo": "Apresentar o reconhecimento patrimonial e seus reflexos sobre ativo, passivo e patrimônio líquido.",
        "topicos": [
            "Reconhecimento patrimonial",
            "Ativo",
            "Passivo",
            "Patrimônio líquido",
            "Integração entre dimensão orçamentária e patrimonial"
        ],
        "explicacao": [
            ("Ativo", "Recurso controlado pela entidade do qual se espera potencial de serviços ou benefícios econômicos futuros."),
            ("Passivo", "Obrigação presente derivada de evento passado cuja liquidação exigirá saída de recursos."),
            ("Patrimônio líquido", "Valor residual dos ativos após a dedução dos passivos."),
            ("Integração", "A execução orçamentária produz efeitos patrimoniais que precisam ser reconhecidos.")
        ],
        "exemplos": [
            "Liquidação da despesa gerando obrigação com fornecedores",
            "Aquisição de bem permanente",
            "Consumo de material em estoque"
        ],
        "fala": "Mostre que a contabilidade patrimonial amplia a leitura da execução orçamentária."
    }
}

EXERCICIOS = [
    ("Classifique o fato: impostos arrecadados.", "Receita, orçamentária, corrente, efetiva e VPA."),
    ("Classifique o fato: pagamento de pessoal ativo.", "Despesa, orçamentária, corrente, efetiva e VPD."),
    ("Classifique o fato: aquisição de equipamentos.", "Despesa, orçamentária, de capital, mutação patrimonial e variação qualitativa."),
    ("Qual a sequência correta dos estágios da receita?", "Previsão, lançamento, arrecadação e recolhimento."),
    ("Qual a sequência correta dos estágios da despesa?", "Empenho, liquidação e pagamento."),
    ("A compra de material para estoque altera imediatamente o patrimônio líquido?", "Não necessariamente. Em geral, trata-se de variação qualitativa no momento da aquisição; o efeito quantitativo aparece no consumo."),
]

ROTEIROS = [
    {
        "titulo": "Arrecadação de impostos",
        "etapas": ["Receita orçamentária", "Gera VPA", "Aumenta disponibilidade financeira"],
        "observacao": "Exemplo clássico de receita corrente, efetiva e quantitativamente aumentativa."
    },
    {
        "titulo": "Pagamento de pessoal ativo",
        "etapas": ["Despesa orçamentária", "Despesa corrente", "Gera VPD"],
        "observacao": "Reduz o patrimônio líquido e representa gasto típico de custeio."
    },
    {
        "titulo": "Aquisição de equipamentos",
        "etapas": ["Despesa orçamentária de capital", "Mutação patrimonial", "Variação qualitativa"],
        "observacao": "Substitui um ativo financeiro por um ativo permanente, sem reduzir imediatamente o patrimônio líquido."
    },
    {
        "titulo": "Liquidação da despesa com fornecedor",
        "etapas": ["Reconhecimento da obrigação", "Registro patrimonial do passivo", "Integração entre orçamento e patrimônio"],
        "observacao": "Momento importante para mostrar a ponte entre enfoque orçamentário e patrimonial."
    }
]

MAPA = [
    "Variações Patrimoniais",
    "Classificação dos Fatos",
    "Receita Pública",
    "Despesa Pública",
    "Registros Patrimoniais",
    "Revisão para a P1"
]

# =============================
# HELPERS
# =============================
def render_card(title, content):
    st.markdown(f"""
    <div class="card">
        <h3>{title}</h3>
        {content}
    </div>
    """, unsafe_allow_html=True)

def render_soft(title, content):
    st.markdown(f"""
    <div class="soft-card">
        <h4>{title}</h4>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

# =============================
# HEADER
# =============================
st.markdown("""
<div class="hero">
    <h1>Contabilidade Pública</h1>
    <p>Versão visual ampliada para apresentação em sala, revisão da P1, roteiros contábeis e mapa mental da disciplina.</p>
</div>
""", unsafe_allow_html=True)

# =============================
# NAVEGAÇÃO
# =============================
nav_labels = ["Home", "Aulas", "Exercícios P1", "Roteiros Contábeis", "Mapa Mental"]
nav_cols = st.columns(len(nav_labels))

if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

for i, label in enumerate(nav_labels):
    with nav_cols[i]:
        if st.button(label, use_container_width=True):
            st.session_state.pagina = label

pagina = st.session_state.pagina

# =============================
# HOME
# =============================
if pagina == "Home":
    c1, c2 = st.columns([1.1, 0.9])

    with c1:
        render_card(
            "Estrutura até a P1",
            """
            <div class="badge">Aula 1 • Variações Patrimoniais</div>
            <div class="badge">Aula 2 • Classificação dos Fatos</div>
            <div class="badge">Aula 3 • Receita Pública</div>
            <div class="badge">Aula 4 • Despesa Pública</div>
            <div class="badge">Aula 5 • Registros Patrimoniais</div>
            <div class="badge">Revisão • Preparação para a P1</div>
            <hr>
            <p class="subtle">A estrutura segue o material do professor e acrescenta apenas apoio visual e organização didática.</p>
            """
        )

    with c2:
        render_card(
            "Como usar em aula",
            """
            <p>• Use a aba <b>Aulas</b> durante a exposição.</p>
            <p>• Use a aba <b>Exercícios P1</b> para revisão.</p>
            <p>• Use a aba <b>Roteiros Contábeis</b> como reforço didático.</p>
            <p>• Use a aba <b>Mapa Mental</b> para fechar a lógica da disciplina.</p>
            """
        )

    st.markdown('<div class="section-title">Cronograma resumido</div>', unsafe_allow_html=True)
    st.table({
        "Encontro": ["1", "2", "3", "4", "5", "6"],
        "Tema": [
            "Variações Patrimoniais",
            "Classificação dos Fatos Contábeis",
            "Registros da Receita",
            "Registros da Despesa",
            "Registros dos Fatos de Natureza Patrimonial",
            "Revisão para a P1"
        ]
    })

    st.markdown('<div class="section-title">Lógica da disciplina</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow">Orçamento Público -> Registro Contábil -> Efeito Patrimonial -> Revisão para a Prova</div>', unsafe_allow_html=True)

# =============================
# AULAS
# =============================
elif pagina == "Aulas":
    aula_selecionada = st.selectbox("Selecione a aula", list(AULAS.keys()))
    aula = AULAS[aula_selecionada]

    st.markdown(f'<div class="section-title">{aula["titulo"]}</div>', unsafe_allow_html=True)

    ca, cb = st.columns([1.05, 0.95])

    with ca:
        render_card("Objetivo", f"<p>{aula['objetivo']}</p>")
        topicos_html = "".join([f"<p>• {t}</p>" for t in aula["topicos"]])
        render_card("Tópicos principais", topicos_html)

    with cb:
        render_card("Observação para sua fala", f"<p>{aula['fala']}</p>")

    st.markdown('<div class="section-title">Explicações centrais</div>', unsafe_allow_html=True)
    ecols = st.columns(2)
    for i, (titulo, texto) in enumerate(aula["explicacao"]):
        with ecols[i % 2]:
            render_soft(titulo, texto)

    st.markdown('<div class="section-title">Exemplos para usar em sala</div>', unsafe_allow_html=True)
    ex_cols = st.columns(3 if len(aula["exemplos"]) >= 3 else len(aula["exemplos"]))
    for i, ex in enumerate(aula["exemplos"]):
        with ex_cols[i % len(ex_cols)]:
            render_soft("Exemplo", ex)

    if aula_selecionada == "Aula 1":
        st.markdown('<div class="section-title">Quadro-resumo</div>', unsafe_allow_html=True)
        st.markdown('<div class="flow">VPA -> aumenta o patrimônio líquido | VPD -> reduz o patrimônio líquido | Qualitativa -> muda a composição do patrimônio</div>', unsafe_allow_html=True)

    if aula_selecionada == "Aula 2":
        st.markdown('<div class="section-title">Critérios de classificação</div>', unsafe_allow_html=True)
        st.markdown('<div class="flow">Receita/Despesa -> Orçamentária/Extraorçamentária -> Corrente/Capital -> Efetiva/Mutação -> Quantitativa/Qualitativa</div>', unsafe_allow_html=True)

    if aula_selecionada == "Aula 3":
        st.markdown('<div class="section-title">Fluxo da receita</div>', unsafe_allow_html=True)
        st.markdown('<div class="flow">Previsão -> Lançamento -> Arrecadação -> Recolhimento</div>', unsafe_allow_html=True)

    if aula_selecionada == "Aula 4":
        st.markdown('<div class="section-title">Fluxo da despesa</div>', unsafe_allow_html=True)
        st.markdown('<div class="flow">Dotação -> Empenho -> Liquidação -> Pagamento</div>', unsafe_allow_html=True)

    if aula_selecionada == "Aula 5":
        st.markdown('<div class="section-title">Integração dos enfoques</div>', unsafe_allow_html=True)
        st.markdown('<div class="flow">Execução orçamentária -> Reconhecimento patrimonial -> Evidenciação contábil</div>', unsafe_allow_html=True)

# =============================
# EXERCÍCIOS
# =============================
elif pagina == "Exercícios P1":
    st.markdown('<div class="section-title">Exercícios para revisão da P1</div>', unsafe_allow_html=True)
    st.info("Você pode usar esta tela ao vivo em sala, pedindo que os alunos respondam antes de abrir a resposta.")

    for i, (pergunta, resposta) in enumerate(EXERCICIOS, start=1):
        with st.expander(f"Questão {i}"):
            st.write(pergunta)
            st.success(resposta)

    st.markdown('<div class="section-title">Pontos de atenção para a prova</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        render_soft("Confusão comum 1", "Diferenciar bem arrecadação e recolhimento.")
        render_soft("Confusão comum 2", "Não confundir empenho com pagamento.")
    with c2:
        render_soft("Confusão comum 3", "Compra de equipamento não é, em regra, despesa efetiva.")
        render_soft("Confusão comum 4", "Consumo de estoque é que tende a produzir VPD.")

# =============================
# ROTEIROS CONTÁBEIS
# =============================
elif pagina == "Roteiros Contábeis":
    st.markdown('<div class="section-title">Roteiros contábeis didáticos</div>', unsafe_allow_html=True)
    st.info("Estes roteiros são um reforço didático para explicar a lógica dos principais fatos, sem substituir o material-base do professor.")

    for item in ROTEIROS:
        with st.expander(item["titulo"]):
            for etapa in item["etapas"]:
                st.write(f"• {etapa}")
            st.caption(item["observacao"])

    st.markdown('<div class="section-title">Resumo visual</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow">Fato administrativo -> Classificação -> Registro orçamentário -> Reflexo patrimonial -> Evidenciação contábil</div>', unsafe_allow_html=True)

# =============================
# MAPA MENTAL
# =============================
elif pagina == "Mapa Mental":
    st.markdown('<div class="section-title">Mapa mental da disciplina até a P1</div>', unsafe_allow_html=True)

    st.markdown('<div class="flow">Contabilidade Pública</div>', unsafe_allow_html=True)
    st.markdown('<div class="flow">↓</div>', unsafe_allow_html=True)

    cols = st.columns(len(MAPA))
    for i, item in enumerate(MAPA):
        with cols[i]:
            st.markdown(f'<div class="soft-card"><p style="text-align:center; font-weight:700;">{item}</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Síntese final</div>', unsafe_allow_html=True)
    render_card(
        "Em uma frase",
        "<p>A disciplina até a P1 mostra como os fatos da execução pública são classificados, registrados e interpretados à luz do orçamento e do patrimônio.</p>"
    )
