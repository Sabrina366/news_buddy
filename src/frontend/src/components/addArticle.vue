<template>
    <form @submit.prevent="handleSubmit">
        <input type="author" placeholder="Author" required v-model="author">
        <input type="date" placeholder="Published date" required v-model="date">
        <input type="url" placeholder="Link to article" required v-model="url">
        <textarea type="article" placeholder="Article" required v-model="article"></textarea>
        

        <div class="submit">
            <button>Submit article</button>
        </div>
    </form>

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


</style>
