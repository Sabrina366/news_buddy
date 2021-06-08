import { createRouter, createWebHistory } from 'vue-router'
import Home from '/src/components/Home.vue'
import ArticleList from '/src/views/ArticleList.vue'
import Article from '/src/views/Article.vue'
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
        path: '/articles',
        name: 'Articles',
        component: ArticleList,
    },
    {

    path: '/addArticle',
    name: 'addArticle',
    component: addArticle,
    },

]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router