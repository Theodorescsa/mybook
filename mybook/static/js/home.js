alls = document.querySelectorAll.bind(document)
one = document.querySelector.bind(document)
all_book = alls("div#book")
console.log(all_book)
for (var item = 0;item<all_book.length;item++) {
    console.log(item)
}