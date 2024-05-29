(function ($) {
  $(document).ready(function () {
    $('#btn_translate').click(function () {
      const urlLink = 'https://hellosalut.stefanbohacek.dev/?lang=';
      const val = $('#language_code').val();
      const newUrl = urlLink + val;
      $.ajax({
        url: newUrl,
        dataType: 'json',
        success: function (data) {
          $('#hello').text(data.hello);
        },
        error: function (error) {
          console.error('Error fetching data: ', error);
        }
      });
    });
  });
})(window.jQuery);
