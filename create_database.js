// Seleciona (ou cria) o banco de dados
use ecommerce_db;

// Criação das coleções
db.createCollection("users");
db.createCollection("products");
db.createCollection("carts");
db.createCollection("orders");

// Índices úteis
db.users.createIndex({ email: 1 }, { unique: true });
db.products.createIndex({ name: 1 }, { unique: true });
db.carts.createIndex({ user_id: 1 }, { unique: true });
db.orders.createIndex({ user_id: 1 });

// Documentos de exemplo

// Usuários
db.users.insertMany([
    { name: "Rodolfo", email: "rodolfo@example.com", password: "123456" },
    { name: "Maria", email: "maria@example.com", password: "abcdef" }
    ]);

// Produtos
db.products.insertMany([
    { name: "Notebook Dell", description: "Notebook i7 16GB RAM", price: 4500.00 },
    { name: "Smartphone Samsung", description: "Galaxy S23", price: 3500.00 },
    { name: "Fone Bluetooth", description: "Fone sem fio", price: 250.00 }
]);

// Carrinho inicial (exemplo para Rodolfo)
db.carts.insertOne({
    user_id: "rodolfo@example.com",
    items: [
        { product_id: "Notebook Dell", quantity: 1 },
        { product_id: "Fone Bluetooth", quantity: 2 }
    ]
});

// Pedido inicial (simulação de compra)
db.orders.insertOne({
    user_id: "rodolfo@example.com",
    items: [
        { product_id: "Notebook Dell", quantity: 1 },
        { product_id: "Fone Bluetooth", quantity: 2 }
    ],
  total: 4500.00 + (250.00 * 2)
});
