document.addEventListener("DOMContentLoaded", () => {
  // this enables toasts any where
  var toastElList = [].slice.call(document.querySelectorAll(".toast"));
  var toastList = toastElList.map(function (toastEl) {
    let el = new bootstrap.Toast(toastEl, { autohide: false });

    el.show();

    return el;
  });

});
