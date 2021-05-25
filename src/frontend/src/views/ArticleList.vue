<template>
  <input 
  type="text" 
  placeholder="search..."
  v-model="input">
  <div class="articles">
    <ArticleItems v-for="(a, index) of articles" :key="index" :article="a"/>
  </div>
</template>

<script>
import ArticleItems from "../components/ArticleItems.vue";

export default {
    data() {
      return{
        input: ''
      }
    },
    components:{
    ArticleItems
  },
  computed:{
    articles(){
        return this.$store.state.articles.filter(article =>
        article.title.toLowerCase().includes(this.input.toLowerCase())
      );
    }
  },

}
</script>

<style scoped>
  *{
    
  }
</style>

