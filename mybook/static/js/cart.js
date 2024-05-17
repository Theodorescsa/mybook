var btnAddToCarts = document.getElementsByClassName("add-to-cart")
for(i=0; i<btnAddToCarts.length;i++) {
    btnAddToCarts[i].addEventListener("click",function(){
        var itemId = this.dataset.itemId
        var action = this.dataset.action
        
        console.log("itemId",itemId,"action",action)
        addToCart(itemId,action) 
    })
}
function addToCart(itemId, action) {
    var url = "/cart/add_to_cart/"
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({
            "itemId": itemId,
            "action": action
        })
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        console.log("data", data)
        // document.getElementsById('cart').innerText= data.total
    })
    .catch((error)=>{
        console.log("error", error)
    })
}