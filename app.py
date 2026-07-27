import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Art & Joa - Gestão de Projetos",
    page_icon="⚡",
    layout="wide"
)

# --- BANCO DE DADOS SQLite ---
def get_connection():
    return sqlite3.connect("gerencia.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS projects (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    status TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    project TEXT,
                    assignee TEXT,
                    status TEXT,
                    due_date TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS commissions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    client TEXT NOT NULL,
                    value REAL,
                    status TEXT,
                    partner TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

# --- ESTILIZAÇÃO VISUAL CLEAN ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #161b22;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.title("🚀 Art & Joa")
st.sidebar.markdown("Painel de Gestão Integrado")
menu = st.sidebar.radio("Navegação", ["Dashboard", "Projetos", "Tarefas", "Comissões"])

conn = get_connection()

# --- DASHBOARD ---
if menu == "Dashboard":
    st.title("📊 Dashboard Geral")
    st.markdown("Visão geral das atividades da equipe em tempo real.")
    
    df_proj = pd.read_sql("SELECT * FROM projects", conn)
    df_task = pd.read_sql("SELECT * FROM tasks", conn)
    df_comm = pd.read_sql("SELECT * FROM commissions", conn)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projetos Totais", len(df_proj))
    col2.metric("Tarefas Pendentes", len(df_task[df_task['status'] != 'Concluído']) if not df_task.empty else 0)
    col3.metric("Tarefas Concluídas", len(df_task[df_task['status'] == 'Concluído']) if not df_task.empty else 0)
    
    total_comm = df_comm['value'].sum() if not df_comm.empty and 'value' in df_comm.columns else 0
    col4.metric("Comissões Totais", f"R$ {total_comm:,.2f}")

    st.divider()
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📌 Tarefas Recentes")
        if not df_task.empty:
            st.dataframe(df_task.tail(5), use_container_width=True)
        else:
            st.info("Nenhuma tarefa cadastrada.")
            
    with col_b:
        st.subheader("📁 Projetos Recentes")
        if not df_proj.empty:
            st.dataframe(df_proj.tail(5), use_container_width=True)
        else:
            st.info("Nenhum projeto cadastrado.")

# --- PROJETOS ---
elif menu == "Projetos":
    st.title("📁 Gerenciamento de Projetos")
    
    tab1, tab2 = st.tabs(["Visualizar / Adicionar", "Editar / Excluir"])
    
    with tab1:
        with st.form("form_project", clear_on_submit=True):
            st.subheader("Novo Projeto")
            p_name = st.text_input("Nome do Projeto")
            p_desc = st.text_area("Descrição")
            p_status = st.selectbox("Status", ["Planejamento", "Em Andamento", "Concluído"])
            submit_p = st.form_submit_button("Cadastrar Projeto")
            
            if submit_p and p_name:
                c = conn.cursor()
                c.execute("INSERT INTO projects (name, description, status) VALUES (?, ?, ?)", (p_name, p_desc, p_status))
                conn.commit()
                st.success("Projeto cadastrado com sucesso!")
                st.rerun()

        st.subheader("Lista de Projetos")
        df_proj = pd.read_sql("SELECT * FROM projects", conn)
        if not df_proj.empty:
            st.dataframe(df_proj, use_container_width=True)
        else:
            st.info("Nenhum projeto cadastrado.")

    with tab2:
        df_proj = pd.read_sql("SELECT * FROM projects", conn)
        if not df_proj.empty:
            proj_id = st.selectbox("Selecione o Projeto", df_proj['id'], format_func=lambda x: f"ID {x} - {df_proj[df_proj['id']==x]['name'].values[0]}")
            row = df_proj[df_proj['id'] == proj_id].iloc[0]
            
            with st.form("edit_proj_form"):
                new_name = st.text_input("Nome", value=row['name'])
                new_desc = st.text_area("Descrição", value=row['description'])
                statuses = ["Planejamento", "Em Andamento", "Concluído"]
                new_status = st.selectbox("Status", statuses, index=statuses.index(row['status']) if row['status'] in statuses else 0)
                
                col_e1, col_e2 = st.columns(2)
                update_btn = col_e1.form_submit_button("Salvar Alterações")
                delete_btn = col_e2.form_submit_button("Excluir Projeto")
                
                if update_btn:
                    c = conn.cursor()
                    c.execute("UPDATE projects SET name = ?, description = ?, status = ? WHERE id = ?", (new_name, new_desc, new_status, proj_id))
                    conn.commit()
                    st.success("Atualizado com sucesso!")
                    st.rerun()
                elif delete_btn:
                    c = conn.cursor()
                    c.execute("DELETE FROM projects WHERE id = ?", (proj_id,))
                    conn.commit()
                    st.warning("Projeto excluído!")
                    st.rerun()
        else:
            st.info("Nenhum projeto disponível para edição.")

# --- TAREFAS ---
elif menu == "Tarefas":
    st.title("✅ Gerenciamento de Tarefas")
    
    df_proj = pd.read_sql("SELECT name FROM projects", conn)
    proj_list = df_proj['name'].tolist() if not df_proj.empty else ["Geral"]

    tab_t1, tab_t2 = st.tabs(["Visualizar / Adicionar", "Editar / Excluir"])

    with tab_t1:
        with st.form("form_task", clear_on_submit=True):
            st.subheader("Nova Tarefa")
            t_title = st.text_input("Título da Tarefa")
            t_proj = st.selectbox("Projeto Relacionado", proj_list)
            t_assignee = st.selectbox("Responsável", ["João", "Artur", "Ambos"])
            t_status = st.selectbox("Status", ["Pendente", "Em Andamento", "Concluído"])
            t_date = st.date_input("Prazo Final")
            submit_t = st.form_submit_button("Adicionar Tarefa")
            
            if submit_t and t_title:
                c = conn.cursor()
                c.execute("INSERT INTO tasks (title, project, assignee, status, due_date) VALUES (?, ?, ?, ?, ?)", 
                          (t_title, t_proj, t_assignee, t_status, str(t_date)))
                conn.commit()
                st.success("Tarefa adicionada!")
                st.rerun()

        st.subheader("Lista de Tarefas")
        df_task = pd.read_sql("SELECT * FROM tasks", conn)
        if not df_task.empty:
            st.dataframe(df_task, use_container_width=True)
        else:
            st.info("Nenhuma tarefa cadastrada.")

    with tab_t2:
        df_task = pd.read_sql("SELECT * FROM tasks", conn)
        if not df_task.empty:
            task_id = st.selectbox("Selecione a Tarefa", df_task['id'], format_func=lambda x: f"ID {x} - {df_task[df_task['id']==x]['title'].values[0]}")
            row = df_task[df_task['id'] == task_id].iloc[0]
            
            with st.form("edit_task_form"):
                new_title = st.text_input("Título", value=row['title'])
                new_proj = st.selectbox("Projeto", proj_list, index=proj_list.index(row['project']) if row['project'] in proj_list else 0)
                
                assignees = ["João", "Artur", "Ambos"]
                new_assign = st.selectbox("Responsável", assignees, index=assignees.index(row['assignee']) if row['assignee'] in assignees else 0)
                
                statuses = ["Pendente", "Em Andamento", "Concluído"]
                new_status = st.selectbox("Status", statuses, index=statuses.index(row['status']) if row['status'] in statuses else 0)
                
                try:
                    d_val = datetime.strptime(row['due_date'], "%Y-%m-%d").date()
                except:
                    d_val = datetime.now().date()
                new_date = st.date_input("Prazo", value=d_val)
                
                col_t1, col_t2 = st.columns(2)
                up_t_btn = col_t1.form_submit_button("Salvar Alterações")
                del_t_btn = col_t2.form_submit_button("Excluir Tarefa")
                
                if up_t_btn:
                    c = conn.cursor()
                    c.execute("UPDATE tasks SET title = ?, project = ?, assignee = ?, status = ?, due_date = ? WHERE id = ?", 
                              (new_title, new_proj, new_assign, new_status, str(new_date), task_id))
                    conn.commit()
                    st.success("Tarefa atualizada!")
                    st.rerun()
                elif del_t_btn:
                    c = conn.cursor()
                    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
                    conn.commit()
                    st.warning("Tarefa excluída!")
                    st.rerun()
        else:
            st.info("Nenhuma tarefa disponível para edição.")

# --- COMISSÕES ---
elif menu == "Comissões":
    st.title("💰 Controle de Comissões")

    tab_c1, tab_c2 = st.tabs(["Visualizar / Registrar", "Editar / Excluir"])

    with tab_c1:
        with st.form("form_comm", clear_on_submit=True):
            st.subheader("Nova Comissão")
            c_client = st.text_input("Nome do Cliente")
            c_value = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
            c_status = st.selectbox("Status do Pagamento", ["Pendente", "Pago"])
            c_partner = st.selectbox("Responsável", ["João", "Artur", "Ambos"])
            submit_c = st.form_submit_button("Registrar Comissão")
            
            if submit_c and c_client:
                c = conn.cursor()
                c.execute("INSERT INTO commissions (client, value, status, partner) VALUES (?, ?, ?, ?)", 
                          (c_client, c_value, c_status, c_partner))
                conn.commit()
                st.success("Comissão registrada!")
                st.rerun()

        st.subheader("Histórico de Comissões")
        df_comm = pd.read_sql("SELECT * FROM commissions", conn)
        if not df_comm.empty:
            st.dataframe(df_comm, use_container_width=True)
        else:
            st.info("Nenhuma comissão registrada.")

    with tab_c2:
        df_comm = pd.read_sql("SELECT * FROM commissions", conn)
        if not df_comm.empty:
            comm_id = st.selectbox("Selecione a Comissão", df_comm['id'], format_func=lambda x: f"ID {x} - Cliente: {df_comm[df_comm['id']==x]['client'].values[0]}")
            row = df_comm[df_comm['id'] == comm_id].iloc[0]
            
            with st.form("edit_comm_form"):
                new_client = st.text_input("Cliente", value=row['client'])
                new_value = st.number_input("Valor (R$)", min_value=0.0, value=float(row['value']), format="%.2f")
                
                pay_st = ["Pendente", "Pago"]
                new_pay = st.selectbox("Status", pay_st, index=pay_st.index(row['status']) if row['status'] in pay_st else 0)
                
                partners = ["João", "Artur", "Ambos"]
                new_part = st.selectbox("Responsável", partners, index=partners.index(row['partner']) if row['partner'] in partners else 0)
                
                col_c1, col_c2 = st.columns(2)
                up_c_btn = col_c1.form_submit_button("Salvar Alterações")
                del_c_btn = col_c2.form_submit_button("Excluir Comissão")
                
                if up_c_btn:
                    c = conn.cursor()
                    c.execute("UPDATE commissions SET client = ?, value = ?, status = ?, partner = ? WHERE id = ?", 
                              (new_client, new_value, new_pay, new_part, comm_id))
                    conn.commit()
                    st.success("Comissão atualizada!")
                    st.rerun()
                elif del_c_btn:
                    c = conn.cursor()
                    c.execute("DELETE FROM commissions WHERE id = ?", (comm_id,))
                    conn.commit()
                    st.warning("Comissão excluída!")
                    st.rerun()
        else:
            st.info("Nenhuma comissão disponível para edição.")

conn.close()
