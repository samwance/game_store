

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

$(function() {
    // Function to handle add to cart button clicks
    function handleAddToCart(formId, url, errorMessage) {
        $(formId + ' button').on('click', function(event) {
            event.preventDefault();
            var gameId = $(this).closest('form').find('input[name="game_id"]').val();
            var data = { game_id: gameId };
            var _vm=$(this);

            var cartText = $(`.btn-cart${gameId}`).text()
            var trim = $.trim(cartText)

            let res;
            var cartItems = $(`.cart-items`).text()
            var cartPrice = $(`.cart-price`).text()
            var trimCount = parseInt(cartItems)
            var trimPrice = parseFloat(cartPrice)
            var gamePrice = parseFloat($(this).closest('form').find('input[name="game_price"]').val());

            $.ajax({
                type: 'POST',
                url: url,
                data: data,
                headers: { 'X-CSRFToken': csrftoken },
                success: function(response) {
                    if(trim === 'Remove') {
                        $(`.btn-cart${gameId}`).text('Add')
                        res = trimCount - 1
                        trimPrice -= gamePrice;
                    } else {
                        $(`.btn-cart${gameId}`).text('Remove')
                        res = trimCount + 1
                        trimPrice += gamePrice;
                    }

                    $(`.cart-items`).text(res)
                    $(`.cart-price`).text(trimPrice.toFixed(2))
                },
                error: function(xhr, status, error) {
                    console.error(errorMessage, error);
                }
            });
        });
    }

    // Function to handle add to wishlist button clicks
    function handleAddToWishlist(formId, url, errorMessage) {
        $(formId + ' button').on('click', function(event) {
            event.preventDefault();
            var gameId = $(this).closest('form').find('input[name="game_id"]').val();
            var data = { game_id: gameId };
            var _vm=$(this);

            var cartText = $(`.btn-wishlist${gameId}`).text()
            var trim = $.trim(cartText)

            let res;
            var wishlistItems = $(`.wishlist-items`).text()
            var trimCount = parseInt(wishlistItems)

            $.ajax({
                type: 'POST',
                url: url,
                data: data,
                headers: { 'X-CSRFToken': csrftoken },
                success: function(response) {
                    console.log(response)
                    if(trim === 'Unlike') {
                        $(`.btn-wishlist${gameId}`).text('Like')
                        res = trimCount - 1
                    } else {
                        $(`.btn-wishlist${gameId}`).text('Unlike')
                        res = trimCount + 1
                    }

                    $(`.wishlist-items`).text(res)
                },
                error: function(xhr, status, error) {
                    console.error(errorMessage, error);
                }
            });
        });
    }

    // Call the functions with the appropriate parameters
    handleAddToCart('#manage-cart-form', '/manage_cart/', 'Error adding game to cart.');
    handleAddToWishlist('#manage-wishlist-form', '/manage_wishlist/', 'Error adding game to wishlist.');
});
