const cart = { items: [], total: 0 };

function updateCartUI() {
    const list = document.getElementById('cart-list');
    const totalEl = document.getElementById('cart-total');

    cart.items.forEach(item => {
        const div = document.createElement('div');
        div.innerText = `${item.nome} - R$ ${item.preco}`;
        list.appendChild(div);
    });

    list.innerHTML = cart.items.length === 0 ? 'Vazio' : '';
    totalEl.innerText = cart.total.toFixed(2);
}

updateCartUI();

window.addEventListener('cart:add', (e) => {
    const { nome, preco } = e.detail;
    console.log(`[CARRINHO] Recebi notificação de adição: ${nome}`);

    cart.total += preco;

    cart.items.push({ nome, preco });
    updateCartUI();
});
