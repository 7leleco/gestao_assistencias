/* =========================================================
   NOVA ASSISTÊNCIA — Lógica do formulário
   ========================================================= */

let notaFeita = false;

document.addEventListener("DOMContentLoaded", () => {
    const hoje = new Date().toISOString().slice(0, 10);
    document.getElementById("data_os").value = hoje;

    configurarBotoesNota();
    configurarCalculoTotal();
    configurarUploadFoto();

    document.getElementById("form-nova-os").addEventListener("submit", salvarOS);
});

function configurarBotoesNota() {
    const botoes = document.querySelectorAll(".nota-btn");
    botoes.forEach((btn) => {
        btn.addEventListener("click", () => {
            botoes.forEach((b) => b.classList.remove("active"));
            btn.classList.add("active");
            notaFeita = btn.dataset.nota === "true";
        });
    });
}

function configurarCalculoTotal() {
    const campos = ["visita", "mao_de_obra", "pecas", "km_rodado", "valor_km", "deslocamento", "extras"];
    campos.forEach((id) => {
        document.getElementById(id).addEventListener("input", atualizarTotal);
    });
    atualizarTotal();
}

function atualizarTotal() {
    const visita = Number(document.getElementById("visita").value) || 0;
    const maoDeObra = Number(document.getElementById("mao_de_obra").value) || 0;
    const pecas = Number(document.getElementById("pecas").value) || 0;
    const kmRodado = Number(document.getElementById("km_rodado").value) || 0;
    const valorKm = Number(document.getElementById("valor_km").value) || 0;
    const deslocamento = Number(document.getElementById("deslocamento").value) || 0;
    const extras = Number(document.getElementById("extras").value) || 0;

    const deslocamentoKm = kmRodado * valorKm;
    const total = visita + maoDeObra + pecas + deslocamentoKm + deslocamento + extras;

    document.getElementById("total-preview").textContent = total.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL",
    });
}

function configurarUploadFoto() {
    const uploadBox = document.querySelector(".upload-box");
    const inputFoto = document.getElementById("foto");

    if (!uploadBox || !inputFoto) return;

    uploadBox.addEventListener("click", () => inputFoto.click());
    inputFoto.addEventListener("change", async () => {
        const arquivo = inputFoto.files[0];
        if (!arquivo) return;

        try {
            const formData = new FormData();
            formData.append("arquivo", arquivo);

            const res = await fetch("/api/upload", {
                method: "POST",
                body: formData,
            });

            if (!res.ok) throw new Error("Erro no upload");

            const dados = await res.json();
            uploadBox.dataset.foto = dados.caminho;
            uploadBox.querySelector("span").textContent = `✅ ${arquivo.name}`;
            uploadBox.style.borderColor = "#16a34a";
            uploadBox.style.color = "#16a34a";
        } catch (erro) {
            alert("Erro ao enviar foto: " + erro.message);
        }
    });
}

async function salvarOS(e) {
    e.preventDefault();

    const btnSalvar = document.querySelector(".btn-adicionar");
    btnSalvar.disabled = true;
    btnSalvar.textContent = "Salvando...";

    const uploadBox = document.querySelector(".upload-box");
    const fotoCaminho = uploadBox.dataset.foto || "[]";

    const dados = {
        numero_os: document.getElementById("numero_os").value,
        seguradora: document.getElementById("seguradora").value,
        tipo_servico: document.getElementById("tipo_servico").value,
        segurado: document.getElementById("segurado").value,
        telefone: document.getElementById("telefone").value,
        prestador: document.getElementById("prestador").value || "Não informado",
        endereco: document.getElementById("endereco").value,
        bairro: document.getElementById("bairro").value,
        cidade: document.getElementById("cidade").value,
        uf: document.getElementById("uf").value,
        visita: Number(document.getElementById("visita").value) || 0,
        mao_de_obra: Number(document.getElementById("mao_de_obra").value) || 0,
        pecas: Number(document.getElementById("pecas").value) || 0,
        km_rodado: Number(document.getElementById("km_rodado").value) || 0,
        valor_km: Number(document.getElementById("valor_km").value) || 0,
        deslocamento: Number(document.getElementById("deslocamento").value) || 0,
        extras: Number(document.getElementById("extras").value) || 0,
        valor_total: 0,
        nota_feita: notaFeita,
        observacoes: document.getElementById("observacoes").value,
        fotos: fotoCaminho !== "[]" ? JSON.stringify([fotoCaminho]) : "[]",
    };

    dados.valor_total =
        dados.visita +
        dados.mao_de_obra +
        dados.pecas +
        (dados.km_rodado * dados.valor_km) +
        dados.deslocamento +
        dados.extras;

    try {
        await criarOrdem(dados);
        alert("✅ Assistência cadastrada com sucesso!");
        window.location.href = "/site";
    } catch (erro) {
        alert("❌ Erro ao salvar: " + erro.message);
        btnSalvar.disabled = false;
        btnSalvar.textContent = "Adicionar ao caderno";
    }
}