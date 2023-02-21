import { createStore } from 'vuex'

export default createStore({
  state: {
    cart:{
      items:[],
    },
    isLoading: false,
  },
  getters: {
  },
  mutations: {
    InitializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'))
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },
    addToCart(state, item) {
      state.cart.items.push(item)
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    ClearCart(state) {
      state.cart = {items:[]}
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  actions: {
  },
  modules: {
  }
})
