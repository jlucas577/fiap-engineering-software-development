const cart = { items: [], total: 0 };

function updateCartUI() {
    const list = document.getElementById('cart-list');
    const totalEl = document.getElementById('cart-total');

    list.innerHTML = '';

    if (cart.items.length === 0) {
        list.innerText = 'Vazio';
    } else {
        const clustered = {};

        cart.items.forEach(item => {
            if (!clustered[item.nome]) {
                clustered[item.nome] = {
                    quantity: 0,
                    unitValue: item.preco
                };
            }

            clustered[item.nome].quantity++;
        });

        Object.entries(clustered).forEach(([nome, dados]) => {
            const div = document.createElement('div');
            const finalValue = dados.quantity * dados.unitValue;

            div.innerText = `${nome} (${dados.quantity}x) - R$ ${formatCurrency(finalValue)}`;

            list.appendChild(div);
        });
    }

    totalEl.innerText = formatCurrency(cart.total);
}

function formatCurrency(value) {
    return Number(value).toLocaleString('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
}

updateCartUI();

window.addEventListener('cart:add', (e) => {
    const { nome, preco } = e.detail;
    console.log(`[CARRINHO] Recebi notificação de adição: ${nome}`);

    cart.total += preco;

    cart.items.push({ nome, preco });
    updateCartUI();
});
