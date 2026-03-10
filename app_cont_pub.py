
import streamlit as st
import pandas as pd

############################################################################################

# Usuário e senha
USUARIO = "ladeira"
SENHA = "ladeira"

def login():
    st.title("Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == USUARIO and senha == SENHA:
            st.session_state["logado"] = True
        else:
            st.error("Usuário ou senha incorretos")

# Verificação de login
if "logado" not in st.session_state:
    st.session_state["logado"] = False

if not st.session_state["logado"]:
    login()
    st.stop()

############################################################################################

st.set_page_config(
    page_title="Contabilidade Pública",
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
        background-color: #484549FF;
        color: green;
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
        background-color: #410657FF;
    }
    .flow-box {
        border: 1px dashed #9db3e0;
        border-radius: 12px;
        padding: 14px 16px;
        margin-bottom: 12px;
        background-color: #410657FF;
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
        "subtitulo": "App de apoio para a disciplina de Contabilidade Pública."
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
        "carga": "Carga horária total (60 horas/aula) organizada ao longo do semestre, em dois blocos: fundamentos/registros e demonstrações contábeis.",
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
        "curriculum": "Professor responsável pela disciplina: Waldir Jorge Ladeira dos Santos é Doutor em Políticas Públicas e Comportamento Humano pelo PPFH/UERJ, Mestre em Contabilidade Financeira pela FAF/UERJ, Pós-graduado em Auditoria Interna, em Administração de Recursos Humanos e em Docência Superior, Contador e Administrador de Empresas."
                        "Sua experiência profissional inclui os cargos de Oficial do Exército Brasileiro na 1ª. Inspetoria de Contabilidade e Finanças do Exército, Professor Universitário, Secretário Municipal de Fazenda, de Controle Interno e Executivo, Presidente de Fundação Municipal de Saúde, Coordenador em diversas IES e Co-autor dos livros Contabilidade dos Investimentos em Participações Societárias e Contabilização de Ativos Financeiros em Participações Societárias (ed. FGV); Tópicos Contemporâneos de Gestão Pública: Finanças em Foco (ed. Freitas Bastos); Planejamento, Controle e Informação (ed. Interciência), Contabilidade Geral I e II (ed. CEDERJ); Membro de Bancas de Concursos Públicos, Membro do Conselho Editorial da Revista Científica Pensar Contábil do CRCRJ e da Revista Educação e Pesquisa em Contabilidade do CFC, Conselheiro (2002/21) e Presidente do CRC/RJ (2018/19), detentor das Medalhas: Alumni, da UNESA; Tiradentes, da Assembleia Legislativa do Estado do Rio de Janeiro; Pedro Ernesto, da Câmara Municipal do Rio de Janeiro; Mérito Contábil, da Câmara Municipal de Duque de Caxias-RJ; e Mérito Contábil Estadual Orlando Martins Pinto, do CRCRJ."
                        "Atualmente é sócio da WL Capital Intelectual, Capacitação e Treinamento, Consultor, Professor Titular, Vice Diretor e Coordenador Geral do Programa de Mestrado Profissional em Controladoria e Gestão Pública da Faculdade de Administração e Finanças - FAF/UERJ, onde leciona nos Mestrados Profissional e Acadêmico e nas Graduações de Administração e Ciências Contábeis, Professor Associado da UFRJ e Professor Convidado de Pós Graduação MBA da Fundação Getúlio Vargas – FGV, desde 1999, Acadêmico da Academia de Ciências Contábeis do Estado do Rio de Janeiro – ACCERJ e da Academia Nacional de Economia e Políticas Sociais – ANE."

    },
    "Contabilidade Aplicada ao Setor Público": {
        "titulo": "2. Contabilidade Aplicada ao Setor Público",
        "objetivo": "Apresentar o conceito, objeto, objetivo, campo de aplicação e finalidade da contabilidade pública.",
        "topicos": [
            "Objeto da contabilidade pública: patrimônio público",
            "Funções de registro, controle e evidenciação",
            "Integração entre orçamento, finanças e patrimônio",
            "Base normativa da contabilidade aplicada ao setor público"
        ],
        "explicacao": [
            ("Conceito", "A contabilidade aplicada no setor público é um ramo das Ciências Contábeis e apresenta como base de sua aplicação a Lei 4.320, de 17 de março de 1.964, que trata de Normas Gerais de Direito Financeiro para Elaboração e Controle dos Orçamentos e Balanços da União, Estados, Municípios e Distrito Federal."),
            ("Objetivo", "Fornecer informações contábeis atualizadas, confiáveis e relevantes à administração pública, de modo a subsidiar o processo de tomada de decisões, bem como apoiar os órgãos de controle interno e externo no cumprimento da legislação. Além disso, disponibilizar dados de interesse para instituições governamentais e para a sociedade, incluindo informações estatísticas e outras necessárias à análise e ao acompanhamento da gestão pública."),
            ("Objeto", "A contabilidade aplicada ao setor público tem por objeto o patrimônio público."),
            ("Finalidade", "Registrar, controlar e evidenciar os atos e fatos da gestão pública."),
            ("Abrangência", "Acompanha orçamento, execução financeira, patrimônio e suas variações."),
            ("Campo de aplicação", "É aplica aos quatro níveis de governo: Federal, Estadual, Municipal, Distrito Federal, aos três Poderes constituídos, bem como as suas autarquias e fundações."),
            ("Normas", "A disciplina se apoia na Lei 4.320/64, nas NBC T SP / NBC TSP e no MCASP.")
        ],
        "fala": "Nesta seção, continuamos a mostar a lógica do orçamento, mas avançando para a evidenciação patrimonial."
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
                <p>4. Registro das operações típicas conforme as NBC TSP e MCASP</p>
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
                <h4>Didática</h4>
                <p>• Seguir o material didático como eixo principal</p>
                <p>• Usar o app como roteiro de exposição</p>
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
        st.markdown('<div class="box"><h4>1.4 Conteúdo programático</h4>' + "".join([f"<p>• {x}</p>" for x in sec["conteudo"]]) + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="box"><h4>1.5 Metodologia</h4>' + "".join([f"<p>• {x}</p>" for x in sec["metodologia"]]) + '</div>', unsafe_allow_html=True)
    with c2:
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
    st.divider()
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
        
    with c2:
        st.markdown(
            '<div class="box"><h4>Tópicos principais</h4>' +
            "".join([f"<p>• {x}</p>" for x in sec["topicos"]]) +
            '</div>',
            unsafe_allow_html=True
        )

        # st.markdown(
        #     f"""
        #     <div class="box">
        #         <h4>Observação</h4>
        #         <p>{sec["fala"]}</p>
        #     </div>
        #     """,
        #     unsafe_allow_html=True
        # )
    st.divider()
    st.markdown('<div class="section-title"></div>', unsafe_allow_html=True)
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

##################################################################################################################
# Seção específica para Contabilidade Aplicada ao Setor Público
    if pagina == "Contabilidade Aplicada ao Setor Público":
        st.divider()
        st.markdown('<div class="section-title">Normas Brasileiras de Contabilidade Aplicadas ao Setor Público </div>', unsafe_allow_html=True)

        img_col1, img_col2 = st.columns(2)

        with img_col1:
            st.image(
                "imagens/cfc_normas_nbc_tsp.png",  # imagem da página das normas do CFC
                caption="CFC - Normas NBC TSP",
                use_container_width=True
            )
            st.markdown(
                """
                <div class="light-box">
                    <h4>Link de acesso</h4>
                    <p><a href="https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-tsp-do-setor-publico/" target="_blank">
                    Acessar página das normas NBC TSP no CFC
                    </a></p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with img_col2:
            st.image(
                "imagens/cfc_estrutura_conceitual.png",  # imagem da resolução / ementa
                caption="CFC - Estrutura Conceitual",
                use_container_width=True
            )

        st.divider()

        # Seção: Diferenças entre Contabilidade Societária e Contabilidade Pública
        st.markdown(
            '<div class="section-title">Principais diferenças entre a Contabilidade Societária e a Contabilidade Pública</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            """
        Existem diferenças estruturais entre as técnicas de contabilidade utilizadas na contabilidade societária e na contabilidade aplicada ao setor público.  
        O quadro a seguir apresenta algumas dessas diferenças fundamentais.
        """
        )

        dados = {
            "Tópico Analisado": [
                "Legislação básica",
                "Regime Contábil",
                "Resultado",
                "Controle Interno",
                "Demonstrações",
                "Prestação de contas",
                "Orçamento",
                "Sistemas de contas",
                "Registros",
                "Contas de resultado",
                "Legalidade",
                "Agentes responsáveis",
                "Princípios"
            ],

            "Contabilidade Societária": [
                "Lei 6.404/76, 11.638/07 e 11.941/09",
                "Competência",
                "Lucro ou prejuízo do exercício",
                "Auditoria interna vinculada à administração",
                "Balanço Patrimonial, DRE, DFC, DMPL, DVA",
                "Conselho de administração e acionistas",
                "Orçamento operacional ou financeiro",
                "Sistema único de contas",
                "Registro principalmente de fatos",
                "Receitas e despesas",
                "Permitido fazer o que a lei não proíbe",
                "Diretores, gerentes e administradores",
                "Princípios de Contabilidade"
            ],

            "Contabilidade Pública": [
                "Lei 4.320/64, Lei 8.666/93, LC 101/00 e NBC TSP",
                "Orçamentário = misto / Patrimonial = competência",
                "Superávit ou déficit da gestão",
                "Controle para cumprimento da legislação e responsabilização de agentes públicos",
                "Balanço Orçamentário, Patrimonial, Financeiro, DVP, DFC e Notas Explicativas",
                "Poder Legislativo (Tribunais de Contas) e sociedade",
                "PPA, LDO e LOA",
                "Sistemas: orçamentário, patrimonial, compensação e custos",
                "Registro de atos e fatos",
                "Ingressos e dispêndios",
                "Permitido fazer apenas o que a lei autoriza",
                "Ordenador de despesas e responsáveis por bens e valores",
                "Princípios Contábeis e Princípios Orçamentários"
            ]
        }

        df = pd.DataFrame(dados)

        st.table(df)


##################################################################################################################
    if pagina == "Plano de Contas e Subsistemas":
        ##################################################################################################################
        # Seção: Plano de Contas e Subsistemas
        st.divider()
        # st.markdown(
        # '<div class="section-title">Plano de Contas e Subsistemas</div>',
        # unsafe_allow_html=True
        # )

        st.markdown(
        """
        Para que a contabilidade forneça informações úteis aos seus usuários, é necessário registrar adequadamente os **atos e fatos administrativos**.  
        Esses registros são realizados por meio das **contas contábeis**, que representam conjuntos de transações de natureza semelhante.

        As contas funcionam como o principal instrumento de **memória das informações quantitativas da entidade**.
        """
        )

        st.markdown(
        """
        <div class="light-box">
        <h4>Exemplo</h4>
        <p>
        Receber dinheiro e pagar uma dívida são operações diferentes, mas ambas envolvem recursos financeiros.  
        Essas transações são registradas em contas representativas dessa natureza, como <b>Caixa</b> ou <b>Tesouraria</b>.
        </p>
        </div>
        """,
        unsafe_allow_html=True
        )

        st.divider()

        # Plano de contas

        st.markdown(
        '<div class="section-title">Plano de Contas</div>',
        unsafe_allow_html=True
        )

        st.markdown(
        """
        O **Plano de Contas** é uma relação lógica e ordenada de todas as contas que podem ser utilizadas por uma entidade.

        Ele possui três elementos fundamentais:

        • **Elenco**: relação de todas as contas utilizadas pela instituição, com seus respectivos códigos e título.

        • **Função**: indica a finalidade de cada conta dentro do sistema contábil (descrição da conta).

        • **Funcionamento**: demonstra como cada conta é movimentada a débito e a crédito.
        """
        )


        st.divider()

        # Estrutura do PCASP

        st.markdown(
        '<div class="section-title">Estrutura do PCASP</div>',
        unsafe_allow_html=True
        )

        st.markdown(
        """
        Na contabilidade pública brasileira utiliza-se o **Plano de Contas Aplicado ao Setor Público (PCASP)**, organizado em classes numeradas de **1 a 8**.
        """
        )


        dados_pcasp = {
        "Classe": [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8"
        ],

        "Descrição": [
        "Ativo",
        "Passivo e Patrimônio Líquido",
        "Variações Patrimoniais Diminutivas",
        "Variações Patrimoniais Aumentativas",
        "Controles da Aprovação do Planejamento e Orçamento",
        "Controles da Execução do Planejamento e Orçamento",
        "Controles Devedores",
        "Controles Credores"
        ]
        }

        c1, c2 = st.columns([1.1, 0.9])

        with c1:
            df_pcasp = pd.DataFrame(dados_pcasp)
            st.dataframe(df_pcasp, hide_index=True, use_container_width=True)
        with c2:
            st.markdown(
            """
            <div class="light-box">
            As contas são estruturadas em <b>níveis de desdobramento</b>, partindo do nível mais sintético para o mais analítico, de forma a atender diferentes necessidades de informação.
            </div>
            """,
            unsafe_allow_html=True
            )

            st.markdown(
            """
            <div class="light-box">
            <b>NATUREZA DAS CONTAS:<br><br>
            </b> No PCASP, a natureza das contas pode ser identificada pela numeração da classe:<br><br>
            • Contas iniciadas por número **ímpar** → natureza **devedora**<br><br>  
            • Contas iniciadas por número **par** → natureza **credora**
            </div>
            """,
            unsafe_allow_html=True
            )

        st.divider()

        # Classificação das contas

        st.markdown(
        '<div class="section-title">Classificação das Contas</div>',
        unsafe_allow_html=True
        )

        dados_class = {
        "Critério": [
        "Natureza do saldo",
        "Utilização",
        "Movimentação",
        "Extensão"
        ],

        "Classificações": [
        "Estáveis ou instáveis",
        "Estáticas ou dinâmicas",
        "Unilaterais ou bilaterais",
        "Sintéticas ou analíticas"
        ]
        }

        c1, c2 = st.columns([1.1, 0.9])

        with c1:
            df_class = pd.DataFrame(dados_class)
            st.dataframe(df_class, hide_index=True, use_container_width=True)
            
        with c2:
            st.markdown(
            """
            <div class="light-box">
            <b>Contas sintéticas</b> representam contas de nível mais agregado.  
            <b>Contas analíticas</b> representam o detalhamento das contas sintéticas, podendo chegar ao nível de <b>conta corrente</b>.
            </div>
            """,
            unsafe_allow_html=True
            )

        st.divider()

        # Subsistemas de contas

        st.markdown(
        '<div class="section-title">Subsistemas de Contas</div>',
        unsafe_allow_html=True
        )

        st.markdown(
        """
        A **Lei 4.320/64** e as **NBC TSP** determinam que os registros contábeis no setor público sejam organizados em **subsistemas independentes, porém integrados**.
        """
        )

        dados_subsistemas = {
        "Subsistema": [
        "Orçamentário",
        "Patrimonial",
        "Compensação"
        ],

        "Descrição": [
        "Registra os atos de natureza orçamentária relacionados à previsão da receita e à fixação e execução da despesa.",
        "Registra ingressos e dispêndios de recursos, bem como ativos, passivos e variações patrimoniais.",
        "Controla atos administrativos que não alteram imediatamente o patrimônio, mas podem afetá-lo no futuro."
        ]
        }

        c1, c2 = st.columns([1.6, 0.4])

        with c1:
            df_sub = pd.DataFrame(dados_subsistemas)
            st.dataframe(df_sub, hide_index=True, use_container_width=True)
            
        with c2:
            st.markdown(
            """
            <div class="light-box">
            Exemplos de registros no sistema de compensação incluem:
            <ul>
                <li>contratos / convênios</li>
                <li>garantias / cauções / fianças</li>
                <li>disponib. financ. por fonte</li>
                <li>demais controles</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
            )


##################################################################################################################

    if pagina == "Registro das Operações Típicas":
        st.markdown('<div class="section-title">Fluxos essenciais</div>', unsafe_allow_html=True)
        st.code("Receita: Previsão -> Lançamento -> Arrecadação -> Recolhimento", language=None)
        st.code("Despesa: Dotação -> Empenho -> Liquidação -> Pagamento", language=None)

        st.divider()
        st.markdown(
        """
        ### Registros das operações típicas conforme a NBC TSP – Estrutura Conceitual

        A contabilidade aplicada ao setor público tem como objetivo fornecer informações úteis para a prestação de contas (accountability) e para a tomada de decisões dos usuários das informações contábeis.

        Nesse contexto, os registros contábeis devem representar adequadamente os fenômenos econômicos que afetam o patrimônio das entidades públicas.
        """
        )

        st.markdown(
        """
        De acordo com a **NBC TSP – Estrutura Conceitual**, as informações contábeis devem refletir fielmente os eventos econômicos ocorridos, sendo elaboradas com base no **regime de competência**.

        Assim, os efeitos das transações devem ser reconhecidos **no período em que ocorrem**, independentemente do recebimento ou pagamento de caixa.
        """
        )

        st.markdown(
        """
        No setor público, muitas operações ocorrem por meio de **transações sem contraprestação**, como:

        • arrecadação de tributos  
        • transferências governamentais  
        • contribuições obrigatórias  

        Nessas situações, a entidade recebe ou entrega recursos **sem troca direta de valor equivalente**, característica típica da atuação governamental.
        """
        )

        st.markdown('<div class="section-title">Reconhecimento dos Elementos Contábeis</div>', unsafe_allow_html=True)

        st.markdown(
        """
        A Estrutura Conceitual define os principais elementos das demonstrações contábeis:
        """
        )

        st.markdown(
        """
        <div class="light-box">
        <b>Ativo</b><br>
        Recurso controlado pela entidade pública no presente, resultante de eventos passados, do qual se espera obter benefícios econômicos ou potencial de serviços.

        <br><br>

        <b>Passivo</b><br>
        Obrigação presente decorrente de eventos passados, cuja liquidação resultará na saída de recursos.

        <br><br>

        <b>Receita</b><br>
        Aumentos no patrimônio líquido durante o período que não decorrem de contribuições dos proprietários.

        <br><br>

        <b>Despesa</b><br>
        Reduções no patrimônio líquido resultantes do consumo de ativos ou do surgimento de obrigações.
        </div>
        """,
        unsafe_allow_html=True
        )

        st.markdown('<div class="section-title">Fluxos essenciais</div>', unsafe_allow_html=True)

        st.code("Receita: Previsão -> Lançamento -> Arrecadação -> Recolhimento", language=None)

        st.code("Despesa: Dotação -> Empenho -> Liquidação -> Pagamento", language=None)

        st.markdown('<div class="section-title">Exemplos de registros contábeis</div>', unsafe_allow_html=True)

        st.markdown(
        """
        <div class="light-box">
        <b>Arrecadação de receitas públicas</b>

        Exemplo: recebimento de tributos.

        Registro conceitual:

        Débito – Caixa ou Bancos  
        Crédito – Receita Tributária
        </div>
        """,
        unsafe_allow_html=True
        )

        st.markdown(
        """
        <div class="light-box">
        <b>Execução da despesa pública</b>

        Exemplo: pagamento de fornecedores.

        Registro conceitual:

        Débito – Despesa  
        Crédito – Caixa ou Obrigações a Pagar
        </div>
        """,
        unsafe_allow_html=True
        )

        st.markdown(
        """
        <div class="light-box">
        <b>Aquisição de bens ou serviços</b>

        Exemplo: compra de equipamentos para a administração pública.

        Registro patrimonial:

        Débito – Ativo Imobilizado  
        Crédito – Caixa ou Fornecedores
        </div>
        """,
        unsafe_allow_html=True
        )

        st.markdown('<div class="section-title">Características qualitativas da informação contábil</div>', unsafe_allow_html=True)

        st.markdown(
        """
        As informações contábeis devem possuir características que garantam sua utilidade para os usuários:

        • **Relevância** – capacidade de influenciar decisões  
        • **Representação fidedigna** – refletir adequadamente a realidade econômica  
        • **Compreensibilidade** – permitir entendimento pelos usuários  
        • **Comparabilidade** – possibilitar análise entre períodos e entidades  
        • **Tempestividade** – disponibilização em tempo adequado
        """
        )

        st.markdown('<div class="section-title">Relação com a prestação de contas</div>', unsafe_allow_html=True)

        st.markdown(
        """
        A contabilidade pública desempenha papel fundamental no processo de **accountability**, permitindo que a sociedade e os órgãos de controle avaliem:

        • a utilização dos recursos públicos  
        • a eficiência das políticas públicas  
        • a sustentabilidade das finanças governamentais

        O registro adequado das operações garante **transparência, controle e suporte à tomada de decisões**.
        """
        )

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
