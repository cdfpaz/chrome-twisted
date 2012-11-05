// Object to hold information about the current page
var pageInfo = {
    "title": document.title
};

// Send the information back to the extension
chrome.extension.sendRequest(pageInfo);