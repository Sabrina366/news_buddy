import { createRouter, createWebHistory } from 'vue-router'
import Home from '/src/components/Home.vue'
import Article from '/src/components/Article.vue'
const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/articles/:id/:title',
        name: 'Article',
        component: Article,
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router