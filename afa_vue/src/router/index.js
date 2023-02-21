import { createRouter, createWebHistory } from 'vue-router'
import AboutView from '../views/AboutView.vue'
import CartView from '../views/CartView.vue'
import CheckoutView from '../views/CheckoutView.vue'
import CollectionDetailsView from '../views/CollectionDetailsView.vue'
import CollectionsView from '../views/CollectionsView.vue'
import ContactView from '../views/ContactView.vue'
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import SuccessView from '../views/SuccessView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/collections/',
    name: 'collections',
    component: CollectionsView,
  },
  {
    path: '/:collection_slug/:product_slug/',
    name: 'product',
    component: ProductView,
  },
  {
    path: '/:collection_slug/',
    name: 'collection',
    component: CollectionDetailsView,
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactView,
  },

  {
    path: '/cart',
    name: 'cart',
    component: CartView,
  },

  {
    path: '/cart/checkout',
    name: 'checkout',
    component: CheckoutView,
  },

  {
    path: '/cart/success',
    name: 'success',
    component: SuccessView,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
