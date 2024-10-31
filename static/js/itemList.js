function loadItems() {
  var filterWord = $("#txtSearchInput").val();

  $.ajax({
    url: "/item/listAllItems",
    type: "GET",
    data: {
      filterWord: filterWord,
    },
    contentType: "application/json",
    success: function (response) {
      //console.log(response);
      var items = response.items;
      onLoadItems(items);
    },
    error: function (xhr, status, error) {
      var errorMessage = xhr.status + ": " + (xhr.responseText || error);
      alert("Get all data failed: " + errorMessage);
    },
  });
}

function onLoadItems(dataList) {
  var dataColumns = [
    { headerName: "Name", field: "name", width: "15%" },
    { headerName: "Price", field: "priceDisplay", width: "10%" },
    { headerName: "Stock", field: "stock", width: "10%" },
    { headerName: "Type", field: "type", width: "10%" },
    { headerName: "Weight", field: "weight", width: "10%" },
    { headerName: "PricePerKilo", field: "pricePerKiloDisplay", width: "10%" },
    { headerName: "PricePerUnit", field: "pricePerUnitDisplay", width: "10%" },
    { headerName: "PricePerPack", field: "pricePerPackDisplay", width: "10%" },
  ];

  populateTable("#itemTable", dataList, dataColumns, "", "");
}

function loadPremadeBoxes() {
  $.ajax({
    url: "/item/listAllPremadeBoxes",
    type: "GET",
    contentType: "application/json",
    success: function (response) {
      //console.log(response);
      var premadeBoxes = response.premadeBoxes;
      onLoadPremadeBoxs(premadeBoxes);
    },
    error: function (xhr, status, error) {
      var errorMessage = xhr.status + ": " + (xhr.responseText || error);
      alert("Get all data failed: " + errorMessage);
    },
  });
}

function onLoadPremadeBoxs(dataList) {
  console.log("premadebox", dataList);
  //each box create a table
  dataList.forEach((box) => {
    let boxItems = box.items;
    var dataColumns = [
      { headerName: "Name", field: "name", width: "15%" },
      { headerName: "Price", field: "priceDisplay", width: "10%" },
      { headerName: "Type", field: "type", width: "10%" },
      { headerName: "Quantity", field: "quantity", width: "10%" },
      { headerName: "Weight", field: "weight", width: "10%" },
      {
        headerName: "PricePerKilo",
        field: "pricePerKiloDisplay",
        width: "10%",
      },

      {
        headerName: "PricePerUnit",
        field: "pricePerUnitDisplay",
        width: "10%",
      },
      {
        headerName: "PricePerPack",
        field: "pricePerPackDisplay",
        width: "10%",
      },
    ];

    var tableId = "boxTable" + box.id;
    var tableTitle = "Box: " + box.name;
    var tableDivId = "boxTableDiv" + box.id;

    var table = `<table id="${tableDivId}" class="table"></table>`;
    var title = `<h5>${box.name}</h5>`;
    $("#premadeBoxDiv").append(title);
    $("#premadeBoxDiv").append(table);

    populatePremadeBoxTable("#" + tableDivId, boxItems, dataColumns, "", "");

    //calculate total price
    let totalPrice = 0;
    boxItems.forEach((item) => {
      totalPrice += item.item.price * item.quantity;
    });

    var totalPriceDiv = `<div>Total Price: $${totalPrice}</div>`;
    $("#premadeBoxDiv").append(totalPriceDiv);
  });
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

function postItemInit() {
  loadItems();
  loadPremadeBoxes();
}

function bindItemEvents() {
  $("#btnSearch").on("click", loadItems);
  $("#itemPageOutDiv").on("keypress", function (e) {
    if (e.keyCode == 13 || e.which == 13) {
      loadItems();
    }
  });

  // Search input change event
  $("#txtSearchInput").on(
    "input",
    throttle(function () {
      if (!$("#txtSearchInput").val()) {
        loadItems();
      }
    }, 500)
  );
}

$(document).ready(function () {
  bindItemEvents();
  postItemInit();
});
