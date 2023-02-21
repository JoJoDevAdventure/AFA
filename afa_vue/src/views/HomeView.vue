<template>
  <div class="home">
    <section id="header-section">
      <div class="container">
        <div class="row">
          <div class="col-lg-6">
            <h1 class="display-4">New<br>Collection <br> <span>Corales</span></h1>
            <p class="lead">From under the sea<br>To right under your feet</p>
            <button class="btn btn-primary btn-lg btn-outline-gradient ">Shop now</button>
          </div>
          <div class="col-lg-6">
          </div>
        </div>
      </div>
    </section>
    <!-------------------------- Popular products  -------------------->
    <section id="popular-products-section">
      <div class="container">
        <h1 class="text-left">Popular <span>products</span> </h1>
        <div class="row">

          <div class="col-md-6 col-lg-3"
            v-for="product in latestProducts"
            v-bind:key="product.id"
            v-bind:product="product">

            <router-link class="card"
            v-bind:to="product.get_absolute_url">
              <img :src="product.get_thumbnail" class="card-img-top" alt="Product 1">
              <div class="card-body">
                <h5 class="card-title text-white">{{product.title}}</h5>
                <div class="d-flex justify-content-between align-items-center">
                  <span class="price"> {{product.price}} DT</span>
                  <router-link v-bind:to="product.get_absolute_url" class="btn btn-primary">Add to Cart</router-link>
                </div>
              </div>
            </router-link>
            
          </div>
        </div>
      </div>
    </section>
    <!-------------------------- Collections  -------------------->
    <section id="afa-collections-section">
      <div class="container">
        <div class="d-flex justify-content-between align-items-center">
          <h1 class="title">AFA <span>Collections</span> </h1>
          <router-link to="/collections" class="btn btn-primary">See All
            Collections</router-link>
        </div>
        <div class="row">
          <div class="col-md-4"
            v-for="collection in latestCollections"
            v-bind:key="collection.id"
            v-bind:collection="collection">

            <router-link class="card"
              v-bind:to="collection.get_absolute_url">
              <img :src="collection.get_thumbnail" class="card-img-top" alt="Collection 1">
              <div class="card-body">
                <h5 class="card-title text-white">{{ collection.name }} <span>&rarr;</span></h5>
              </div>
            </router-link>

          </div>
        </div>
      </div>
    </section>

    <!-------------------------- Services  -------------------->
    <section id="our-services-section">
      <div class="container">
        <h1 class="text-center">Our <span class="services-text">Services</span></h1>
        <div class="row">
          <div class="col-md-4">
            <div class="card">
              <div class="card-outline">
                <i class="fas fa-icon fa-regular fa-paintbrush fa-fade"></i>
                <h5 class="card-title">Custom model</h5>
                <p class="card-description">Description of Service 1</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card">
              <div class="card-outline">
                <i class="fas fa-icon fa-regular fa-truck-fast fa-bounce"></i>
                <h5 class="card-title">Free Shipping</h5>
                <p class="card-description">Description of Service 2</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card">
              <div class="card-outline">
                <i class="fas fa-icon fa-regular fa-headset fa-shake"></i>
                <h5 class="card-title">Customer Service</h5>
                <p class="card-description">Description of Service 3</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section id="about-us">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <img src="../assets/About-us.svg" alt="About Us Image" class="about-us-image">
          </div>
          <div class="col-md-6">
            <p class="small-text" style="color: #FD6756">About Us</p>
            <h1>We Provide <span>High <br> Quality </span>Shoes.</h1>
            <p class="about-us-description">Air Force Artisans, We are a band of creators & Artists who love to transform
              boring sneakers into masterpieces. We only deliver high quality and unique designs.</p>
            <p>Stay up-to-date with the latest collections and be the first to know when it's available, subscribe to our
              newsletter and join our community of fashion lovers!</p>
            <form class="form-group">
              <input type="email" class="form-control" placeholder="Your e-mail">
              <button class="btn btn-primary" type="submit">Subscribe</button>
            </form>
          </div>
        </div>
      </div>
    </section>

    <section id="testimonials-section">
      <div class="container">
        <h1 class="text-left testimonial-title">What our<br><span>Customers say</span></h1>
        <div class="row">
          <div class="col-md-4">
            <div class="card testimonial-card">
              <img src="path_to_customer_image_1" alt="Customer 1" class="rounded-image">
              <p class="customer-name">John Doe</p>
              <p class="review-description">"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam volutpat eros
                ac nisi pulvinar, at consequat enim gravida."</p>
              <img src="../assets/stars.svg" alt="Star Rating" class="star-rating">
            </div>
          </div>
          <div class="col-md-4">
            <div class="card testimonial-card">
              <img src="path_to_customer_image_2" alt="Customer 2" class="rounded-image">
              <p class="customer-name">Jane Smith</p>
              <p class="review-description">"Ut fringilla, urna nec condimentum pellentesque, arcu tellus interdum mauris,
                vel eleifend nunc turpis ut purus."</p>
              <img src="../assets/stars.svg" alt="Star Rating" class="star-rating">
            </div>
          </div>
          <div class="col-md-4">
            <div class="card testimonial-card">
              <img src="path_to_customer_image_3" alt="Customer 3" class="rounded-image">
              <p class="customer-name">Michael Johnson</p>
              <p class="review-description">"Aenean consectetur neque dolor, at ullamcorper tellus interdum vel. Donec
                sagittis sapien sit amet magna feugiat."</p>
              <img src="../assets/stars.svg" alt="Star Rating" class="star-rating">
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'home',
  data() {
    return {
      latestProducts: [],
      latestCollections: [],
    }
  },
  mounted() {
    this.getLatestProducts()
    this.getLatestCollections()
    document.title = 'Home | AFA'
  },

  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
          this.$store.commit('setIsLoading', false)
        })
        .catch(error => {
          console.log(error)
        })
    },

    async getLatestCollections() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/v1/latest-collections/')
        .then(response => {
          this.latestCollections = response.data
          this.$store.commit('setIsLoading', false)
        })
        .catch(error => {
          console.log(error)
        })


    },
  }
}
</script>

