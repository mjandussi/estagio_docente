
import streamlit as st
import pandas as pd
from io import BytesIO
import re
from core.estilos import titulo_app
from core.estilos import aplicar_estilos, render_timeline 
from core.funcoes import exportar_razoes_para_excel, importar_razoes_de_excel


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

titulo_app()
aplicar_estilos()


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
            "Registro das operações típicas conforme o MCASP.",
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
            "Contabilidade Aplicada ao Setor Público",
            "Plano de Contas e Subsistemas",
            "Registro das operações típicas conforme as NBC T SP 16",
            "Exercícios e Cases - parte 1",
            "Elaboração das Demonstrações Contábeis",
            "Exercícios e Cases - parte 2"
        ],
        "metodologia": [
            "Aulas expositivas com apoio visual.",
            "Discussão de conceitos e exemplos práticos.",
            "Resolução de exercícios em sala.",
            "Uso de cases para consolidação do conteúdo."
        ],
        "bibliografia": [
            "Lei nº 4.320/1964",
            "NBC TSP EC",
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
            ("Normas", "A disciplina se apoia na Lei 4.320/64, nas NBC TSP e no MCASP.")
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
        # "case": [
        #     "Receita prevista de IPTU e sua arrecadação ao longo do exercício.",
        #     "Despesa com pessoal empenhada, liquidada e paga.",
        #     "Aquisição de bem permanente com efeito qualitativo no patrimônio."
        # ]
        "fatos_janeiro": [
        "0) Lançamento inicial de constituição do ente fictício no valor de R$ 1.000.000,00 contra as contas de Banco e Saldo Patrimonial.",
        "1) O orçamento anual foi fixado em R$ 2.000.000,00, em equilíbrio entre receitas e despesas, sendo 70% Corrente e o restante Capital.",
        "2) Houve empenho para pagamento da folha de pessoal no valor correspondente a 1/12 do custo anual de R$ 1.200.000,00.",
        "3) Houve a liquidação da folha de pessoal, com retenção de contribuição previdenciária de 11%.",
        "4) Houve o pagamento líquido da folha aos servidores.",
        "5) Houve lançamento de receita tributária no valor de R$ 180.000,00.",
        "6) Houve arrecadação e recolhimento de 80% da receita tributária lançada e estes valores foram para o Tesouro.",
        "7) Houve compra de material de consumo para estoque no valor de R$ 10.000,00, e com a liquidação e pagamento apenas no valor de R$ 5.000,00.",
        "8) Houve obtenção de Empréstimo e Financiamento no valor de R$ 100.000,00",
        "9) Houve inscrição de Dívida Ativa dos valores não arrecadados de receita tributária"
        ],
        "fatos_dezembro": [
        "10) Houve arrecadação sobre um convênio firmado para copra de ambulância e o valor recebido foi de R$ 50.000,00.",
        "11) Houve compra de 1 ambulância no valor de R$40.000,00 (empenho e liquidação).",
        "12) Houve a depreciação de 1 mês da ambulância adquirida.",
        "13) Houve pagamento (repasse) de toda contribuição previdenciária retida",
        "14) Houve inscrição de Dívida Ativa dos valores não arrecadados de receita tributária",
        "15) Houve doação recebida de computadores no valor de $3.000.",
        "16) Consumo de metade do Estoque atualizado",
        "17) Aumento do saldo de empréstimos contraídos em $2000 devido a variação cambial",
        "18) Houve a inscrição dos valores de Restos a Pagar Processados",
        "19) Houve a inscrição dos valores de Restos a Pagar Processados"
        ],
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

##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################

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
            ativo = st.session_state.pagina == label

            # abre um wrapper com classe diferente se estiver ativo
            classe = "menu-wrapper active" if ativo else "menu-wrapper"
            st.markdown(f'<div class="{classe}">', unsafe_allow_html=True)

            if st.button(label, use_container_width=True, key=f"btn_{label}"):
                st.session_state.pagina = label
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

pagina = st.session_state.pagina

##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################


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
                <p>2. Contabilidade Aplicada ao Setor Público</p>
                <p>3. Plano de Contas e Subsistemas</p>
                <p>4. Registro das operações típicas conforme as NBC TSP e MCASP</p>
                <p>5. Exercícios e Cases - parte 1</p>
                <p>6. Elaboração das Demonstrações Contábeis</p>
                <p>7. Exercícios e Cases - parte 2</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="box">
                <h4>Didática e Material</h4>
                <p>• Material didático como eixo principal</p>
                <p>• Usar o app como roteiro de exposição</p>
                <p>• Exercícios ao final de cada parte</p>
                <p>• Revisar os conceitos centrais antes das avaliações</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Lógica da disciplina</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="flow-box">Fundamentos da Contabilidade Pública -> Plano de Contas -> Registros das Operações -> Exercícios e Cases -> Demonstrações Contábeis -> Exercícios e Cases</div>',
        unsafe_allow_html=True
    )


