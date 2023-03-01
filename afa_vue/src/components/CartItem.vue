<template>
    <tr id="item">
        <td>
            <RouterLink :to="item.product.get_absolute_url" class="details">
                <img :src="item.product.get_thumbnail" alt="Product 1">
                {{ item.product.name }}
            </RouterLink>
        </td>
        <td>
            <p class="price">{{ item.product.price }}</p>
        </td>
        <td>
            <div class="size">
                <a @click="decrementSize(item)">-</a>
                <p>{{ item.size }} </p>
                <a @click="incrementSize(item)">+</a>
            </div>
        </td>
        <td><button class="delete" @click="removeFromCart(item)"><i class="fa-regular fa-trash trash" style="color: #e32400;"></i></button></td>
    </tr>
</template>

<style>
#item {
    text-decoration: none;
}

#item .details {
    color: white;
    text-decoration: none;
    font-size: 28px;
}

#item .details img {
    margin-right: 20px;
    height: 100px;
    border-radius: 5px;
}

#item .price {
    color: white;
    align-content: center;
    justify-content: center;
    margin-top: 10%;
}

#item .size {
    color: white;
    display: flex;
    margin-top: 10%;
    font-size: 28px;
    }

#item .size a{
    margin: 0 10px;
    cursor: pointer;
}

#item .delete{
    margin-top: 30px;
    color: white;
    background-color: transparent;
    text-decoration: none;
    border: none;
}

#item .trash{
    font-size: 25px;
}

@media only screen and (max-width: 600px) {
    #item {
    text-decoration: none;
}

#item .details {
    color: white;
    text-decoration: none;
    font-size: 18px;
}

#item .details img {
    margin-bottom: 5px;
    height: 80px;
    border-radius: 5px;
}

#item .price {
    color: white;
    align-content: center;
    justify-content: center;
    margin-top: 10%;
    font-size: 20px;
}

#item .size {
    color: white;
    display: flex;
    margin-top: 10%;
    font-size: 20px;
    }

#item .size a{
    margin: 0 10px;
    cursor: pointer;
    font-size: 20px;
}

#item .delete{
    margin-top: 13px;
    color: white;
    background-color: transparent;
    text-decoration: none;
    border: none;
}

#item .trash{
    font-size: 20px;
}
}
</style>

<script>

export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        decrementSize(item) {
            let s = Number(item.size)
            s -= 1
            item.size = String(s)
            this.updateCart()
        },
        incrementSize(item) {
            let s = Number(item.size)
            s += 1
            item.size = String(s)
            this.updateCart()
        },

        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },

        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart()
        }
    }
}

</script>