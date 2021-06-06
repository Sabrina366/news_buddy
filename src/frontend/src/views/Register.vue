<template>
<article>
    <div class="container">
      <form @submit.prevent="newUser">
      <label>Email</label>
      <input v-model="email" type="email" placeholder="email" required>
      <label>Password</label>
      <input v-model="password" type="password" placeholder="password" required>
      <label>Confirm Password</label>
      <input v-model="passwordCeck" type="password" placeholder="confirm password" required>
      <button type="submit">Register</button>
  </form>
    </div>
</article>
</template>

<script>
export default {
    data(){
        return{
            email: '',
            password: '',
            passwordCheck: ''
        }
    },
    methods:{
        newUser(){
            let user = {
                email: this.email,
                password: this.password
            }
            
            this.$store.dispatch('postUser', user)
        }

    },
}

</script>

<style scoped>
article{
  align-items: center;
  display: flex;
  justify-content: center;
  height: 100vh;
}
.container{
    background-color: #5474AA ;
    height: 60%;
    position: relative;
    width: 40%;
}
input{
background-color: white;
  border-radius: 12px;
  border: 0;
  box-sizing: border-box;
  height: 100%;
  outline: 0;
  padding: 4px 20px 0;
  width: 20%;
}
button{
    background-color: #DDEFFD;
    color: #5474AA;
    cursor: pointer;
    border-radius: 4px;
    border: none;
    padding: 5px;
    margin: 5px;
    font-weight: 600;
    border-radius: 4px;
    box-sizing: border-box;
    height: 50px;
    margin-top: 38px;
    text-align: center;
    width: 20%;
}
</style>