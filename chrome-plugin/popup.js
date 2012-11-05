var req = new XMLHttpRequest();
req.open(
    "GET",
    "http://10.0.0.106:8088/login?" + chrome.i18n.getMessage("@@extension_id"),
    true);
req.onload = loginResponse;
req.send(null);

function loginResponse() {

  try {
    ret = JSON.parse( req.responseText );
    if ( ret.ack == chrome.i18n.getMessage("@@extension_id") ) {
        console.log('==>', ret);        
    }
  } catch(err) {
    ret = err
  }
}

function onPageInfo(o) { 
    document.getElementById("textUrl").value = o.title; 
} 

window.onload = function() { 
    var bg = chrome.extension.getBackgroundPage();
    bg.getPageInfo(onPageInfo);
}
