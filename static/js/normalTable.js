function populateTable(
  tableId,
  items,
  columns,
  editCallback,
  deleteCallback,
  deletedButtonName
) {
  var table = $(tableId);
  table.empty();
  if (!items || items.length === 0) return;
  table.addClass("table table-striped table-hover table-custom");

  var headerRow = "<thead class='thead-dark'><tr>";
  columns.forEach(function (column) {
    var headerWidth = column.width ? column.width : "auto";
    headerRow += `<th style='width:${headerWidth};'>${column.headerName}</th>`;
  });
  if (editCallback || deleteCallback) {
    headerRow += deletedButtonName
      ? "<th style='width:15%; min-width: 180px;'>Actions</th></tr></thead>"
      : "<th style='width:15%; min-width: 150px;'>Actions</th></tr></thead>";
  }

  table.append(headerRow);

  var tbody = $("<tbody></tbody>");
  items.forEach(function (item, index) {
    var row = "<tr>";
    columns.forEach(function (column) {
      var value = item[column.field];
      // Check if a formatter function is provided for the column
      if (column.formatter) {
        // Use the formatter function to get the formatted value
        value = column.formatter(value, item);
      } else {
        // Fallback to the item's value or an empty string if the value is undefined
        value = value || "";
      }
      //check column.width is not undefined and has value, otherwise set it to auto
      var width = column.width ? column.width : "auto";
      row += `<td style="width:${width}">${value}</td>`;
    });
    if (editCallback) {
      row += `<td>
              <button class="btn btn-primary btn-edit" data-id="${item.id}">Edit</button>`;
    }

    if (item.canBeDeleted) {
      row += `<button class="btn btn-danger btn-delete" data-id="${item.id}" style="margin-left:5px;">Delete</button>`;
    } else if (deleteCallback) {
      if (
        item.canBeDeleted == undefined ||
        item.canBeDeleted == null ||
        item.canBeDeleted
      ) {
        row += `<button class="btn btn-danger btn-delete" data-id="${
          item.id
        }" style="margin-left:5px;">${
          deletedButtonName ? deletedButtonName : "Delete"
        }</button>`;
      } else {
        console.log("canBeDeleted is false");
      }
    }

    row += `</td></tr>`; // Close the row
    tbody.append(row);
  });
  table.append(tbody);

  tbody.on("click", ".btn-edit", function () {
    var dataId = $(this).data("id");
    //console.log("dataId", dataId);
    editCallback(dataId);
  });

  tbody.on("click", ".btn-delete", function () {
    var dataId = $(this).data("id");
    let message = `Are you sure you want to ${
      deletedButtonName ? deletedButtonName : "delete"
    } this row?`;
    var confirmation = confirm(message);
    if (confirmation && deleteCallback) {
      deleteCallback(dataId);
    }
  });
}

function populatePremadeBoxTable(
  tableId,
  items,
  columns,
  editCallback,
  deleteCallback,
  deletedButtonName
) {
  var table = $(tableId);
  table.empty();
  if (!items || items.length === 0) return;
  table.addClass("table table-striped table-hover table-custom");

  var headerRow = "<thead class='thead-dark'><tr>";
  columns.forEach(function (column) {
    var headerWidth = column.width ? column.width : "auto";
    headerRow += `<th style='width:${headerWidth};'>${column.headerName}</th>`;
  });
  if (editCallback || deleteCallback) {
    headerRow += deletedButtonName
      ? "<th style='width:15%; min-width: 180px;'>Actions</th></tr></thead>"
      : "<th style='width:15%; min-width: 150px;'>Actions</th></tr></thead>";
  }

  table.append(headerRow);

  var tbody = $("<tbody></tbody>");
  items.forEach(function (data, index) {
    var item = data.item;
    var row = "<tr>";
    columns.forEach(function (column) {
      var value = item[column.field];
      if (column.field == "quantity") {
        value = data.quantity;
      }

      // Check if a formatter function is provided for the column
      if (column.formatter) {
        // Use the formatter function to get the formatted value
        value = column.formatter(value, data);
      } else {
        // Fallback to the item's value or an empty string if the value is undefined
        value = value || "";
      }
      //check column.width is not undefined and has value, otherwise set it to auto
      var width = column.width ? column.width : "auto";
      row += `<td style="width:${width}">${value}</td>`;
    });
    if (editCallback) {
      row += `<td>
              <button class="btn btn-primary btn-edit" data-id="${data.id}">Edit</button>`;
    }

    if (data.canBeDeleted) {
      row += `<button class="btn btn-danger btn-delete" data-id="${data.id}" style="margin-left:5px;">Delete</button>`;
    } else if (deleteCallback) {
      if (
        data.canBeDeleted == undefined ||
        data.canBeDeleted == null ||
        data.canBeDeleted
      ) {
        row += `<button class="btn btn-danger btn-delete" data-id="${
          data.id
        }" style="margin-left:5px;">${
          deletedButtonName ? deletedButtonName : "Delete"
        }</button>`;
      } else {
        console.log("canBeDeleted is false");
      }
    }

    row += `</td></tr>`; // Close the row
    tbody.append(row);
  });
  table.append(tbody);

  tbody.on("click", ".btn-edit", function () {
    var dataId = $(this).data("id");
    //console.log("dataId", dataId);
    editCallback(dataId);
  });

  tbody.on("click", ".btn-delete", function () {
    var dataId = $(this).data("id");
    let message = `Are you sure you want to ${
      deletedButtonName ? deletedButtonName : "delete"
    } this row?`;
    var confirmation = confirm(message);
    if (confirmation && deleteCallback) {
      deleteCallback(dataId);
    }
  });
}
