const emailAddress = "oskarlegner@gmail.com";

function triggerOnLastMondayOfTheMonth() {
  if (isLastMondayOfTheMonth()) {
    console.log("Hell yeah! Today is the last Monday of the month!");
    console.log("Creating a new budget sheet!");
    createBudgetSheet();
  }
}

function isLastMondayOfTheMonth() {
  const today = new Date();
  const currentMonth = today.getMonth();
  const currentDayOfWeek = today.getDay();

  // 0 is Sunday, lol
  if (currentDayOfWeek !== 1) return false;

  // Increment the date by 7 days to check if it's in the next month
  const nextMonday = new Date();
  nextMonday.setDate(nextMonday.getDate() + 7);

  // If the next Monday is in the next month, it means today is the last Monday of the current month
  return nextMonday.getMonth() !== currentMonth;
}

function shiftedDate(days) {
  const today = new Date();
  return new Date(today.getTime() + days * 24 * 60 * 60 * 1000);
}

function moveSpreadsheetToFolder(spreadsheet, folder) {
  const file = DriveApp.getFileById(spreadsheet.getId());
  file.moveTo(folder);
}

function getSpreadsheetNameByMonthName(monthNo) {
  const polishMonths = [
    "styczeń",
    "luty",
    "marzec",
    "kwiecień",
    "maj",
    "czerwiec",
    "lipiec",
    "sierpień",
    "wrzesień",
    "październik",
    "listopad",
    "grudzień",
  ];

  const monthName = polishMonths[monthNo];
  return `${monthNo + 1}-${monthName}-Budzet-domowy`;
}

function clearEntryLabelAndValue(startRange, row, col) {
  startRange.offset(row, col).clearContent(); // label
  startRange.offset(row, col + 1).clearContent(); // value
}

function clearExpensesEntries(spreadsheet) {
  const tabName = "Wydatki";
  const startCell = "M8";
  const untouchableEntries = ["planned"];

  // Choose tab
  const sheet = spreadsheet.getSheetByName(tabName);

  // Select starting cell
  const startRange = sheet.getRange(startCell);
  const lastRow = sheet.getLastRow();
  const lastCol = sheet.getLastColumn();

  // Get the data in the range
  const data = sheet
    .getRange(startRange.getRow(), startRange.getColumn(), lastRow, lastCol)
    .getValues();

  for (let row = 0; row < data.length; row += 1) {
    for (let col = 0; col < data[row].length; col += 2) {
      const label = data[row][col];
      if (untouchableEntries.includes(label)) continue;
      clearEntryLabelAndValue(startRange, row, col);
    }
  }
}

function isFormula(cell) {
  return cell.getFormula() !== "";
}

function clearPlannedExpenses(spreadsheet) {
  const tabName = "Wydatki";
  const startCell = "F8";

  const sheet = spreadsheet.getSheetByName(tabName);

  // Select starting cell
  const startRange = sheet.getRange(startCell);
  const lastRow = sheet.getLastRow();

  // Get the data in the range
  const data = sheet
    .getRange(startRange.getRow(), startRange.getColumn(), lastRow)
    .getValues();

  data.forEach((row, rowIndex) => {
    const currentCell = startRange.offset(rowIndex, 0);

    // If value is formula or label, skip
    if (isFormula(currentCell)) return;
    if (typeof currentCell.getValue() !== "number") return;

    // Copy default planned expenses
    // desc: Default values are in column E, next to each cleared entry
    //      If there is no default value, entry is cleared
    const defaultValueCell = startRange.offset(rowIndex, -1);
    defaultValueCell.copyTo(currentCell, { contentsOnly: true });
  });
}

function updateFWNincome(sheet) {
  console.log("TODO FWN");
}

function sendInfoEmail(sheetUrl, email) {
  const subject = "[Home Budget] New budget sheet created!";
  const body = `New budget sheet has been created!
You can find it here: ${sheetUrl}

  Cheers!`;
  GmailApp.sendEmail(email, subject, body);
}

function createBudgetSheet() {
  const prevMonth = shiftedDate(-7).getMonth();
  const nextMonth = shiftedDate(7).getMonth();
  const prevYear = shiftedDate(-7).getFullYear();
  const nextYear = shiftedDate(7).getFullYear();

  const folderName = "Budżet domowy";
  const folder = DriveApp.getFoldersByName(folderName).next();

  // Get previous month's Spreadsheet
  const prevYearSubfolderName = prevYear.toString();
  const prevYearSubfolder = folder
    .getFoldersByName(prevYearSubfolderName)
    .next();
  const prevSpreadsheetName = getSpreadsheetNameByMonthName(prevMonth);
  const prevSpreadsheet = prevYearSubfolder
    .getFilesByName(prevSpreadsheetName)
    .next();

  // Create a new Spreadsheet based on the previous month's Spreadsheet
  const nextSpreadsheetName = getSpreadsheetNameByMonthName(nextMonth);
  const newSpreadsheet = SpreadsheetApp.openById(prevSpreadsheet.getId()).copy(
    `test-${nextSpreadsheetName}`
  );

  const nextYearSubfolderName = nextYear.toString();
  const nextYearSubfolder = folder
    .getFoldersByName(nextYearSubfolderName)
    .next();

  moveSpreadsheetToFolder(newSpreadsheet, nextYearSubfolder);

  // Open the new Spreadsheet
  const newSpreadsheetId = newSpreadsheet.getId();
  const newSpreadsheetUrl =
    "https://docs.google.com/spreadsheets/d/" + newSpreadsheetId;

  const openSpreadsheet = SpreadsheetApp.openById(newSpreadsheetId);
  clearExpensesEntries(openSpreadsheet);
  updateFWNincome(openSpreadsheet);

  sendInfoEmail(newSpreadsheetUrl, emailAddress);
}
