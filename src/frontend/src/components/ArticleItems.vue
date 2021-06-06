<template>
  <div class="border">
    <article class="article">
        <teleport to="#confirm">
          <div class="confirmDelete" v-if="showConfirm">
            <p class="confirmtxt">
              Delete Article?
            </p>
            <button @click="delArticle" class="deletebtn">Delete</button>
            <button @click="showConfirm = false" class="cancelbtn">Cancel</button>
          </div>
        </teleport>
        <button @click="showConfirm = true" class="delbtn">X</button>
        <router-link :to="'/articles/' + article.id + '/' + article.title">
            <h3>{{ article.title }}</h3>
        </router-link>
        <p class="author">By {{ article.author }}</p>
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
    delArticle(){
      console.log(this.article.id)
      this.$store.commit('removeArticle', this.article)
      this.$store.dispatch('deleteArticle', this.article)
      this.showConfirm = false
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
 .delbtn{
   float: right;
   border-style: none;
   cursor: pointer;
   outline: none;
   background-color: transparent;
   color:darkred;
   font-weight: bold;
   box-shadow: grey;
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
  border-width: 1px;
  border-color: darkgray;
  box-shadow: darkslategray;
}
.deletebtn{
  background-color:darkred;
  cursor: pointer;
  color: ghostwhite;
  padding: 2%;
  border-width: 1px;
  margin-top: 10%;
  margin-right: 1.5%;

}
.cancelbtn{
  cursor: pointer;
  background-color: lightgray;
  padding: 1%;
  padding: 2%;
  margin-top: 10%;
  margin-left: 1.5%;
  border-width: 1px;
}
.confirmtxt{
  margin-top: 10%;
}

.articles a {
    text-decoration: none;
    color: inherit;
}
</style>