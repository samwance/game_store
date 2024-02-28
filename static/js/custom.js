
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
  $('#add-to-cart-form button').on('click', function(event) {
    event.preventDefault(); // предотвращаем стандартное действие кнопки
    var gameId = $(this).closest('form').find('input[name="game_id"]').val();
    var url = '/add/';
    var data = {
      game_id: gameId
    };

    $.ajax({
      type: 'POST',
      url: url,
      data: data,
      headers: {
        'X-CSRFToken': csrftoken
      },
      success: function(response) {
        // обработка успешного добавления в корзину
        console.log('Игра добавлена в корзину:', response);
      },
      error: function(xhr, status, error) {
        // обработка ошибки
        console.error('Ошибка при добавлении игры в корзину:', error);
      }
    });
  });

  $('#add-to-wishlist-form button').on('click', function(event) {
    event.preventDefault(); // предотвращаем стандартное действие кнопки
    var gameId = $(this).closest('form').find('input[name="game_id"]').val();
    var url = '/like/';
    var data = {
      game_id: gameId
    };

    $.ajax({
      type: 'POST',
      url: url,
      data: data,
      headers: {
        'X-CSRFToken': csrftoken
      },
      success: function(response) {
        // обработка успешного добавления в список желаемого
        console.log('Игра добавлена в список желаемого:', response);
      },
      error: function(xhr, status, error) {
        // обработка ошибки
        console.error('Ошибка при добавлении игры в список желаемого:', error);
      }
    });
  });

  $('#remove-from-cart-form button').on('click', function(event) {
    event.preventDefault(); // предотвращаем стандартное действие кнопки
    var gameId = $(this).closest('form').find('input[name="game_id"]').val();
    var url = '/remove/';
    var data = {
      game_id: gameId
    };

    $.ajax({
      type: 'POST',
      url: url,
      data: data,
      headers: {
        'X-CSRFToken': csrftoken
      },
      success: function(response) {
        // обработка успешного удаления из корзины
        console.log('Игра удалена из корзины:', response);
      },
      error: function(xhr, status, error) {
        // обработка ошибки
        console.error('Ошибка при удалении игры из корзины:', error);
      }
    });
  });

  $('#remove-from-wishlist-form button').on('click', function(event) {
    event.preventDefault(); // предотвращаем стандартное действие кнопки
    var gameId = $(this).closest('form').find('input[name="game_id"]').val();
    var url = '/unlike/';
    var data = {
      game_id: gameId
    };

    $.ajax({
      type: 'POST',
      url: url,
      data: data,
      headers: {
        'X-CSRFToken': csrftoken
      },
      success: function(response) {
        // обработка успешного удаления из списка желаемого
        console.log('Игра удалена из списка желаемого:', response);
      },
      error: function(xhr, status, error) {
        // обработка ошибки
        console.error('Ошибка при удалении игры из списка желаемого:', error);
      }
    });
  });
});
