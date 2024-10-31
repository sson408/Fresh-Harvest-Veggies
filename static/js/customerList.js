function loadCustomers() {
  var filterWord = $("#txtSearchInput").val();

  $.ajax({
    url: "/user/listAllCustomers",
    type: "GET",
    data: {
      filterWord: filterWord,
    },
    contentType: "application/json",
    success: function (response) {
      //console.log(response);
      var customers = response.customers;
      onLoadUsers(customers);
    },
    error: function (xhr, status, error) {
      var errorMessage = xhr.status + ": " + (xhr.responseText || error);
      alert("Get all customers failed: " + errorMessage);
    },
  });
}

function onLoadUsers(dataList) {
  var userColumns = [
    { headerName: "UserName", field: "username", width: "15%" },
    { headerName: "FirstName", field: "firstName", width: "10%" },
    { headerName: "LastName", field: "lastName", width: "10%" },
    { headerName: "Email", field: "email", width: "10%" },
    { headerName: "Discount Rate", field: "discountRate", width: "10%" },
    { headerName: "Max Credit", field: "maxCredit", width: "10%" },
    { headerName: "Min Balance", field: "minBalance", width: "10%" },
    { headerName: "Customer Balance", field: "customerBalance", width: "10%" },
    { headerName: "Customer Address", field: "customerAddress", width: "10%" },
  ];

  populateTable("#userTable", dataList, userColumns, "", "");
}

function throttle(func, delay) {
  let lastCall = 0;
  return function (...args) {
    const now = new Date().getTime();
    if (now - lastCall < delay) return;
    lastCall = now;
    return func(...args);
  };
}

function postUserInit() {
  loadCustomers();
}

function bindUserEvents() {
  $("#btnSearch").on("click", loadCustomers);
  $("#userPageOutDiv").on("keypress", function (e) {
    if (e.keyCode == 13 || e.which == 13) {
      loadCustomers();
    }
  });

  // Search input change event
  $("#txtSearchInput").on(
    "input",
    throttle(function () {
      if (!$("#txtSearchInput").val()) {
        loadCustomers();
      }
    }, 500)
  );
}

$(document).ready(function () {
  bindUserEvents();
  postUserInit();
});
