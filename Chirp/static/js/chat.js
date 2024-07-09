let reciever = null;
let chatSocket = null;
let room_name = null;


const loadChats = async (username) => {
    const response = await fetch(`/chats/${username}`)
    if(response.status == 200) {
        const data = await response.json()
        let text = ``
        for(let chat of data.chats){
            text+=`${chat.sender}: ${chat.message}\n`
        }
        document.getElementsByClassName('chats')[0].innerText = text
        localStorage.setItem("reciever", username)
        reciever = username;
        room_name = data.room_name;

        establishChatSocketConnection();
    }
}

const establishChatSocketConnection = () => {

    if(room_name == null) return;

    if(chatSocket != null) {
        chatSocket.close();
    }

    chatSocket = new WebSocket('ws://' + window.location.host + `/ws/chat/${room_name}/`);

    chatSocket.onopen = function() {
        console.log('WebSocket connection established.');
    };
    
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const message = data['message'];
        console.log("Incoming", message)
        document.getElementsByClassName('chats')[0].innerText += `${data.sender}: ${data.message}\n`
    };
    
    chatSocket.onclose = function(e) {
        console.log(e)
        console.log('Chat socket closed');
    };
    
}


function sendMessage(sender) {
    const message = document.getElementById('inp').value
    chatSocket.send(JSON.stringify({
        'sender': sender,
        'reciever': localStorage.getItem('reciever'),
        'message': message
    }));
    document.getElementById('inp').value = ''
}


