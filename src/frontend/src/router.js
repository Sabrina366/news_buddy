import { createRouter, createWebHistory } from 'vue-router'
import Home from '/src/components/Home.vue'
import Article from '/src/components/Article.vue'
import addArticle from '/src/components/addArticle.vue'
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
        path: '/addArticle',
        name: "addArticle",
        component: addArticle,
    },
    
]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router