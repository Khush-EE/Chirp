const items = document.getElementsByTagName('li')

window.addEventListener("load", (e) => {
    Array.from(items).forEach(element => {
        const endpoint = element.firstChild.getAttribute("href");
        if(window.location.pathname.slice(0) == endpoint) {
            element.classList.add('active');
        } else {
            element.classList.remove('active')
        }
    });
});

document.getElementsByTagName('img')[0].addEventListener('click', () => {
    if(document.getElementsByClassName('dropdown')[0].style.opacity == '0') {
        document.getElementsByClassName('dropdown')[0].style.opacity = 1;
    } else {
        document.getElementsByClassName('dropdown')[0].style.opacity = 0;
    }
})

// items[1].addEventListener()
const nav = (id) => {
    window.location.pathname = `/chirp/${id}`
}