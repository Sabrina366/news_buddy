<template>

 <nav class="navbar">
    <div class="logo">
    <a href="/"><img class="icon" src="src/assets/NewsBuddy-logo.png" alt="Icon"></a>
    <a href="/"><img class="icon-small" src="src/assets/NewsBuddy-IconSmall.png" alt="IconSmall"></a>
   </div>
   <div class="link1">
    <a href="/">Create Content</a>
   </div>
    <div class="link2">
    <a href="/">Articles</a>
   </div>
  </nav>

</template>

<script>
export default {
}
</script>

<style scoped>
.navbar{
  position: fixed;
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
}

.icon{
  display: flex;
  max-width: 120px;
  height: auto;
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
  flex-grow: 1;
  order: 1;
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

/* @media (max-width: 1000px) {
  .navbar {
    font-size: 15px;
    flex-direction: row;
    align-items: center;
    display: flex;
    justify-content: space-between;
  }
} */

</style>