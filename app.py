import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gestão de Sites - Equipe",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove cabeçalhos, rodapés, bordas e trava a rolagem externa para ficar uma barra única
st.markdown("""
    <style>
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {visibility: hidden !important;}
        footer {display: none !important;}
        .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100% !important;
            overflow: hidden !important;
        }
        iframe {
            width: 100% !important;
            height: 100vh !important;
            border: none !important;
        }
        html, body, [data-testid="stAppViewContainer"] {
            overflow: hidden !important;
            height: 100vh !important;
            background-color: #05050a;
        }
    </style>
""", unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestão de Sites & Comandas</title>
    <style>
        :root {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --accent: #ec4899;
            --success: #10b981;
            --danger: #ef4444;
            --warning: #f59e0b;
            --bg: #05050a;
            --card-bg: #111827;
            --text: #f9fafb;
            --gray: #9ca3af;
            --border: #1f2937;
            --shadow: 0 10.5px 25px -5px rgba(0, 0, 0, 0.5);
        }

        [data-theme="light"] {
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --accent: #ec4899;
            --success: #10b981;
            --danger: #ef4444;
            --warning: #f59e0b;
            --bg: #f1f5f9;
            --card-bg: #ffffff;
            --text: #0f172a;
            --gray: #64748b;
            --border: #e2e8f0;
            --shadow: 0 10.5px 25px -5px rgba(99, 102, 241, 0.07);
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            padding: 30px 20px;
            box-sizing: border-box;
            transition: background 0.3s, color 0.3s;
        }

        .container {
            width: 100%;
            max-width: 440px;
            padding: 20px;
            box-sizing: border-box;
            margin-top: 40px;
        }

        .card {
            background: var(--card-bg);
            padding: 35px;
            border-radius: 24px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
            backdrop-filter: blur(10px);
        }

        h2 {
            margin-top: 0;
            color: var(--text);
            font-size: 1.8rem;
            text-align: center;
            font-weight: 800;
            letter-spacing: -0.5px;
        }

        p.subtitle {
            text-align: center;
            color: var(--gray);
            font-size: 0.9rem;
            margin-top: 4px;
            margin-bottom: 25px;
        }

        label {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--gray);
            display: block;
            margin-top: 14px;
        }

        input, select, textarea {
            width: 100%;
            padding: 12px 14px;
            margin-top: 6px;
            border-radius: 12px;
            border: 1px solid var(--border);
            box-sizing: border-box;
            font-size: 0.95rem;
            background: var(--bg);
            color: var(--text);
            transition: all 0.2s;
        }

        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
        }

        button {
            width: 100%;
            padding: 13px;
            margin-top: 22px;
            border-radius: 12px;
            border: none;
            background: linear-gradient(135deg, var(--primary), var(--primary-hover));
            color: white;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.1s, opacity 0.2s;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }

        button:hover { opacity: 0.9; transform: translateY(-1px); }
        button:active { transform: translateY(0); }

        .link-text {
            text-align: center;
            margin-top: 16px;
            font-size: 0.85rem;
            color: var(--primary);
            cursor: pointer;
            font-weight: 600;
        }
        .link-text:hover { text-decoration: underline; }

        #painel-app {
            display: none;
            max-width: 1300px;
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
            margin: 0 auto;
        }

        .dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            background: var(--card-bg);
            padding: 18px 24px;
            border-radius: 16px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }

        .painel-secao {
            background: var(--card-bg);
            padding: 28px;
            border-radius: 16px;
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }

        .grid-resumo {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin-bottom: 24px;
        }

        .box-info {
            background: var(--card-bg);
            padding: 20px;
            border-radius: 16px;
            text-align: center;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            position: relative;
            overflow: hidden;
        }
        .box-info::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--accent));
        }
        .box-info span { font-size: 0.78rem; color: var(--gray); display: block; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; }
        .box-info h3 { margin: 8px 0 4px 0; font-size: 1.5rem; font-weight: 800; }
        .box-info p { margin: 0; font-size: 0.8rem; color: var(--gray); }

        .sub-abas {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
        }
        .btn-sub-aba {
            flex: 1;
            padding: 12px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 12px;
            font-weight: 700;
            margin: 0;
            cursor: pointer;
            font-size: 0.9rem;
            box-shadow: none;
        }
        .btn-sub-aba.ativa {
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }

        table.tabela-gestao {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
            margin-top: 12px;
        }
        table.tabela-gestao th, table.tabela-gestao td {
            padding: 14px 12px;
            border-bottom: 1px solid var(--border);
            text-align: left;
        }
        table.tabela-gestao th {
            color: var(--gray);
            font-weight: 700;
            font-size: 0.8rem;
            text-transform: uppercase;
        }

        .btn-acao {
            background: none;
            border: none;
            cursor: pointer;
            font-weight: 600;
            padding: 6px 10px;
            border-radius: 8px;
            font-size: 0.82rem;
            margin-right: 6px;
            width: auto;
            box-shadow: none;
        }
        .btn-excluir { color: var(--danger); background: rgba(239, 68, 68, 0.1); }
        .btn-excluir:hover { background: rgba(239, 68, 68, 0.2); transform: none; }
        .btn-editar { color: var(--primary); background: rgba(99, 102, 241, 0.1); }
        .btn-editar:hover { background: rgba(99, 102, 241, 0.2); transform: none; }

        .badge {
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            display: inline-block;
        }
        .badge-fase { background: rgba(99, 102, 241, 0.15); color: var(--primary); }
    </style>
