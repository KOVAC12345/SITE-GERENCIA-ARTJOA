import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Gestão Art & Joa", page_icon="🚀", layout="wide")

# --- BANCO DE DADOS SQLite ---
def get_connection():
    conn = sqlite3.connect("gerencia.db", check_same_thread=False)
    return conn

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

# --- INTERFACE ---
st.sidebar.title("🛠️ Art & Joa Gestão")
menu = st.sidebar.radio("Navegação", ["Dashboard", "Projetos", "Tarefas", "Comissões"])

conn = get_connection()

if menu == "Dashboard":
    st.title("📊 Dashboard Geral")
    
    df_proj = pd.read_sql("SELECT * FROM projects", conn)
    df_task = pd.read_sql("SELECT * FROM tasks", conn)
    df_comm = pd.read_sql("SELECT * FROM commissions", conn)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Projetos Cadastrados", len(df_proj))
    col2.metric("Tarefas Pendentes", len(df_task[df_task['status'] != 'Concluído']) if not df_task.empty else 0)
    
    total_comm = df_comm['value'].sum() if not df_comm.empty and 'value' in df_comm.columns else 0
    col3.metric("Total em Comissões", f"R$ {total_comm:.2f}")

    st.divider()
    st.subheader("📋 Resumo Recente")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("### Tarefas Recentes")
        if not df_task.empty:
            st.dataframe(df_task.tail(5), use_container_width=True)
        else:
            st.info("Nenhuma tarefa cadastrada ainda.")
    with col_b:
        st.markdown("### Projetos Recentes")
        if not df_proj.empty:
            st.dataframe(df_proj.tail(5), use_container_width=True)
        else:
            st.info("Nenhum projeto cadastrado ainda.")

elif menu == "Projetos":
    st.title("📁 Gerenciamento de Projetos")
    
    with st.form("form_project", clear_on_submit=True):
        st.subheader("Adicionar Novo Projeto")
        p_name = st.text_input("Nome do Projeto")
        p_desc = st.text_area("Descrição")
        p_status = st.selectbox("Status", ["Planejamento", "Em Andamento", "Concluído"])
        submit_p = st.form_submit_button("Salvar Projeto")
        
        if submit_p and p_name:
            c = conn.cursor()
            c.execute("INSERT INTO projects (name, description, status) VALUES (?, ?, ?)", (p_name, p_desc, p_status))
            conn.commit()
            st.success("Projeto salvo com sucesso!")
            st.rerun()

    st.subheader("Lista de Projetos")
    df_proj = pd.read_sql("SELECT * FROM projects", conn)
    if not df_proj.empty:
        st.dataframe(df_proj, use_container_width=True)
        
        proj_to_delete = st.selectbox("Selecionar ID do projeto para excluir (opcional)", [None] + list(df_proj['id']))
        if st.button("Excluir Projeto Selecionado") and proj_to_delete:
            c = conn.cursor()
            c.execute("DELETE FROM projects WHERE id = ?", (proj_to_delete,))
            conn.commit()
            st.warning("Projeto excluído!")
            st.rerun()
    else:
        st.info("Nenhum projeto cadastrado.")

elif menu == "Tarefas":
    st.title("✅ Gerenciamento de Tarefas")
    
    df_proj = pd.read_sql("SELECT name FROM projects", conn)
    proj_list = df_proj['name'].tolist() if not df_proj.empty else ["Geral"]

    with st.form("form_task", clear_on_submit=True):
        st.subheader("Nova Tarefa")
        t_title = st.text_input("Título da Tarefa")
        t_proj = st.selectbox("Projeto Relacionado", proj_list)
        t_assignee = st.selectbox("Responsável", ["João", "Artur", "Ambos"])
        t_status = st.selectbox("Status", ["Pendente", "Em Andamento", "Concluído"])
        t_date = st.date_input("Prazo")
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
        
        task_to_delete = st.selectbox("Selecionar ID da tarefa para excluir (opcional)", [None] + list(df_task['id']))
        if st.button("Excluir Tarefa Selecionada") and task_to_delete:
            c = conn.cursor()
            c.execute("DELETE FROM tasks WHERE id = ?", (task_to_delete,))
            conn.commit()
            st.warning("Tarefa excluída!")
            st.rerun()
    else:
        st.info("Nenhuma tarefa cadastrada.")

elif menu == "Comissões":
    st.title("💰 Controle de Comissões")

    with st.form("form_comm", clear_on_submit=True):
        st.subheader("Registrar Comissão / Venda")
        c_client = st.text_input("Nome do Cliente")
        c_value = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
        c_status = st.selectbox("Status do Pagamento", ["Pendente", "Pago"])
        c_partner = st.selectbox("Responsável/Parceiro", ["João", "Artur", "Ambos"])
        submit_c = st.form_submit_button("Salvar Comissão")
        
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
        
        comm_to_delete = st.selectbox("Selecionar ID da comissão para excluir (opcional)", [None] + list(df_comm['id']))
        if st.button("Excluir Comissão Selecionada") and comm_to_delete:
            c = conn.cursor()
            c.execute("DELETE FROM commissions WHERE id = ?", (comm_to_delete,))
            conn.commit()
            st.warning("Comissão excluída!")
            st.rerun()
    else:
        st.info("Nenhuma comissão registrada.")

conn.close()
