<template>
  <div class="spinner-wrapper text-danger" v-bind:class="{'isLoading': $store.state.isLoading}">
    <div class="spinner-border">
      <span class="visually-hidden"></span>
    </div>
  </div>
  <div class="main">
    <div class="container">
      <nav class="navbar navbar-expand-lg navbar-dark ">
        <a class="navbar-brand" href="#">
          <img src="./assets/AFALogo.png"  width="60" height="60" class="d-inline-block align-top" alt="">
        </a>

        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mx-auto">
            <li class="nav-item">
              <router-link to="/home" class="nav-link">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/about" class="nav-link">About</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/collections" class="nav-link">Collections</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/testimonials" class="nav-link">Testimonials</router-link>
            </li>
          </ul>

          <div class="d-flex">
            <router-link to="/cart" class="cart" type="button">
              <i class="fa-regular fa-cart-shopping fa-bounce" style="color: #ffffff;"></i>
              <span style="color: #ffffff;">({{ cartTotalLength }})</span>
            </router-link>
            <router-link to="/contact" class="btn btn-outline-gradient">
              Contact us
            </router-link>
          </div>
        </div>
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
                <a href="#!" class="text-white">About us</a>
              </h6>
            </div>
            <!-- Grid column -->

            <!-- Grid column -->
            <div class="col-md-2">
              <h6 class="text-uppercase font-weight-bold">
                <a href="#!" class="text-white">Products</a>
              </h6>
            </div>
            <!-- Grid column -->

            <!-- Grid column -->
            <div class="col-md-2">
              <h6 class="text-uppercase font-weight-bold">
                <a href="#!" class="text-white">Awards</a>
              </h6>
            </div>
            <!-- Grid column -->

            <!-- Grid column -->
            <div class="col-md-2">
              <h6 class="text-uppercase font-weight-bold">
                <a href="#!" class="text-white">Help</a>
              </h6>
            </div>
            <!-- Grid column -->

            <!-- Grid column -->
            <div class="col-md-2">
              <h6 class="text-uppercase font-weight-bold">
                <a href="#!" class="text-white">Contact</a>
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
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt
                distinctio earum repellat quaerat voluptatibus placeat nam,
                commodi optio pariatur est quia magnam eum harum corrupti
                dicta, aliquam sequi voluptate quas.
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
            <i class="fab fa-google"></i>
          </a>
          <a href="" class="text-white me-4">
            <i class="fab fa-instagram"></i>
          </a>
          <a href="" class="text-white me-4">
            <i class="fab fa-linkedin"></i>
          </a>
          <a href="" class="text-white me-4">
            <i class="fab fa-github"></i>
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
      this.$store.commit('initializeStore')
    },
    computed: {
      cartTotalLength() {
        let totalLength = 0
        for(let i=0; i< this.cart.items.length; i++) {
          totalLength += 1
        }
        return totalLength
      }
    }
  }

</script>

<style lang="scss">
@import '../node_modules/bootstrap';
@import "~@fortawesome/fontawesome-free/css/all.css";

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
}

.cart i {
  position: relative;
  zoom: 130%;
}
</style>
