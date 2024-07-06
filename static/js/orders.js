document.addEventListener('DOMContentLoaded', function() {
    loadOrders();

    function loadOrders() {
        $.get('/getOrders', function(data) {
            const ordersSection = $('#ordersSection');
            ordersSection.empty();
            data.forEach(order => {
                const orderElement = `
                    <div class="order">
                        <p><strong>Order ID:</strong> ${order.order_id}</p>
                        <p><strong>Customer Name:</strong> ${order.customer_name}</p>
                        <p><strong>Total Price:</strong> ${order.total}</p>
                        <p><strong>Order Date:</strong> ${order.order_date}</p>
                        <div class="order-actions">
                            <button class="btn btn-danger" onclick="deleteOrder(${order.order_id})">Delete</button>
                        </div>
                    </div>
                `;
                ordersSection.append(orderElement);
            });
        });
    }

    function deleteOrder(orderId) {
        if (confirm('Are you sure you want to delete this order?')) {
            $.ajax({
                url: `/deleteOrder/${orderId}`,
                type: 'DELETE',
                success: function(response) {
                    alert('Order deleted successfully!');
                    loadOrders(); // Reload orders after deletion
                }
            });
        }
    }
});
