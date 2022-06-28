

{
    order_details : {
        product : [
            {
                product_id : 1,
                qty: 3
            },
            {
                product_id : 2,
                qty: 2
            }
        ]
    }
}

2.1  for loop on product
2.2  fire query on product table >> return product_id >>object
2.3  price = product_price* quqntity
2.4  create order in order table

order : 
    order_id : uuid
    user_id
    overall /total
    order_date
    order_status

order_details
    order_id
    priduct_id
    product_price 
    product_qty >>>> payload
     total price =  product_price * product_qty
