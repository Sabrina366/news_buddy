import { createRouter, createWebHistory } from 'vue-router'
import Home from '/src/components/Home.vue'
import ArticleList from '/src/views/ArticleList.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/articles',
        name: 'Articles',
        component: ArticleList,
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router