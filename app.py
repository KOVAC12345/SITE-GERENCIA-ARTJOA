import streamlit as st
import sqlite3
from datetime import datetime

st.set_page_config(
    page_title="Gestão de Sites - Equipe",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- BANCO DE DADOS SQLITE ---
def get_db():
    conn = sqlite3.connect("gerencia.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password TEXT NOT NULL
                )''')
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('joao', '123')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('artur', '123')")
    
    c.execute('''CREATE TABLE IF NOT EXISTS comandas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente TEXT NOT NULL,
                    valor TEXT NOT NULL,
                    status TEXT,
                    pctJoao REAL,
                    pctArtur REAL,
                    dataEntrega TEXT,
                    arquivos TEXT,
                    obs TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS arquivos_gerais (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    url TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

init_db()

# --- AUTENTICAÇÃO COM SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# --- TELA DE LOGIN ---
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### 🔐 Gestão de Equipe - Acesso Restrito")
        with st.form("form_login"):
            user_input = st.text_input("Usuário (joao ou artur)").strip().lower()
            pass_input = st.text_input("Senha", type="password").strip()
            submit_login = st.form_submit_button("Entrar", use_container_width=True)
            
            if submit_login:
                conn = get_db()
                user_row = conn.execute("SELECT * FROM users WHERE username = ?", (user_input,)).fetchone()
                conn.close()
                
                if user_row and user_row["password"] == pass_input:
                    st.session_state.logged_in = True
                    st.session_state.username = user_input
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos.")
    st.stop()

# --- PAINEL PRINCIPAL (AUTENTICADO) ---
usuario_ativo = st.session_state.username

# Cabeçalho do Painel
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.title(f"Olá, {usuario_ativo.upper()}")
    st.caption("Painel de Controle e Gestão de Projetos")
with header_col2:
    if st.button("🚪 Sair", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

st.divider()

# Carregar dados do banco
conn = get_db()
comandas = [dict(row) for row in conn.execute("SELECT * FROM comandas").fetchall()]
arquivos = [dict(row) for row in conn.execute("SELECT * FROM arquivos_gerais").fetchall()]
conn.close()

# Calcular Resumos
faturamento_total = 0.0
total_joao = 0.0
total_artur = 0.0

for c in comandas:
    val_str = str(c["valor"]).replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
    val_limpo = float(val_str) if val_str else 0.0
    p_joao = c["pctJoao"] if c["pctJoao"] is not None else 50.0
    p_artur = c["pctArtur"] if c["pctArtur"] is not None else 50.0

    faturamento_total += val_limpo
    total_joao += val_limpo * (p_joao / 100.0)
    total_artur += val_limpo * (p_artur / 100.0)

# Indicadores Gerais (Métricas)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Faturamento Total", f"R$ {faturamento_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
m2.metric("Total a Receber (João)", f"R$ {total_joao:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
m3.metric("Total a Receber (Artur)", f"R$ {total_artur:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
m4.metric("Total de Projetos", len(comandas))

st.markdown("<br>", unsafe_allow_html=True)

# Abas do Painel
tab_comandas, tab_arquivos, tab_perfil = st.tabs(["📋 Comanda de Sites", "📂 Repositório de Arquivos", "⚙️ Meu Perfil"])

with tab_comandas:
    st.subheader("Adicionar / Atualizar Projeto")
    
    if "edit_id" not in st.session_state:
        st.session_state.edit_id = None
        st.session_state.edit_cliente = ""
        st.session_state.edit_valor = ""
        st.session_state.edit_status = "Em Andamento"
        st.session_state.edit_pct_joao = 50.0
        st.session_state.edit_pct_artur = 50.0
        st.session_state.edit_data = ""
        st.session_state.edit_arquivos = ""
        st.session_state.edit_obs = ""

    with st.form("form_comanda"):
        col_c1, col_c2, col_c3, col_c4, col_c5 = st.columns([2, 1, 1, 1, 1])
        
        with col_c1:
            cli = st.text_input("Cliente / Projeto", value=st.session_state.edit_cliente)
        with col_c2:
            val = st.text_input("Valor (R$)", value=st.session_state.edit_valor, placeholder="Ex: 1500,00")
        with col_c3:
            status_opts = ["Em Andamento", "Pronto", "Concluído"]
            idx_status = status_opts.index(st.session_state.edit_status) if st.session_state.edit_status in status_opts else 0
            stat = st.selectbox("Status", status_opts, index=idx_status)
        with col_c4:
            p_j = st.number_input("% do João", min_value=0.0, max_value=100.0, value=float(st.session_state.edit_pct_joao))
        with col_c5:
            p_a = st.number_input("% do Artur", min_value=0.0, max_value=100.0, value=float(st.session_state.edit_pct_artur))
            
        col_c6, col_c7 = st.columns(2)
        with col_c6:
            try:
                default_date = datetime.strptime(st.session_state.edit_data, "%Y-%m-%d").date() if st.session_state.edit_data else datetime.today().date()
            except:
                default_date = datetime.today().date()
            dt_entrega = st.date_input("Data de Entrega", value=default_date)
        with col_c7:
            arq_link = st.text_input("Links ou Arquivos", value=st.session_state.edit_arquivos, placeholder="GitHub, Drive...")
            
        obs_text = st.text_area("Observações", value=st.session_state.edit_obs, placeholder="Detalhes ou pendências")
        
        btn_label = "Atualizar Projeto" if st.session_state.edit_id else "Salvar na Comanda"
        submitted = st.form_submit_button(btn_label, use_container_width=True)
        
        if submitted:
            if not cli or not val:
                st.error("Preencha o cliente e o valor.")
            else:
                conn = get_db()
                c_cursor = conn.cursor()
                dt_str = dt_entrega.strftime("%Y-%m-%d")
                if st.session_state.edit_id:
                    c_cursor.execute("""UPDATE comandas SET cliente=?, valor=?, status=?, pctJoao=?, pctArtur=?, dataEntrega=?, arquivos=?, obs=? WHERE id=?""",
                                     (cli, val, stat, p_j, p_a, dt_str, arq_link, obs_text, st.session_state.edit_id))
                    st.success("Projeto atualizado com sucesso!")
                else:
                    c_cursor.execute("""INSERT INTO comandas (cliente, valor, status, pctJoao, pctArtur, dataEntrega, arquivos, obs) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                                     (cli, val, stat, p_j, p_a, dt_str, arq_link, obs_text))
                    st.success("Projeto salvo com sucesso!")
                conn.commit()
                conn.close()
                st.session_state.edit_id = None
                st.session_state.edit_cliente = ""
                st.session_state.edit_valor = ""
                st.session_state.edit_status = "Em Andamento"
                st.session_state.edit_pct_joao = 50.0
                st.session_state.edit_pct_artur = 50.0
                st.session_state.edit_data = ""
                st.session_state.edit_arquivos = ""
                st.session_state.edit_obs = ""
                st.rerun()

    if st.session_state.edit_id:
        if st.button("❌ Cancelar Edição"):
            st.session_state.edit_id = None
            st.session_state.edit_cliente = ""
            st.session_state.edit_valor = ""
            st.session_state.edit_status = "Em Andamento"
            st.session_state.edit_pct_joao = 50.0
            st.session_state.edit_pct_artur = 50.0
            st.session_state.edit_data = ""
            st.session_state.edit_arquivos = ""
            st.session_state.edit_obs = ""
            st.rerun()

    st.divider()
    st.subheader("Trabalhos Atuais")
    
    pesquisa = st.text_input("🔍 Pesquisar projeto...", placeholder="Digite o nome do cliente ou observação")
    
    comandas_filtradas = [
        c for c in comandas 
        if pesquisa.lower() in c["cliente"].lower() or (c["obs"] and pesquisa.lower() in c["obs"].lower())
    ] if pesquisa else comandas

    if not comandas_filtradas:
        st.info("Nenhum projeto encontrado.")
    else:
        for c in comandas_filtradas:
            with st.container(border=True):
                col_t1, col_t2, col_t3, col_t4, col_t5 = st.columns([2, 1, 1.2, 1, 1])
                with col_t1:
                    st.markdown(f"**{c['cliente']}**")
                    if c["obs"]:
                        st.caption(f"Obs: {c['obs']}")
                with col_t2:
                    st.text(f"R$ {c['valor']}")
                with col_t3:
                    pj = c['pctJoao'] if c['pctJoao'] is not None else 50
                    pa = c['pctArtur'] if c['pctArtur'] is not None else 50
                    st.markdown(f"João: {pj}% | Artur: {pa}%")
                with col_t4:
                    st.markdown(f"Status: **{c['status']}**")
                    if c['dataEntrega']:
                        dt_fmt = '-'.join(c['dataEntrega'].split('-')[::-1])
                        st.caption(f"Entrega: {dt_fmt}")
                with col_t5:
                    if c['arquivos']:
                        st.markdown(f"[🔗 Acessar]({c['arquivos']})")
                    
                    col_btn1, col_btn2 = st.columns(2)
                    with col_btn1:
                        if st.button("✏️", key=f"edit_{c['id']}"):
                            st.session_state.edit_id = c['id']
                            st.session_state.edit_cliente = c['cliente']
                            st.session_state.edit_valor = str(c['valor'])
                            st.session_state.edit_status = c['status']
                            st.session_state.edit_pct_joao = c['pctJoao'] if c['pctJoao'] is not None else 50.0
                            st.session_state.edit_pct_artur = c['pctArtur'] if c['pctArtur'] is not None else 50.0
                            st.session_state.edit_data = c['dataEntrega'] or ""
                            st.session_state.edit_arquivos = c['arquivos'] or ""
                            st.session_state.edit_obs = c['obs'] or ""
                            st.rerun()
                    with col_btn2:
                        if st.button("🗑️", key=f"del_{c['id']}"):
                            conn = get_db()
                            conn.execute("DELETE FROM comandas WHERE id = ?", (c['id'],))
                            conn.commit()
                            conn.close()
                            st.success("Projeto excluído!")
                            st.rerun()

with tab_arquivos:
    st.subheader("Repositório de Arquivos Gerais")
    with st.form("form_arquivo"):
        arq_titulo = st.text_input("Título do Arquivo/Link", placeholder="Ex: Logos e Assets")
        arq_url = st.text_input("URL / Link", placeholder="https://...")
        sub_arq = st.form_submit_button("Adicionar ao Repositório", use_container_width=True)
        
        if sub_arq:
            if not arq_titulo or not arq_url:
                st.error("Preencha o título e o link.")
            else:
                conn = get_db()
                conn.execute("INSERT INTO arquivos_gerais (titulo, url) VALUES (?, ?)", (arq_titulo, arq_url))
                conn.commit()
                conn.close()
                st.success("Arquivo adicionado com sucesso!")
                st.rerun()

    st.divider()
    st.subheader("Arquivos da Equipe")
    if not arquivos:
        st.info("Nenhum arquivo cadastrado.")
    else:
        for a in arquivos:
            col_a1, col_a2, col_a3 = st.columns([2, 3, 1])
            with col_a1:
                st.markdown(f"**{a['titulo']}**")
            with col_a2:
                st.markdown(f"[🔗 {a['url']}]({a['url']})")
            with col_a3:
                if st.button("Excluir", key=f"del_arq_{a['id']}"):
                    conn = get_db()
                    conn.execute("DELETE FROM arquivos_gerais WHERE id = ?", (a['id'],))
                    conn.commit()
                    conn.close()
                    st.success("Arquivo excluído!")
                    st.rerun()

with tab_perfil:
    st.subheader("Configurações de Perfil")
    st.write(f"Usuário Conectado: **{usuario_ativo.upper()}**")
    
    with st.form("form_senha"):
        nova_senha = st.text_input("Nova Senha", type="password")
        sub_senha = st.form_submit_button("Atualizar Senha")
        
        if sub_senha:
            if not nova_senha:
                st.error("Digite a nova senha.")
            else:
                conn = get_db()
                conn.execute("UPDATE users SET password = ? WHERE username = ?", (nova_senha, usuario_ativo))
                conn.commit()
                conn.close()
                st.success("Senha atualizada com sucesso!")
                st.rerun()
