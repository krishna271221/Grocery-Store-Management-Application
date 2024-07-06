$(document).ready(function() {
    loadProducts();
    loadUnits();

    $('#productForm').submit(function(e) {
        e.preventDefault();
        addProduct();
    });

    $('#addNewProduct').click(function() {
        $('#newProductForm').toggle();
    });
});

function loadProducts() {
    $.get('/getProducts', function(data) {
        const productsTable = $('#productsTable');
        productsTable.empty();
        data.forEach(product => {
            productsTable.append(`
                <tr>
                    <td>${product.name}</td>
                    <td>${product.unit_name}</td>
                    <td>${product.price_per_unit}</td>
                    <td>
                        <button class="btn btn-danger" onclick="deleteProduct(${product.product_id})">Delete</button>
                    </td>
                </tr>
            `);
        });
    });
}

function loadUnits() {
    $.get('/getUnits', function(data) {
        const unitSelect = $('#unitId');
        unitSelect.empty();
        unitSelect.append('<option value="">Select Unit</option>');
        data.forEach(unit => {
            unitSelect.append(`<option value="${unit.unit_id}">${unit.unit_name}</option>`);
        });
    });
}

function addProduct() {
    const productName = $('#productName').val();
    const unitId = $('#unitId').val();
    const pricePerUnit = $('#pricePerUnit').val();

    $.ajax({
        url: '/insertProduct',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            name: productName,
            unit_id: unitId,
            price_per_unit: pricePerUnit
        }),
        success: function(response) {
            alert('Product added successfully!');
            loadProducts();
            $('#newProductForm').hide();
            $('#productForm')[0].reset();
        }
    });
}

function deleteProduct(productId) {
    if (confirm('Are you sure you want to delete this product?')) {
        $.ajax({
            url: `/deleteProduct/${productId}`,
            type: 'DELETE',
            success: function(response) {
                alert('Product deleted successfully!');
                loadProducts();
            }
        });
    }
}

function showNewProductForm() {
    $('#newProductForm').toggle();
}

