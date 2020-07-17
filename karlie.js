

async function hello()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "https://karlie.vavo.be"+window.location.search); // false for synchronous request
    xmlHttp.send( null );
}
hello();