<template>
    <div id="cart">
        <div class="container">
            <h1 class="title text-white">Cart</h1>

            <table class="table full-with" v-if="cartTotalLength">
                <thead>
                    <tr class="titles">
                        <th>Product</th>
                        <th>Price</th>
                        <th>Size</th>
                        <th></th>
                    </tr>
                </thead>

                <tbody>
                    <CartItem v-for="item in cart.items" v-bind:key="item.product.id" v-bind:initialItem="item" v-on:removeFromCart="removeFromCart"/>
                </tbody>
            </table>
            <p class="empty" v-else>Cart is currently empty.</p>

            <div v-if="cartTotalLength" class="summary">
                <h2>Summary</h2>
                <strong> {{ Number(CartTotalPrice).toFixed(2) }} DT</strong>, {{ cartTotalLength }} items

                <hr>
                <Router-link to="/cart/checkout" class="btn btn-grad"> Proceed to checkout</Router-link>
            </div>
        </div>

    </div>
</template>

<script>
import CartItem from '@/components/CartItem.vue';
export default {
    name: 'cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        document.title = 'Cart | AFA'
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.length
        },
        CartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                Number(acc)
                return acc += curVal.product.price
            }, 0)
        }
    }
}
</script>

<style>
#cart {
    min-height: 50vh;
}

#cart .empty {
    color: white;
    text-align: center;
    margin-top: 10%;
    font-size: 28px;
}

#cart .titles {
    color: white;
}

table td, table th {
  border: none;
}

#cart .summary {
    color: white;
    margin-top: 10%;
}

#cart .btn-grad {
    margin-top: 30px;
    background: none;
    color: #fff;
    border: 2px solid transparent;
    background-clip: padding-box;
    background-image: linear-gradient(to right, #9570F7, #FD6756);
  }

  #cart .btn-grad:hover {
    color: #fff;
    background-color: #0E0F0A;
    background-image: none;
    border: 2px solid #9570F7;
  }

  @media only screen and (max-width: 600px) { }
</style>