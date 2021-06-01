<template>
  <article id="articlepage">
    <div class="input">
      <input 
    type="text" 
    placeholder="search..."
    v-model="input">
    <img src="src\assets\Web search-rafiki.png" alt="">
    </div>
    <div class="articles">
      <ArticleItems v-for="(a, index) of articles" :key="index" :article="a"/>
    </div>
  </article>
</template>

<script>
import ArticleItems from "../components/ArticleItems.vue";

export default {
    data() {
      return{
        input: '',
        articlesSorted: []
      }
    },
    components:{
    ArticleItems
  },
  computed:{
    articles(){
        let articlesSorted = this.$store.state.articles.filter(article =>
        article.title.toLowerCase().includes(this.input.toLowerCase())).reverse()
        return articlesSorted
    }
  },

}
</script>

<style scoped>
  img{
    height: 100px;
    width: 105px;
}
  input{
    border-color: rgb(64, 115, 209);
    border-width: 1.5px;
    border-radius: 4px;
    margin: 20px 10px;
    
  }
  .articles{
    max-height: 65vh;
    overflow: auto;
  }
  .articlepage{
    max-height: 100vh;
    font-size: 12px;
  }
  .articles::-webkit-scrollbar {
  width: 12px;
}

.articles::-webkit-scrollbar-track {
  background: gainsboro; 
}

.articles::-webkit-scrollbar-thumb {
  background-color:rgb(179, 179, 179); 
  border-radius: 5px;   
  border: 3px solid gainsboro;  
}

</style>

