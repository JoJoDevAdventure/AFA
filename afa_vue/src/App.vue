<template>
  <div class="spinner-wrapper text-danger" v-bind:class="{'isLoading': $store.state.isLoading}">
    <div class="spinner-border">
      <span class="visually-hidden"></span>
    </div>
  </div>
  <div class="main">
    <div class="container">
      <nav class="navbar navbar-expand-lg navbar-dark ">
        <router-link to="/" class="navbar-brand">
          <img src="./assets/AFALogo.png"  width="60" height="60" class="d-inline-block align-top" alt="">
        </router-link>

          <ul id="sidemenu" class=" navbar-nav mx-auto">
            <li class="nav-item">
              <router-link to="/" class="nav-link" @click="closemenu">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/about" class="nav-link" @click="closemenu">About</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/collections" class="nav-link" @click="closemenu">Collections</router-link>
            </li>
            <li class="nav-item">
              <a href="#testimonials-section" class="nav-link" @click="closemenu">Testimonials</a>
            </li>
            <i class="fas fa-times" @click="closemenu"></i>
          </ul>

          <div class="d-flex">
            <router-link to="/cart" class="cart" type="button" @click="closemenu">
              <i class="fa-regular fa-cart-shopping fa-bounce" style="color: #ffffff;" ></i>
              <span style="color: #ffffff;">({{ cartTotalLength }})</span>
            </router-link>
            <router-link to="/contact" class="btn btn-outline-gradient">
              Contact us
            </router-link>
          </div>

          <i class="fas fa-bars" @click="openmenu"></i>

      </nav>
    </div>
    <router-view />
    <!-- Remove the container if you want to extend the Footer to full width. -->
    <!-- Footer -->
    <footer class="text-center text-white" style="background-color: #22231F">
      <!-- Grid container -->
      <div class="container">
        <!-- Section: Links -->
        <section class="mt-5">
          <!-- Grid row-->
          <div class="row text-center d-flex justify-content-center pt-5">
            <!-- Grid column -->
            <div class="col-md-2">
              <h6 class="text-uppercase font-weight-bold">
                <router-link to="/about" class="text-white">About us</router-link>
              </h6>
            </div>
            <!-- Grid column -->

            <!-- Grid column -->
            <div class="col-md-2">
              <h6 class="text-uppercase font-weight-bold">
                <router-link to="/collections" class="text-white">Products</router-link>
              </h6>
            </div>
            <!-- Grid column -->

            <!-- Grid column -->
            <div class="col-md-2">
              <h6 class="text-uppercase font-weight-bold">
                <router-link to="/contact" class="text-white">Contact</router-link>
              </h6>
            </div>
            <!-- Grid column -->
          </div>
          <!-- Grid row-->
        </section>
        <!-- Section: Links -->

        <hr class="my-5" />

        <!-- Section: Text -->
        <section class="mb-5">
          <div class="row d-flex justify-content-center">
            <div class="col-lg-8">
              <p>
                We are a band of creators & Artists who love to transform
              boring sneakers into masterpieces. We only deliver high quality and unique designs.
              </p>
            </div>
          </div>
        </section>
        <!-- Section: Text -->

        <!-- Section: Social -->
        <section class="text-center mb-5">
          <a href="" class="text-white me-4">
            <i class="fab fa-facebook-f"></i>
          </a>
          <a href="" class="text-white me-4">
            <i class="fab fa-twitter"></i>
          </a>
          <a href="" class="text-white me-4">
            <i class="fab fa-instagram"></i>
          </a>
          <a href="" class="text-white me-4">
            <i class="fab fa-linkedin"></i>
          </a>
        </section>
        <!-- Section: Social -->
      </div>
      <!-- Grid container -->

      <!-- Copyright -->
      <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
        © 2023 Copyright AFA
      </div>
      <!-- Copyright -->
    </footer>
    <!-- Footer -->
  </div>
  <!-- End of .container -->
</template>

<script>
  export default {
    data() {
      return {
        cart: {
          items: []
        }
      }
    },
    mounted(){
      this.cart = this.$store.state.cart
    },
    beforeCreate() {
      this.$store.commit('InitializeStore')
    },
    computed: {
      cartTotalLength() {
        let totalLength = 0
        for(let i=0; i< this.cart.items.length; i++) {
          totalLength += 1
        }
        return totalLength
      }
    },

    methods: {
      openmenu() {
        var sidemenu = document.getElementById("sidemenu");
        if (sidemenu) {
        sidemenu.style.right = "0";
      }
      },

      closemenu() {
        var sidemenu = document.getElementById("sidemenu");
        sidemenu.style.right = "-200px";
      },

    }


  }
  var sidemenu = document.getElementById("sidemenu");
function openmenu() {
    sidemenu.style.right = "0";
}
function closemenu() {
    sidemenu.style.right = "-200px";
}


</script>

<style lang="scss">
@import '../node_modules/bootstrap';
@import "~@fortawesome/fontawesome-free/css/all.css";

nav .fas {
  color: white;
  display: none;
}

nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    height: 84px;
    background-color: #1B1B1B;
}

.spinner-wrapper {
  background-color: #0E0F0A;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 9999;
  display: flex;
  justify-content: center;
  align-items: center;
  display: none;
}

.spinner-border {
  height: 60px;
  width: 60px;
}

.isLoading {
  display: flex;
}

.main {
  background-color: #0E0F0A;
}

.navbar {
  background-color: transparent;
  margin-bottom: 0px;
}

.btn-outline-gradient {
  background: none;
  color: #fff;
  border: 2px solid transparent;
  background-clip: padding-box;
  background-image: linear-gradient(to right, #9570F7, #FD6756);
}

.btn-outline-gradient:hover {
  color: #fff;
  background-image: linear-gradient(to right, #9570F7, #FD6756);
}

.cart {
  background-color: transparent;
  text-decoration: none;
  border: none;
  margin-right: 20px;
  margin-top: 10px;
}

.cart i {
  position: relative;
  zoom: 130%;
}

@media only screen and (max-width: 992px) { 
  nav .fas {
        display: block;
        font-size: 25px;
    }

  nav ul {
    background-image: linear-gradient(to right, #9570F7, #FD6756);
    position: fixed;
        top: 0;
        right: -200px;
        width: 200px;
        height: 100vh;
        padding-top: 50px;
        z-index: 2;
        transition: right 0.5s;
  }

  nav ul .fas {
        position: absolute;
        top: 25px;
        left: 25px;
        cursor: pointer;
    }
  

  nav ul li {
    color: white;
        display: block;
        margin: 10px;
        margin-left: 25px;
    }
}
</style>