<style>
@font-face {
  font-family: 'Yipes';
  src: url('../assets/Yipes\ Regular.otf') format('otf');
}

.home {
  background-color: #0E0F0A;
}

#header-section {
  margin-top: -70px;
  background-image: url(../assets/Background1440.jpg);
  width: 100%;
  background-size: cover;
  background-position: center;
  height: 80vh;
}

#header-section .col-lg-6 {
  color: white;
}

#header-section .col-lg-6 h1 {
  color: white;
  font-weight: bold;
  font-size: 96px;
}

#header-section .col-lg-6 span {
  color: #D55F37;
  font-weight: lighter;
  font-family: 'Yipes';
}

#header-section .btn-outline-gradient {
  margin-top: 30px;
  background: none;
  color: #fff;
  border: 2px solid transparent;
  background-clip: padding-box;
  background-image: linear-gradient(to right, #9570F7, #FD6756);
}

#header-section .btn-outline-gradient:hover {
  color: #fff;
  background-image: linear-gradient(to right, #9570F7, #FD6756);
}

#popular-products-section {
  margin-top: 10px;
}

#popular-products-section .text-left {
  color: #fff;
  margin-bottom: 50px;
  font-size: 58px;
}

#popular-products-section .text-left span {
  color: #FD6554;
}

#popular-products-section .popular-products-section h1 {
  font-size: 24px;
  font-weight: bold;
  text-align: left;
}

#popular-products-section .card {
  background: none;
  border: none;
  box-shadow: 0 2px 8px 0 #BD5353;
  transition: box-shadow 0.3s ease;
  text-decoration: none;
}

#popular-products-section button {
  background-color: #4400FF;
  outline: none;
}

#popular-products-section .price {
  color: white;
}

#popular-products-section .card:hover {
  background-image: linear-gradient(to right, #9570F7, #FD6756);
  box-shadow: none;
}

#popular-products-section .card button:hover{
  background-color: #0E0F0A;
  border-width:1px ;
  border-color: #4400FF;
}

#popular-products-section .card-title {
  font-size: 24px;
}

#afa-collections-section {
  margin-top: 100px;
}

#afa-collections-section h1 {
  margin-bottom: 0px;
  font-size: 58px;
  color: #fff;
}

#afa-collections-section h1 span {
  color: #FD6554;
}

#afa-collections-section .btn {
  height: 50px;
  background-image: linear-gradient(to right, #9570F7, #FD6756);
  transform: 1s;
}

#afa-collections-section .btn:hover {
  background-color: #0E0F0A;
  background-image: none;
}

#afa-collections-section .card {
  background-color: transparent;
  transition: box-shadow 0.3s ease;
  text-decoration: none;
}

#afa-collections-section .card:hover {
  box-shadow: 0 2px 8px 0 #BD5353;
}

#afa-collections-section .card {
  background-color: transparent;
  margin: 50px;
}

#our-services-section {
  margin-top: 50px;
}

