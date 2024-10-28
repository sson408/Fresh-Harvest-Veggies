function onClickLogin() {
  window.location.href = "/signIn";
}

function onViewDashboard() {
  window.location.href = "/dashboard";
}

function btnManageProfile() {
  loadAndShowUserProfileModal(0);
}

function loadAndShowUserProfileModal(userId, isNewUser) {
  loadAndShowModal("/modalUserProfile", "#userProfileModal", {
    selectedUserId: userId,
    isNewUser: isNewUser,
  });
}
function onClickLogout() {
  $.ajax({
    url: "/logout",
    type: "POST",
    contentType: "application/json",
    success: function (response) {
      console.log(response);
      //clear session storage
      sessionStorage.clear();

      window.location.href = "/";
    },
    error: function (xhr, status, error) {
      // Handle error - display error message, etc.
      alert("Logout failed: " + xhr.responseText || error);
    },
  });
}

function onClickCheckOut() {
  //window.location.href = "/checkout";
  //open a new page
  window.open("/checkout", "_blank");
}

function showShoppingCartDetails() {
  updateCartDisplayFromDatabase();
}

function bindNavBarEvents() {
  //console.log("Binding bar events");
  $("#btnLogin").on("click", onClickLogin);
  $("#btnLogout").on("click", onClickLogout);
  $("#btnManageProfile").on("click", btnManageProfile);
  $("#btnViewDashboard").on("click", onViewDashboard);
  $("#checkOut").on("click", onClickCheckOut);
}

$(document).ready(function () {
  bindNavBarEvents();
  showShoppingCartDetails();
});
