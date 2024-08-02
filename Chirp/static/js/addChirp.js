window.onload = () => {
    document.getElementById("image").addEventListener('change', (e) => {
        document.getElementById("show").src = URL.createObjectURL(e.target.files[0])
    })
}