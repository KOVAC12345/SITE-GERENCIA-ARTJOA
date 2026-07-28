import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gestão de Sites - Equipe",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

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
            --bg: #f1f5f9;
            --card-bg: #ffffff;
            --text: #0f172a;
            --gray: #64748b;
            --border: #e2e8f0;
            --shadow: 0 10.5px 25px -5px rgba(99, 102, 241, 0.07);
        }

        [data-theme="dark"] {
            --primary: #818cf8;
            --primary-hover: #6366f1;
            --accent: #f472b6;
            --success: #34d399;
            --danger: #f87171;
            --warning: #fbbf24;
            --bg: #05050a;
            --card-bg: #111827;
            --text: #f9fafb;
            --gray: #9ca3af;
            --border: #1f2937;
            --shadow: 0 10.5px 25px -5px rgba(0, 0, 0, 0.5);
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            transition: background 0.3s, color 0.3s;
        }

        .container {
            width: 100%;
            max-width: 440px;
            padding: 20px;
            box-sizing: border-box;
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
            max-width: 1100px;
            width: 100%;
            padding: 30px 20px;
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
        .badge-andamento { background: rgba(245, 158, 11, 0.15); color: var(--warning); }
        .badge-concluido { background: rgba(16, 185, 129, 0.15); color: var(--success); }
        .badge-membro { background: rgba(99, 102, 241, 0.15); color: var(--primary); }
    </style>
</head>
<body>

    <!-- TELA DE LOGIN -->
    <div class="container" id="tela-login">
        <div class="card">
            <h2>🚀 Gestão da Equipe</h2>
            <p class="subtitle">Acesso restrito (João & Artur)</p>
            
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
                <button onclick="alternarTema()" class="btn-acao" style="background: var(--bg); border: 1px solid var(--border); color: var(--text); padding: 8px 14px; margin:0;">🌓 Tema</button>
                <button onclick="fazerLogout()" class="btn-acao btn-excluir" style="padding: 8px 14px; margin-left: 8px;">Sair</button>
            </div>
        </div>

        <!-- INDICADORES GERAIS E PORCENTAGEM DA EQUIPE -->
        <div class="grid-resumo">
            <div class="box-info">
                <span>Faturamento Total</span>
                <h3 id="res-faturamento" style="color: var(--success);">R$ 0,00</h3>
                <p>Total de gerimento geral</p>
            </div>
            <div class="box-info">
                <span>Participação do João</span>
                <h3 id="res-part-joao" style="color: var(--primary);">0%</h3>
                <p id="val-joao">R$ 0,00 (0 sites)</p>
            </div>
            <div class="box-info">
                <span>Participação do Artur</span>
                <h3 id="res-part-artur" style="color: var(--accent);">0%</h3>
                <p id="val-artur">R$ 0,00 (0 sites)</p>
            </div>
            <div class="box-info">
                <span>Repositório de Arquivos</span>
                <h3 id="res-total-arquivos" style="color: var(--warning);">0</h3>
                <p>Links e arquivos salvos</p>
            </div>
        </div>

        <div class="painel-secao">
            <div class="sub-abas">
                <button class="btn-sub-aba ativa" onclick="mudarAba('comandas')" id="tab-comandas">📋 Comanda de Sites</button>
                <button class="btn-sub-aba" onclick="mudarAba('arquivos')" id="tab-arquivos">📁 Repositório de Arquivos</button>
            </div>

            <!-- ABA COMANDAS -->
            <div id="secao-comandas">
                <div style="background: var(--bg); padding: 20px; border-radius: 16px; margin-bottom: 24px; border: 1px solid var(--border);">
                    <h3 style="margin-top: 0; font-size: 1rem;">Adicionar / Atualizar Site na Comanda</h3>
                    <input type="hidden" id="comanda-id-editando">
                    <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 12px;">
                        <div>
                            <label>Nome do Cliente / Projeto:</label>
                            <input type="text" id="cmd-cliente" placeholder="Ex: Imobiliária Furtado">
                        </div>
                        <div>
                            <label>Valor Cobrado (R$):</label>
                            <input type="text" id="cmd-valor" placeholder="1500,00">
                        </div>
                        <div>
                            <label>Responsável:</label>
                            <select id="cmd-responsavel">
                                <option value="João">João</option>
                                <option value="Artur">Artur</option>
                            </select>
                        </div>
                        <div>
                            <label>Status:</label>
                            <select id="cmd-status">
                                <option value="Em Andamento">Em Andamento</option>
                                <option value="Concluído">Concluído</option>
                            </select>
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
                                <th>Responsável</th>
                                <th>Status</th>
                                <th>Arquivos / Links</th>
                                <th>Observações</th>
                                <th style="text-align: right;">Ações</th>
                            </tr>
                        </thead>
                        <tbody id="tabela-comandas-corpo">
                            <tr><td colspan="7" style="text-align: center; color: var(--gray);">Nenhum site na comanda.</td></tr>
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
        </div>
    </div>

    <script>
        function obterUsuarios() {
            let salvos = localStorage.getItem('gp_users');
            if (salvos) {
                return JSON.parse(salvos);
            }
            return { "joao": "123", "artur": "123" };
        }

        function fazerLogin() {
            const user = document.getElementById('login-usuario').value.trim().toLowerCase();
            const pass = document.getElementById('login-senha').value.trim();
            const usuarios = obterUsuarios();

            if (usuarios[user] && usuarios[user] === pass) {
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

            let usuarios = obterUsuarios();
            usuarios[user] = novaSenha;
            localStorage.setItem('gp_users', JSON.stringify(usuarios));
            alert("Senha alterada com sucesso! Faça login com a nova senha.");
            document.getElementById('reset-nova-senha').value = '';
            mostrarEsqueceuSenha(false);
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
            document.getElementById('saudacao-usuario').innerText = `Olá, ${usuario.toUpperCase()} 👋`;
            atualizarDados();
        }

        window.onload = function() {
            if (localStorage.getItem('gp_tema') === 'dark') {
                document.documentElement.setAttribute('data-theme', 'dark');
            }
            if (localStorage.getItem('gp_logado') === 'true') {
                carregarApp();
            }
        }

        function alternarTema() {
            const html = document.documentElement;
            if (html.getAttribute('data-theme') === 'dark') {
                html.removeAttribute('data-theme');
                localStorage.setItem('gp_tema', 'light');
            } else {
                html.setAttribute('data-theme', 'dark');
                localStorage.setItem('gp_tema', 'dark');
            }
        }

        function mudarAba(aba) {
            document.getElementById('secao-comandas').style.display = aba === 'comandas' ? 'block' : 'none';
            document.getElementById('secao-arquivos').style.display = aba === 'arquivos' ? 'block' : 'none';
            document.getElementById('tab-comandas').classList.toggle('ativa', aba === 'comandas');
            document.getElementById('tab-arquivos').classList.toggle('ativa', aba === 'arquivos');
        }

        function salvarComanda() {
            const idEdit = document.getElementById('comanda-id-editando').value;
            const cliente = document.getElementById('cmd-cliente').value.trim();
            const valor = document.getElementById('cmd-valor').value.trim();
            const responsavel = document.getElementById('cmd-responsavel').value;
            const status = document.getElementById('cmd-status').value;
            const arquivos = document.getElementById('cmd-arquivos').value.trim();
            const obs = document.getElementById('cmd-obs').value.trim();

            if (!cliente || !valor) {
                alert("Preencha o nome do cliente e o valor cobrado.");
                return;
            }

            let comandas = JSON.parse(localStorage.getItem('gp_comandas')) || [];

            if (idEdit) {
                let idx = comandas.findIndex(c => c.id == idEdit);
                if (idx >= 0) {
                    comandas[idx] = { id: Number(idEdit), cliente, valor, responsavel, status, arquivos, obs };
                }
                document.getElementById('comanda-id-editando').value = '';
            } else {
                comandas.push({ id: Date.now(), cliente, valor, responsavel, status, arquivos, obs });
            }

            localStorage.setItem('gp_comandas', JSON.stringify(comandas));
            limparFormComanda();
            atualizarDados();
        }

        function limparFormComanda() {
            document.getElementById('cmd-cliente').value = '';
            document.getElementById('cmd-valor').value = '';
            document.getElementById('cmd-arquivos').value = '';
            document.getElementById('cmd-obs').value = '';
            document.getElementById('comanda-id-editando').value = '';
        }

        function editarComanda(id) {
            let comandas = JSON.parse(localStorage.getItem('gp_comandas')) || [];
            let c = comandas.find(item => item.id == id);
            if (c) {
                document.getElementById('comanda-id-editando').value = c.id;
                document.getElementById('cmd-cliente').value = c.cliente;
                document.getElementById('cmd-valor').value = c.valor;
                document.getElementById('cmd-responsavel').value = c.responsavel || 'João';
                document.getElementById('cmd-status').value = c.status;
                document.getElementById('cmd-arquivos').value = c.arquivos;
                document.getElementById('cmd-obs').value = c.obs;
                mudarAba('comandas');
            }
        }

        function excluirComanda(id) {
            let comandas = JSON.parse(localStorage.getItem('gp_comandas')) || [];
            comandas = comandas.filter(c => c.id != id);
            localStorage.setItem('gp_comandas', JSON.stringify(comandas));
            atualizarDados();
        }

        function salvarArquivoGeral() {
            const titulo = document.getElementById('arq-titulo').value.trim();
            const url = document.getElementById('arq-url').value.trim();

            if (!titulo || !url) {
                alert("Preencha o título e o link do arquivo.");
                return;
            }

            let arquivos = JSON.parse(localStorage.getItem('gp_arquivos_gerais')) || [];
            arquivos.push({ id: Date.now(), titulo, url });
            localStorage.setItem('gp_arquivos_gerais', JSON.stringify(arquivos));

            document.getElementById('arq-titulo').value = '';
            document.getElementById('arq-url').value = '';
            atualizarDados();
        }

        function excluirArquivoGeral(id) {
            let arquivos = JSON.parse(localStorage.getItem('gp_arquivos_gerais')) || [];
            arquivos = arquivos.filter(a => a.id != id);
            localStorage.setItem('gp_arquivos_gerais', JSON.stringify(arquivos));
            atualizarDados();
        }

        function atualizarDados() {
            let comandas = JSON.parse(localStorage.getItem('gp_comandas')) || [];
            let arquivos = JSON.parse(localStorage.getItem('gp_arquivos_gerais')) || [];

            const corpoCmd = document.getElementById('tabela-comandas-corpo');
            corpoCmd.innerHTML = '';
            
            let faturamentoTotal = 0;
            let fatJoao = 0;
            let qtdJoao = 0;
            let fatArtur = 0;
            let qtdArtur = 0;

            if (comandas.length === 0) {
                corpoCmd.innerHTML = `<tr><td colspan="7" style="text-align: center; color: var(--gray);">Nenhum site cadastrado na comanda.</td></tr>`;
            } else {
                comandas.forEach(c => {
                    let valLimpo = parseFloat(c.valor.toString().replace('.', '').replace(',', '.')) || 0;
                    faturamentoTotal += valLimpo;

                    if (c.responsavel === 'Artur') {
                        fatArtur += valLimpo;
                        qtdArtur++;
                    } else {
                        fatJoao += valLimpo;
                        qtdJoao++;
                    }

                    let badgeStatus = c.status === 'Concluído' ? 'badge badge-concluido' : 'badge badge-andamento';
                    let linkHtml = c.arquivos ? `<a href="${c.arquivos}" target="_blank" style="color: var(--primary); font-weight:600;">Acessar Link</a>` : 'Nenhum';

                    corpoCmd.innerHTML += `
                        <tr>
                            <td><strong>${c.cliente}</strong></td>
                            <td>R$ ${c.valor}</td>
                            <td><span class="badge badge-membro">${c.responsavel || 'João'}</span></td>
                            <td><span class="${badgeStatus}">${c.status}</span></td>
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
            if (arquivos.length === 0) {
                corpoArq.innerHTML = `<tr><td colspan="3" style="text-align: center; color: var(--gray);">Nenhum arquivo geral cadastrado.</td></tr>`;
            } else {
                arquivos.forEach(a => {
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

            let pctJoao = faturamentoTotal > 0 ? ((fatJoao / faturamentoTotal) * 100).toFixed(1) : 0;
            let pctArtur = faturamentoTotal > 0 ? ((fatArtur / faturamentoTotal) * 100).toFixed(1) : 0;

            document.getElementById('res-faturamento').innerText = `R$ ${faturamentoTotal.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
            document.getElementById('res-part-joao').innerText = `${pctJoao}%`;
            document.getElementById('val-joao').innerText = `R$ ${fatJoao.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (${qtdJoao} sites)`;
            document.getElementById('res-part-artur').innerText = `${pctArtur}%`;
            document.getElementById('val-artur').innerText = `R$ ${fatArtur.toLocaleString('pt-BR', {minimumFractionDigits: 2})} (${qtdArtur} sites)`;
            document.getElementById('res-total-arquivos').innerText = arquivos.length + comandas.filter(c => c.arquivos).length;
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=820, scrolling=True)
