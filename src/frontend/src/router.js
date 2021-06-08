import { createRouter, createWebHistory } from 'vue-router'
import Home from '/src/components/Home.vue'
import ArticleList from '/src/views/ArticleList.vue'
import Article from '/src/views/Article.vue'
import AddArticle from '/src/components/AddArticle.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
       
        path: '/articles/:title/:id',
        name: 'Article',
        component: Article,
    },
    {
        path: '/articles',
        name: 'Articles',
        component: ArticleList,
    },
    {
        path: '/add',
        name: 'AddArticle',
        component: AddArticle,
    },
]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router