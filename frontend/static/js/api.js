/* =========================================================
   API — Funções para chamar o backend
   ========================================================= */

const API_BASE = "/api";

/**
 * Busca todas as ordens de serviço.
 * Aceita filtros opcionais (busca, data_de, data_ate, seguradora).
 */
async function buscarOrdens(filtros = {}) {
    const params = new URLSearchParams();
    if (filtros.busca) params.append("busca", filtros.busca);
    if (filtros.data_de) params.append("data_de", filtros.data_de);
    if (filtros.data_ate) params.append("data_ate", filtros.data_ate);
    if (filtros.seguradora) params.append("seguradora", filtros.seguradora);
    if (filtros.status_nota) params.append("status_nota", filtros.status_nota);

    const url = `${API_BASE}/ordens?${params.toString()}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error("Erro ao buscar ordens");
    return res.json();
}

/**
 * Busca uma OS específica por ID.
 */
async function buscarOrdem(id) {
    const res = await fetch(`${API_BASE}/ordens/${id}`);
    if (!res.ok) throw new Error("OS não encontrada");
    return res.json();
}

/**
 * Cria uma nova OS.
 */
async function criarOrdem(dados) {
    const res = await fetch(`${API_BASE}/ordens`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
    });
    if (!res.ok) {
        const erro = await res.json();
        throw new Error(erro.detail || "Erro ao criar OS");
    }
    return res.json();
}

/**
 * Edita uma OS existente.
 */
async function editarOrdem(id, dados) {
    const res = await fetch(`${API_BASE}/ordens/${id}`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados),
    });
    if (!res.ok) throw new Error("Erro ao editar OS");
    return res.json();
}

/**
 * Deleta uma OS.
 */
async function deletarOrdem(id) {
    const res = await fetch(`${API_BASE}/ordens/${id}`, {
        method: "DELETE",
    });
    if (!res.ok) throw new Error("Erro ao deletar OS");
    return true;
}

/**
 * Busca as seguradoras cadastradas.
 */
async function buscarSeguradoras() {
    const res = await fetch(`${API_BASE}/seguradoras`);
    if (!res.ok) return [];
    return res.json();
}