$(document).ready(function() {
    let productCount = 1;
    loadProductOptions();

    $('#addProduct').click(function() {
        productCount++;
        addProductRow(productCount);
    });

    $('#productContainer').on('click', '.removeProduct', function() {
        $(this).closest('.product').remove();
        calculateTotalPrice();
    });

    $('#productContainer').on('change', '.productName', function() {
        const productId = $(this).val();
        const priceField = $(this).closest('.product').find('.price');
        if (productId) {
            $.get(`/getProduct/${productId}`, function(data) {
                priceField.val(data.price_per_unit);
                updateProductTotal(priceField.closest('.product'));
            });
        } else {
            priceField.val('');
            updateProductTotal(priceField.closest('.product'));
        }
    });

    $('#productContainer').on('input', '.quantity', function() {
        updateProductTotal($(this).closest('.product'));
    });

    $('#orderForm').submit(function(e) {
        e.preventDefault();
        saveOrder();
    });

    function loadProductOptions() {
        $.get('/getProducts', function(data) {
            const selectHtml = data.map(product =>
                `<option value="${product.product_id}">${product.name}</option>`).join('');
            $('.productName').each(function() {
                if ($(this).children().length <= 1) {
                    $(this).html(`<option value="">Select Product</option>${selectHtml}`);
                }
            });
        });
    }

    function addProductRow(count) {
        const productRow = `
            <div class="product">
                <div class="form-row">
                    <div class="form-group col-md-4">
                        <label for="productName${count}">Product Name</label>
                        <select class="form-control productName" id="productName${count}" required>
                            ${$('#productName1').html()}
                        </select>
                    </div>
                    <div class="form-group col-md-2">
                        <label for="price${count}">Price</label>
                        <input type="number" class="form-control price" id="price${count}" readonly>
                    </div>
                    <div class="form-group col-md-2">
                        <label for="quantity${count}">Quantity</label>
                        <input type="number" class="form-control quantity" id="quantity${count}" required>
                    </div>
                    <div class="form-group col-md-2">
                        <label for="total${count}">Total</label>
                        <input type="number" class="form-control total" id="total${count}" readonly>
                    </div>
                    <div class="form-group col-md-2">
                        <label>&nbsp;</label>
                        <button type="button" class="btn btn-danger removeProduct">Remove</button>
                    </div>
                </div>
            </div>
        `;
        $('#productContainer').append(productRow);
        loadProductOptions();
    }

    function updateProductTotal(productElement) {
        const price = parseFloat(productElement.find('.price').val()) || 0;
        const quantity = parseFloat(productElement.find('.quantity').val()) || 0;
        const total = price * quantity;
        productElement.find('.total').val(total);
        calculateTotalPrice();
    }

    function calculateTotalPrice() {
        let totalPrice = 0;
        $('.total').each(function() {
            totalPrice += parseFloat($(this).val()) || 0;
        });
        $('#totalPrice').val(totalPrice);
    }

    function saveOrder() {
        const orderDetails = [];
        $('.product').each(function() {
            const productName = $(this).find('.productName').val();
            const price = $(this).find('.price').val();
            const quantity = $(this).find('.quantity').val();
            const total = $(this).find('.total').val();
            if (productName && quantity && total) {
                orderDetails.push({
                    product_id: productName,
                    quantity: quantity,
                    total_price: total
                });
            }
        });

        const order = {
            customer_name: $('#customerName').val(),
            total: $('#totalPrice').val(),
            order_details: orderDetails
        };

        $.ajax({
            url: '/insertOrder',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(order),
            success: function(response) {
                alert('Order saved successfully!');
                window.location.href = "/";
            }
        });
    }
});



