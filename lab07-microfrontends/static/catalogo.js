async function renderCatalogo() {
    const response = await fetch('/api/bff/home');
    const data = await response.json();
    const container = document.getElementById('vitrine-list');

    container.innerHTML = '';

    data.vitrine.forEach(p => {
        const div = document.createElement('div');
        div.className = 'product';
        div.innerHTML = `
            <span><strong>${p.nome}</strong> - R$ ${p.preco}</span>
            <span class="stock-tag">Status: ${p.estoque}</span></span>
            <button onclick="adicionarAoCarrinho('${p.nome}', ${p.preco})">Adicionar</button>
        `;
        container.appendChild(div);
    });
}

function adicionarAoCarrinho(nome, preco) {
    console.log(`[CATALOGO] Evento: Adicionar ${nome}`);

    const event = new CustomEvent('cart:add', { 
        detail: { nome, preco } 
    });

    window.dispatchEvent(event);
}

renderCatalogo();