#our-services-section h1 {
  font-size: 58px;
  margin-bottom: 50px;
  color: #fff;
}

#our-services-section .our-services-section .services-text {
  font-weight: bold;
}

#our-services-section .card {
  text-align: center;
  cursor: pointer;
  position: relative;
  height: 300px;
  border: none;
  overflow: hidden;
  transition: 0.3s;
  background-color: transparent;
}

#our-services-section .card .card-outline {
  padding: 20px;
  background: none;
  border: 5px solid transparent;
  border-image: linear-gradient(to right, #9570F7, #FD6756) 1;
  border-image-slice: 1;
  transition: 0.3s;
  height: 300px;
}

#our-services-section .card:hover .card-outline {
  background-image: linear-gradient(to right, #9570F7, #FD6756);
  border: none;
}

#our-services-section .card .fa-icon {
  font-size: 80px;
  color: white;
  margin-bottom: 10px;
  margin-top: 60px;
  transition: 0.3s;
}

#our-services-section .card:hover .fa-icon {
  margin-top: 20px;
  transition: 0.3s;
}

#our-services-section .card .card-title {
  color: white;
  margin-top: 10px;
  font-weight: bold;
}

#our-services-section .card .card-description {
  display: none;
  color: white;
  transition: 0.3s;
}

#our-services-section .card:hover .card-description {
  display: block;
  transition: 0.3s;
}

#about-us {
  margin-top: 200px;
}

#about-us .small-text{
margin-top: 50px;
}

#about-us h1 {
  color: white;
  letter-spacing: 0.085em;
  font-weight: 600;
  font-size: 56px;
  line-height: 68px;
}

#about-us h1 span {
  color: #FD6554;
}

#about-us p {
  color: #c1c1c1
}

#about-us form {
  display: flex;
  margin-top: 10px;
}

#about-us form input {
  margin-right: 10px;
  width: 75%;
}

#testimonials-section {
  margin-top:  100px;
}

#testimonials-section .testimonial-title {
  font-size: 58px;
  line-height: 1.2;
  color: white;;
  margin-bottom: 50px;
}

#testimonials-section .row {
  padding-top: 50px;
  padding-bottom: 50px;
  position: relative;
  background-size: 1000px;
}

#testimonials-section .testimonial-card {
  padding: 30px;
  border-radius: 10px;
  background-color: transparent;
  margin-bottom: 30px;
}

#testimonials-section .rounded-image {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin: 0 auto;
  margin-bottom: 10px;
  display: block;
  background-color: white;
}

#testimonials-section .customer-name {
  color: #ffffff;
  font-weight: bold;
  text-align: center;
  margin-top: 10px;
}

#testimonials-section .review-description {
  color: #c1c1c1;
  text-align: center;
  margin-top: 10px;
}

#testimonials-section .star-rating {
  display: block;
  margin: 0 auto;
  margin-top: 20px;
}

#testimonials-section .testimonial-card:hover {
  margin-top: -20px;
  transition: 1s;
  background-color: #343434;
}

@media only screen and (max-width: 600px) {
  #header-section {
    background-image: url(../assets/Background1280.jpg);
  }
}

