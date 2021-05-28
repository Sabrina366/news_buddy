<template>
  <div class="border">
    <article class="article">
        <teleport to="#confirm">
          <div class="confirmDelete" v-if="showConfirm">
            <p>
              Delete Article?
            </p>
            <button @click="deleteArticle,showConfirm = false" >Delete</button>
            <button @click="showConfirm = false">Cancel</button>
          </div>
        </teleport>
        <button @click="showConfirm = true">X</button>
        <h3>{{ article.title }}</h3>
        <p class="author">Author  {{ article.author }}</p>
        <p class="text">{{ article.text }}</p>
    </article>
  </div>
</template>

<script>
export default {
  data(){
    return{
      showConfirm: false,
    }

  },
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
  border-radius: 5px;
  border-width: 1.5px;
  border-color:lightgray;
  height: 20vh;
  overflow: hidden;
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
 .author{
   font-size: 10px;
 }
 .timestamp{
   font-size: 10px;
 }
.confirmDelete{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 150px;
  width: 300px;
  background:gainsboro;
  text-align: center;
  border-radius: 5px;
  border-style: solid;
}

</style>