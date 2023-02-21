import { createRouter, createWebHistory } from 'vue-router'
import CartView from '../views/CartView.vue'
import CollectionDetailsView from '../views/CollectionDetailsView.vue'
import CollectionsView from '../views/CollectionsView.vue'
import ContactView from '../views/ContactView.vue'
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
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
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
