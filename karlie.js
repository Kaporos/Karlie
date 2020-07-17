

async function hello()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "SERVER_ADDR"+window.location.search); // false for synchronous request
    xmlHttp.send( null );
}
hello();