<template>
    <div class="container">
        <h1>Checkout</h1>
        <form>
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" v-model="name" required>
            </div>
            <div class="mb-3">
                <label for="address" class="form-label">Address</label>
                <input type="text" class="form-control" id="address" v-model="address" required>
            </div>
            <div class="mb-3">
                <label for="city" class="form-label">City</label>
                <input type="text" class="form-control" id="city" v-model="city" required>
            </div>
            <div class="mb-3">
                <label for="phone" class="form-label">Phone Number</label>
                <input type="tel" class="form-control" id="phone" v-model="phone" required>
            </div>
        </form>
        <button class="btn btn-primary" @click="Order()">Submit</button>
    </div>
</template>
  
<script>
import axios from 'axios';


export default {

    data() {
        return {
            items: [],
            name: '',
            address: '',
            city: '',
            phone: '',
        };
    },
    mounted() {
        document.title = 'Checkout | AFA'
        this.items = this.$store.state.cart.items
    },
    methods: {
        async Order() {
            this.$store.commit('setIsLoading', true)

            for (let i = 0; i < this.items.length; i++) {
                const item = this.items[i]

                const data = {
                    'name': this.name,
                    'address': this.address,
                    'city': this.city,
                    'phone': this.phone,
                    'item_name': item.product.name,
                    'item_size': item.size,
                    'item_price': item.product.price,
                }

                await axios
                    .post('/api/v1/checkout/', data)
                    .then(response => {
                        this.$store.commit('ClearCart')
                        this.$router.push('/cart/success')
                    })
                    .catch(error => {
                        this.error.push('something went wrong. Please try again')
                    })
                    this.$store.commit('setIsLoading', false)

            }
        }
    }
};
</script>
  
<style scoped>
.container {
    margin-top: 50px;
    color: white;
}

.container form {
    width: 50%;
}

.container form input {

    background: #262626;
    padding: 15px;
    color: #fff;
    font-size: 18px;
    border-image: linear-gradient(to right, #9671F6, #FD6756) 1;
    height: 50px;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;

}

button {
    background-image: solid;
    background-image: linear-gradient(to right, #9671F6, #FD6756) 1;
    margin-top: 30px;
    width: 50%;
    height: 40px;
}

@media only screen and (max-width: 600px) {
    .container {
        margin-top: 0px;
        color: white;
    }

    .container form {
        width: 100%;
    }

    .container form input {

        background: #262626;
        padding: 15px;
        color: #fff;
        font-size: 18px;
        border-image: linear-gradient(to right, #9671F6, #FD6756) 1;
        height: 50px;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;

    }

    .container form button {
        background-image: solid;
        background-image: linear-gradient(to right, #9671F6, #FD6756) 1;
        margin-top: 30px;
        width: 100%;
        height: 40px;
    }

}
</style>
  