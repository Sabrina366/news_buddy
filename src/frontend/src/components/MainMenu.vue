<template>

 <nav class="navbar">
    <div class="logo">
    <router-link to="/"><img class="icon" src="src/assets/NewsBuddy-logo.png" alt="Icon"></router-link>
    <router-link to="/"><img class="icon-small" src="src/assets/NewsBuddy-IconSmall.png" alt="IconSmall"></router-link>
  </div>
   <div class="link1">
     <router-link to="/">Add Article</router-link>
   </div>
    <div class="link2">
      <router-link to="/articles">Articles</router-link>
   </div>
  </nav>

</template>

<script>
export default {
}
</script>

<style scoped>
.navbar{
  font-size: 20px;
  margin-bottom: 5px;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
  display: flex;
  min-width: 100%;
  background: 255,255,255;
}
.icon-small{
  display: none;
  pointer-events: visible;
  max-width: 120px;
  height: auto;
}

.icon{
  display: flex;
  max-width: 100px;
  height: auto;
  pointer-events: visible;
}

.link1{
  order: 2;
  flex-grow: 1;
}

.link2{
  order: 3;
  flex-grow: 1;
  
}

.logo{
  float: left;
  margin: 0px;
  flex-grow: 3;
  order: 1;
  pointer-events: none;
}
  
.navbar a{
  color: #5474AA;
  text-decoration: none;
}

.navbar a:hover{
  color: #DDEFFD;
}

@media (max-width: 1300px) {
  .icon{
    display: none;
  }
  .icon-small{
    display: flex;
  }
}

</style>