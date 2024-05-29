(function ($) {
  $(document).ready(function () {
    const urlLink = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    $.ajax({
      url: urlLink,
      dataType: 'json',
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function (error) {
        console.error('Error fetching data: ', error);
      }
    });
  });
})(window.jQuery);
