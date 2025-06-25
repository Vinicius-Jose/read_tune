
function generate_playlist(book_id) {
    element = document.getElementById(`select_${book_id}`)
    style = element.value
    window.location.href = `/book/${book_id}/?style=${style}`
}