##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################


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
        st.markdown(
                """
                <div class="light-box">
                    <h4>Links para acesso as bibliografia recomendada</h4>
                    <p><a href="https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade/nbc-tsp-do-setor-publico/" target="_blank">
                    Acessar página das normas NBC TSP no CFC
                    </a></p>
                    <p><a href="https://www.tesourotransparente.gov.br/publicacoes/manual-de-contabilidade-aplicada-ao-setor-publico-mcasp/2025/26" target="_blank">
                    Acessar página do MCASP
                    </a></p>
                    </a></p>
                    <p><a href="https://siconfi.tesouro.gov.br/siconfi/pages/public/conteudo/conteudo.jsf?id=12503" target="_blank">
                    Acessar página do Anexo II da Portaria STN 642, de 20 de Setembro de 2019 (Leiaute MSC)
                    </a></p>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown(f'<div class="box"><h4>1.7 Curriculum resumido do professor</h4><p>{sec["curriculum"]}</p></div>', unsafe_allow_html=True)
        


##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################

# =========================
# BLOCOS TEÓRICOS (comum as 4 páginas de Teoria)
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
                <h4>Objetivo desta seção</h4>
                <p>{sec["objetivo"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with c2:
        st.markdown(
            '<div class="box"><h4>Principais tópicos que serão abordados</h4>' +
            "".join([f"<p>• {x}</p>" for x in sec["topicos"]]) +
            '</div>',
            unsafe_allow_html=True
        )

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
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################

    #############################################
    ########    CONTABILIDADE PÚBLICA    ########
    #############################################

# Seção específica para Contabilidade Aplicada ao Setor Público
    st.divider()
    if pagina == "Contabilidade Aplicada ao Setor Público":
        st.markdown(
            '<div class="section-title">Evolução histórica e normativa da Contabilidade Aplicada ao Setor Público</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
        A Contabilidade Aplicada ao Setor Público no Brasil passou por uma evolução normativa e conceitual significativa ao longo do tempo. 
        De um modelo historicamente voltado ao controle do orçamento e dos fluxos financeiros do Tesouro, avançou-se para uma estrutura mais ampla, 
        orientada também pela transparência, pela responsabilidade fiscal, pela padronização nacional e pelo enfoque patrimonial.

        A linha do tempo a seguir apresenta, de forma resumida, os principais marcos dessa evolução, destacando como a Lei nº 4.320/1964, 
        a Constituição Federal de 1988, a Lei de Responsabilidade Fiscal, a convergência às NBC TSP, a Matriz de Saldos Contábeis e o Ranking Siconfi 
        contribuíram para a configuração do modelo atual.
        """)

        render_timeline()

        st.markdown("""
        <div class="light-box">
            <h4>Síntese da evolução</h4>
            <p>
            Em termos didáticos, essa trajetória pode ser compreendida em três grandes fases:
            <br><br>
            <strong>1. Período anterior à Lei nº 4.320/1964:</strong> predominância do controle do Tesouro, com baixa padronização nacional;
            <br>
            <strong>2. Modelo estruturado pela Lei nº 4.320/1964:</strong> consolidação das normas gerais de direito financeiro e fortalecimento do enfoque orçamentário;
            <br>
            <strong>3. Modelo contemporâneo:</strong> ampliação da transparência fiscal, convergência às NBC TSP, padronização pelo PCASP, uso da MSC e avaliação da qualidade da informação no Siconfi.
            </p>
        </div>
        """, unsafe_allow_html=True)



        st.divider()
        st.markdown('<div class="section-title">Normas Brasileiras de Contabilidade Aplicadas ao Setor Público</div>', unsafe_allow_html=True)

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

        df_dif_entre_conts = pd.DataFrame(dados)
        st.dataframe(df_dif_entre_conts, hide_index=True, use_container_width=True)

