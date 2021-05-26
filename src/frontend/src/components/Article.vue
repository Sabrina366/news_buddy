<template>
    <div class="article-page">
        <article>
            <h1>{{article.title}}</h1>
            <a href="{{article.url}}">{{article.url}}</a>
            <p class="info">by: {{article.author}} | published: {{article.published_date}} | added: {{article.timestamp}}</p>
            <p class="text">{{article.text}}</p>
        </article>
    </div>
</template>

<script>
export default {
    data() {
        return{
            article: {
                id: 1,
                title: "Lorem",
                text: "Fusce vulputate eleifend sapien. Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Vestibulum ullamcorper mauris at ligula. Aenean ut eros et nisl sagittis vestibulum. Ut varius tincidunt libero. Fusce vulputate eleifend sapien. Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Vestibulum ullamcorper mauris at ligula. \n\n Aenean ut eros et nisl sagittis vestibulum. Ut varius tincidunt libero. Fusce vulputate eleifend sapien. Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Vestibulum ullamcorper mauris at ligula. Aenean ut eros et nisl sagittis vestibulum. Ut varius tincidunt libero. Fusce vulputate eleifend sapien. Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Vestibulum ullamcorper mauris at ligula. Aenean ut eros et nisl sagittis vestibulum. Ut varius tincidunt libero. Fusce vulputate eleifend sapien. \n\n Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Vestibulum ullamcorper mauris at ligula. Aenean ut eros et nisl sagittis vestibulum. Ut varius tincidunt libero. Fusce vulputate eleifend sapien. Fusce risus nisl, viverra et, tempor et, pretium in, sapien. Vestibulum ullamcorper mauris at ligula. Aenean ut eros et nisl sagittis vestibulum. Ut varius tincidunt libero.",
                author: "Test Testsson",
                url: "www.somenewspaper.com",
                published_date: "2019-01-01",
                timestamp: "2020-05-25",
                summary: "Mauris turpis nunc, blandit et, volutpat molestie, porta ut"
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
    font-size: 15vh;
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