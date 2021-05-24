<template>
  <div>
      <article v-for="article in articles" :key="article.id">
        <h3>{{ article.title }}</h3>
        <p>{{ article.text }}</p>
        <p>{{ article.author }}</p>
        <p>{{ article.publicationDate }}</p>
        <button>Delete</button>
    </article>

  </div>
  
</template>

<script>
export default {
    computed:{
    articles(){
        return this.$store.state.articles
    }
  },

}
</script>

<style>

</style>