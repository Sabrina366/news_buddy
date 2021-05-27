import { createStore } from "vuex" 

const store = createStore({
    state:{
        search: {
            searchText: "lorem ipsum lorem"
        },
        articles: [
            {
                id: 201,
                title: "Lorem1",
                text: "Mauris turpis nunc, blandit et, volutpat molestie, porta ut, ligula. Vestibulum suscipit nulla quis orci. Fusce risus nisl, viverra et, tempor et, pretium in, sapien.\n\n Mauris turpis nunc, blandit et, volutpat molestie, porta ut, ligula. Vestibulum suscipit nulla quis orci. Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Mauris turpis nunc, blandit et, volutpat molestie, porta ut, ligula. Vestibulum suscipit nulla quis orci. Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Mauris turpis nunc, blandit et, volutpat molestie, porta ut, ligula. Vestibulum suscipit nulla quis orci. \n\n Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Mauris turpis nunc, blandit et, volutpat molestie, porta ut, ligula. Vestibulum suscipit nulla quis orci. Fusce risus nisl, viverra et, tempor et, pretium in, sapien.",
                author: "Test Testsson",
                url: "www.somenewspaper.com",
                published_date: "2019-01-01",
                timestamp: "2020-05-25",
                summary: "Mauris turpis nunc, blandit et, volutpat molestie, porta ut"
            },
            {
                id: 202,
                title: "Lorem2",
                text: "Mauris turpis nunc, blandit et, volutpat molestie, porta ut, ligula. Vestibulum suscipit nulla quis orci. Fusce risus nisl, viverra et, tempor et, pretium in, sapien.",
                author: "Test Testsson",
                url: "www.somenewspaper.com",
                published_date: "2019-01-01",
                timestamp: "2020-05-25",
                summary: "Mauris turpis nunc, blandit et, volutpat molestie, porta ut"
            },
            {
                id: 203,
                title: "Lorem3",
                text: "Mauris turpis nunc, blandit et, volutpat molestie, porta ut, ligula. Vestibulum suscipit nulla quis orci. Fusce risus nisl, viverra et, tempor et, pretium in, sapien.",
                author: "Test Testsson",
                url: "www.somenewspaper.com",
                published_date: "2019-01-01",
                timestamp: "2020-05-25",
                summary: "Mauris turpis nunc, blandit et, volutpat molestie, porta ut"
            }
        ]
    },
    mutations:{
        setArticles(state, articles) {
            state.articles = articles
        },
        setSearch(state, searchTextToAppend) {
            state.search.searchText = searchTextToAppend
        }
    },
    actions:{
        async getArticles({ commit }) {
            let res = await fetch('/rest/articles')
            let data = await res.json()
            commit('setArticles', data)
        },
        async sendSearch({ dispatch, state }) {
            let res = await fetch('/rest/search', {
                method: 'post',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify(state.search.searchText)
            })
            let data = await res.json()
            dispatch('setSearch', state.search.searchText)
        }
    }
})

export default store