<template>
    <div class="homepage">
        <img alt="Vue logo" src="../assets/Taking_notes-rafiki.png" />
        <form @submit.prevent="sendText">
            <textarea v-model="searchText" placeholder="search for content..."></textarea>
            <button>Search</button>
        </form>
        <div class="articles">
            <div v-for="article in articles">
                <router-link :to="'/articles/' + article.id + '/' + article.title">
                    <article>
                        <h2>{{article.title}}</h2>
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
        }
    },
    computed: {
        articles(){
            var articlesSortedByScore = this.$store.state.searchResult.slice(0);
            articlesSortedByScore.sort(function(a,b) {
                return b.score - a.score;
            });
            return articlesSortedByScore
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

</style>