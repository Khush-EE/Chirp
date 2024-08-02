window.onload = () => {
    const contentBoxes = document.getElementsByClassName('content');

    for (let content of contentBoxes) {
        content.innerText = content.innerText.slice(0, 100);
    }

    console.log('executed')
}