var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", "https://karlie.vavo.be"+window.location.search, false ); // false for synchronous request
xmlHttp.send( null );
return xmlHttp.responseText;