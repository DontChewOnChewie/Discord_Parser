let json_view, chat_view, content_div;
let chat_data;

window.onload = () => {
    content_div = document.querySelector(".content");
    chat_data = content_div.innerHTML;
    
    json_view = document.getElementById("json-view");
    json_view.addEventListener("click", function() { 
        if (json_view.className == "") {
            json_view.className = "active-view";
            chat_view.className = "";
            content_div.innerHTML = json_data;
        }
    });

    chat_view = document.getElementById("chat-view");
    chat_view.addEventListener("click", function() { 
        if (chat_view.className == "") {
            chat_view.className = "active-view";
            json_view.className = "";
            content_div.innerHTML = chat_data;
        }
     });
}
