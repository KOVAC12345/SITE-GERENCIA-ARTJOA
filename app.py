import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gestão de Sites - Equipe",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestão de Sites e Comandas</title>
    <style>
        :root {
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --success: #059669;
            --danger: #dc2626;
            --warning: #d97706;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text: #0f172a;
            --gray: #64748b;
            --border: #cbd5e1;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        }

        [data-theme="dark"] {
            --primary: #3b82f6;
            --primary-hover: #2563eb;
            --success: #10b981;
            --danger: #ef4444;
            --warning: #f59e0b;
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text: #f8fafc;
            --gray: #94a3b8;
            --border: #334155;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            transition: background 0.2s, color 0.2s;
        }

        .container {
            width: 100%;
            max-width: 420px;
            padding: 20px;
            box-sizing: border-box;
        }

        .card {
            background: var(--card-bg);
            padding: 30px;
            border-radius: 12px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }

        h2 {
            margin-top: 0;
            color: var(--text);
            font-size: 1.5rem;
            text-align: center;
            font-weight: 700;
        }

        p.subtitle {
            text-align: center;
            color: var(--gray);
            font-size: 0.85rem;
            margin-top: 4px;
            margin-bottom: 24px;
        }

        label {
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--gray);
            display: block;
            margin-top: 12px;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px 12px;
            margin-top: 6px;
            border-radius: 8px;
            border: 1px solid var(--border);
            box-sizing: border-box;
            font-size: 0.9rem;
            background: var(--bg);
            color: var(--text);
        }

        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
        }

        button {
            width: 100%;
            padding: 11px;
            margin-top: 18px;
            border-radius: 8px;
            border: none;
            background: var(--primary);
            color: white;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            transition: background 0.2s;
        }

        button:hover { background: var(--primary-hover); }

        #painel-app {
            display: none;
            max-width: 1150px;
            width: 100%;
            padding: 24px 16px;
            box-sizing: border-box;
            margin: 0 auto;
        }

        .dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            background: var(--card-bg);
            padding: 16px 20px;
            border-radius: 10px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }

        .painel-secao {
            background: var(--card-bg);
            padding: 24px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: var(--shadow);
            border: 1px solid var(--border);
        }

        .grid-resumo {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 14px;
            margin-bottom: 20px;
        }

        .box-info {
            background: var(--card-bg);
            padding: 16px;
            border-radius: 10px;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
        }
        .box-info span { font-size: 0.75rem; color: var(--gray); display: block; font-weight: 700; text-transform: uppercase; }
        .box-info h3 { margin: 6px 0 2px 0; font-size: 1.3rem; font-weight: 700; }
        .box-info p { margin: 0; font-size: 0.78rem; color: var(--gray); }

        .sub-abas {
            display: flex;
            gap: 8px;
            margin-bottom: 18px;
            flex-wrap: wrap;
        }
        .btn-sub-aba {
            flex: 1;
            min-width: 130px;
            padding: 10px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text);
            border-radius: 8px;
            font-weight: 600;
            margin: 0;
            cursor: pointer;
            font-size: 0.85rem;
        }
        .btn-sub-aba.ativa {
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
        }

        .barra-ferramentas {
            display: flex;
            gap: 10px;
            margin-bottom: 16px;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        table.tabela-gestao {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
            margin-top: 10px;
        }
        table.tabela-gestao th, table.tabela-gestao td {
            padding: 12px 10px;
            border-bottom: 1px solid var(--border);
            text-align: left;
        }
        table.tabela-gestao th {
            color: var(--gray);
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.75rem;
        }

        .btn-acao {
            background: none;
            border: none;
            cursor: pointer;
            font-weight: 600;
            padding: 5px 8px;
            border-radius: 6px;
            font-size: 0.78rem;
            margin-right: 4px;
            width: auto;
        }
        .btn-excluir { color: var(--danger); background: rgba(220, 38, 38, 0.1); }
        .btn-editar { color: var(--primary); background: rgba(37, 99, 235, 0.1); }

        .badge {
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 0.72rem;
            font-weight: 700;
            display: inline-block;
        }
        .badge-andamento { background: rgba(217, 119, 6, 0.15); color: var(--warning); }
        .badge-pronto { background: rgba(5, 150, 105, 0.15); color: var(--success); }
        .badge-concluido { background: rgba(37, 99, 235, 0.15); color: var(--primary); }
        .badge-membro { background: rgba(100, 116, 139, 0.15); color: var(--text); }
    </style>
</head>
<body>

    <!-- TELA DE LOGIN -->
    <div class="container" id="tela-login">
        <div class="card">
            <h2>Gestão de Equipe</h2>
            <p class="subtitle">Acesso restrito</p>
            
            <div id="form-login-bloco">
                <label>Usuário:</label>
                <input type="text" id="login-usuario" placeholder="joao ou artur">
                
                <label>Senha:</label>
                <input type="password" id="login-senha" placeholder="******">
                
                <button onclick="fazerLogin()">Entrar</button>
            </div>
        </div>
    </div>

    <!-- PAINEL PRINCIPAL -->
    <div id="painel-app">
        <div class="dashboard-header">
            <div>
                <h2 id="saudacao-usuario" style="margin: 0; font-size: 1.1rem; text-align: left;">Olá</h2>
                <span style="font-size: 0.78rem; color: var(--gray);">Painel de Controle e Gestão de Projetos</span>
            </div>
            <div>
                <button onclick="alternarTema()" class="btn-acao" style="background: var(--bg); border: 1px solid var(--border); color: var(--text); padding: 7px 12px; margin:0;">Tema</button>
                <button onclick="fazerLogout()" class="btn-acao btn-excluir" style="padding: 7px 12px; margin-left: 6px;">Sair</button>
            </div>
        </div>

        <!-- INDICADORES GERAIS -->
        <div class="grid-resumo">
            <div class="box-info">
                <span>Faturamento Total</span>
                <h3 id="res-faturamento" style="color: var(--success);">R$ 0,00</h3>
                <p>Valor somado dos projetos</p>
            </div>
            <div class="box-info">
                <span>Total a Receber (João)</span>
                <h3 id="val-joao">R$ 0,00</h3>
                <p>Baseado na divisão por projeto</p>
            </div>
            <div class="box-info">
                <span>Total a Receber (Artur)</span>
                <h3 id="val-artur">R$ 0,00</h3>
                <p>Baseado na divisão por projeto</p>
            </div>
            <div class="box-info">
                <span>Total de Projetos</span>
                <h3 id="res-total-sites">0</h3>
                <p>Cadastrados na comanda</p>
            </div>
        </div>

        <div class="painel-secao">
            <div class="sub-abas">
                <button class="btn-sub-aba ativa" onclick="mudarAba('comandas')" id="tab-comandas">Comanda de Sites</button>
                <button class="btn-sub-aba" onclick="mudarAba('arquivos')" id="tab-arquivos">Repositório de Arquivos</button>
                <button class="btn-sub-aba" onclick="mudarAba('perfil')" id="tab-perfil">Meu Perfil</button>
            </div>

            <!-- ABA COMANDAS -->
            <div id="secao-comandas">
                <div style="background: var(--bg); padding: 16px; border-radius: 8px; margin-bottom: 20px; border: 1px solid var(--border);">
                    <h3 style="margin-top: 0; font-size: 0.95rem;">Adicionar / Atualizar Projeto</h3>
                    <input type="hidden" id="comanda-id-editando">
                    <div style="display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr; gap: 10px;">
                        <div>
                            <label>Cliente / Projeto:</label>
                            <input type="text" id="cmd-cliente" placeholder="Nome do cliente">
                        </div>
                        <div>
                            <label>Valor (R$):</label>
                            <input type="text" id="cmd-valor" placeholder="0,00">
                        </div>
                        <div>
                            <label>Status:</label>
                            <select id="cmd-status">
                                <option value="Em Andamento">Em Andamento</option>
                                <option value="Pronto">Pronto</option>
                                <option value="Concluído">Concluído</option>
                            </select>
                        </div>
                        <div>
                            <label>% do João:</label>
                            <input type="number" id="cmd-pct-joao" value="50" min="0" max="100" oninput="sincronizarPct('joao')">
                        </div>
                        <div>
                            <label>% do Artur:</label>
                            <input type="number" id="cmd-pct-artur" value="50" min="0" max="100" oninput="sincronizarPct('artur')">
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px;">
                        <div>
                            <label>Data de Entrega:</label>
                            <input type="date" id="cmd-data">
                        </div>
                        <div>
                            <label>Links ou Arquivos:</label>
                            <input type="text" id="cmd-arquivos" placeholder="GitHub, Drive ou Hospedagem">
                        </div>
                    </div>
                    <div style="margin-top: 10px;">
                        <label>Observações:</label>
                        <textarea id="cmd-obs" placeholder="Detalhes ou pendências do projeto" rows="2"></textarea>
                    </div>
                    <button onclick="salvarComanda()" style="margin-top: 12px;">Salvar na Comanda</button>
                </div>

                <div class="barra-ferramentas">
                    <h3 style="font-size: 1rem; margin: 0; align-self: center;">Trabalhos Atuais</h3>
                    <input type="text" id="busca-projeto" placeholder="Pesquisar projeto..." oninput="atualizarDados()" style="max-width: 260px; padding: 8px 12px;">
                </div>

                <div style="overflow-x: auto;">
                    <table class="tabela-gestao">
                        <thead>
                            <tr>
                                <th>Projeto</th>
                                <th>Valor</th>
                                <th>Divisão (% por Trabalho)</th>
                                <th>Status</th>
                                <th>Entrega</th>
                                <th>Arquivos</th>
                                <th>Observações</th>
                                <th style="text-align: right;">Ações</th>
                            </tr>
                        </thead>
                        <tbody id="tabela-comandas-corpo">
                            <tr><td colspan="8" style="text-align: center; color: var(--gray);">Nenhum projeto cadastrado.</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- ABA ARQUIVOS GERAIS -->
            <div id="secao-arquivos" style="display: none;">
                <div style="background: var(--bg); padding: 16px; border-radius: 8px; margin-bottom: 20px; border: 1px solid var(--border);">
                    <h3 style="margin-top: 0; font-size: 0.95rem;">Adicionar Arquivo ou Link Geral</h3>
                    <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 10px;">
                        <div>
                            <label>Título:</label>
                            <input type="text" id="arq-titulo" placeholder="Ex: Logos e Assets">
                        </div>
                        <div>
                            <label>Link:</label>
                            <input type="text" id="arq-url" placeholder="https://...">
                        </div>
                    </div>
                    <button onclick="salvarArquivoGeral()" style="margin-top: 12px;">Adicionar ao Repositório</button>
                </div>

                <h3 style="font-size: 1rem; margin-bottom: 10px;">Arquivos da Equipe</h3>
                <div style="overflow-x: auto;">
                    <table class="tabela-gestao">
                        <thead>
                            <tr>
                                <th>Título</th>
                                <th>Link</th>
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
                <div style="background: var(--bg); padding: 20px; border-radius: 8px; border: 1px solid var(--border); max-width: 500px;">
                    <h3 style="margin-top: 0; font-size: 1rem;">Configurações de Perfil</h3>
                    <p style="font-size: 0.85rem; color: var(--gray);">Gerencie sua conta e altere sua senha de acesso ao sistema.</p>
                    
                    <label>Usuário Atual:</label>
                    <input type="text" id="perfil-usuario-ativo" disabled style="background: var(--card-bg);">

                    <label>Nova Senha:</label>
                    <input type="password" id="perfil-nova-senha" placeholder="Digite a nova senha">

                    <button onclick="salvarAlteracaoSenha()" style="margin-top: 14px;">Atualizar Senha</button>
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
                alert("Usuário ou senha incorretos.");
            }
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
            let usuario = localStorage.getItem('gp_usuario') || 'usuário';
            document.getElementById('saudacao-usuario').innerText = "Olá, " + usuario.toUpperCase();
            document.getElementById('perfil-usuario-ativo').value = usuario;

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
            document.getElementById('secao-perfil').style.display = aba === 'perfil' ? 'block' : 'none';

            document.getElementById('tab-comandas').classList.toggle('ativa', aba === 'comandas');
            document.getElementById('tab-arquivos').classList.toggle('ativa', aba === 'arquivos');
            document.getElementById('tab-perfil').classList.toggle('ativa', aba === 'perfil');
        }

        function sincronizarPct(origem) {
            let pctJoao = document.getElementById('cmd-pct-joao');
            let pctArtur = document.getElementById('cmd-pct-artur');
            if (origem === 'joao') {
                let val = parseFloat(pctJoao.value) || 0;
                if (val > 100) val = 100;
                if (val < 0) val = 0;
                pctArtur.value = 100 - val;
            } else {
                let val = parseFloat(pctArtur.value) || 0;
                if (val > 100) val = 100;
                if (val < 0) val = 0;
                pctJoao.value = 100 - val;
            }
        }

        function salvarComanda() {
            const idEdit = document.getElementById('comanda-id-editando').value;
            const cliente = document.getElementById('cmd-cliente').value.trim();
            const valor = document.getElementById('cmd-valor').value.trim();
            const status = document.getElementById('cmd-status').value;
            const pctJoao = parseFloat(document.getElementById('cmd-pct-joao').value) || 50;
            const pctArtur = parseFloat(document.getElementById('cmd-pct-artur').value) || 50;
            const dataEntrega = document.getElementById('cmd-data').value;
            const arquivos = document.getElementById('cmd-arquivos').value.trim();
            const obs = document.getElementById('cmd-obs').value.trim();

            if (!cliente || !valor) {
                alert("Preencha o cliente e o valor.");
                return;
            }

            let comandas = JSON.parse(localStorage.getItem('gp_comandas')) || [];

            if (idEdit) {
                let idx = comandas.findIndex(c => c.id == idEdit);
                if (idx >= 0) {
                    comandas[idx] = { id: Number(idEdit), cliente, valor, status, pctJoao, pctArtur, dataEntrega, arquivos, obs };
                }
                document.getElementById('comanda-id-editando').value = '';
            } else {
                comandas.push({ id: Date.now(), cliente, valor, status, pctJoao, pctArtur, dataEntrega, arquivos, obs });
            }

            localStorage.setItem('gp_comandas', JSON.stringify(comandas));
            limparFormComanda();
            atualizarDados();
        }

        function limparFormComanda() {
            document.getElementById('cmd-cliente').value = '';
            document.getElementById('cmd-valor').value = '';
            document.getElementById('cmd-pct-joao').value = '50';
            document.getElementById('cmd-pct-artur').value = '50';
            document.getElementById('cmd-data').value = '';
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
                document.getElementById('cmd-status').value = c.status;
                document.getElementById('cmd-pct-joao').value = c.pctJoao !== undefined ? c.pctJoao : 50;
                document.getElementById('cmd-pct-artur').value = c.pctArtur !== undefined ? c.pctArtur : 50;
                document.getElementById('cmd-data').value = c.dataEntrega || '';
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
                alert("Preencha o título e o link.");
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

        function salvarAlteracaoSenha() {
            const novaSenha = document.getElementById('perfil-nova-senha').value.trim();
            const usuarioAtivo = localStorage.getItem('gp_usuario');

            if (!novaSenha) {
                alert("Digite a nova senha.");
                return;
            }

            let usuarios = obterUsuarios();
            usuarios[usuarioAtivo] = novaSenha;
            localStorage.setItem('gp_users', JSON.stringify(usuarios));
            alert("Senha alterada com sucesso.");
            document.getElementById('perfil-nova-senha').value = '';
        }

        function atualizarDados() {
            let comandas = JSON.parse(localStorage.getItem('gp_comandas')) || [];
            let arquivos = JSON.parse(localStorage.getItem('gp_arquivos_gerais')) || [];
            let termoBusca = (document.getElementById('busca-projeto').value || "").toLowerCase();

            const corpoCmd = document.getElementById('tabela-comandas-corpo');
            corpoCmd.innerHTML = '';
            
            let faturamentoTotal = 0;
            let totalJoao = 0;
            let totalArtur = 0;
            let projetosFiltrados = comandas.filter(c => c.cliente.toLowerCase().includes(termoBusca) || (c.obs && c.obs.toLowerCase().includes(termoBusca)));

            if (projetosFiltrados.length === 0) {
                corpoCmd.innerHTML = `<tr><td colspan="8" style="text-align: center; color: var(--gray);">Nenhum projeto encontrado.</td></tr>`;
            } else {
                projetosFiltrados.forEach(c => {
                    let valLimpo = parseFloat(c.valor.toString().replace('.', '').replace(',', '.')) || 0;
                    let pJoao = c.pctJoao !== undefined ? c.pctJoao : 50;
                    let pArtur = c.pctArtur !== undefined ? c.pctArtur : 50;

                    faturamentoTotal += valLimpo;
                    totalJoao += valLimpo * (pJoao / 100);
                    totalArtur += valLimpo * (pArtur / 100);

                    let badgeStatus = 'badge-andamento';
                    if (c.status === 'Pronto') badgeStatus = 'badge-pronto';
                    if (c.status === 'Concluído') badgeStatus = 'badge-concluido';

                    let linkHtml = c.arquivos ? `<a href="${c.arquivos}" target="_blank" style="color: var(--primary); font-weight:600;">Acessar</a>` : 'Nenhum';
                    let dataFormatada = c.dataEntrega ? c.dataEntrega.split('-').reverse().join('/') : '-';

                    corpoCmd.innerHTML += `
                        <tr>
                            <td><strong>${c.cliente}</strong></td>
                            <td>R$ ${c.valor}</td>
                            <td><span class="badge badge-membro">João: ${pJoao}%</span> <span class="badge badge-membro">Artur: ${pArtur}%</span></td>
                            <td><span class="badge ${badgeStatus}">${c.status}</span></td>
                            <td>${dataFormatada}</td>
                            <td>${linkHtml}</td>
                            <td style="font-size: 0.82rem; color: var(--gray);">${c.obs || '-'}</td>
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
                corpoArq.innerHTML = `<tr><td colspan="3" style="text-align: center; color: var(--gray);">Nenhum arquivo cadastrado.</td></tr>`;
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

            document.getElementById('res-faturamento').innerText = "R$ " + faturamentoTotal.toLocaleString('pt-BR', {minimumFractionDigits: 2});
            document.getElementById('val-joao').innerText = "R$ " + totalJoao.toLocaleString('pt-BR', {minimumFractionDigits: 2});
            document.getElementById('val-artur').innerText = "R$ " + totalArtur.toLocaleString('pt-BR', {minimumFractionDigits: 2});
            document.getElementById('res-total-sites').innerText = comandas.length;
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=820, scrolling=True)