<template>
    <div class="article-page">
        <article>
            <h1>{{article.title}}</h1>
            <a :href="article.url" target="_blank">{{article.url}}</a>
            <p class="info">by: {{article.author}} | published: {{article.pub_date}} | added: {{dateConvert(article.timestamp)}}</p>
            <p class="text">{{article.text}}</p>
        </article>
    </div>
</template>

<script>
export default {
    created() {
        this.$store.dispatch('getArticle', this.$route.params.id)
    },
    computed: {
        article(){
            return this.$store.state.article
        }
    },
    methods: {
        dateConvert(unix) {            
            let date = new Date(unix * 1000).toLocaleDateString()
                
            return date            
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
    font-size: 3em;
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