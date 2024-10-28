function onBtnSignInClick() {
  window.location.href = "signIn";
}

function onBtnSignUpClick() {
  var userName = $("#txtUsername").val();
  var password = $("#txtPassword").val();
  let confirmPassword = $("#txtConfirmPassword").val();

  if (!userName) {
    alert("User Name is required");
    return;
  }

  if (!password) {
    alert("Password is required");
    return;
  } else if (password.length < 8 || password.length > 50) {
    alert(
      "Password must be at least 8 characters long and less than 50 characters long"
    );
    return false;
  }

  if (!confirmPassword) {
    alert("Confirm password is required");
    return false;
  } else if (confirmPassword !== password) {
    alert("Passwords do not match");
    return false;
  }

  // Check for a mix of character types: uppercase, lowercase, numbers, and symbols
  var upperCase = /[A-Z]/;
  var lowerCase = /[a-z]/;
  var numbers = /[0-9]/;
  var symbols = /[\W_]/; // This regex will match any non-word character and underscore, representing symbols

  if (
    !(
      upperCase.test(password) &&
      lowerCase.test(password) &&
      numbers.test(password) &&
      symbols.test(password)
    )
  ) {
    alert(
      "Password must include uppercase and lowercase letters, numbers, and symbols"
    );
    return false;
  }

  $.ajax({
    url: "/auth/register",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({
      userName: userName,
      password: password,
    }),
    success: function (response) {
      //console.log(response);
      var user = response.user;
      sessionStorage.setItem("userId", user.userId);
      sessionStorage.setItem("username", user.username);
      sessionStorage.setItem("userRole", user.userRole);
      $("#messageRow").show().addClass("alert-success");
      $("#messageText")
        .text("Registration successful. Redirecting...")
        .addClass("alert-success");
      setTimeout(function () {
        window.location.href = "/dashboard";
      }, 1000);
    },
    error: function (xhr, status, error) {
      var jsonResponse = JSON.parse(xhr.responseText);
      $("#messageRow").show().addClass("alert-danger");
      $("#messageText")
        .text("Registration failed: " + jsonResponse.message + "!")
        .addClass("alert-danger padiingLeft-0");

      clearAfterTimeout(3000);
    },
  });
}

function clearAfterTimeout(seconds) {
  seconds = seconds || 3000;
  setTimeout(function () {
    $("#messageRow").hide().removeClass("alert-danger");
    $("#messageText").text("").removeClass("alert-danger");
  }, seconds);
}

function bindSignUpEvents() {
  $("#btnSignIn").on("click", onBtnSignInClick);
  $("#btnSignUp").on("click", onBtnSignUpClick);
}

$(document).ready(function () {
  bindSignUpEvents();
});
