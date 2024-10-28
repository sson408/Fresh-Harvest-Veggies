function onClickLogin() {
  var userName = $("#txtUsername").val();
  var password = $("#txtPassword").val();

  if (!userName) {
    alert("userName is required");
    return;
  }

  if (!password) {
    alert("Password is required");
    return;
  }

  $.ajax({
    url: "/login",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      username: userName.trim(),
      password: password,
    }),
    success: function (response) {
      console.log("user", response.user);
      var user = response.user;
      //add user to session storage
      sessionStorage.setItem("userId", user.userId);
      sessionStorage.setItem("username", user.username);
      sessionStorage.setItem("userRole", user.userRole);
      $("#messageRow").show().addClass("alert-success");
      $("#messageText")
        .text("Login successful. Redirecting...")
        .addClass("alert-success");
      setTimeout(function () {
        window.location.href = "/dashboard";
      }, 1000);
    },
    error: function (xhr, status, error) {
      var errorMessage = xhr.responseText || error;
      console.log("errorMessage", errorMessage);
      $("#messageRow").show().addClass("alert-danger");
      $("#messageText")
        .text("Login failed: " + JSON.parse(errorMessage).message + "!")
        .addClass("alert-danger");
    },
  });
}

function onClickSignUp() {
  window.location.href = "signUp";
}

function bindSignInEvents() {
  $("#btnLogin").on("click", onClickLogin);
  $("#btnSignUp").on("click", onClickSignUp);

  $(document).on("keypress", function (e) {
    if (e.keyCode == 13 || e.which == 13) {
      onClickLogin();
    }
  });
}

$(document).ready(function () {
  bindSignInEvents();
});
