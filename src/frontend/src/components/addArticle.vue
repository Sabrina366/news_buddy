<template>
    <div class="addArticle">
    <img alt="readingNews" src="../assets/News-bro.png"  >
    <form @submit.prevent="handleSubmit">
        <div><input type="author" placeholder="Author" required v-model="author" id="author"> 
        </div>
        <div><input type="date" placeholder="Published date" required v-model="date" id="date">
        </div>
        <textarea type="article" placeholder="Article" required v-model="article"></textarea> 
        <div><input type="url" placeholder="Link to article" required v-model="url" id="link">
        </div>
        
        <div class="submit">
            <button>Submit article</button>
        </div>
    </form>
    </div>
</template>

<script>
export default {
    data(){
        return{
            author: '' ,
            date: '',
            article: '',
        }
    },
    

    methods: {
    handlesubmit(){
        


    }
    }
}
        




</script>

<style scoped>

.addArticle {
    display: flex;
    flex-direction: column;
    align-items: center;
}

button{
    background: rgb(87, 87, 192);
    border: 0;
    padding: 10px 20px;
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
    margin: 3px;
    border-radius: 4px;
    height: 17px;
    width: 96.5%;
    
}


img {
    width: 45%;
    height: 60vh;
    object-fit: cover;
    object-position: center top;
}


</style>
