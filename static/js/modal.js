// modalLoader.js
function loadAndShowModal(url, modalId, data = {}, closeCallback = null) {
  $.get(url, function (response) {
    $("body").append(response);
    var modal = $(modalId).data(data).modal("show");
    modal.on("hidden.bs.modal", function () {
      $(this).remove();

      if (typeof closeCallback === "function") {
        closeCallback();
      }
    });
  });
}

function loadAndShowModalWithMultiCallbacks(
  url,
  modalId,
  data = {},
  closeCallbacks = []
) {
  $.get(url, function (response) {
    $("body").append(response);
    var modal = $(modalId).data(data).modal("show");
    modal.on("hidden.bs.modal", function () {
      $(this).remove();

      if (Array.isArray(closeCallbacks)) {
        closeCallbacks.forEach(function (callback) {
          if (typeof callback === "function") {
            callback();
          }
        });
      }
    });
  });
}
