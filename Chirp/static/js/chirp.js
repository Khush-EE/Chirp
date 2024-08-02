const toggleLike = async (id) => {
    const response = await fetch(`/like?id=${id}`);
    // console.log("response", response)
    const data = await response.json();
    // console.log(data)
    if(data.success) {
        const likesCount = document.getElementById('likesCount')
        const toggle = document.getElementById('toggle')
        console.log(likesCount.innerText)
        if(data.liked) {
            likesCount.innerText = Number(likesCount.innerText) + 1
            toggle.innerHTML = '<i class="fa-solid fa-heart" style={margin: "3px";}></i>'
        } else {
            likesCount.innerText = Number(likesCount.innerText) - 1
            toggle.innerHTML = '<i class="fa-regular fa-heart" style={margin: "3px";}></i>'
        }
    }
}