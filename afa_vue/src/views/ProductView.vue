<template>
    <div class="container">
        <div class="row">
            <div class="col-lg-6">
                <h1 class="product-title">{{ product.name }}</h1>
                <img :src="product.get_image" alt="Product Image" class="product-image">
            </div>
            <div class="col-lg-6">
                <div class="product-details">
                    <p class="product-description">{{ product.description }}</p>
                    <div class="buy">
                        <div class="form-group">
                            <label for="size">Size:</label>
                            <input type="number" id="size" class="form-control" placeholder="36" value="36">
                        </div>
                        <div class="price-tag">
                            <span class="price">{{ product.price }}DT</span>
                            <button class="add-to-cart-btn" @click="addToCart">Add to cart</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            size: 36,
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const collection_slug = this.$route.params.collection_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${collection_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title = this.product.name + ' | ' + this.product.collection_slug
                    this.$store.commit('setIsLoading', false)
                })

                .catch(error => {
                    console.log(error)
                })


        },

        addToCart() {
            this.size = document.getElementById("size").value
            const item = {
                product: this.product,
                size: this.size,
            }

            this.$store.commit('addToCart', item)
        }

    }
}
</script>

<style>
.row {
    margin-top: 70px;
}

.product-details-container {
    display: flex;
    align-items: space-between;
}

.product-title {
    color: white;
    font-size: 48px;
    margin-bottom: 30px;
}

.product-image {
    width: 100%;
    max-width: 500px;
    height: auto;
    border-radius: 20px;
}

.product-description {
    margin-top: 70px;
    font-size: 16px;
    margin-bottom: 10px;
    color: rgb(133, 133, 133);
    white-space: pre-line;
}

.buy {
    margin-top: 75px;
}

.form-group {
    display: flex;
}

.form-group label {
    margin-right: 30px;
    color: white;
    font-size: 24px;
}

.form-group input {
    background: #262626;
    width: 15%;
    color: #fff;
    font-size: 18px;
    border-image: linear-gradient(to right, #9370F9, #FD6554) 1;
}

.price-tag {
    display: flex;
    margin-top: 50px;
}

.price {
    color: #fff;
    margin-right: 30px;
    font-size: 24px;
    margin-top: 5px;
}

.add-to-cart-btn {
    border-radius: 7px;
    border: 1px solid transparent;
    background: linear-gradient(90deg, #9370F9 0%, #FD6554 94.37%);
    padding: 10px 40px;
    text-decoration: none;
    color: white;
    transition: background 0.5s;
    text-align: center;
    cursor: pointer;
}

.add-to-cart-btn:hover {
    background: transparent;
    border: 1px solid #9370F9;
}

.price-tag {
    display: flex;
}


@media only screen and (max-width: 600px) {
    .row {
        margin-top: 10px;
    }

    .product-details-container {
        display: flex;
        align-items: space-between;
        align-items: center;
    }

    .product-title {
        color: white;
        font-size: 38px;
        margin-bottom: 30px;
    }

    .product-image {
        width: 100%;
        max-width: 500px;
        height: auto;
        border-radius: 20px;
    }

    .product-description {
        margin-top: 40px;
        font-size: 16px;
        margin-bottom: 10px;
        color: rgb(133, 133, 133);
        white-space: pre-line;
    }

    .buy {
        display: flex;
    align-items: left;
    justify-content: left;
    flex-wrap: wrap;
        display: flex;
    }

    .form-group {
        display: flex;
    }

    .form-group label {
        margin-right: 30px;
        color: white;
        font-size: 24px;
    }

    .form-group input {
        background: #262626;
        width: 45%;
        color: #fff;
        font-size: 18px;
        border-image: linear-gradient(to right, #9370F9, #FD6554) 1;
    }

    .price-tag {
        display: flex;
    align-items: left;
    justify-content: left;
    flex-wrap: wrap;
        margin-top: 20px;
    }

    .price {
        color: #fff;
        margin-right: 15px;
        font-size: 24px;
        margin-bottom:0px;
    }

    .add-to-cart-btn {
        border-radius: 7px;
        border: 1px solid transparent;
        background: linear-gradient(90deg, #9370F9 0%, #FD6554 94.37%);
        padding: 10px;
        height: 40px;
        width: 100px;
        text-decoration: none;
        color: white;
        font-size: 12px;
        transition: background 0.5s;
        text-align: center;
        cursor: pointer;
        margin-bottom:0px;
    }

    .add-to-cart-btn:hover {
        background: transparent;
        border: 1px solid #9370F9;
    }

}
</style>