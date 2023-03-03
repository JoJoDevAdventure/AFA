<template>
    <div id="our-collections">
      <div class="head">
        <h2 class="title">Our <span>collections</span> </h2>
        <p class="sub">Discover all our collections</p>
      </div>

      <div class="collections-list">

        <router-link v-bind:to="collection.get_absolute_url"
        class="collection"
        v-for= "collection in allCollections"
        v-bind:key="collection.id"
        >
          <figure class="collection-image">
            <img :src="collection.get_thumbnail">
          </figure>
          <h3 class="title">{{collection.name}}</h3>
        </router-link>

      </div>
    </div>
  </template>

<style>
/* All collections section */
#our-collections {
  margin-bottom: 50px;
  padding: 10px 10%;
}

#our-collections .head {
  gap: 20px;
  margin-bottom: 30px;
}

#our-collections .title {
  color: white;
  font-size: 52px;
  text-align: center;
  margin-bottom: 30px;
}

#our-collections .sub {
  color: #878787;
  font-size: 22px;
  text-align: center;
  margin-bottom: 30px;
  font-weight: 200;
}

#our-collections .title span {
  color: #FD6554;
}

#our-collections .collections-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 50px;
}

#our-collections .collection {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: calc(25%);
  transition: all 0.3s ease;
  border-radius: 15px;
  text-decoration: none;
}

#our-collections .collection .title{
  margin-top: 10px;
}

#our-collections .collection:hover {
  background: linear-gradient(90deg, #9370F9 0%, #FD6554 94.37%);
  box-shadow: 0px 1px 25px rgba(189, 83, 83, 0.5);
  cursor: pointer;
}

#our-collections .collection:hover .title {
  color: #ffffff;
}

#our-collections .collection .collection-image {
  width: 100%;
  margin-bottom: 0px;
  margin-top: 0%;
}

#our-collections .collection .collection-image img {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 15px 15px 0px 0px;
}


#our-collections .collection .title {
  margin-bottom: 10px;
  font-size: 22px;
  font-weight: bold;
  color: #eaeaea;
}

@media only screen and (max-width: 600px) {

  #our-collections {
  margin-bottom: 50px;
  padding: 10px 10%;
}

#our-collections .head {
  gap: 20px;
  margin-bottom: 30px;
}

#our-collections .title {
  color: white;
  font-size: 38px;
  text-align: center;
  margin-bottom: 30px;
}

#our-collections .sub {
  color: #878787;
  font-size: 20px;
  text-align: center;
  margin-bottom: 30px;
  font-weight: 200;
}

#our-collections .title span {
  color: #FD6554;
}

#our-collections .collections-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

#our-collections .collection {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: calc(45%);
  transition: all 0.3s ease;
  border-radius: 15px;
  text-decoration: none;
}

#our-collections .collection .title{
  margin-top: 10px;
}

#our-collections .collection:hover {
  background: linear-gradient(90deg, #9370F9 0%, #FD6554 94.37%);
  box-shadow: 0px 1px 25px rgba(189, 83, 83, 0.5);
  cursor: pointer;
}

#our-collections .collection:hover .title {
  color: #ffffff;
}

#our-collections .collection .collection-image {
  width: 100%;
  margin-bottom: 0px;
  margin-top: 0%;
}

#our-collections .collection .collection-image img {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 15px 15px 0px 0px;
}


#our-collections .collection .title {
  margin-bottom: 10px;
  font-size: 18px;
  font-weight: bold;
  color: #eaeaea;
}
}

</style>
  
  <script>
  import axios from 'axios'
    export default {
      name: 'collections',
      data() {
        return {
          allCollections: []
        }
      },
      components: {
      },
      mounted() {
        this.getAllCollections()

        document.title = 'Collections | AFA'
      },
      methods: {
        getAllCollections ( ) {
          this.$store.commit('setIsLoading', true)
          axios
            .get ('/api/v1/collections/')
            .then (response => {
              this.allCollections = response.data
              this.$store.commit('setIsLoading', false)
            })
            .catch(error => {
              console.log(error)
            })
        }
      }
    }
  </script>
  
