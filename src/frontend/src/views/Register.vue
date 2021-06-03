<template>
<article>
    <div>
      <form @submit.prevent="newUser">
      <label>Email</label>
      <input v-model="email" type="email" placeholder="email" required>
      <label>Password</label>
      <input v-model="password" type="password" placeholder="password" required>
      <label>Confirm Password</label>
      <input type="password" placeholder="confirm password" required>
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
            password: ''
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

<style>

</style>