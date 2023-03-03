<template>
  <div id="collection-details">
    <div class="head">
      <h2 class="title"> {{ collection.name }} </h2>
      <p class="desc">{{ collection.description }}</p>
    </div>
    <div class="row">

      <div class="col-md-6 col-lg-3" v-for="product in allProducts" v-bind:key="product.id" v-bind:product="product">

        <router-link class="card" v-bind:to="product.get_absolute_url">
          <img :src="product.get_thumbnail" class="card-img-top" alt="Product 1">
          <div class="card-body">
            <h5 class="card-title text-white">{{ product.title }}</h5>
            <div class="d-flex justify-content-between align-items-center">
              <span class="price"> {{ product.price }} DT</span>
              <button class="btn btn-primary">Add to Cart</button>
            </div>
          </div>
        </router-link>

      </div>
    </div>
  </div>
</template>

<style>
/* All collectionsa section */
/* Latest products section */
#collection-details {
  margin-bottom: 50px;
  padding: 10px 10%;
}

#collection-details .head {
  gap: 20px;
  margin-bottom: 30px;
}

#collection-details .title {
  color: white;
  font-size: 52px;
  text-align: center;
  margin-bottom: 30px;
}

#collection-details .desc {
  color: white;
  font-size: 20px;
  text-align: center;
  margin-bottom: 60px;
}

#collection-details .row {
  align-items: center;
}

#collection-details .card {
  background: none;
  border: none;
  box-shadow: 0 2px 8px 0 #BD5353;
  transition: box-shadow 0.3s ease;
  text-decoration: none;
}

#collection-details button {
  background-color: #4400FF;
  outline: none;
}

#collection-details .price {
  color: white;
}

#collection-details .card:hover {
  background-image: linear-gradient(to right, #9570F7, #FD6756);
  box-shadow: none;
}

#collection-details .card button:hover{
  background-color: #0E0F0A;
  border-width:1px ;
  border-color: #4400FF;
}

#collection-details .card-title {
  font-size: 24px;
}

@media only screen and (max-width: 600px) {
  #collection-details .card {
    margin: 20px 5px;
}

}

</style>
  
<script>
import axios from 'axios'

export default {
  name: 'CollectionDetails',
  data() {
    return {
      collection: {},
      allProducts: []
    }
  },
  mounted() {
    this.getCollection()
    this.getProducts()

    document.title = 'Collection | AFA'
  },
  methods: {
    getCollection() {
      this.$store.commit('setIsLoading', true)
      const collection_slug = this.$route.params.collection_slug

      axios
        .get(`/api/v1/collections/${collection_slug}`)
        .then(response => {
          this.collection = response.data
          this.$store.commit('setIsLoading', false)
        })

        .catch(error => {
          console.log(error)
        })
    },

    getProducts() {
      const collection_slug = this.$route.params.collection_slug

      axios
        .get(`/api/v1/collections/${collection_slug}/all`)
        .then(response => {
          this.allProducts = response.data
        })

        .catch(error => {
          console.log(error)
        })
    },
  }
}
</script>