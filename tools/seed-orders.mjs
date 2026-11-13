// Seeds sample orders as the test user, then moves some through the state machine as admin.
const API = "http://localhost:3000/api";
const post = async (path, body, token, method = "POST") => {
  const r = await fetch(API + path, {
    method,
    headers: { "Content-Type": "application/json", ...(token && { Authorization: `Bearer ${token}` }) },
    body: JSON.stringify(body),
  });
  const j = await r.json();
  if (!r.ok) throw new Error(`${method} ${path} -> ${r.status} ${JSON.stringify(j)}`);
  return j;
};

const user = (await post("/login", { email: "test@eshop.com", password: "Test1234!" })).token;
const admin = (await post("/login", { email: "admin@eshop.com", password: "Admin123!" })).token;
const products = await (await fetch(API + "/products")).json();

// [product indexes with qty, target status]
const plan = [
  [[[0, 1]], "pending"],
  [[[1, 2], [2, 1]], "pending"],
  [[[3, 1]], "confirmed"],
  [[[0, 2], [4, 1]], "shipping"],
  [[[2, 3]], "delivered"],
  [[[1, 1]], "canceled"],
];
const path = { pending: [], confirmed: ["confirmed"], shipping: ["confirmed", "shipping"], delivered: ["confirmed", "shipping", "delivered"], canceled: ["canceled"] };
const addresses = ["227 Nguyễn Văn Cừ, Q5, TP.HCM", "12 Lê Lợi, Q1, TP.HCM", "45 Trần Hưng Đạo, Hà Nội"];

for (const [i, [items, status]] of plan.entries()) {
  const total = items.reduce((s, [p, q]) => s + products[p % products.length].price * q, 0);
  const { orderId } = await post("/checkout", { total_amount: total, shipping_address: addresses[i % 3] }, user);
  for (const s of path[status]) await post(`/admin/orders/${orderId}/status`, { status: s }, admin, "PUT");
  console.log(`order #${orderId}: ${total.toLocaleString("vi-VN")} ₫ -> ${status}`);
}
