import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'
import PostListView from '../views/PostListView.vue'
import PostDetailView from '../views/PostDetailView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/posts',
      name: 'posts',
      component: PostListView
    },
    {
      path: '/posts/:pk',
      name: 'detail',
      component: PostDetailView
    }
  ]
})

export default router
