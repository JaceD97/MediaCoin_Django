function getUUID() {
	function s4() {
		return Math.floor((1 + Math.random()) * 0x10000)
			.toString(16)
			.substring(1);
	}
	return s4() + s4() + '-' + s4() + '-' + s4() + '-' + s4() + '-' + s4() + s4() + s4();
}

function getCurUserIdentify() {
	var name = 'userIdentifyID' + "=";
	var decodedCookie = decodeURIComponent(document.cookie);
	var ca = decodedCookie.split(';');
	for(var i = 0; i < ca.length; i++) {
	    var c = ca[i];
	    while (c.charAt(0) == ' ') {
	        c = c.substring(1);
	    }
	    if (c.indexOf(name) == 0) {
	        return c.substring(name.length, c.length);
	    }
	}
	return "";
}