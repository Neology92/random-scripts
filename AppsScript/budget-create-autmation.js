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

function moveSheetToFolder(sheet, folder) {
  const file = DriveApp.getFileById(sheet.getId());
  file.moveTo(folder);
}

function getSheetNameByMonthName(monthNo) {
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

function clearBudgetEntries(sheet) {
  console.log("TODO Budget clean");
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

  // Get previous month's sheet
  const prevYearSubfolderName = prevYear.toString();
  const prevYearSubfolder = folder
    .getFoldersByName(prevYearSubfolderName)
    .next();
  const prevSheetName = getSheetNameByMonthName(prevMonth);
  const prevSheet = prevYearSubfolder.getFilesByName(prevSheetName).next();

  // Create a new sheet based on the previous month's sheet
  const nextSheetName = getSheetNameByMonthName(nextMonth);
  const newSheet = SpreadsheetApp.openById(prevSheet.getId()).copy(
    `test-${nextSheetName}`
  );

  const nextYearSubfolderName = nextYear.toString();
  const nextYearSubfolder = folder
    .getFoldersByName(nextYearSubfolderName)
    .next();

  moveSheetToFolder(newSheet, nextYearSubfolder);

  // Open the new sheet
  const newSheetId = newSheet.getId();
  const newSheetUrl = "https://docs.google.com/spreadsheets/d/" + newSheetId;

  clearBudgetEntries(newSheet);
  updateFWNincome(newSheet);
  sendInfoEmail(newSheetUrl, emailAddress);
}
