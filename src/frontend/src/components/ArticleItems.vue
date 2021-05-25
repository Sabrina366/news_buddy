<template>
  <div >
    <article class="article">
        <button @click="deleteArticle" >X</button>
        <h3>{{ article.title }}</h3>
        <p class="author">Author  {{ article.author }}</p>
        <p class="text">{{ article.text }}</p>
        <p>{{ article.publicationDate }}</p>
    </article>
  </div>
</template>

<script>
export default {
    props: ['article'],
    methods: {
    deleteArticle(){
      this.$store.commit('removeArticle', this.article)
    }
  }
}
</script>
  
<style scoped>
 .article{
  padding: 10px;
  margin: 15px 50px;
  border-style: dotted;
  border-radius: 8px;
  border-width: 1.5px;
  border-color:lightgray;   
 } 
 button{
   float: right;
   border-style: none;
   cursor: pointer;
   outline: none;
   background-color: transparent;
   color:darkred;
   font-weight: bold;
 }

</style>