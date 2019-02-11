window.onload = function () {
    $('.minus-btn').on('click', function (e) {
        e.preventDefault();
        var $this = $(this);
        var cart_product_pk = $this.closest('div').siblings(".cart-product-id").text();
        var product_total_price = $this.closest('div').next(".total-price");
        var $input = $this.closest('div').find('input');
        var value = parseInt($input.val());

        if (value > 1) {
            value = value - 1;
        } else {
            value = 1;
        }

        $input.val(value);

        $.ajax({
            url: "/cart/edit/" + cart_product_pk + "/" + value + "/",
            success: function (data) {
                product_total_price.html("$" + data.product_price_total);
                $('#cart-price-total').text(data.cart_price_total);
                $('#cart-items-total').text(data.cart_items_total);
            },
        });

    });

    $('.plus-btn').on('click', function (e) {
        e.preventDefault();
        var $this = $(this);
        var cart_product_pk = $this.closest('div').siblings(".cart-product-id").text();
        var product_total_price = $this.closest('div').next(".total-price");
        var $input = $this.closest('div').find('input');

        var value = parseInt($input.val());

        if (value < 100) {
            value = value + 1;
        } else {
            value = 100;
        }

        $input.val(value);

        $.ajax({
            url: "/cart/edit/" + cart_product_pk + "/" + value + "/",
            success: function (data) {
                product_total_price.html("$" + data.product_price_total);
                $('#cart-price-total').text(data.cart_price_total);
                $('#cart-items-total').text(data.cart_items_total);
            },
        });
    });


    $('.dropdown-item').on('click', function(){
        var category = $(this).text().toLowerCase();
        $('#dropdownMenuButton').text(category);

        $.ajax({
            url: "/admin/products/list/" + category + "/",
            success: function (data) {
                var products_data = data.products;
                var products = $('#prducts-by-category');
                products.html("");

                for (var i = 0; i < products_data.length; i++) {
                    products.append(`<li class="list-group-item d-flex justify-content-between align-items-center">
                                        <a href="/admin/products/read/${products_data[i].product_id}/" class="text-dark">
                                            ${products_data[i].product_name}
                                        </a>
                                        <span>
                                            <a class="btn btn-warning" href="/admin/products/update/${products_data[i].product_id}/" role="button"> Edit </a>
                                            <a class="btn btn-danger" href="/admin/products/delete/${products_data[i].product_id}/" role="button">Delete</a>
                                        </span>
                                    </li>`);
                }
            },
        });

    });

}
