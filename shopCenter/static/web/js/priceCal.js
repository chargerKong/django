function priceCal(){
// (function(){
  let cart_footer_num = document.querySelector("#totalCount"),
  mz_checkboxs = document.querySelectorAll(".mz-checkbox"),
  add = document.querySelectorAll('mz-adder-add'),
  sub = document.querySelectorAll('mz-adder-subtract'),

  num = 0,
  cart_product_price = document.querySelectorAll(".cart-product-price.total"),
  singPrice = document.querySelectorAll(".prices"),
  total = 0;


//先执行一遍
cal()

cart_product_price.forEach(function(item,index){
	let nums = document.querySelectorAll('.goodsnum');
	cart_product_price[index].innerText = Number(nums[index].value)*Number(singPrice[index].innerText);
})

mz_checkboxs.forEach(function(item,index){
	item.onclick = cal
})


function cal(items,index){
    mz_checkbox = document.querySelectorAll("#mz-checkbox");
    cart_product_price = document.querySelectorAll(".cart-product-price.total");
    num = 0;
    total=0;
    totalPrice = document.getElementById("totalPrice");
    
    mz_checkbox.forEach(function(item,index){
    	if (item.classList.contains('checked')){
     		num++;
     		total += Number(cart_product_price[index].innerText)
  		}
    })
    cart_footer_num.innerText = num
    totalPrice.innerText = total;
  }
// })()
}

function returnId(){
	let mz_checkbox = document.querySelectorAll("#mz-checkbox"),
		id=[] ;
	mz_checkbox.forEach(function(item,index){
		if (item.classList.contains('checked')){
			var a =document.querySelectorAll("#goodsid");
			id.push( a[index].value)
		}
	})
	return id.join(",")
}

a=returnId();
