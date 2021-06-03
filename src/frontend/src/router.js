import { createRouter, createWebHistory } from 'vue-router'
import Home from '/src/components/Home.vue'
import ArticleList from '/src/views/ArticleList.vue'
import Article from '/src/views/Article.vue'
import Register from '/src/views/Register.vue'

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
    },
    {
        path: '/articles',
        name: 'Articles',
        component: ArticleList,
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router