##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################

    ########################################
    ########    PLANO DE CONTAS     ########
    ########################################

    if pagina == "Plano de Contas e Subsistemas":
        ##################################################################################################################
        # Seção: Plano de Contas e Subsistemas
        st.divider()

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
        Aas operações de recebimento de recursos financeiros e de pagamento de obrigações correspondem a transações distintas do ponto de vista administrativo. Contudo, ambas envolvem movimentações relacionadas ao dinheiro disponível da entidade. Para registrar essas operações de forma organizada, utiliza-se uma conta específica que representa esse elemento patrimonial, usualmente denominada Caixa ou Tesouraria.
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

        img_col1, img_col2 = st.columns(2)

        with img_col1:
            st.image(
                "imagens/pcasp_motivação_para_criação.png",  # imagem da página do pcasp_motivação_para_criação
                caption="PCASP - Motivação para criação",
                use_container_width=True
            )

        with img_col2:
            st.image(
                "imagens/pcasp_alcance.png",  # imagem da página do pcasp_alcance
                caption="PCASP - Alcance",
                use_container_width=True
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
            • Contas iniciadas por número **ímpar** → natureza **devedora**<br> 
            • Contas iniciadas por número **par** → natureza **credora**
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
        "Controle"
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

        st.divider()

        c1, c2 = st.columns(2)

        with c1:
            st.image(
                "imagens/pcasp_natureza_da_informação.png",  # imagem da página das pcasp_natureza_da_informação
                caption="PCASP - naturezas da Informação",
                use_container_width=True
            )
            
        with c2:
            st.image(
                "imagens/pcasp_classes_e_subsistemas.png",  # imagem da página das pcasp_classes_e_subsistemas
                caption="PCASP - Classes e Subsistemas",
                use_container_width=True
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


        st.markdown('<div class="section-title">PCASP - Detalhamento do Código da Conta Contábil e Mecanismo de Consolidação</div>', unsafe_allow_html=True)

        img_col1, img_col2 = st.columns(2)

        with img_col1:
            st.image(
                "imagens/pcasp_estrutura_código_contábil.png",  # imagem da página do Detalhamento dos Níveis das Contas do PCASP
                caption="PCASP - Níveis de desdobramento",
                use_container_width=True
            )

            st.markdown(
                """
                <div class="light-box">
                    <h4>Link de acesso</h4>
                    <p><a href="https://www.tesourotransparente.gov.br/publicacoes/manual-de-contabilidade-aplicada-ao-setor-publico-mcasp/2025/26" target="_blank">
                    Acessar página do MCASP
                    </a></p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with img_col2:
            st.image(
                "imagens/pcasp_mecanismo_de_consolidação.png",  # imagem da página dos Níveis de Consolidação (OFSS) do PCASP
                caption="PCASP - Níveis de Consolidação (OFSS)",
                use_container_width=True
            )

        st.divider()


##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################


    if pagina == "Registro das Operações Típicas":
        st.markdown('<div class="section-title">Fases (Estágios) da Receita e Despesa</div>', unsafe_allow_html=True)
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

        Nessas situações, a entidade recebe ou entrega recursos **sem troca direta de valor equivalente**, característica típica da atuação governamental.
        """
        )
        st.divider()

        st.markdown('<div class="section-title">Reconhecimento dos Elementos Contábeis</div>', unsafe_allow_html=True)

        st.markdown(
        """
        A Estrutura Conceitual define os principais elementos das demonstrações contábeis:
        """
        )

        st.markdown(
        """
        <div class="light-box">
        <ul>
                <li><b>Ativo</b> - Recurso controlado pela entidade pública no presente, resultante de eventos passados, do qual se espera obter benefícios econômicos ou potencial de serviços.</li>
                <li><b>Passivo</b> - Obrigação presente decorrente de eventos passados, cuja liquidação resultará na saída de recursos.</li>
                <li><b>Receita</b> - Aumentos no patrimônio líquido durante o período que não decorrem de contribuições dos proprietários.</li>
                <li> <b>Despesa</b> - Reduções no patrimônio líquido resultantes do consumo de ativos ou do surgimento de obrigações.</li>
                </ul>
            </div>
        """,
        unsafe_allow_html=True
        )

        st.divider()

        # st.markdown('<div class="section-title">Exemplos de registros contábeis</div>', unsafe_allow_html=True)

        # st.markdown(
        # """
        # <b>Arrecadação de receitas públicas</b>
        # <div class="light-box">

        # Exemplo: recebimento de tributos.

        # Débito – Caixa ou Bancos  
        # Crédito – Receita Tributária
        # </div>
        # """,
        # unsafe_allow_html=True
        # )

        # st.markdown(
        # """
        # <b>Execução da despesa pública</b>
        # <div class="light-box">
        
        # Exemplo: pagamento de fornecedores.

        # Débito – Despesa  
        # Crédito – Caixa ou Obrigações a Pagar
        # </div>
        # """,
        # unsafe_allow_html=True
        # )

        # st.markdown(
        # """
        # <b>Aquisição de bens ou serviços</b>
        # <div class="light-box">
        
        # Exemplo: compra de equipamentos para a administração pública.

        # Débito – Ativo Imobilizado  
        # Crédito – Caixa ou Fornecedores
        # </div>
        # """,
        # unsafe_allow_html=True
        # )

        # st.divider()


        st.markdown('<div class="section-title">Características qualitativas da informação contábil</div>', unsafe_allow_html=True)

        st.markdown(
            """
            As informações contábeis devem possuir características que garantam sua utilidade para os usuários:
            <div class="light-box">
                <ul>
                    <li><b>Relevância</b> – capacidade de influenciar decisões</li>
                    <li><b>Representação fidedigna</b> – refletir adequadamente a realidade econômica</li>
                    <li><b>Compreensibilidade</b> – permitir entendimento pelos usuários</li>
                    <li><b>Comparabilidade</b> – possibilitar análise entre períodos e entidades</li>
                    <li><b>Tempestividade</b> – disponibilização em tempo adequado</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.markdown('<div class="section-title">Relação com a prestação de contas</div>', unsafe_allow_html=True)

        st.markdown(
            """
            A contabilidade pública desempenha papel fundamental no processo de **accountability**, permitindo que a sociedade e os órgãos de controle avaliem:

            <div class="light-box">
                <ul>
                    <li>a utilização dos recursos públicos</li>
                    <li>a eficiência das políticas públicas</li>
                    <li>a sustentabilidade das finanças governamentais</li>
                </ul>
            </div>

             O registro adequado das operações garante **transparência, controle e suporte à tomada de decisões**.
            """,
            unsafe_allow_html=True
        )

        st.divider()

        ############################################################

        st.markdown("## Lançamentos Típicos da Contabilidade Aplicada ao Setor Público")

        evento = st.selectbox(
            "Escolha um Ato/Fato Contábil",
            [
                "Arrecadação E Recolhimento de tributo não lançado",
                "Arrecadação E Recolhimento de tributo lançado",
                "Empenho da despesa",
                "Liquidação da despesa",
                "Pagamento da despesa",
                "Apropriação da VPD antes da liquidação",
                "Apropriação da VPD após a liquidação",
                "Aquisição de veículo",
                "Depreciação de bem público",
                "Inscrição em restos a pagar",
                "Cancelamento de restos a pagar"
            ]
        )

        mostrar = st.button("Mostrar lançamento")

        if mostrar:

            if evento == "Arrecadação E Recolhimento de tributo não lançado":
                st.markdown("### Arrecadação E Recolhimento de tributo não lançado")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito: 1.1.1.1.x.xx.xx - Caixa e Equivalentes de Caixa em Moeda Nacional (F)\n  
        Crédito: 4.1.X.X.x.xx.xx - Receita Tributária (VPA)
        """)
                st.info("Efeito: aumento do patrimônio líquido.")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.1.1.x.xx.xx - Receita a Realizar (Corrente ou Capital)\n  
        Crédito: 6.2.1.2.x.xx.xx - Receita Realizada (Corrente ou Capital)
        """)
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 7.2.1.1.x.xx.xx - Controle da Disponibilidade de Recursos\n
        Crédito: 8.2.1.1.1.xx.xx - Disponibilidade por Destinação de Recursos (DDR)
        """)
                
            elif evento == "Arrecadação E Recolhimento de tributo lançado":
                st.markdown("### Arrecadação E Recolhimento de tributo lançado")
                st.markdown("**1º Momento (fato gerador):**")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito: 1.1.2.1.x.xx.xx  - Créditos Tributários a Receber (P)\n  
        Crédito: 4.1.X.X.x.xx.xx - Receita Tributária (VPA)
        """)
                st.info("Efeito: aumento do patrimônio líquido.")
                st.markdown("---")
                st.markdown("**2º Momento (Arrecadação e Recolhimento):**")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito: 1.1.1.1.x.xx.xx - Caixa e Equivalentes de Caixa em Moeda Nacional (F)\n
        Crédito: 1.1.2.1.x.xx.xx  - Créditos Tributários a Receber (P)
        """)
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.1.1.x.xx.xx - Receita a Realizar (Corrente ou Capital)\n  
        Crédito: 6.2.1.2.x.xx.xx - Receita Realizada (Corrente ou Capital)
        """)
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 7.2.1.1.x.xx.xx - Controle da Disponibilidade de Recursos\n
        Crédito: 8.2.1.1.1.xx.xx - Disponibilidade por Destinação de Recursos (DDR)
        """)


            elif evento == "Empenho da despesa":
                st.markdown("### Empenho da despesa")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.2.1.1.xx.xx - Crédito Disponível\n  
        Crédito: 6.2.2.1.3.01.xx - Crédito Empenhado a Liquidar
        """)
                st.info("O empenho não gera efeito patrimonial.")
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 8.2.1.1.1.xx.xx - Disponibilidade por Destinação de Recursos (DDR)\n  
        Crédito: 8.2.1.1.2.xx.xx - DDR Comprometida por Empenho
        """)


            elif evento == "Liquidação da despesa":
                st.markdown("### Liquidação da despesa")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito:  3.3.2.x.x.xx.xx - Variação Patrimonial Diminutiva – Serviços (VPD)\n  
        Crédito: 2.1.3.x.x.xx.xx - Fornecedores e Contas a Pagar a Curto Prazo (F)
        """)
                st.info("Aqui ocorre a variação patrimonial diminutiva.")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: Crédito Empenhado a Liquidar\n  
        Crédito: Crédito Empenhado Liquidado
        """)
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 8.2.1.1.2.xx.xx - DDR Comprometida por Empenho\n  
        Crédito: 8.2.1.1.3.xx.xx - DDR Comprometida por Liquidação e Entradas Compensatórias
        """)


            elif evento == "Pagamento da despesa":
                st.markdown("### Pagamento da despesa")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: Crédito Empenhado Liquidado  
        Crédito: Crédito Empenhado Pago
        """)
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito: Obrigações a Pagar  
        Crédito: Caixa ou Bancos
        """)
                

            elif evento == "Apropriação da VPD antes da liquidação":
                st.markdown("### Apropriação da VPD antes da liquidação")
                st.markdown("**1º Apropriação mensal (1/12 do 13º salário):**")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito: 3.1.1.x.x.xx.xx  - Remuneração a Pessoal\n  
        Crédito: 2.1.1.1.x.xx.xx - Pessoal a Pagar - 13º Salário (P)
        """)
                st.info("Efeito: diminuição do patrimônio líquido.")
                st.markdown("---")
                st.markdown("**2º EMPENHO nos meses do pagamento:**")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito:  2.1.1.1.x.xx.xx - Pessoal a Pagar - 13º Salário (P)\n
        Crédito: 2.1.1.1.x.xx.xx  - Pessoal a Pagar – 13º Salário (F)
        """)
                st.info("IMPORTANTE: Troca de Atributo do ISF de 'P' para 'F'.")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.2.1.1.xx.xx - Crédito Disponível\n  
        Crédito: 6.2.2.1.3.01.xx - Crédito Empenhado a Liquidar\n
        Débito: 6.2.2.1.3.01.xx - Crédito Empenhado a Liquidar\n  
        Crédito: 6.2.2.1.3.02.xx - Crédito Empenhado em Liquidação
        """)
                st.info("IMPORTANTE: Figura do 'Em Liquidação'.")
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 8.2.1.1.1.xx.xx - Disponibilidade por Destinação de Recursos (DDR)\n  
        Crédito: 8.2.1.1.2.xx.xx - DDR Comprometida por Empenho
        """)
                st.markdown("---")
                st.markdown("**3º LIQUIDAÇÃO nos meses do pagamento:**")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.2.1.3.02.xx - Crédito Empenhado em Liquidação\n  
        Crédito: 6.2.2.1.3.03.xx - Crédito Empenhado Liquidado a Pagar
        """)
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 8.2.1.1.2.xx.xx - DDR Comprometida por Empenho\n  
        Crédito: 8.2.1.1.3.xx.xx - DDR Comprometida por Liquidação e Entradas Compensatórias
        """)
                st.markdown("---")
                st.markdown("**4º PAGAMENTO nos meses do pagamento:**")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito:  2.1.1.1.x.xx.xx - Pessoal a Pagar – 13º Salário (F)\n
        Crédito:  1.1.1.1.1.xx.xx  - Caixa e Equivalentes de Caixa em Moeda Nacional (F) 
        """)
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.2.1.3.03.xx - Crédito Empenhado Liquidado a Pagar\n  
        Crédito: 6.2.2.1.3.04.xx - Crédito Empenhado Pago
        """)
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 8.2.1.1.3.xx.xx - DDR Comprometida por Liquidação e Entradas Compensatórias\n  
        Crédito: 8.2.1.1.4.xx.xx - DDR Utilizada
        """)
                

            elif evento == "Apropriação da VPD após a liquidação":
                st.markdown("### Apropriação da VPD após a liquidação")
                st.markdown("**1º EMPENHO:**")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.2.1.1.xx.xx - Crédito Disponível\n  
        Crédito: 6.2.2.1.3.01.xx - Crédito Empenhado a Liquidar
        """)
                st.info("O empenho não gera efeito patrimonial.")
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 8.2.1.1.1.xx.xx - Disponibilidade por Destinação de Recursos (DDR)\n  
        Crédito: 8.2.1.1.2.xx.xx - DDR Comprometida por Empenho
        """)
                st.markdown("---")
                st.markdown("**2º No momento do recebimento e incorporação ao estoque:**")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito:  1.1.5.6.x.xx.xx - Estoque - Almoxarifado\n
        Crédito: 2.1.3.x.x.xx.xx  - Fornecedores e Contas a Pagar a Curto Prazo (F)
        """)
                st.info("IMPORTANTE: Atributo do ISF já surge como 'F'.")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.2.1.3.01.xx - Crédito Empenhado a Liquidar\n  
        Crédito: 6.2.2.1.3.02.xx - Crédito Empenhado em Liquidação
        """)
                st.info("IMPORTANTE: Figura do 'Em Liquidação'.")
         
                st.markdown("---")
                st.markdown("**3º LIQUIDAÇÃO e incorporação ao estoque:**")
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.2.1.3.02.xx - Crédito Empenhado em Liquidação\n  
        Crédito: 6.2.2.1.3.03.xx - Crédito Empenhado Liquidado a Pagar
        """)
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 8.2.1.1.2.xx.xx - DDR Comprometida por Empenho\n  
        Crédito: 8.2.1.1.3.xx.xx - DDR Comprometida por Liquidação e Entradas Compensatórias
        """)
                st.markdown("---")
                st.markdown("**4º PAGAMENTO nos meses do pagamento:**")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito:  2.1.1.1.x.xx.xx - Pessoal a Pagar – 13º Salário (F)\n
        Crédito:  1.1.1.1.1.xx.xx  - Caixa e Equivalentes de Caixa em Moeda Nacional (F) 
        """)
                st.markdown("**Registro Orçamentário**")
                st.success("""
        Débito: 6.2.2.1.3.03.xx - Crédito Empenhado Liquidado a Pagar\n  
        Crédito: 6.2.2.1.3.04.xx - Crédito Empenhado Pago
        """)
                st.markdown("**Registro Controle**")
                st.success("""
        Débito: 8.2.1.1.3.xx.xx - DDR Comprometida por Liquidação e Entradas Compensatórias\n  
        Crédito: 8.2.1.1.4.xx.xx - DDR Utilizada
        """)
                st.markdown("---")
                st.markdown("**5º momento da saída do estoque:**")
                st.markdown("**Registro Patrimonial**")
                st.success("""
        Débito:   3.3.1.1.1.xx.xx - Consumo de Material – Consolidação\n
        Crédito:  1.1.5.6.x.xx.xx - Estoque - Almoxarifado 
        """)



            elif evento == "Aquisição de veículo":

                st.markdown("### Aquisição de veículo")

                st.markdown("**Registro Patrimonial (modelo atual)**")

                st.success("""
        Débito: Imobilizado – Veículos  
        Crédito: Fornecedores
        """)

                st.info("Reconhecimento do ativo imobilizado.")

            elif evento == "Depreciação de bem público":

                st.markdown("### Depreciação de bem público")

                st.markdown("**Registro Patrimonial**")

                st.success("""
        Débito: VPD – Depreciação  
        Crédito: Depreciação Acumulada
        """)

                st.info("Representa consumo do potencial de serviço do ativo.")

            elif evento == "Inscrição em restos a pagar":

                st.markdown("### Inscrição em Restos a Pagar")

                st.markdown("**Registro Orçamentário**")

                st.success("""
        Débito: Crédito Empenhado Liquidado  
        Crédito: Restos a Pagar
        """)

            elif evento == "Cancelamento de restos a pagar":

                st.markdown("### Cancelamento de Restos a Pagar")

                st.markdown("**Registro Orçamentário**")

                st.success("""
        Débito: Restos a Pagar  
        Crédito: Crédito Disponível
        """)


##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################

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
        
    with c2:
        st.markdown('<div class="section-title">Questões para discussão</div>', unsafe_allow_html=True)

        for pergunta, resposta in sec["questoes"]:
            with st.expander(pergunta):
                st.success(resposta)


    st.divider()

    st.markdown("### ✍️ Com base nas informações abaixo, sobre os atos e fatos de um determinado ente no ano X26, lance e contabilize nos razonetes disponíveis por conta contábil:")

    if pagina == "Exercícios e Cases I":
        c3, c4 = st.columns([1.05, 0.95])

        with c3:
            st.markdown('<div class="section-title">Atos e Fatos Janeiro</div>', unsafe_allow_html=True)
            for item in sec["fatos_janeiro"]:
                st.markdown(
                    f"""
                    <div class="light-box">
                        <p>{item}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        with c4:
            st.markdown('<div class="section-title">Atos e Fatos Dezembro</div>', unsafe_allow_html=True)
            for item in sec["fatos_dezembro"]:
                st.markdown(
                    f"""
                    <div class="light-box">
                        <p>{item}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    

    
    st.divider()

    ###############################################################
    # SEÇÃO DOS RAZONETES
    ###############################################################


    # ==========================================
    # CONTAS AGRUPADAS POR NATUREZA
    # ==========================================
    CONTAS_POR_CATEGORIA = {
        "Orçamentária": [
            "Previsão Inicial da Receita",
            "Receita a Realizar Co",
            "Receita a Realizar Cap",
            "Receita Realizada Co",
            "Receita Realizada Cap",
            "Crédito Inicial",
            "Crédito Disponível Co",
            "Crédito Disponível Cap",
            "Despesa ou Créditos Empenhados Co",
            "Despesa ou Créditos Empenhados Cap",
            "Despesa ou Créditos Liquidados Co",
            "Despesa ou Créditos Liquidados Cap",
            "Despesa ou Créditos Pagos Co",
            "Despesa ou Créditos Pagos Cap",
            "Inscrição de Restos a Pagar Não Processado",
            "Inscrição de Restos a Pagar Processado",
        ],
        "Patrimonial": [
            "Banco Conta Única",
            "Receita a Tributária a Receber",
            "Dívida Ativa Tributária",
            "Estoque de Materiais",
            "Obras em Andamento",
            "Bens Móveis",
            "Bens Imóveis",
            "Depósito de Terceiros",
            "Consignações",
            "Pessoal a Pagar",
            "Fornecedores",
            "Empréstimos Concedidos",
            "Empréstimos Contraídos",
            "Dívida Fundada",
            "Saldo Patrimonial",
            "Variação Aumentativa: Receita Corrente",
            "Variação Aumentativa: Transferência de Cap",
            "Variação Aumentativa Indep. Orçamento",
            "Variação Diminutiva: Despesa Corrente",
            "Variação Diminutiva Indep. Orçamento",
        ],
        "Controle / Compensação": [
            "Disponibilidade por Fonte Corrente",
            "Disponibilidade por Fonte Capital",
            "Disponibilidade Financeira",
        ]
    }

    # Lista única com todas as contas
    CONTAS_FIXAS = [
        conta
        for lista_contas in CONTAS_POR_CATEGORIA.values()
        for conta in lista_contas
    ]

    # Inicializa os razonetes no session_state
    if "razoes" not in st.session_state:
        st.session_state.razoes = {}

    for conta in CONTAS_FIXAS:
        if conta not in st.session_state.razoes:
            st.session_state.razoes[conta] = pd.DataFrame({
                "Histórico": ["", "", "", ""],
                "Débito": [0.0, 0.0, 0.0, 0.0],
                "Crédito": [0.0, 0.0, 0.0, 0.0]
            })

    if pagina == "Exercícios e Cases I":

        st.markdown("## Razão Contábil Interativo")

        st.warning(
            "⚠️ **Atenção:** Os dados preenchidos nos razonetes ficam salvos apenas "
            "durante a sessão atual do navegador. Para não perder o exercício, "
            "**exporte o arquivo Excel dos Razonetes do exercício antes de sair do app.**"
        )

        # ==========================================
        # ESCOLHA DA CONTA
        # ==========================================
        st.markdown(
            """
            <div class="light-box">
            Siga os passos abaixo para efetuar os registros nos razonetes
            <ul>
                <li>1) Escolha a natureza da conta</li>
                <li>2) Escolha a conta a ser preenchida</li>
                <li>3) Digite no quadro/tabela o respectivo valor a ser lançado na coluna de débito ou crédito</li>
            </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            categoria_escolhida = st.selectbox(
                "Selecione a natureza da conta",
                list(CONTAS_POR_CATEGORIA.keys())
            )

        with col2:
            conta_escolhida = st.selectbox(
                "Selecione a conta para preencher",
                CONTAS_POR_CATEGORIA[categoria_escolhida]
            )

        df_conta = st.session_state.razoes[conta_escolhida]

        razao_edit = st.data_editor(
            df_conta,
            hide_index=True,
            use_container_width=True,
            num_rows="dynamic",
            column_config={
                "Histórico": st.column_config.TextColumn("Histórico", width="medium"),
                "Débito": st.column_config.NumberColumn("Débito", format="%.2f", width="small"),
                "Crédito": st.column_config.NumberColumn("Crédito", format="%.2f", width="small")
            },
            key=f"razao_editor_{conta_escolhida}"
        )

        # salva no estado
        st.session_state.razoes[conta_escolhida] = razao_edit

        total_debito = pd.to_numeric(razao_edit["Débito"], errors="coerce").fillna(0).sum()
        total_credito = pd.to_numeric(razao_edit["Crédito"], errors="coerce").fillna(0).sum()
        saldo = total_debito - total_credito

        st.markdown(f"### Conta: {conta_escolhida}")
        st.caption(f"Natureza: {categoria_escolhida}")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Total Débito", f"R$ {total_debito:,.2f}")
        with c2:
            st.metric("Total Crédito", f"R$ {total_credito:,.2f}")
        with c3:
            natureza = "Devedor" if saldo >= 0 else "Credor"
            st.metric("Saldo", f"R$ {abs(saldo):,.2f} ({natureza})")

        st.divider()

        # # ==========================================
        # # IMPORTAÇÃO E EXPORTAÇÃO
        # # ==========================================

        st.markdown("### 💾 Importar Razonte anterior ou Exportar Razonete do atual exercício")

        st.markdown("""
            <div class="light-box">
            <p>
            📌 <b>Nesta área é possível <b>salvar o razonete do exercício realizado</b> ou <b>continuar um trabalho iniciado anteriormente e importar os razonetes</b><br><br>

            📥 <b>Importar exercício</b> → para carregar um arquivo de razonetes salvo anteriormente e continuar os lançamentos.<br>
            📤 <b>Exportar razonetes</b> → para baixar os razonetes do seu exercício em Excel e guardar seu trabalho.<br><br>

            ⚠️ Os dados ficam disponíveis apenas durante a sessão do navegador. Para não perder o trabalho, exporte o arquivo ao final do exercício.
            </p>
            </div>
            """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 📥 Importar Razontes de exercício anteriormente feito")
            
            arquivo_importado = st.file_uploader(
                "Selecionar arquivo Excel salvo anteriormente",
                type=["xlsx"],
                key="upload_razoes"
            )

            if arquivo_importado is not None:
                if st.button("Importar dados"):
                    razoes_importadas = importar_razoes_de_excel(arquivo_importado, CONTAS_FIXAS)

                    for conta in CONTAS_FIXAS:
                        if conta in razoes_importadas:
                            st.session_state.razoes[conta] = razoes_importadas[conta]

                    st.success("Dados importados com sucesso.")

        with col2:
            st.markdown("#### 📤 Exportar Razonetes do exercício")

            nome_arquivo = st.text_input(
                "Nome do arquivo",
                value="razoes_contabeis",
                key="nome_arquivo_exportacao"
            ).strip()

            if nome_arquivo == "":
                nome_arquivo = "razoes_contabeis"

            nome_arquivo = re.sub(r'[<>:"/\\|?*]', "_", nome_arquivo)

            if not nome_arquivo.lower().endswith(".xlsx"):
                nome_arquivo = f"{nome_arquivo}.xlsx"

            arquivo_excel = exportar_razoes_para_excel(st.session_state.razoes)

            st.download_button(
                label="Baixar razonetes em Excel",
                data=arquivo_excel,
                file_name=nome_arquivo,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

        st.success(
            "✔️ Terminou o exercício? "
            "Clique em **Baixar razonetes em Excel** para salvar seu trabalho."
        )

        if st.button("🔄 Reiniciar (limpar) Razonetes do exercício"):
            st.session_state.razoes = {}
            st.rerun()

    
        st.divider()

        # ==========================================
        # RESUMO GERAL
        # ==========================================
        st.markdown("## Resumo dos saldos de todas as contas")

        resumo = []
        for conta, df in st.session_state.razoes.items():
            deb = pd.to_numeric(df["Débito"], errors="coerce").fillna(0).sum()
            cred = pd.to_numeric(df["Crédito"], errors="coerce").fillna(0).sum()
            saldo = deb - cred

            resumo.append({
                "Conta": conta,
                "Total Débito": deb,
                "Total Crédito": cred,
                "Saldo": abs(saldo),
                "Natureza do Saldo": "Devedor" if saldo >= 0 else "Credor"
            })

        df_resumo = pd.DataFrame(resumo)

        st.dataframe(
            df_resumo,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Conta": st.column_config.Column(width="large"),
                "Total Débito": st.column_config.NumberColumn(format="%.2f"),
                "Total Crédito": st.column_config.NumberColumn(format="%.2f"),
                "Saldo": st.column_config.NumberColumn(format="%.2f"),
                "Natureza do Saldo": st.column_config.Column(width="small")
            }
        )

        st.divider()


        #############################################################

        st.markdown("## Balanço Patrimonial Interativo")

        df_ativo = pd.DataFrame({
            "Conta": ["Caixa", "Créditos a Receber", "Imobilizado"],
            "Valor": [0.0, 0.0, 0.0]
        })

        df_passivo_pl = pd.DataFrame({
            "Conta": ["Fornecedores", "Obrigações", "Patrimônio Líquido"],
            "Valor": [0.0, 0.0, 0.0]
        })

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Ativo")
            ativo_edit = st.data_editor(
                df_ativo,
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
                column_config={
                    "Conta": st.column_config.TextColumn("Conta", width="medium"),
                    "Valor": st.column_config.NumberColumn("Valor", format="%.2f", width="small")
                },
                key="ativo_editor"
            )

        with col2:
            st.markdown("### Passivo + Patrimônio Líquido")
            passivo_edit = st.data_editor(
                df_passivo_pl,
                hide_index=True,
                use_container_width=True,
                num_rows="dynamic",
                column_config={
                    "Conta": st.column_config.TextColumn("Conta", width="medium"),
                    "Valor": st.column_config.NumberColumn("Valor", format="%.2f", width="small")
                },
                key="passivo_editor"
            )

        total_ativo = ativo_edit["Valor"].fillna(0).sum()
        total_passivo = passivo_edit["Valor"].fillna(0).sum()

        st.markdown("### Totais")

        c1, c2 = st.columns(2)
        with c1:
            st.metric("Total do Ativo", f"R$ {total_ativo:,.2f}")
        with c2:
            st.metric("Total do Passivo + PL", f"R$ {total_passivo:,.2f}")

        if round(total_ativo, 2) == round(total_passivo, 2):
            st.success("Balanço em equilíbrio: Ativo = Passivo + Patrimônio Líquido.")
        else:
            diferenca = total_ativo - total_passivo
            st.warning(f"Balanço sem equilíbrio. Diferença: R$ {diferenca:,.2f}")
