<template>
  <div >
    <article class="article">
        <h3>{{ article.title }}</h3>
        <p>{{ article.text }}</p>
        <p>{{ article.author }}</p>
        <p>{{ article.publicationDate }}</p>
        <button>X</button>
    </article>
  </div>
</template>

<script>
export default {
    props: ['article'],
}
</script>
  
<style scoped>
 .article{
  padding: 10px;
  margin: 15px;
 } 

</style>