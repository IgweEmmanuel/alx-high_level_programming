(function ($) {
  $(document).ready(function () {
    const urlLink = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.ajax({
      url: urlLink,
      dataType: 'json',
      success: function (data) {
        const results = data.result;
        results.forEach(function (titles) {
          $('#list_movies').append('<li>' + titles.title + '</li>');
        });
      },
      error: function (error) {
        console.error('Error fetching data: ', error);
      }
    });
  });
})(window.jQuery);
