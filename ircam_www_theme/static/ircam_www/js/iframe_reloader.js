// In the <iframe> host page
window.addEventListener("message", function(message) {
    if(message.data == 'reload') {
        console.log('Reloading the iframe...');
        var iframe = document.getElementById("shop-iframe");
        iframe.src = iframe.src;
    }
}, false);
