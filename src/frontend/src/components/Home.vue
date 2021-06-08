<template>
    <div class="homepage">
        <img alt="Vue logo" src="../assets/Taking_notes-rafiki.png" />
        <form @submit.prevent="sendText">
            <textarea v-model="searchText" placeholder="search for content..."></textarea>
            <button>Search</button>
        </form>
        <div v-if="loading" v-cloak>
            <div class="loader"></div>
        </div>
        <div class="articles">
            <div v-for="article in articles">
                <router-link :to="'/articles/' + article.title+ '/'   + article.id">
                    <article>
                        <h2>{{article.title}}</h2>
                        <div class="info">
                            <p>Full reading time: {{showTime(article.full_readingtime)}} min</p>
                            <p>Summary reading time: {{showTime(article.summary_readingtime)}} min</p>
                        </div>
                        <p>{{article.summary}}</p>
                    </article>
                </router-link>
            </div>
        </div>
    </div>
</template>


<script>

export default {
    methods:{
        sendText(){
            this.$store.commit('setSearch', this.searchText)
            this.$store.dispatch('sendSearch', this.searchText)
            this.$router.push('/')
            this.loading = true;
        },
        showTime(time){
            let timeRounded = Math.ceil(time)
            if(time < 1) timeRounded = "<" + timeRounded
            return timeRounded
        }
    },
    data() {
        return{
            loading: false
        }

    },
    computed: {
        articles(){
            let searchResult = this.$store.state.searchResult.slice(0);
            let sortedArticles = [];
            searchResult.sort(function(a,b) {
                return b.score - a.score;
            });
            searchResult.forEach((item)=>{
                if (item.score > 0) {
                    sortedArticles.push(item);
                }
            })
            this.loading = false;
            return sortedArticles
        }
    }
}
</script>

<style scoped>

.homepage {
    display: flex;
    flex-direction: column;
    align-items: center;
}

img {
    width: 60%;
    height: 60vh;
    object-fit: cover;
    object-position: center top;
}

form {
    display: flex;
    flex-direction: column;
    width: 80%;
    max-width: 800px;
    height: 200px;
}

textarea {
    height: 120px;
    border: 3px solid #5474AA;
    padding: 5px;
    margin: 5px;
    resize: none;
    border-radius: 4px;
}

button {
    display: flex;
    align-self: flex-end;
    background-color: #DDEFFD;
    color: #5474AA;
    border-radius: 4px;
    border: none;
    padding: 5px;
    margin: 5px;
    font-weight: 600;
}

.articles {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.articles a {
    text-decoration: none;
    color: inherit;
}

article {
    width: 300px;
    border: dashed 2px rgb(196, 186, 186);
    margin: 40px;
    padding: 10px;
    border-radius: 4px;
}

.info {
    color: #5474AA;
}

.info p {
    margin: 0;
    padding: 0;
    font-size: 14px;
}

/* Loader */
.loader {
    border: 16px solid #f3f3f3;
    border-top: 16px solid #3498db;
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

</style>