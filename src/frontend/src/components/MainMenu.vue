<template>

 <nav class="navbar">
    <div class="logo">
    <a href="/"><img class="icon" src="src/assets/NewsBuddy-logo.png" alt="Icon"></a>
   </div>
    <a href="/">Create Content</a>
    <a href="/">Articles</a>
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
  justify-content: space-around;
  align-items: center;
  display: flex;
  height: 0px;
}
.logo{
  width: 30vw;
  float: left;
  padding: 0px;
  margin: 0px;
}
.icon {
  padding: 15px;
  background-size: cover;
  width: 30%;
  margin-top: 15px;
}

  
.navbar a{
  color: #5474AA;
  text-decoration: none;
  padding: 0px 5px;
}

.navbar a:hover{
  color: #DDEFFD;
}

/* 
@media (max-width: 1000px) {
  .navbar {
      font-size: 15px;
      flex-direction: row;
      align-items: center;
      flex-wrap: wrap;
      display: flex;
      justify-content: space-between;
  } 
}
*/
</style>