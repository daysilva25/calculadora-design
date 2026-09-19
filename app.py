
import streamlit as st

# ==============================================================================
# CALCULADORA DE PREÇOS PARA DESIGN GRÁFICO
# Criada e idealizada por Daiane (Estudante de Design & Programação)
# ==============================================================================

st.set_page_config(
    page_title="DesignPrice • Calculadora para Designers",
    page_icon="✒️",
    layout="centered"
)

# --- TEORIA DAS CORES E HARMONIA VISUAL ---
st.markdown("""
<style>
    /* Tipografia e Títulos com Roxo Vibrante */
    h1, h2, h3 {
        color: #C084FC !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        letter-spacing: -0.5px;
    }
    
    /* Botão Principal com Degradê Roxo Criativo e Efeito Hover */
    .stButton>button {
        background: linear-gradient(135deg, #8B5CF6 0%, #6D28D9 100%) !important;
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.75rem 2rem !important;
        box-shadow: 0 4px 20px 0 rgba(139, 92, 246, 0.45) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) scale(1.01) !important;
        box-shadow: 0 8px 25px 0 rgba(139, 92, 246, 0.6) !important;
        background: linear-gradient(135deg, #A855F7 0%, #7C3AED 100%) !important;
    }

    /* Card de Apresentação da Autora (Glassmorphism / Roxo Translúcido) */
    .apresentacao-card {
        background: linear-gradient(145deg, rgba(124, 58, 237, 0.18) 0%, rgba(76, 29, 149, 0.25) 100%) !important;
        border: 1px solid rgba(168, 85, 247, 0.35) !important;
        border-left: 6px solid #A855F7 !important;
        color: #F5F3FF !important;
        padding: 1.4rem !important;
        border-radius: 12px !important;
        margin-bottom: 1.5rem !important;
        line-height: 1.65 !important;
        backdrop-filter: blur(10px);
    }
    
    .apresentacao-card b, .apresentacao-card strong {
        color: #FFFFFF !important;
    }
    
    .destaque-dourado {
        color: #FBBF24 !important;
        font-weight: 600;
    }

    /* Ajuste de Métricas */
    [data-testid="stMetricValue"] {
        color: #E9D5FF !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #C084FC !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- CABEÇALHO DO APP ---
st.title("🎨 Calculadora de Preços para Designers")
st.caption("✨ Desenvolvido por Daiane | Design Gráfico & Programação")

st.markdown("""
<div class="apresentacao-card">
    <b>Olá! Meu nome é Daiane, sou estudante de Design e Programação.</b><br><br>
    Desenvolvi esta ferramenta para auxiliar designers — especialmente quem está no início da jornada — a precificar seus trabalhos com mais segurança, técnica e autonomia.<br><br>
    O sistema utiliza valores médios de mercado e cruza essas informações com o seu <span class="destaque-dourado">nível de experiência</span>, o <span class="destaque-dourado">mercado regional</span> e o <span class="destaque-dourado">grau de complexidade</span> de cada projeto.<br><br>
    💡 <i><b>Importante:</b> esta ferramenta serve como um guia de apoio e orientação, e não como uma regra engessada. Sinta-se à vontade para adaptar os valores à sua realidade!</i>
</div>
""", unsafe_allow_html=True)

# --- TABELA BASE DE SERVIÇOS DO DESIGN (COM ÍCONES ESPECÍFICOS) ---
servicos = {
    "Logotipo": {"preco": 800.0, "unidade": "peças", "label": "✒️ Logotipo — R$ 800,00 (Identidade Essencial)"},
    "Identidade visual Completa": {"preco": 2500.0, "unidade": "peças", "label": "💎 Identidade Visual Completa — R$ 2.500,00 (Manual, Paleta, Tipografia)"},
    "Cartão de visita": {"preco": 300.0, "unidade": "peças", "label": "💳 Cartão de Visita — R$ 300,00 (Papelaria Frente e Verso)"},
    "Folder ou panfleto": {"preco": 500.0, "unidade": "peças", "label": "📜 Folder ou Panfleto — R$ 500,00 (Editorial / Impresso A4)"},
    "Banner para redes sociais": {"preco": 200.0, "unidade": "peças", "label": "📱 Banner para Redes Sociais — R$ 200,00 (Social Media / Feed e Stories)"},
    "E-mail marketing": {"preco": 400.0, "unidade": "peças", "label": "📧 E-mail Marketing — R$ 400,00 (Layout promocional ou newsletter)"},
    "Apresentação corporativa": {"preco": 1200.0, "unidade": "peças", "label": "📊 Apresentação Corporativa — R$ 1.200,00 (Deck / Slides Comerciais)"},
    "Website (design visual)": {"preco": 3000.0, "unidade": "peças", "label": "🌐 Website UI/UX — R$ 3.000,00 (Design Visual de até 5 telas)"},
    "Manutenção e atualizações": {"preco": 100.0, "unidade": "horas", "label": "🛠️ Manutenção e Ajustes Finos — R$ 100,00 / hora"},
}

# Tabela expansível no formato de cardápio criativo
with st.expander("📋 Ver Tabela de Preços de Referência"):
    st.markdown("""
    | Serviço Criativo | Unidade | Preço Base de Mercado |
    | :--- | :--- | :--- |
    | ✒️ **Logotipo Personalizado** | Por projeto | R$ 800,00 |
    | 💎 **Identidade Visual Completa** | Por projeto | R$ 2.500,00 |
    | 💳 **Cartão de Visita** | Por arte | R$ 300,00 |
    | 📜 **Folder ou Panfleto** | Por arte | R$ 500,00 |
    | 📱 **Banner para Redes Sociais** | Por peça | R$ 200,00 |
    | 📧 **E-mail Marketing** | Por disparo/layout | R$ 400,00 |
    | 📊 **Apresentação Corporativa** | Por deck completo | R$ 1.200,00 |
    | 🌐 **Website (Design Visual UI)** | Até 5 páginas | R$ 3.000,00 |
    | 🛠️ **Manutenção e Ajustes** | Por hora gasta | R$ 100,00 / hora |
    """)

st.divider()

# --- 1. ESCOLHA DO SERVIÇO ---
st.subheader("✒️ 1. Qual serviço criativo você vai realizar?")

opcoes_servicos = list(servicos.keys())
nome_servico = st.selectbox(
    "Selecione o serviço:",
    opcoes_servicos,
    index=0,
    format_func=lambda x: servicos[x]["label"]
)

servico_info = servicos[nome_servico]
preco_base = servico_info["preco"]
is_manutencao = nome_servico == "Manutenção e atualizações"
unidade_texto = "horas" if is_manutencao else "peças"

label_qtd = (
    "⏳ Quantas horas estimadas de ajustes serão necessárias?"
    if is_manutencao
    else f"🖼️ Quantas peças de '{nome_servico}' serão entregues?"
)
quantidade = st.number_input(label_qtd, min_value=1, value=1, step=1)

# --- 2. GRAU DE EXPERIÊNCIA DO DESIGNER ---
st.subheader("🎯 2. Qual é o seu nível de senioridade?")
experiencias = {
    "🌱 Iniciante / Estudante (0.6x - praticando e construindo portfólio)": 0.6,
    "🌿 Júnior (1.0x - até 2 anos de prática, preço base de tabela)": 1.0,
    "🌳 Pleno (1.3x - experiência sólida e entregas autônomas)": 1.3,
    "⭐ Sênior (1.6x - especialista com direção de arte e alto valor)": 1.6,
}
opcao_exp = st.radio("Selecione seu momento profissional:", list(experiencias.keys()), index=0)
mult_exp = experiencias[opcao_exp]
nome_exp = opcao_exp

# --- 3. ESTADO / MERCADO REGIONAL ---
st.subheader("📍 3. Estado de atuação ou do cliente")
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
    "🌎 Internacional / Clientes no Exterior": 1.40,
}

estado_selecionado = st.selectbox(
    "Selecione a região/estado de referência:",
    list(estados_fatores.keys()),
    index=list(estados_fatores.keys()).index("São Paulo")
)
mult_regiao = estados_fatores[estado_selecionado]
nome_regiao = f"{estado_selecionado} (Fator: {mult_regiao:.2f}x)"

# --- 4. GRAU DE COMPLEXIDADE DO PROJETO ---
st.subheader("⚡ 4. Qual o grau de complexidade criativa?")
complexidades = {
    "🟢 Baixa (1.0x - briefing direto, identidade e materiais prontos)": 1.0,
    "🟡 Média (1.2x - processo padrão com pesquisa de referências e revisões)": 1.2,
    "🔴 Alta (1.4x - criação conceitual do zero, muita pesquisa e refações)": 1.4,
}
opcao_comp = st.radio("Selecione o nível de esforço criativo:", list(complexidades.keys()), index=1)
mult_comp = complexidades[opcao_comp]
nome_comp = opcao_comp

st.divider()

# --- 5. CÁLCULO E PROPOSTA FINAL ---
if st.button("💎 Gerar Proposta de Orçamento", type="primary", use_container_width=True):
    custo_base_total = preco_base * quantidade
    preco_estimado = custo_base_total * mult_exp * mult_regiao * mult_comp

    st.subheader("📋 Resumo Técnico da Proposta")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Serviço Criativo", nome_servico)
        st.metric("Volume de Entrega", f"{quantidade} {unidade_texto}")
    with col2:
        st.metric("Preço Base de Tabela", f"R$ {preco_base:.2f}")

    st.write(f"**Senioridade:** {nome_exp}")
    st.write(f"**Mercado Regional:** {nome_regiao}")
    st.write(f"**Complexidade Criativa:** {nome_comp}")

    st.divider()
    st.success(f"### 💵 ESTIMATIVA SUGERIDA: R$ {preco_estimado:.2f}")
    st.caption("✨ Dica de Designer: Apresente esse valor destacando o valor agregado e o tempo dedicado ao projeto!")