</head>
<body>

    <!-- TELA DE LOGIN -->
    <div class="container" id="tela-login">
        <div class="card">
            <h2>Gestão da Equipe</h2>
            <p class="subtitle">Acesso restrito (Joao & Artur)</p>
            
            <div id="form-login-bloco">
                <label>Usuário:</label>
                <input type="text" id="login-usuario" placeholder="joao ou artur">
                
                <label>Senha:</label>
                <input type="password" id="login-senha" placeholder="******">
                
                <button onclick="fazerLogin()">Entrar no Sistema</button>
                <div class="link-text" onclick="mostrarEsqueceuSenha(true)">Esqueceu / Redefinir Senha?</div>
            </div>

            <!-- TELA DE REDEFINIR SENHA -->
            <div id="form-reset-bloco" style="display: none;">
                <label>Qual usuário deseja alterar?</label>
                <select id="reset-usuario">
                    <option value="joao">João</option>
                    <option value="artur">Artur</option>
                </select>

                <label>Nova Senha:</label>
                <input type="password" id="reset-nova-senha" placeholder="Digite a nova senha">

                <button onclick="salvarNovaSenha()">Salvar Nova Senha</button>
                <div class="link-text" onclick="mostrarEsqueceuSenha(false)">Voltar para o Login</div>
            </div>
        </div>
    </div>

    <!-- PAINEL PRINCIPAL -->
    <div id="painel-app">
        <div class="dashboard-header">
            <div style="display: flex; align-items: center; gap: 14px;">
                <div>
                    <h2 id="saudacao-usuario" style="margin: 0; font-size: 1.2rem; text-align: left;">Olá</h2>
                    <span style="font-size: 0.8rem; color: var(--gray);">Central de Controle de Sites & Comandas</span>
                </div>
            </div>
            <div>
                <button onclick="alternarTema()" class="btn-acao" style="background: var(--bg); border: 1px solid var(--border); color: var(--text); padding: 8px 14px; margin:0;">Tema</button>
                <button onclick="fazerLogout()" class="btn-acao btn-excluir" style="padding: 8px 14px; margin-left: 8px;">Sair</button>
            </div>
        </div>

        <!-- INDICADORES GERAIS E PORCENTAGEM DA EQUIPE -->
        <div class="grid-resumo">
            <div class="box-info">
                <span>Faturamento Total</span>
                <h3 id="res-faturamento" style="color: var(--success);">R$ 0,00</h3>
                <p>Total gerido em projetos</p>
            </div>
            <div class="box-info">
                <span>Total Joao (Comissões)</span>
                <h3 id="res-total-joao" style="color: var(--primary);">R$ 0,00</h3>
                <p>Soma das porcentagens</p>
            </div>
            <div class="box-info">
                <span>Total Artur (Comissões)</span>
                <h3 id="res-total-artur" style="color: var(--accent);">R$ 0,00</h3>
                <p>Soma das porcentagens</p>
            </div>
            <div class="box-info">
                <span>Repositório de Arquivos</span>
                <h3 id="res-total-arquivos" style="color: var(--warning);">0</h3>
                <p>Links e arquivos salvos</p>
            </div>
        </div>

        <div class="painel-secao">
            <div class="sub-abas">
                <button class="btn-sub-aba ativa" onclick="mudarAba('comandas')" id="tab-comandas">Comanda de Sites</button>
                <button class="btn-sub-aba" onclick="mudarAba('arquivos')" id="tab-arquivos">Repositório de Arquivos</button>
                <button class="btn-sub-aba" onclick="mudarAba('perfil')" id="tab-perfil">Configuração de Perfil</button>
            </div>

            <!-- ABA COMANDAS -->
            <div id="secao-comandas">
                <div style="background: var(--bg); padding: 20px; border-radius: 16px; margin-bottom: 24px; border: 1px solid var(--border);">
                    <h3 style="margin-top: 0; font-size: 1rem;">Adicionar / Atualizar Site na Comanda</h3>
                    <input type="hidden" id="comanda-id-editando">
                    <div style="display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 12px;">
                        <div>
                            <label>Nome do Cliente / Projeto:</label>
                            <input type="text" id="cmd-cliente" placeholder="Ex: Imobiliária Furtado">
                        </div>
                        <div>
                            <label>Valor Cobrado (R$):</label>
                            <input type="text" id="cmd-valor" placeholder="1500,00">
                        </div>
                        <div>
                            <label>Fase / Status:</label>
                            <select id="cmd-status">
                                <option value="Criação de Design">Criação de Design</option>
                                <option value="Desenvolvimento de Design">Desenvolvimento de Design</option>
                                <option value="Funcionamento de Funções">Funcionamento de Funções</option>
                                <option value="Polimento">Polimento</option>
                                <option value="Hospedagem">Hospedagem</option>
                                <option value="Entrega">Entrega</option>
                            </select>
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px;">
                        <div>
                            <label>Porcentagem Joao (%):</label>
                            <input type="number" id="cmd-pct-joao" value="50" min="0" max="100" oninput="sincronizarPorcentagens('joao')">
                        </div>
                        <div>
                            <label>Porcentagem Artur (%):</label>
                            <input type="number" id="cmd-pct-artur" value="50" min="0" max="100" oninput="sincronizarPorcentagens('artur')">
                        </div>
                    </div>
                    <div style="margin-top: 12px;">
                        <label>Links ou Arquivos do Site (GitHub, Drive, Hospedagem):</label>
                        <input type="text" id="cmd-arquivos" placeholder="https://github.com/exemplo/site">
                    </div>
                    <div style="margin-top: 12px;">
                        <label>Observações / Tarefas:</label>
                        <textarea id="cmd-obs" placeholder="Detalhes do projeto, pendências..." rows="2"></textarea>
                    </div>
                    <button onclick="salvarComanda()" style="margin-top: 16px;">Salvar na Comanda</button>
                </div>

                <h3 style="font-size: 1.1rem; margin-bottom: 12px;">Trabalhos Atuais</h3>
                <div style="overflow-x: auto;">
                    <table class="tabela-gestao">
                        <thead>
                            <tr>
                                <th>Projeto / Cliente</th>
                                <th>Valor</th>
                                <th>Divisão (Joao / Artur)</th>
                                <th>Fase / Status</th>
                                <th>Arquivos / Links</th>
                                <th>Observações</th>
                                <th style="text-align: right;">Ações</th>
                            </tr>
                        </thead>
                        <tbody id="tabela-comandas-corpo">
                            <tr><td colspan="7" style="text-align: center; color: var(--gray);">Carregando dados da nuvem...</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- ABA ARQUIVOS GERAIS -->
            <div id="secao-arquivos" style="display: none;">
                <div style="background: var(--bg); padding: 20px; border-radius: 16px; margin-bottom: 24px; border: 1px solid var(--border);">
                    <h3 style="margin-top: 0; font-size: 1rem;">Adicionar Link ou Arquivo Geral da Equipe</h3>
                    <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 12px;">
                        <div>
                            <label>Título do Arquivo/Recurso:</label>
                            <input type="text" id="arq-titulo" placeholder="Ex: Logos / Layout Base">
                        </div>
                        <div>
                            <label>Link de Acesso (Drive, GitHub, Figma):</label>
                            <input type="text" id="arq-url" placeholder="https://...">
                        </div>
                    </div>
                    <button onclick="salvarArquivoGeral()" style="margin-top: 16px;">Adicionar ao Repositório</button>
                </div>

                <h3 style="font-size: 1.1rem; margin-bottom: 12px;">Repositório Geral</h3>
                <div style="overflow-x: auto;">
                    <table class="tabela-gestao">
                        <thead>
                            <tr>
                                <th>Título</th>
                                <th>Link de Acesso</th>
                                <th style="text-align: right;">Ações</th>
                            </tr>
                        </thead>
                        <tbody id="tabela-arquivos-corpo">
                            <tr><td colspan="3" style="text-align: center; color: var(--gray);">Nenhum arquivo cadastrado.</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- ABA PERFIL -->
            <div id="secao-perfil" style="display: none;">
                <div style="background: var(--bg); padding: 20px; border-radius: 16px; max-width: 500px; margin: 0 auto; border: 1px solid var(--border);">
                    <h3 style="margin-top: 0; font-size: 1.1rem;">Configuração de Perfil e Acesso</h3>
                    <p style="font-size: 0.85rem; color: var(--gray);">Altere seu nome de usuário ou senha de acesso ao sistema.</p>
                    
                    <label>Usuário Atual:</label>
                    <select id="perfil-usuario-selecionado" onchange="carregarDadosPerfil()">
                        <option value="joao">João</option>
                        <option value="artur">Artur</option>
                    </select>

                    <label>Novo Nome de Usuário:</label>
                    <input type="text" id="perfil-novo-usuario" placeholder="Digite o novo nome de usuário">

                    <label>Nova Senha:</label>
                    <input type="password" id="perfil-nova-senha" placeholder="Digite a nova senha">

                    <button onclick="salvarConfigPerfil()" style="margin-top: 20px;">Salvar Alterações</button>
                </div>
            </div>
        </div>
    </div>

    <!-- FIREBASE INTEGRATION -->
    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
        import { getDatabase, ref, set, get, onValue, remove } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";

        const firebaseConfig = {
            apiKey: "AIzaSyAb2gk6d1nsQ8B8x426k4FMH277J9Z6J5Q",
            authDomain: "gestao-sites-equipe.firebaseapp.com",
            databaseURL: "https://gestao-sites-equipe-default-rtdb.firebaseio.com",
            projectId: "gestao-sites-equipe",
            storageBucket: "gestao-sites-equipe.firebasestorage.app",
            messagingSenderId: "639078202731",
            appId: "1:639078202731:web:eba777dfff6215f6b2602e",
            measurementId: "G-3DW3RB7265"
        };

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        window.db = db;
        window.dbRef = ref;
        window.dbSet = set;
        window.dbGet = get;
        window.dbOnValue = onValue;
        window.dbRemove = remove;

        window.iniciarListenersFirebase();
    </script>

    <script>
        let globalComandas = [];
        let globalArquivos = [];
        let globalUsers = { "joao": "123", "artur": "123" };

        window.iniciarListenersFirebase = function() {
            // Sincronizar Usuários
            window.dbOnValue(window.dbRef(window.db, 'users'), (snapshot) => {
                if (snapshot.exists()) {
                    globalUsers = snapshot.val();
                } else {
                    window.dbSet(window.dbRef(window.db, 'users'), { "joao": "123", "artur": "123" });
                }
            });

            // Sincronizar Comandas em Tempo Real
            window.dbOnValue(window.dbRef(window.db, 'comandas'), (snapshot) => {
                const data = snapshot.val();
                globalComandas = data ? Object.values(data) : [];
                atualizarDados();
            });

            // Sincronizar Arquivos em Tempo Real
            window.dbOnValue(window.dbRef(window.db, 'arquivos_gerais'), (snapshot) => {
                const data = snapshot.val();
                globalArquivos = data ? Object.values(data) : [];
                atualizarDados();
            });
        }

        function fazerLogin() {
            const user = document.getElementById('login-usuario').value.trim().toLowerCase();
            const pass = document.getElementById('login-senha').value.trim();

            if (globalUsers[user] && globalUsers[user] === pass) {
                localStorage.setItem('gp_logado', 'true');
                localStorage.setItem('gp_usuario', user);
                carregarApp();
            } else {
                alert("Usuário ou senha incorretos!");
            }
        }

        function mostrarEsqueceuSenha(mostrar) {
            document.getElementById('form-login-bloco').style.display = mostrar ? 'none' : 'block';
            document.getElementById('form-reset-bloco').style.display = mostrar ? 'block' : 'none';
        }

        function salvarNovaSenha() {
            const user = document.getElementById('reset-usuario').value;
            const novaSenha = document.getElementById('reset-nova-senha').value.trim();

            if (!novaSenha) {
                alert("Digite a nova senha.");
                return;
            }

            globalUsers[user] = novaSenha;
            window.dbSet(window.dbRef(window.db, 'users'), globalUsers).then(() => {
                alert("Senha alterada com sucesso! Faça login com a nova senha.");
                document.getElementById('reset-nova-senha').value = '';
                mostrarEsqueceuSenha(false);
            });
        }

        function fazerLogout() {
            localStorage.removeItem('gp_logado');
            localStorage.removeItem('gp_usuario');
            document.getElementById('painel-app').style.display = 'none';
            document.getElementById('tela-login').style.display = 'block';
        }

        function carregarApp() {
            document.getElementById('tela-login').style.display = 'none';
            document.getElementById('painel-app').style.display = 'block';
            let usuario = localStorage.getItem('gp_usuario') || 'Usuário';
            document.getElementById('saudacao-usuario').innerText = `Olá, ${usuario.toUpperCase()}`;
            document.getElementById('perfil-usuario-selecionado').value = usuario.toLowerCase();
            carregarDadosPerfil();
            atualizarDados();
        }

        function carregarDadosPerfil() {
            const selUser = document.getElementById('perfil-usuario-selecionado').value;
            document.getElementById('perfil-novo-usuario').value = selUser;
            document.getElementById('perfil-nova-senha').value = '';
        }

        function salvarConfigPerfil() {
            const usuarioAntigo = document.getElementById('perfil-usuario-selecionado').value;
            const novoUsuario = document.getElementById('perfil-novo-usuario').value.trim().toLowerCase();
            const novaSenha = document.getElementById('perfil-nova-senha').value.trim();

            if (!novoUsuario) {
                alert("O nome de usuário não pode estar vazio.");
                return;
            }

            let senhaSalva = novaSenha ? novaSenha : globalUsers[usuarioAntigo];

            if (usuarioAntigo !== novoUsuario) {
                if (globalUsers[novoUsuario]) {
                    alert("Este nome de usuário já existe.");
                    return;
                }
                delete globalUsers[usuarioAntigo];
            }

            globalUsers[novoUsuario] = senhaSalva;
            window.dbSet(window.dbRef(window.db, 'users'), globalUsers).then(() => {
                localStorage.setItem('gp_usuario', novoUsuario);
                alert("Perfil atualizado com sucesso!");
                carregarApp();
            });
        }

        window.onload = function() {
            if (localStorage.getItem('gp_tema') === 'light') {
                document.documentElement.setAttribute('data-theme', 'light');
            }
            if (localStorage.getItem('gp_logado') === 'true') {
                carregarApp();
            }
        }

        function alternarTema() {
            const html = document.documentElement;
            if (html.getAttribute('data-theme') === 'light') {
                html.removeAttribute('data-theme');
                localStorage.setItem('gp_tema', 'dark');
            } else {
                html.setAttribute('data-theme', 'light');
                localStorage.setItem('gp_tema', 'light');
            }
        }

        function mudarAba(aba) {
            document.getElementById('secao-comandas').style.display = aba === 'comandas' ? 'block' : 'none';
            document.getElementById('secao-arquivos').style.display = aba === 'arquivos' ? 'block' : 'none';
            document.getElementById('secao-perfil').style.display = aba === 'perfil' ? 'block' : 'none';
            document.getElementById('tab-comandas').classList.toggle('ativa', aba === 'comandas');
            document.getElementById('tab-arquivos').classList.toggle('ativa', aba === 'arquivos');
            document.getElementById('tab-perfil').classList.toggle('ativa', aba === 'perfil');
        }

        function sincronizarPorcentagens(origem) {
            let pJoao = parseFloat(document.getElementById('cmd-pct-joao').value) || 0;
            let pArtur = parseFloat(document.getElementById('cmd-pct-artur').value) || 0;
            if (origem === 'joao') {
                pArtur = Math.max(0, Math.min(100, 100 - pJoao));
                document.getElementById('cmd-pct-artur').value = pArtur;
            } else {
                pJoao = Math.max(0, Math.min(100, 100 - pArtur));
                document.getElementById('cmd-pct-joao').value = pJoao;
            }
        }

        function salvarComanda() {
            const idEdit = document.getElementById('comanda-id-editando').value;
            const cliente = document.getElementById('cmd-cliente').value.trim();
            const valor = document.getElementById('cmd-valor').value.trim();
            const status = document.getElementById('cmd-status').value;
            let pctJoao = parseFloat(document.getElementById('cmd-pct-joao').value) || 50;
            let pctArtur = parseFloat(document.getElementById('cmd-pct-artur').value) || 50;
            const arquivos = document.getElementById('cmd-arquivos').value.trim();
            const obs = document.getElementById('cmd-obs').value.trim();

            if (!cliente || !valor) {
                alert("Preencha o nome do cliente e o valor cobrado.");
                return;
            }

            const id = idEdit ? Number(idEdit) : Date.now();
            const comandaData = { id, cliente, valor, status, pctJoao, pctArtur, arquivos, obs };

            window.dbSet(window.dbRef(window.db, 'comandas/' + id), comandaData).then(() => {
                limparFormComanda();
            });
        }

        function limparFormComanda() {
            document.getElementById('cmd-cliente').value = '';
            document.getElementById('cmd-valor').value = '';
            document.getElementById('cmd-pct-joao').value = '50';
            document.getElementById('cmd-pct-artur').value = '50';
            document.getElementById('cmd-arquivos').value = '';
            document.getElementById('cmd-obs').value = '';
            document.getElementById('comanda-id-editando').value = '';
        }

        function editarComanda(id) {
            let c = globalComandas.find(item => item.id == id);
            if (c) {
                document.getElementById('comanda-id-editando').value = c.id;
                document.getElementById('cmd-cliente').value = c.cliente;
                document.getElementById('cmd-valor').value = c.valor;
                document.getElementById('cmd-status').value = c.status || 'Criação de Design';
                document.getElementById('cmd-pct-joao').value = c.pctJoao !== undefined ? c.pctJoao : 50;
                document.getElementById('cmd-pct-artur').value = c.pctArtur !== undefined ? c.pctArtur : 50;
                document.getElementById('cmd-arquivos').value = c.arquivos || '';
                document.getElementById('cmd-obs').value = c.obs || '';
                mudarAba('comandas');
            }
        }

        function excluirComanda(id) {
            window.dbRemove(window.dbRef(window.db, 'comandas/' + id));
        }

        function salvarArquivoGeral() {
            const titulo = document.getElementById('arq-titulo').value.trim();
            const url = document.getElementById('arq-url').value.trim();

            if (!titulo || !url) {
                alert("Preencha o título e o link do arquivo.");
                return;
            }

            const id = Date.now();
            const arqData = { id, titulo, url };

            window.dbSet(window.dbRef(window.db, 'arquivos_gerais/' + id), arqData).then(() => {
                document.getElementById('arq-titulo').value = '';
                document.getElementById('arq-url').value = '';
            });
        }

        function excluirArquivoGeral(id) {
            window.dbRemove(window.dbRef(window.db, 'arquivos_gerais/' + id));
        }

        function atualizarDados() {
            const corpoCmd = document.getElementById('tabela-comandas-corpo');
            corpoCmd.innerHTML = '';
            
            let faturamentoTotal = 0;
            let totalJoao = 0;
            let totalArtur = 0;

            if (globalComandas.length === 0) {
                corpoCmd.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--gray);">Nenhum site cadastrado na comanda.</td></tr>`;
            } else {
                globalComandas.forEach(c => {
                    let valLimpo = parseFloat(c.valor.toString().replace('.', '').replace(',', '.')) || 0;
                    faturamentoTotal += valLimpo;

                    let pJ = c.pctJoao !== undefined ? c.pctJoao : 50;
                    let pA = c.pctArtur !== undefined ? c.pctArtur : 50;

                    let valJoao = valLimpo * (pJ / 100);
                    let valArtur = valLimpo * (pA / 100);

                    totalJoao += valJoao;
                    totalArtur += valArtur;

                    let linkHtml = c.arquivos ? `<a href="${c.arquivos}" target="_blank" style="color: var(--primary); font-weight:600;">Acessar Link</a>` : 'Nenhum';

                    corpoCmd.innerHTML += `
                        <tr>
                            <td><strong>${c.cliente}</strong></td>
                            <td>R$ ${c.valor}</td>
                            <td>Joao: ${pJ}% (R$ ${valJoao.toLocaleString('pt-BR', {minimumFractionDigits: 2})})<br>Artur: ${pA}% (R$ ${valArtur.toLocaleString('pt-BR', {minimumFractionDigits: 2})})</td>
                            <td><span class="badge badge-fase">${c.status || 'Criação de Design'}</span></td>
                            <td>${linkHtml}</td>
                            <td style="font-size: 0.85rem; color: var(--gray);">${c.obs || '-'}</td>
                            <td style="text-align: right;">
                                <button class="btn-acao btn-editar" onclick="editarComanda(${c.id})">Editar</button>
                                <button class="btn-acao btn-excluir" onclick="excluirComanda(${c.id})">Excluir</button>
                            </td>
                        </tr>
                    `;
                });
            }

            const corpoArq = document.getElementById('tabela-arquivos-corpo');
            corpoArq.innerHTML = '';
            if (globalArquivos.length === 0) {
                corpoArq.innerHTML = `<tr><td colspan="3" style="text-align: center; color: var(--gray);">Nenhum arquivo geral cadastrado.</td></tr>`;
            } else {
                globalArquivos.forEach(a => {
                    corpoArq.innerHTML += `
                        <tr>
                            <td><strong>${a.titulo}</strong></td>
                            <td><a href="${a.url}" target="_blank" style="color: var(--primary);">${a.url}</a></td>
                            <td style="text-align: right;">
                                <button class="btn-acao btn-excluir" onclick="excluirArquivoGeral(${a.id})">Excluir</button>
                            </td>
                        </tr>
                    `;
                });
            }

            document.getElementById('res-faturamento').innerText = `R$ ${faturamentoTotal.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
            document.getElementById('res-total-joao').innerText = `R$ ${totalJoao.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
            document.getElementById('res-total-artur').innerText = `R$ ${totalArtur.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
            document.getElementById('res-total-arquivos').innerText = globalArquivos.length + globalComandas.filter(c => c.arquivos).length;
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=950, scrolling=True)
