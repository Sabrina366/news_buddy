<template>
    <div class="addArticle">
    <img alt="readingNews" src="../assets/News-bro.png"  >
 
    <form  @submit.prevent="handlesubmit">
        
        <div><input type="author" placeholder="Author" required v-model="author" id="author"> 
        </div>
        <div><input type="date" placeholder="Published date" required v-model="date" id="date">
        </div>
        <div><input type="text" placeholder="Title" required v-model="title" id="title">
        </div>
        <textarea type="title" placeholder="Article" required v-model="text"></textarea> 
        <div><input type="url" placeholder="Link to article" v-model="url" id="link">
        </div>
        
        <div class="submit">
            <button type="submit" id="submitButton">Submit article</button>
        </div>
        

    </form>

    
    </div>
</template>

<script>


export default {
    data(){
        return{
            title: "",
            author: "",
            pub_date: "",
            text: "",
            url: "",
        
        }
    },
    
    methods: {

    handlesubmit(){
        let article = {
            title:this.title,
            author:this.author, 
            pub_date:this.date, 
            text:this.text, 
            url:this.url,
            timestamp: Math.floor(Date.now() / 1000)}
        this.$store.commit('setArticle', article)
        this.$store.dispatch('addArticle', article)
        this.$router.push('/addArticle')
        console.log(article)
        

    

    },



    
    }

}

</script>

<style scoped>


.addArticle {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#submitButton{
    background: rgb(87, 87, 192);
    border: 0;
    padding: 9px 20px;
    margin-top: 20px;
    color: white;
    border-radius: 20px;


}

.submit{
    text-align: center;
}

form {
    display: flex;
    flex-direction: column;
    width: 80%;
    max-width: 800px;
    height: 600px;
}

textarea {
    height: 200px;
    border: 3px solid #5474AA;
    padding: 5px;
    margin: 5px;
    resize: none;
    border-radius: 4px;
}

input{
    border: 1.5px solid #5474AA;
    padding: 5px;
    margin: 5px;
    border-radius: 4px;
    height: 17px;
    width: 96.5%;
    
}


img {
    width: 40%;
    height: 65vh;
    object-fit: cover;
    object-position: center top;
}



</style>