@media only screen and (max-width: 600px) {
  .home {
    background-color: #0E0F0A;
  }

  #header-section {
    margin-top: 5%;
    margin-bottom: 10%;
  }

  #header-section .col-lg-6 {
    color: white;
  }

  #header-section .col-lg-6 h1 {
    color: white;
    font-weight: bold;
    font-size: 48px;
    text-align: left;
  }

  #header-section .col-lg-6 span {
    color: #D55F37;
    font-weight: lighter;
    font-family: 'Yipes';
  }

  #header-section .btn-outline-gradient {
    margin-top: 30px;
    background: none;
    color: #fff;
    border: 2px solid transparent;
    background-clip: padding-box;
    background-image: linear-gradient(to right, #9570F7, #FD6756);
  }

  #header-section .btn-outline-gradient:hover {
    color: #fff;
    background-image: linear-gradient(to right, #9570F7, #FD6756);
  }

  #popular-products-section {
    margin-top: 50px;
  }

  #popular-products-section .text-left {
    color: #fff;
    margin-bottom: 50px;
    font-size: 36px;
    text-align: left;
  }

  #popular-products-section .text-left span {
    color: #FD6554;
  }

  #popular-products-section .popular-products-section h1 {
    font-size: 18px;
    font-weight: bold;
    text-align: center;
  }

  #popular-products-section .card {
    background: none;
    border: none;
    box-shadow: 0 2px 8px 0 #BD5353;
    transition: box-shadow 0.3s ease;
    margin: 0px 50px 50px;
  }

  #popular-products-section button {
    background-color: #4400FF;
    outline: none;
  }

  #popular-products-section .price {
    color: white;
  }

  #popular-products-section .card:hover {
    background-image: linear-gradient(to right, #9570F7, #FD6756);
    box-shadow: none;
  }

  #popular-products-section .card-title {
    font-size: 18px;
  }

  #afa-collections-section {
    margin-top: 10%;
  }

  #afa-collections-section .title {
    color: #fff;
    margin-bottom: 50px;
    font-size: 36px;
    text-align: left;
  }

  #afa-collections-section .title span {
    color: #FD6554;
  }

  #afa-collections-section .btn {
    height: 65px;
    margin-bottom: 40px;
    text-decoration: none;
  }

  #afa-collections-section .btn:hover {
    background-color: transparent;
    background-image: none;
  }

  #afa-collections-section .card {
    background-color: transparent;
    margin: 0px 50px 50px;
  }

  #our-services-section {
    margin-top: 50px;
  }

  #our-services-section h1 {
    font-size: 36px;
    margin-bottom: 50px;
    color: #fff;
  }

  #our-services-section .our-services-section .services-text {
    font-weight: bold;
  }

  #our-services-section .card {
    text-align: center;
    cursor: pointer;
    position: relative;
    height: 300px;
    border: none;
    overflow: hidden;
    transition: 0.3s;
    background-color: transparent;
    margin: 0px 50px 50px;
  }

  #our-services-section .card .card-outline {
    padding: 20px;
    background: none;
    border: 5px solid transparent;
    border-image: linear-gradient(to right, #9570F7, #FD6756) 1;
    border-image-slice: 1;
    transition: 0.3s;
    height: 300px;
  }

  #our-services-section .card:hover .card-outline {
    background-image: linear-gradient(to right, #9570F7, #FD6756);
    border: none;
  }

  #our-services-section .card .fa-icon {
    font-size: 80px;
    color: white;
    margin-bottom: 10px;
    margin-top: 60px;
    transition: 0.3s;
  }

  #our-services-section .card:hover .fa-icon {
    margin-top: 20px;
    transition: 0.3s;
  }

  #our-services-section .card .card-title {
    color: white;
    margin-top: 10px;
    font-weight: bold;
  }

  #our-services-section .card .card-description {
    display: none;
    color: white;
    transition: 0.3s;
  }

  #our-services-section .card:hover .card-description {
    display: block;
    transition: 0.3s;
  }

  #about-us {
    margin-top: 100px;
  }

  #about-us .about-us-image{
    height: 65%;
  }

  #about-us .small-text {
    margin-top: 0px;
    font-size: 18px;
    text-align: left;
  }

  #about-us h1 {
    color: white;
    letter-spacing: 0.085em;
    font-weight: 600;
    font-size: 36px;
    line-height: 1.2;
    text-align: left;
  }

  #about-us h1 span {
    color: #FD6554;
  }

  #about-us p {
    color: #c1c1c1;
    text-align: left;
  }

  #about-us form {
    display: flex;
  }

  #about-us form input {
    margin: 0 auto;
    margin-bottom: 10px;
    width: 65%;
  }

  #about-us form button{
    margin: 0 auto;
    margin-bottom: 10px;
    width: 30%;
  }

  #testimonials-section {
    margin-top: 50px;
  }

  #testimonials-section .testimonial-title {
    font-size: 36px;
    line-height: 1.2;
    color: white;
    margin-bottom: 30px;
    text-align: center;
  }

  #testimonials-section .row {
    padding-top: 30px;
    padding-bottom: 30px;
    position: relative;
    background-size: 1000px;
  }

  #testimonials-section .testimonial-card {
    padding: 20px;
    border-radius: 10px;
    background-color: transparent;
    margin-bottom: 20px;
    margin: 0px 40px 40px;
  }

  #testimonials-section .rounded-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin: 0 auto;
    margin-bottom: 10px;
    display: block;
    background-color: white;
  }

  #testimonials-section .customer-name {
    color: #ffffff;
    font-weight: bold;
    text-align: center;
    margin-top: 10px;
  }

  #testimonials-section .review-description {
    color: #c1c1c1;
    text-align: center;
    margin-top: 10px;
  }

  #testimonials-section .star-rating {
    display: block;
    margin: 0 auto;
    margin-top: 20px;
  }

  #testimonials-section .testimonial-card:hover {
    margin-top: -10px;
    transition: 0.5s;
    background-color: #343434;
  }
}

</style>




