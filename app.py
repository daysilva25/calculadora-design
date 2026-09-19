import streamlit as st

# ==============================================================================
# CALCULADORA DE PREÇOS PARA DESIGN GRÁFICO
# Criada e idealizada por Daiane (Estudante de Design & Programação)
# ==============================================================================

st.set_page_config(
    page_title="Calculadora de Preços para Designers",
    page_icon="🎨",
    layout="centered"
)

# --- ESTILO PERSONALIZADO EM TONS DE ROXO (DESIGN ELEGANTE) ---
st.markdown("""
<style>
    /* Cor dos títulos principais */
    h1, h2, h3 {
        color: #5B21B6 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Botão principal em roxo vibrante com cantos arredondados */
    .stButton>button {
        background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%) !important;
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.5rem !important;
        box-shadow: 0 4px 14px 0 rgba(124, 58, 237, 0.35) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(124, 58, 237, 0.45) !important;
        background: linear-gradient(135deg, #6D28D9 0%, #5B21B6 100%) !important;
    }

    /* Destaque das caixas de métricas */
    [data-testid="stMetricValue"] {
        color: #6D28D9 !important;
    }
    
    /* Caixa de apresentação da Daiane com borda lilás */
    .apresentacao-box {
        background-color: #F5F3FF;
        border-left: 5px solid #7C3AED;
        padding: 1.2rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("🎨 Calculadora de Preços para Designers")
st.caption("✨ Desenvolvido por Daiane | Design Gráfico & Programação")

st.markdown("""
<div class="apresentacao-box">
    <b>Olá! Meu nome é Daiane, sou estudante de Design e Programação.</b><br><br>
    Desenvolvi esta ferramenta para auxiliar designers — especialmente quem está no início da jornada — a precificar seus trabalhos com mais segurança e autonomia.<br><br>
    O sistema utiliza valores médios praticados no mercado e cruza essas informações com o seu nível de experiência, o estado onde você ou o cliente atuam e o grau de complexidade de cada projeto.<br><br>
    💡 <i><b>Importante:</b> esta ferramenta serve como um guia de apoio e orientação, e não como uma regra engessada. Sinta-se totalmente à vontade para adaptar os valores à sua realidade!</i>
</div>
""", unsafe_allow_html=True)

# --- TABELA BASE DE SERVIÇOS (Valores cadastrados) ---
servicos = {
    "Logotipo": {"preco": 800.0, "unidade": "peças", "label": "Logotipo — R$ 800,00"},
    "Identidade visual Completa": {"preco": 2500.0, "unidade": "peças", "label": "Identidade visual Completa — R$ 2.500,00"},
    "Cartão de visita": {"preco": 300.0, "unidade": "peças", "label": "Cartão de visita — R$ 300,00"},
    "Folder ou panfleto": {"preco": 500.0, "unidade": "peças", "label": "Folder ou panfleto — R$ 500,00"},
    "Banner para redes sociais": {"preco": 200.0, "unidade": "peças", "label": "Banner para redes sociais — R$ 200,00"},
    "E-mail marketing": {"preco": 400.0, "unidade": "peças", "label": "E-mail marketing — R$ 400,00"},
    "Apresentação corporativa": {"preco": 1200.0, "unidade": "peças", "label": "Apresentação corporativa — R$ 1.200,00"},
    "Website (design visual)": {"preco": 3000.0, "unidade": "peças", "label": "Website (design visual) — R$ 3.000,00"},
    "Manutenção e atualizações": {"preco": 100.0, "unidade": "horas", "label": "Manutenção e atualizações — R$ 100,00 / hora"},
}

# Tabela de consulta rápida expansível (estilo catálogo)
with st.expander("📋 Ver Tabela de Preços Base de Mercado"):
    st.markdown("""
    | Serviço | Preço Padrão de Mercado |
    | :--- | :--- |
    | **Logotipo** | R$ 800,00 |
    | **Identidade visual Completa** | R$ 2.500,00 |
    | **Cartão de visita** | R$ 300,00 |
    | **Folder ou panfleto** | R$ 500,00 |
    | **Banner para redes sociais** | R$ 200,00 |
    | **E-mail marketing** | R$ 400,00 |
    | **Apresentação corporativa** | R$ 1.200,00 |
    | **Website (design visual)** | R$ 3.000,00 |
    | **Manutenção e atualizações** | R$ 100,00 / hora |
    """)

st.divider()

# --- 1. ESCOLHA DO SERVIÇO ---
st.subheader("1. Escolha o serviço")

opcoes_servicos = list(servicos.keys())
nome_servico = st.selectbox(
    "Selecione o serviço que será realizado:",
    opcoes_servicos,
    index=0,  # 0 garante que "Logotipo" começa selecionado
    format_func=lambda x: servicos[x]["label"]
)

servico_info = servicos[nome_servico]
preco_base = servico_info["preco"]
is_manutencao = nome_servico == "Manutenção e atualizações"
unidade_texto = "horas" if is_manutencao else "peças"

label_qtd = (
    "Quantas horas estimadas de manutenção serão necessárias?"
    if is_manutencao
    else f"Quantas peças de '{nome_servico}' serão produzidas?"
)
quantidade = st.number_input(label_qtd, min_value=1, value=1, step=1)

# --- 2. GRAU DE EXPERIÊNCIA ---
st.subheader("2. Grau de experiência profissional")
experiencias = {
    "Iniciante / Estudante (0.6x - praticando e construindo portfólio)": 0.6,
    "Júnior (1.0x - até 2 anos de experiência, tabela base)": 1.0,
    "Pleno (1.3x - experiência sólida e entregas autônomas)": 1.3,
    "Sênior (1.6x - especialista com alto valor agregado)": 1.6,
}
opcao_exp = st.radio("Selecione seu nível:", list(experiencias.keys()), index=0)
mult_exp = experiencias[opcao_exp]
nome_exp = opcao_exp

# --- 3. ESTADO / REGIÃO (TABELA OFICIAL DETALHADA) ---
st.subheader("3. Estado de atuação ou do cliente")
estados_fatores = {
    "Acre": 0.90,
    "Alagoas": 0.91,
    "Amapá": 0.93,
    "Amazonas": 0.94,
    "Bahia": 0.93,
    "Ceará": 0.91,
    "Distrito Federal": 1.20,
    "Espírito Santo": 0.98,
    "Goiás": 1.00,
    "Maranhão": 0.85,
    "Mato Grosso": 1.00,
    "Mato Grosso do Sul": 1.03,
    "Minas Gerais": 1.00,
    "Pará": 0.92,
    "Paraíba": 0.92,
    "Paraná": 1.08,
    "Pernambuco": 0.94,
    "Piauí": 0.92,
    "Rio de Janeiro": 1.12,
    "Rio Grande do Norte": 0.96,
    "Rio Grande do Sul": 1.10,
    "Rondônia": 0.96,
    "Roraima": 0.95,
    "Santa Catarina": 1.10,
    "São Paulo": 1.15,
    "Sergipe": 0.93,
    "Tocantins": 0.97,
    "Internacional / Exterior": 1.40,
}

estado_selecionado = st.selectbox(
    "Selecione o Estado:",
    list(estados_fatores.keys()),
    index=list(estados_fatores.keys()).index("São Paulo")
)
mult_regiao = estados_fatores[estado_selecionado]
nome_regiao = f"{estado_selecionado} (Fator: {mult_regiao:.2f}x)"

# --- 4. GRAU DE COMPLEXIDADE ---
st.subheader("4. Grau de complexidade do projeto")
complexidades = {
    "Baixa (1.0x - briefing direto, materiais e referências prontos)": 1.0,
    "Média (1.2x - processo padrão com pesquisa e ajustes)": 1.2,
    "Alta (1.4x - criação do zero, muita pesquisa conceitual e refações)": 1.4,
}
opcao_comp = st.radio("Selecione a complexidade:", list(complexidades.keys()), index=1)
mult_comp = complexidades[opcao_comp]
nome_comp = opcao_comp

st.divider()

# --- 5. CÁLCULO E RESUMO DO ORÇAMENTO ---
if st.button("💰 Calcular Orçamento", type="primary", use_container_width=True):
    custo_base_total = preco_base * quantidade
    preco_estimado = custo_base_total * mult_exp * mult_regiao * mult_comp

    st.subheader("📋 Resumo do Orçamento")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Serviço Selecionado", nome_servico)
        st.metric("Volume de Entrega", f"{quantidade} {unidade_texto}")
    with col2:
        st.metric("Preço Base Unitário", f"R$ {preco_base:.2f}")

    st.write(f"**Nível de Experiência:** {nome_exp}")
    st.write(f"**Estado / Região:** {nome_regiao}")
    st.write(f"**Complexidade:** {nome_comp}")

    st.divider()
    st.success(f"### 💵 ESTIMATIVA SUGERIDA: R$ {preco_estimado:.2f}")
    st.caption("✨ Dica: Use esse valor como base técnica para apresentar a sua proposta com confiança!")
