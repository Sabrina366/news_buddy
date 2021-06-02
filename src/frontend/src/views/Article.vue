<template>
    <div class="article-page">
        <article>
            <h1>{{article.title}}</h1>
            <a :href="article.url" target="_blank">{{article.url}}</a>
            <p class="info">by: {{article.author}} | published: {{article.published_date}} | added: {{article.timestamp}}</p>
            <p class="text">{{article.text}}</p>
        </article>
    </div>
</template>

<script>
export default {

    computed: {
        article(){
            for(let i=0; i<=this.$store.state.articles.length; i++) {
                if(this.$store.state.articles[i].id == this.$route.params.id) {
                    return this.$store.state.articles[i]
                }
            }
        }
    }
}
</script>

<style scoped>
.article-page {
    display: flex;
    flex-direction: column;
    align-items: center;
}

article {
    margin: 0 200px 100px 200px;
}

h1 {
    color: #5474AA;
    font-size: 10vh;
    margin: 30px;
}

.text {
    white-space: pre-wrap;
}

p {
    font-size: 20px;
}

.info {
    color: #5474AA;
    margin: 30px;
}
</style>