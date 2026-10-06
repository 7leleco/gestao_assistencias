/* =========================================================
   APP — Lógica da página principal
   ========================================================= */

/* ===== HELPERS ===== */
function fmtMoeda(v) {
    return (Number(v) || 0).toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL",
    });
}

function fmtData(iso) {
    if (!iso) return "—";
    const d = iso.slice(0, 10);
    const [a, m, dia] = d.split("-");
    return `${dia}/${m}`;
}

function fmtDataCompleta(iso) {
    if (!iso) return "";
    const d = iso.slice(0, 10);
    const [a, m, dia] = d.split("-");
    return `${dia}/${m}/${a}`;
}

/* ===== RENDER KPIs ===== */
function renderKPIs(ordens) {
    const total = ordens.length;
    const feitas = ordens.filter((o) => o.nota_feita).length;
    const pendentes = ordens.filter((o) => !o.nota_feita).length;
    const valor = ordens.reduce((s, o) => s + (Number(o.valor_total) || 0), 0);

    // Cards
    document.querySelectorAll(".card-valor")[0].textContent = total;
    document.querySelectorAll(".card-valor")[1].textContent = feitas;
    document.querySelectorAll(".card-valor")[2].textContent = pendentes;

    // Card do valor total (com olho)
    const elValor = document.getElementById("valor-total");
    if (elValor) {
        elValor.dataset.real = fmtMoeda(valor);
        elValor.textContent = "••••••••";
    }
}

/* ===== RENDER TABELA ===== */
function renderTabela(ordens) {
    const tbody = document.getElementById("tbody-assistencias");
    tbody.innerHTML = "";

    if (ordens.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="13" style="text-align: center; padding: 40px; color: #94a3b8;">
                    Nenhuma assistência cadastrada
                </td>
            </tr>`;
        return;
    }

    // Agrupa por data
    const grupos = {};
    ordens.forEach((o) => {
        const d = o.data.slice(0, 10);
        if (!grupos[d]) grupos[d] = [];
        grupos[d].push(o);
    });

    // Ordena as datas (mais recente primeiro)
    const datas = Object.keys(grupos).sort((a, b) => b.localeCompare(a));

    datas.forEach((data) => {
        const itens = grupos[data];

        // Faixa de grupo (data)
        tbody.insertAdjacentHTML(
            "beforeend",
            `<tr class="row-group">
                <td colspan="13">
                    ${fmtDataCompleta(data)} · ${itens.length} assistência${itens.length > 1 ? "s" : ""}
                </td>
            </tr>`
        );

        // Linhas
        itens.forEach((o) => {
            const badgeCls = o.nota_feita ? "badge-green" : "badge-orange";
            const badgeTxt = o.nota_feita ? "✓ OK" : "⏱ Fazer nota";

            tbody.insertAdjacentHTML(
                "beforeend",
                `<tr class="row-data">
                    <td><input type="checkbox" data-id="${o.id}"></td>
                    <td>${fmtData(o.data)}</td>
                    <td>${o.numero_os || "—"}</td>
                    <td>
                        <strong>${o.seguradora || "—"}</strong>
                        <span class="sub">${o.tipo_servico || ""}</span>
                    </td>
                    <td>
                        <strong>${o.segurado || "—"}</strong>
                        <span class="sub">📍 ${o.cidade || ""}</span>
                    </td>
                    <td>${o.prestador || "Não informado"}</td>
                    <td>${fmtMoeda(o.visita)}</td>
                    <td>${fmtMoeda(o.mao_de_obra)}</td>
                    <td>${fmtMoeda(o.pecas)}</td>
                    <td>${fmtMoeda(o.deslocamento)}</td>
                    <td><strong>${fmtMoeda(o.valor_total)}</strong></td>
                    <td><span class="badge ${badgeCls}">${badgeTxt}</span></td>
                    <td>
                        <div class="actions">
                            <button class="btn-icon" onclick="window.open('/pdf/os/${o.id}', '_blank')">👁</button>
                            <button class="btn-icon">✏️</button>
                            <button class="btn-icon">🗑️</button>
                        </div>
                    </td>
                </tr>`
            );
        });
    });
}

/* ===== CARREGAR DADOS ===== */
async function carregarDados() {
    try {
        const ordens = await buscarOrdens();
        renderKPIs(ordens);
        renderTabela(ordens);
        console.log(`✅ ${ordens.length} OS carregadas`);
    } catch (erro) {
        console.error("❌ Erro ao carregar:", erro);
    }
}

/* ===== INICIALIZAR ===== */
document.addEventListener("DOMContentLoaded", () => {
    carregarDados();
});

/* ===== FUNÇÕES DO OLHO ===== */
function mostrarValor() {
    const el = document.getElementById("valor-total");
    if (el) el.textContent = el.dataset.real || "R$ 0,00";
}

function esconderValor() {
    const el = document.getElementById("valor-total");
    if (el) el.textContent = "••••••••";
}