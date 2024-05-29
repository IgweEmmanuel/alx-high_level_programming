(function ($) {
  $(document).ready(function () {
    const urlLink = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.ajax({
      url: urlLink,
      dataType: 'json',
      success: function (data) {
        $('#character').text(data.name);
      },
      error: function (error) {
        console.error('Error fetching data: ', error);
      }
    });
  });
})(window.jQuery);
