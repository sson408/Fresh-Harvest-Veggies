function onViewCustomerClick() {
  window.location.href = "/dashboard/customerList";
}

function onViewVeggieClick() {
  window.location.href = "/dashboard/itemList";
}

function bindDashboardEvents() {
  $("#btnViewCustomers").on("click", onViewCustomerClick);
  $("#btnViewVeggies").on("click", onViewVeggieClick);
}

$(document).ready(function () {
  bindDashboardEvents();
});
