import { createStore } from "vuex" 

const store = createStore({

    state:{
        urls:{
            springUrl: 'http://127.0.0.1:8080',
            sanicUrl: 'http://127.0.0.1:8000'
        },
        search: {
            searchText: ""
        },
        searchResult: [],
        articles: [],
        article: {}
    },
    mutations:{
        setArticles(state, articles) {
            state.articles = articles
        },
        setArticle(state, article) {
            state.article = article
        },
        setSearch(state, searchTextToAppend) {
            state.search.searchText = searchTextToAppend
        },
        removeArticle(state, articleToRemove){
            state.articles = state.articles.filter(article => article != articleToRemove)
          },
       
    },
    actions:{
        async getArticles({ commit, state }) {
            let res = await fetch(state.urls.springUrl + '/spring/api/articles')
            let data = await res.json()
            commit('setArticles', data)
        },
        async getArticle({ commit, state }, id) {
            let res = await fetch(state.urls.springUrl + '/spring/api/articles/'+ id)
            let data = await res.json()
            commit('setArticle', data)

        },
        async sendSearch({state}) {
            let res = await fetch(state.urls.sanicUrl + '/sanic/api/search', {
                method: 'post',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify(state.search.searchText)
            })
            let data = await res.json()
            state.searchResult = data
        },
        async deleteArticle({state}, article) {
            let res = await fetch(state.urls.springUrl + '/spring/api/articles/'+ article.id, {
                method: 'DELETE',
                headers: {
                    'Content-type': 'application/json'
                },
                
            });
            let resData = 'resource deleted...';
      
            return resData;
        }
    }
})

export default store